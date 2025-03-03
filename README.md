# EXPLICACIÓN DE CÓMO INSTALAR ODOO

## VAGRANT (RECOMENDADO EXCLUSIVAMENTE PARA DESARROLLO DE MÓDULOS)

[VER EXPLICACIÓN](./VagrantDev/README.md)

## ODOO CON DOCKER DESKTOP INSTALADO EN WINDOWS, LINUX O MAC

1. Dirigirse a la carpeta ./WindowsUnixDev para desarrollo o ./WindowsUnixProd para producción

2. Ejecutar los comandos:

- Para levantar los contenedores: 
``` bash
docker compose up
```

- Para eliminar tanto contenedores como volúmenes en caso de error:
``` bash
docker compose down -v
```