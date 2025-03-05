1. Dirigirse a la carpeta ./WindowsUnixDev para desarrollo o ./WindowsUnixProd para producción

2. Crear el archivo .env a partir de .env.example:

- En unix:
```
cp .env.example .env
```

- En Windows:
```
copy .env.example .env
```

Una vez hecho, se debe editar los usuarios y contraseñas al gusto. Se recomienda solo editar las contraseñas

3. Ejecutar los comandos:

- Para levantar los contenedores: 
``` bash
docker compose up
```

- Para eliminar tanto contenedores como volúmenes en caso de error:
``` bash
docker compose down -v
```

4. En caso de que se quiera utilizar la base de datos con el set up inicial, se debe restaurar la base de datos desde la copia de seguridad:
    - Entra al contenedor de la base de datos:
      ```bash
      docker compose exec db bash
      ```
    - Crea una nueva base de datos vacía:
      ```bash
      createdb -U odoo -O odoo odoo
      ```
    - Sal del contenedor:
      ```bash
      exit
      ```
    - Obtén el ID del contenedor con el comando:
      ```bash
      docker ps
      ```
    - Copia el archivo de respaldo de vuelta al contenedor:
      ```bash
      docker cp ./initial_setup.sql <ID_CONTENEDOR>:/
      ```
    - Vuelve a entrar y restaura la copia de seguridad:
      ```bash
      psql -U odoo -d odoo < ./initial_setup.sql
      ```
    - Sal del contenedor:
      ```bash
      exit
      ```

5. Estando el contenedor levantado, se podrá acceder a la insterfaz de odoo a través del siguiente link: http://localhost:8069/