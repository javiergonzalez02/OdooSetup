# GUÍA BÁSICA DE USO

NOTA: Se deberán seguir estos pasos independientemente de la opción de instalación que se haya escogido.

1. Crear el archivo .env a partir de .env.example:

- En unix:
```
cp .env.example .env
```

- En Windows:
```
copy .env.example .env
```

Una vez hecho, se debe editar los usuarios y contraseñas al gusto. Se recomienda solo editar las contraseñas

2. Una vez se ha establecido el entorno para docker, se usarán los siguientes comandos:

- Para levantar los contenedores: 
``` bash
docker compose up
```

- Para eliminar tanto contenedores como volúmenes en caso de error:
``` bash
docker compose down -v
```

3. En caso de que se quiera utilizar la base de datos con el set up inicial, se debe restaurar la base de datos desde la copia de seguridad:
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
  - Obtén el ID del contenedor db con el comando:
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

[Ejemplo Importación Base de Datos](ejemploImportacionDB.png)

- Usuario para iniciar sesión:
  - Correo: admin
  - Contraseña: 1234

- NOTA: Se recomienda crear la base de datos desde 0 ya que la instalación de los módulos es muy simple

4. Estando el contenedor levantado, se podrá acceder a la insterfaz de odoo a través del siguiente link: http://localhost:8069/

- En caso de que se opte por crear la base de datos desde 0, aparecerá la siguiente ventana:

[Creación Base de Datos](setUpDbOdoo.png)

Se deberá establecer el usuario, contraseña, correo, master password e idioma. Una vez hecho eso, nos redirigirá a la página de inicio de sesión.

[Inicio de Sesión](inicioSesion.png)

- En el caso de que se haya importado la base de datos aparecerá la siguiente pantalla, donde podremos importar la base de datos ya creada llamada odoo. Simplemente deberemos seleccionarla y nos llevará al inicio de sesión como en la otra manera.

[Selección Base de Datos](inicioSesion.png)

5. Una vez dentro de la app, aparecerá la siguiente interfaz. Donde se podrá instalar las aplicaciones que se requieran pulsando el botón activar:

[Pantalla Apps](pantallaApps.png)

En el icono de arriba a la izquierda podremos elegir a que aplicación queremos ir, siendo bastante intuitivo.

[Menu Apps](menuApps.png)

6. Para hacer una copia de seguridad de la base de datos, se deberán seguir los siguientes pasos:

1º **Crear la copia de seguridad con `pg_dump`:**
    - Conéctate al contenedor de la base de datos:
      ```bash
      docker compose exec db bash
      ```
    - Parar el servicio de postgres:
      ```bash
      service postgresql stop
      ```
    - Dentro del contenedor crea la copia de seguridad:
      ```bash
      pg_dump -U odoo odoo > backup.sql
      ```
    - Volver a iniciar el servicio de postgres:
      ```bash
        service postgresql start
        ```
    - Sal del contenedor:
      ```bash
      exit
      ```
    - Apaga el contenedor
   
2º **Copiar el archivo de copia de seguridad a la máquina anfitriona:**
    - Usa el siguiente comando cambiando ruta por la ruta donde quieras guardar el archivo:
    ```bash
    docker compose cp db:./backup.sql ./ruta/backup.sql
    ```
    - 

3º **Eliminar los contenedores y limpiar los directorios mapeados:**
    ```bash
    docker compose down -v
    sudo rm -rf dataPG/* sessions/* filestore/* addons/*
    ```