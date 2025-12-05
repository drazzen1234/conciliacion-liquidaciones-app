# 🎯 Sistema de Conciliación de Liquidaciones

**Aplicación Web Profesional para Procesar Liquidaciones de Tarjetas de Crédito**

## 🌟 Características

✅ **Drag & Drop**: Arrastra y suelta tus PDFs  
✅ **Procesamiento Automático**: Extracción inteligente de datos  
✅ **Conciliación Profesional**: Tablas detalladas y consolidadas  
✅ **Exportación Múltiple**: CSV, Copiar, Imprimir  
✅ **100% Web**: Sin instalación, acceso desde cualquier dispositivo  
✅ **Seguro**: Procesamiento en servidor, sin almacenamiento  

## 🚀 Despliegue Rápido en Vercel (5 minutos)

### Opción 1: Despliegue con CLI (Recomendado)

```bash
# 1. Instalar Vercel CLI
npm install -g vercel

# 2. Navegar a la carpeta del proyecto
cd webapp_vercel

# 3. Desplegar
vercel deploy --prod
```

**¡Listo!** Recibirás una URL pública como: `https://tu-app.vercel.app`

### Opción 2: Despliegue con GitHub

1. Sube este proyecto a GitHub
2. Ve a [vercel.com](https://vercel.com)
3. Click en "Import Project"
4. Selecciona tu repositorio
5. Click "Deploy"

**¡Automático!** Vercel detecta la configuración y despliega.

### Opción 3: Despliegue Manual (Sin GitHub)

```bash
# 1. Instalar Vercel CLI
npm install -g vercel

# 2. Login en Vercel
vercel login

# 3. En la carpeta del proyecto
cd webapp_vercel

# 4. Despliegue inicial (interactivo)
vercel

# 5. Despliegue a producción
vercel --prod
```

## 📁 Estructura del Proyecto

```
webapp_vercel/
├── api/
│   └── index.py          # API Flask serverless
├── templates/
│   └── index.html        # Frontend completo
├── requirements.txt      # Dependencias Python
├── vercel.json          # Configuración Vercel
└── README.md            # Esta guía
```

## 🔧 Tecnologías

- **Backend**: Python 3.9 + Flask
- **PDF**: PyPDF2
- **Frontend**: HTML5 + CSS3 + JavaScript
- **Hosting**: Vercel Serverless Functions

## 💡 Uso de la Aplicación

1. **Accede a tu URL**: `https://tu-app.vercel.app`
2. **Arrastra tu PDF** o haz click para seleccionar
3. **Click en "Procesar"**
4. **Obtén resultados**:
   - Resumen ejecutivo
   - Tabla de conciliación
   - Exportación en múltiples formatos

## 📊 Ejemplo de Procesamiento

La aplicación extrae y procesa:

- ✅ Total Presentado (Venta Bruta)
- ✅ Aranceles y costos operativos
- ✅ IVA (s/Arancel + Percepciones)
- ✅ IIBB (Retenciones + Percepciones SIRTAC/QR)
- ✅ Retenciones de Ganancias
- ✅ Neto de Pagos (A Cobrar)
- ✅ Estado de Conciliación

## 🔒 Seguridad

- ✅ PDFs procesados en memoria (no se guardan)
- ✅ Sin base de datos
- ✅ HTTPS automático (Vercel)
- ✅ Sin tracking ni cookies

## ⚡ Rendimiento

- Procesamiento: < 3 segundos
- Límite de archivo: 10 MB
- Hosting: CDN global de Vercel
- Disponibilidad: 99.9%

## 📞 Soporte

Para problemas o mejoras, consulta la documentación completa en el repositorio.

## 📝 Licencia

Proyecto de uso interno profesional.

---

## 🎉 ¡Felicitaciones!

Tu aplicación está lista para producción. Solo falta ejecutar:

```bash
vercel deploy --prod
```

Y obtendrás tu URL pública en segundos. 🚀
