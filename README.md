# Instalación y Uso de Odoo

Bienvenido al repositorio para la instalación y uso de Odoo.  
Aquí encontrarás toda la documentación necesaria para:

- Desarrollar módulos usando **Vagrant** (recomendado exclusivamente para desarrollo).
- Instalar Odoo utilizando **Docker** (compatible con Docker Desktop en Windows/Mac y Docker en Linux).
- Conocer el uso básico de Odoo y realizar copias de seguridad.

---

## Índice

- [Primeros pasos](#primeros-pasos)
- [Instalación con Vagrant](#instalación-con-vagrant)
- [Instalación con Docker](#instalación-con-docker)
- [Uso Básico, Debug y Mantenimiento](#uso-básico-y-mantenimiento)
- [Desarrollo de Módulos de Odoo](#desarrollo-de-módulos-de-odoo)
- [Requerimientos mínimos del servidor](#requerimientos-mínimos-del-servidor)

---

## Primeros pasos

Antes de comenzar, asegúrate de obtener el repositorio. Puedes hacerlo de dos formas:

- Con Git (recomendado):
  Ejecuta en tu terminal:

```bash
    git clone https://github.com/javiergonzalez02/OdooSetup
```

- Descarga manual:
Si no tienes Git instalado, descarga el repositorio manualmente:
![Descargar](./docs/capturaDescargarRepo.png)

---

## Instalación con Vagrant

Nota: Esta opción está orientada exclusivamente al desarrollo de módulos.

Para configurar tu entorno de desarrollo con Vagrant, consulta la guía completa: 
[VER EXPLICACIÓN](./docs/VagrantSetupOdoo.md)

---

## Instalación con Docker

Requisitos:

- Windows/Mac: Docker Desktop
- Linux: Docker Engine

Para obtener la guía detallada, revisa:

[VER EXPLICACIÓN](./docs/DockerOdooSetup.md)

---

## Uso Básico, Debug y Mantenimiento

Esta sección explica cómo utilizar Odoo, hacer debug con VsCode y realizar tareas de mantenimiento, incluyendo la realización de copias de seguridad.

Consulta la guía completa en:
[VER EXPLICACIÓN](./docs/UsoYMantenimiento.md)

---

## Desarrollo de Módulos de Odoo

Para conocer a fondo el desarrollo de módulos de Odoo, referirse a la carpeta [presentaciones](./presentaciones/)

---

## Requerimientos Mínimos del Servidor

> **Nota:** Se recomienda un sistema Linux (Debian o Ubuntu). Si no se dispone de él, se puede usar Vagrant para emularlo.

### Dimensión según número de usuarios

| Concepto | Cálculo | Descripción |
|----------|---------|-------------|
| **Workers** | 1 worker por cada 6 usuarios concurrentes | Se define en `docker-compose.yml` con el parámetro `--workers=`. |
| **CPUs** | `(Workers − 1) ÷ 2` → redondear al entero superior | Basado en la regla óptima: `(NumCPUs × 2) + 1 = Workers`. |
| **RAM** | `Workers × (0.8 × 150 MB + 0.2 × 1024 MB)` | 80 % de memoria para procesos ligeros, 20 % para procesos pesados. |

---

### Ejemplo

**60 usuarios concurrentes**:

1. **Workers**  
   \- Cálculo: `60 ÷ 6 = 10 workers`  
2. **CPUs**  
   \- Fórmula invertida: `(10 − 1) ÷ 2 = 4.5` → **5 CPUs** (redondeo al alza)  
3. **RAM**  
   \- Cálculo: `10 × (0.8 × 150 MB + 0.2 × 1024 MB)`  
   \- Paso intermedio: `0.8×150 MB = 120 MB`; `0.2×1024 MB = 204.8 MB`  
   \- Total por worker: `120 MB + 204.8 MB ≈ 324.8 MB`  
   \- Memoria total: `10 × 324.8 MB ≈ 3 248 MB` → **3.2 GB RAM**

---
### Requisitos mínimos resumidos

| Usuarios concurrentes | Workers | CPUs | RAM aproximada  |
|-----------------------|:-------:|:----:|----------------:|
| 6                     | 1       | 1    | 325 MB          |
| 12                    | 2       | 2    | 650 MB          |
| 18                    | 3       | 2    | 975 MB          |
| 24                    | 4       | 2    | 1.3 GB          |
| 30                    | 5       | 3    | 1.6 GB          |
| 36                    | 6       | 3    | 1.9 GB          |
| 42                    | 7       | 4    | 2.3 GB          |
| 48                    | 8       | 4    | 2.6 GB          |
| 54                    | 9       | 5    | 2.9 GB          |
| 60                    | 10      | 5    | 3.2 GB          |
