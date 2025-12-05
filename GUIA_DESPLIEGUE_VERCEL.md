# 📘 Guía Completa de Despliegue en Vercel

## 🎯 ¿Qué es Vercel?

Vercel es una plataforma de hosting moderna que:
- ✅ **Despliega en segundos** con un solo comando
- ✅ **HTTPS automático** y certificados SSL gratis
- ✅ **CDN Global** para velocidad máxima
- ✅ **Serverless Functions** para el backend Python
- ✅ **Plan gratuito** generoso (100 GB bandwidth/mes)
- ✅ **Zero Configuration** - detecta automáticamente Flask

## 🚀 Método 1: CLI - Despliegue Instantáneo (⏱️ 5 min)

### Paso 1: Instalación de Vercel CLI

**En Windows:**
```bash
# Opción A: Con npm (requiere Node.js)
npm install -g vercel

# Opción B: Con Chocolatey
choco install vercel-cli
```

**En macOS:**
```bash
# Opción A: Con npm
npm install -g vercel

# Opción B: Con Homebrew
brew install vercel-cli
```

**En Linux:**
```bash
# Con npm
npm install -g vercel
```

### Paso 2: Login en Vercel

```bash
vercel login
```

Opciones de login:
- GitHub
- GitLab
- Bitbucket
- Email

**Recomendación**: GitHub para integración continua

### Paso 3: Navegar al Proyecto

```bash
cd webapp_vercel
```

### Paso 4: Despliegue a Producción

```bash
vercel --prod
```

**¡Eso es TODO!** 🎉

Vercel detectará automáticamente:
- `vercel.json` → Configuración
- `requirements.txt` → Dependencias Python
- `api/index.py` → Serverless Function
- `templates/` → Frontend

### Resultado Esperado

```
✅ Production: https://tu-proyecto-abc123.vercel.app [1s]
📝 Deployed to production
🔗 https://tu-proyecto.vercel.app
```

---

## 🐱 Método 2: GitHub - Despliegue Continuo (⏱️ 10 min)

### Paso 1: Subir a GitHub

```bash
# Inicializar Git
git init

# Agregar archivos
git add .

# Commit
git commit -m "Sistema de Conciliación Listo"

# Crear repo en GitHub (en la web)
# Luego conectar:
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git push -u origin main
```

### Paso 2: Importar en Vercel

