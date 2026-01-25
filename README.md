# enlace_reunion

Una aplicación web estática que proporciona acceso centralizado a enlaces de reuniones religiosas y contenido de video para la congregación.

## 📋 Descripción

**enlace_reunion** es una página web simple y elegante diseñada para facilitar el acceso a:
- **Reuniones en vivo**: Enlace de Zoom para las reuniones de miércoles y domingos
- **Asamblea de Circuito 2026**: Cuatro sesiones de video de la asamblea "Tienen que adorarlo con espíritu y con verdad"

## 🚀 Características

- **Diseño Responsivo**: Adaptado para móviles, tablets y escritorio
- **Interfaz Moderna**: Diseño basado en tarjetas con efectos hover y gradientes
- **Accesibilidad**: Etiquetas ARIA, estados de enfoque y soporte para movimiento reducido
- **Sin Dependencias**: HTML5 puro con CSS integrado
- **Contenedor Docker**: Fácil despliegue con Docker y Docker Compose

## 🛠️ Stack Tecnológico

- **Frontend**: HTML5 + CSS3 (sin frameworks de JavaScript)
- **Tipografía**: Inter (Google Fonts)
- **Despliegue**: Docker (base image: `lipanski/docker-static-website`)
- **Orquestación**: Docker Compose

## 📁 Estructura del Proyecto

```
enlace_reunion/
├── index.html          # Archivo HTML principal con CSS integrado
├── Dockerfile          # Configuración de Docker para sitio estático
├── docker-compose.yml  # Configuración de Docker Compose
└── README.md           # Documentación del proyecto
```

## 🏃 Instalación y Uso

### Requisitos Previos

- Docker
- Docker Compose

### Despliegue Local

1. Clonar el repositorio:
```bash
git clone <repository-url>
cd enlace_reunion
```

2. Iniciar el contenedor:
```bash
docker-compose up
```

3. Acceder a la aplicación:
```
http://localhost:3000
```

### Detener el Contenedor

```bash
docker-compose down
```

## 🎨 Diseño

### Paleta de Colores

- **Fondo**: `#eef2ff` (azul claro)
- **Superficie**: `#ffffff` (blanco)
- **Primario**: `#1d4ed8` (azul)
- **Texto Primario**: `#0f172a` (gris oscuro)
- **Texto Secundario**: `#334155` (gris medio)

### Puntos de Quiebre (Breakpoints)

- **Desktop**: > 720px
- **Tablet**: 520px - 720px
- **Móvil**: < 520px

## 📱 Contenido

### Secciones

1. **Reuniones en vivo**
   - Enlace de Zoom para reuniones de miércoles y domingos

2. **Asamblea de Circuito 2026**
   - Mañana - Parte 1
   - Mañana - Parte 2
   - Tarde - Parte 1
   - Tarde - Parte 2

Todos los enlaces externos se abren en nuevas pestañas con atributos de seguridad apropiados.

## 🔧 Configuración

### Puerto

Por defecto, la aplicación se ejecuta en el puerto **3000**. Para cambiar el puerto, modifique el archivo [`docker-compose.yml`](docker-compose.yml:5):

```yaml
ports:
  - "PUERTO_DESEADO:3000"
```

## 🌐 Enlaces Externos

- **Zoom**: Reuniones en vivo
- **CDN**: Videos de la asamblea (alojados en poyiya-net.b-cdn.net)

## 📄 Licencia

Este proyecto es de uso interno para la congregación.

## 👥 Contribuciones

Para sugerencias o mejoras, contacte al administrador del proyecto.

---

**Última actualización**: Enero 2026
