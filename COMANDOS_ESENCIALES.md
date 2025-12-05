# 📋 COMANDOS ESENCIALES - Cheat Sheet

## 🚀 Despliegue Inicial (Primera Vez)

```bash
# 1. Instalar Vercel CLI
npm install -g vercel

# 2. Login
vercel login

# 3. Ir a la carpeta del proyecto
cd webapp_vercel

# 4. Desplegar a producción
vercel --prod
```

**✅ Resultado:** Tu app estará en `https://[nombre].vercel.app`

---

## 🔄 Actualizar la Aplicación

```bash
# Redesplegar después de hacer cambios
vercel --prod
```

---

## 📊 Monitoreo y Logs

```bash
# Ver logs en tiempo real
vercel logs --follow

# Ver logs de producción
vercel logs --prod

# Ver logs de las últimas 24 horas
vercel logs --since 24h

# Ver lista de deployments
vercel ls

# Ver información del proyecto
vercel inspect
```

---

## 🌐 Gestión de Dominios

```bash
# Ver dominios configurados
vercel domains ls

# Agregar dominio personalizado
vercel domains add tudominio.com
```

---

## 🔧 Configuración

```bash
# Ver variables de entorno
vercel env ls

# Agregar variable de entorno
vercel env add VARIABLE_NAME production

# Ver información de la cuenta
vercel whoami

# Ver versión de Vercel CLI
vercel --version
```

---

## 🗑️ Limpieza

```bash
# Eliminar un deployment específico
vercel rm [deployment-url]

# Eliminar proyecto completo
vercel remove [project-name]
```

---

## 🆘 Ayuda

```bash
# Ayuda general
vercel --help

# Ayuda de un comando específico
vercel deploy --help
vercel logs --help
vercel env --help
```

---

## 🔗 URLs Importantes

| Acción | URL |
|--------|-----|
| Dashboard | https://vercel.com/dashboard |
| Documentación | https://vercel.com/docs |
| Estado del servicio | https://vercel-status.com |
| Comunidad | https://github.com/vercel/vercel/discussions |

---

## 💡 Tips Rápidos

### Ver URL de tu app
```bash
vercel ls
# O visita: https://vercel.com/dashboard
```

### Deployment de prueba (no producción)
```bash
vercel
# Crea una URL de preview
```

### Rollback a versión anterior
```bash
# En el dashboard:
# 1. Deployments → Selecciona versión anterior
# 2. Click en menú (...) → Promote to Production
```

### Ver estadísticas
```bash
# Dashboard → Tu Proyecto → Analytics
```

---

## 🎯 Workflow Completo

```bash
# 1. Primera vez (setup)
npm install -g vercel
vercel login
cd webapp_vercel
vercel --prod

# 2. Desarrollo local (opcional)
python api/index.py
# Abrir: http://localhost:5000

# 3. Hacer cambios en el código
# (editar archivos...)

# 4. Redesplegar
vercel --prod

# 5. Verificar
vercel logs --prod
```

---

## 🚨 Solución Rápida de Problemas

| Error | Solución |
|-------|----------|
| `Command not found: vercel` | `npm install -g vercel` |
| `No token found` | `vercel login` |
| Build failed | `vercel logs` para ver detalles |
| 500 Error | `vercel logs --prod` |
| Python error | Verificar `requirements.txt` |

---

## 📞 Soporte

- **Logs en vivo:** `vercel logs --follow`
- **Dashboard:** https://vercel.com/dashboard
- **Docs:** https://vercel.com/docs
- **GitHub:** https://github.com/vercel/vercel

---

## 🎓 Comandos Avanzados

```bash
# Deployment con nombre específico
vercel --name mi-conciliacion --prod

# Deploy desde subdirectorio
vercel ./webapp_vercel --prod

# Ver límites de uso
vercel teams ls
# Luego en dashboard → Settings → Usage

# Configurar alias
vercel alias [deployment-url] mi-alias.vercel.app
```

---

**💾 Guarda este archivo** para consulta rápida. ¡Todo lo que necesitas en una página!