1. Ve a [vercel.com/new](https://vercel.com/new)
2. Click en "Import Git Repository"
3. Selecciona tu repositorio
4. Vercel detectará la configuración automáticamente
5. Click en "Deploy"

### Paso 3: Configuración Automática

Vercel detecta automáticamente:
- Framework: Flask (Python)
- Build Command: (no necesario)
- Output Directory: `api`
- Install Command: `pip install -r requirements.txt`

**¡No cambies nada!** La configuración es perfecta.

### Ventajas del Método GitHub

✅ **Deploy Automático**: Cada `git push` despliega automáticamente  
✅ **Preview URLs**: Cada branch tiene su URL de prueba  
✅ **Rollback Fácil**: Volver a versión anterior en 1 click  
✅ **Team Collaboration**: Múltiples desarrolladores  

---

## 🔧 Método 3: Despliegue Manual sin Git (⏱️ 3 min)

Para quienes NO usan Git/GitHub:

```bash
# 1. Instalar CLI
npm install -g vercel

# 2. Login
vercel login

# 3. En la carpeta del proyecto
cd webapp_vercel

# 4. Desplegar (modo interactivo)
vercel

# 5. Responder preguntas:
# ¿Set up and deploy? → Y
# ¿Link to existing project? → N
# ¿Project name? → conciliacion-tarjetas (o el nombre que quieras)
# ¿Directory? → ./ (actual)
# ¿Override settings? → N

# 6. Desplegar a producción
vercel --prod
```

---

## ⚙️ Verificación Post-Despliegue

### 1. Verificar que la app funciona

```bash
# Tu URL será algo como:
https://conciliacion-tarjetas-abc123.vercel.app
```

**Prueba:**
1. Abre la URL en el navegador
2. Deberías ver la interfaz de carga de PDFs
3. Arrastra un PDF de prueba
4. Verifica que procese correctamente

### 2. Verificar Logs (si hay problemas)

```bash
vercel logs
```

O en el dashboard: [vercel.com/dashboard](https://vercel.com/dashboard)

### 3. Verificar Configuración

En el dashboard de Vercel:
- **Settings** → **Functions**: Python 3.9
- **Settings** → **Environment Variables**: (ninguna necesaria)
- **Deployments**: Ver historial

---

## 🎨 Personalización de Dominio

### Opción 1: Subdominio Vercel Gratis

Ya lo tienes: `tu-proyecto.vercel.app`

### Opción 2: Dominio Personalizado

En el dashboard de Vercel:

1. **Settings** → **Domains**
2. Click en "Add Domain"
3. Ingresa tu dominio: `conciliacion.tuempresa.com`
4. Sigue las instrucciones DNS

**Ejemplo de DNS:**
```
Type: CNAME
Name: conciliacion
Value: cname.vercel-dns.com
```

---

## 📊 Monitoreo y Analytics

### Analytics Integrado (Gratis)

Vercel incluye analytics básico:
- Visitas por día
- Top páginas
- Tiempo de carga
- Ubicación geográfica

**Activar:**
1. Dashboard → Tu Proyecto
2. **Analytics** → Enable

### Logs en Tiempo Real

```bash
# Ver logs en vivo
vercel logs --follow

# Logs de producción
vercel logs --prod

# Logs recientes
vercel logs --since 1h
```

---

## 🔒 Seguridad y Variables de Entorno

### Agregar Variables de Entorno (si las necesitas)

```bash
# Por CLI
vercel env add SECRET_KEY production

# O en el dashboard:
# Settings → Environment Variables
```

Para este proyecto **NO necesitas** variables de entorno.

---

## 🚨 Solución de Problemas Comunes

### Error: "Command not found: vercel"

**Solución:**
```bash
# Reinstalar Vercel CLI
npm install -g vercel

# Verificar instalación
vercel --version
```

### Error: "No token found"

**Solución:**
```bash
# Login nuevamente
vercel login
```

### Error: "Build failed"

**Causa común:** `requirements.txt` mal formateado

**Solución:**
```bash
# Verificar requirements.txt
cat requirements.txt

# Debe contener:
Flask==3.0.0
PyPDF2==3.0.1
Werkzeug==3.0.1
```

### Error 500 en la app

**Verificar logs:**
```bash
vercel logs --prod
```

**Causa común:** Ruta incorrecta de templates

**Solución:** Verificar que `templates/index.html` exista

---

## 📈 Optimización

### 1. Caché de Assets

Ya configurado en `vercel.json`

### 2. Compresión

Vercel comprime automáticamente:
- HTML
- CSS
- JavaScript
- JSON

### 3. CDN Global

Tu app se replica en 20+ regiones:
- América del Norte
- América del Sur
- Europa
- Asia
- Oceanía

---

## 💰 Límites del Plan Gratuito

Vercel ofrece generosamente:

| Recurso | Límite Gratis | ¿Es suficiente? |
|---------|---------------|-----------------|
| Bandwidth | 100 GB/mes | ✅ Sí (≈10,000 PDFs) |
| Builds | 100 builds/día | ✅ Sí |
| Serverless Executions | 100,000/mes | ✅ Sí |
| Function Duration | 10 segundos | ✅ Sí (PDFs < 3s) |
| File Size | 50 MB | ✅ Sí (limite 10MB) |

**Conclusión:** El plan gratuito es MÁS que suficiente para uso normal.

---

## 🔄 Actualizar la Aplicación

### Con GitHub (Deploy Automático)

```bash
# 1. Hacer cambios en el código
# 2. Commit y push
git add .
git commit -m "Mejoras en UI"
git push

# ¡Vercel despliega automáticamente!
```

### Con CLI (Deploy Manual)

```bash
# 1. Hacer cambios
# 2. Redesplegar
vercel --prod
```

---

## 📱 Testing Multi-Dispositivo

Vercel crea **Preview URLs** automáticamente:

```
# URL de producción
https://tu-app.vercel.app

# URL de preview (cada commit)
https://tu-app-git-branch.vercel.app
```

**Probar en:**
- 💻 Desktop (Chrome, Firefox, Safari)
- 📱 Mobile (iOS Safari, Chrome Android)
- 🖥️ Tablet

---

## 🎓 Recursos Adicionales

- [Documentación Vercel](https://vercel.com/docs)
- [Vercel Python Runtime](https://vercel.com/docs/runtimes#official-runtimes/python)
- [Serverless Functions](https://vercel.com/docs/concepts/functions/serverless-functions)
- [Custom Domains](https://vercel.com/docs/concepts/projects/custom-domains)

---

## ✅ Checklist Final

Antes de compartir tu app, verifica:

- [ ] App desplegada: `vercel --prod` ejecutado
- [ ] URL funciona: Abrir en navegador
- [ ] PDF de prueba: Cargar y procesar exitosamente
- [ ] Exportación: Probar CSV, Copiar, Imprimir
- [ ] Mobile: Probar en teléfono
- [ ] Logs limpios: `vercel logs` sin errores

---

## 🎉 ¡Felicitaciones!

Tu aplicación profesional está lista y accesible en Internet.

**URL Final:** `https://[tu-proyecto].vercel.app`

**Tiempo total:** ⏱️ 5 minutos  
**Costo:** 💰 $0 (gratis)  
**Mantenimiento:** 🔧 Cero  
**Escalabilidad:** 📈 Automática  

---

## 🚀 Próximos Pasos Opcionales

1. **Custom Domain**: Configurar `conciliacion.tuempresa.com`
2. **Team Access**: Invitar colaboradores en Vercel
3. **Analytics**: Activar métricas detalladas
4. **Monitoring**: Configurar alertas de errores
5. **CI/CD**: Automatizar tests antes de deploy

---

**¿Necesitas ayuda?** Consulta los logs con `vercel logs` o revisa la [documentación oficial](https://vercel.com/docs).
