"""
Sistema de Conciliación de Liquidaciones de Tarjetas
API para Vercel Serverless Functions
"""
from flask import Flask, render_template, request, jsonify
import PyPDF2
import io
import re
from decimal import Decimal

app = Flask(__name__)

def extraer_texto_pdf(pdf_file):
    """Extrae todo el texto del PDF"""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        texto_completo = ""
        for page in pdf_reader.pages:
            texto_completo += page.extract_text()
        return texto_completo
    except Exception as e:
        return None

def limpiar_numero(valor_str):
    """Convierte string con formato argentino a Decimal"""
    if not valor_str:
        return Decimal('0')
    # Remover todo excepto dígitos, coma y signo menos
    limpio = re.sub(r'[^\d,\-]', '', str(valor_str))
    # Reemplazar coma por punto
    limpio = limpio.replace(',', '.')
    try:
        return Decimal(limpio)
    except:
        return Decimal('0')

def extraer_dato(texto, patron, default='0,00'):
    """Extrae un dato numérico del texto usando expresión regular"""
    match = re.search(patron, texto, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return default

def procesar_liquidacion(texto):
    """Procesa el texto de la liquidación y extrae todos los conceptos"""
    
    # Patrones de extracción
    total_presentado = extraer_dato(
        texto,
        r'Total\s+presentado[:\s]+\$?\s*([\d.,]+)',
        '0,00'
    )
    
    neto_pagos = extraer_dato(
        texto,
        r'Neto\s+de\s+pagos[:\s]+\$?\s*([\d.,]+)',
        '0,00'
    )
    
    # Convertir a Decimal
    total_decimal = limpiar_numero(total_presentado)
    neto_decimal = limpiar_numero(neto_pagos)
    
    # Buscar todos los conceptos de débitos
    conceptos = []
    
    # Patrón general para capturar conceptos con sus montos
    patron_concepto = r'([A-ZÁÉÍÓÚa-záéíóú\s/\-\.]+?)[\s:]+\$?\s*([\d.,]+)'
    
    # Conceptos a buscar
    conceptos_buscar = [
        (r'Arancel[:\s]+\$?\s*([\d.,]+)', 'Arancel', 'operativo'),
        (r'IVA\s+s/\s*Arancel[:\s]+\$?\s*([\d.,]+)', 'IVA s/Arancel', 'iva'),
        (r'Percepci[oó]n\s+de\s+IVA[:\s]+\$?\s*([\d.,]+)', 'Percepción de IVA', 'iva'),
        (r'Retenci[oó]n\s+SIRTAC[:\s]+\$?\s*([\d.,]+)', 'Retención SIRTAC (IIBB)', 'iibb'),
        (r'Retenci[oó]n\s+IIBB[:\s]+\$?\s*([\d.,]+)', 'Retención IIBB', 'iibb'),
        (r'Percepci[oó]n\s+IIBB[:\s]+\$?\s*([\d.,]+)', 'Percepción IIBB', 'iibb'),
        (r'Retenci[oó]n\s+QR[:\s]+\$?\s*([\d.,]+)', 'Retención QR (IIBB)', 'iibb'),
        (r'Retenci[oó]n\s+Ganancias[:\s]+\$?\s*([\d.,]+)', 'Retención Ganancias', 'ganancias'),
    ]
    
    for patron, nombre, categoria in conceptos_buscar:
        matches = re.finditer(patron, texto, re.IGNORECASE)
        for match in matches:
            monto = limpiar_numero(match.group(1))
            if monto > 0:
                conceptos.append({
                    'concepto': nombre,
                    'monto': float(monto),
                    'categoria': categoria
                })
    
    # Consolidar conceptos
    consolidado = {
        'operativo': Decimal('0'),
        'iva': Decimal('0'),
        'iibb': Decimal('0'),
        'ganancias': Decimal('0')
    }
    
    for concepto in conceptos:
        categoria = concepto['categoria']
        monto = Decimal(str(concepto['monto']))
        consolidado[categoria] += monto
    
    # Calcular totales
    total_debitos = sum(consolidado.values())
    diferencia = total_decimal - neto_decimal - total_debitos
    
    # Preparar resultado
    resultado = {
        'total_presentado': float(total_decimal),
        'neto_pagos': float(neto_decimal),
        'diferencia_reportada': float(total_decimal - neto_decimal),
        'conceptos': conceptos,
        'consolidado': {
            'operativo': float(consolidado['operativo']),
            'iva': float(consolidado['iva']),
            'iibb': float(consolidado['iibb']),
            'ganancias': float(consolidado['ganancias']),
            'total': float(total_debitos)
        },
        'conciliacion': {
            'diferencia': float(diferencia),
            'estado': 'EXITOSA' if abs(diferencia) < 0.01 else 'REVISAR',
            'precision': 'Alta' if abs(diferencia) < 0.01 else 'Media'
        },
        'porcentajes': {
            'operativo': float((consolidado['operativo'] / total_decimal * 100) if total_decimal > 0 else 0),
            'iva': float((consolidado['iva'] / total_decimal * 100) if total_decimal > 0 else 0),
            'iibb': float((consolidado['iibb'] / total_decimal * 100) if total_decimal > 0 else 0),
            'ganancias': float((consolidado['ganancias'] / total_decimal * 100) if total_decimal > 0 else 0),
            'eficiencia_cobro': float((neto_decimal / total_decimal * 100) if total_decimal > 0 else 0)
        }
    }
    
    return resultado

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/procesar', methods=['POST'])
def procesar():
    """API para procesar el PDF"""
    try:
        if 'pdf' not in request.files:
            return jsonify({
                'success': False,
                'error': 'No se recibió ningún archivo PDF'
            }), 400
        
        pdf_file = request.files['pdf']
        
        if pdf_file.filename == '':
            return jsonify({
                'success': False,
                'error': 'No se seleccionó ningún archivo'
            }), 400
        
        if not pdf_file.filename.endswith('.pdf'):
            return jsonify({
                'success': False,
                'error': 'El archivo debe ser un PDF'
            }), 400
        
        # Leer el PDF
        pdf_bytes = io.BytesIO(pdf_file.read())
        texto = extraer_texto_pdf(pdf_bytes)
        
        if not texto:
            return jsonify({
                'success': False,
                'error': 'No se pudo extraer texto del PDF'
            }), 400
        
        # Procesar la liquidación
        resultado = procesar_liquidacion(texto)
        
        return jsonify({
            'success': True,
            'data': resultado
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error al procesar: {str(e)}'
        }), 500

# Para desarrollo local
if __name__ == '__main__':
    app.run(debug=True)
