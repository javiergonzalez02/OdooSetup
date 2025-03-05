# ENTORNO DE DESARROLLO DE ODOO CON VAGRANT

1. INSTALACIÓN DE VAGRANT.
Guía de instalación oficial: https://developer.hashicorp.com/vagrant/downloads

Se deberá escoger la opción que se ajuste al sistema operativo que se esté usando. Permite tanto macOS, Windows o Linux.

2. INSTALACIÓN DE VIRTUAL BOX. Link oficial: https://www.virtualbox.org/wiki/Downloads

Se deberá escoger una opción de entre las siguientes.

![Instalación Virtual Box](./virtualBoxInstall.png)

3. Crear el archivo .env a partir de .env.example:

- En unix:

```
cp .env.example .env
```

- En Windows:

```
copy .env.example .env
```

Una vez hecho, se debe editar los usuarios y contraseñas al gusto. Se recomienda solo editar las contraseñas

4. En la carpeta en la que se encuentra el archivo 'Vagrantfile'. En este proyecto será la carpeta VagrantDev (En la cual se encuentra este documento). Ejecuta los siguientes comandos:

- Este comando levantará la Máquina virtual (La primera vez puede tardar unos minutos. Y es posible que, dependiendo de tu ordenador, debas abrir la aplicación de Virtual Box)
``` bash
vagrant up
```

- Este comando dará acceso a la Máquina Virtual a través de terminal
``` bash
vagrant ssh
```

4. Una vez dentro, se deberá acceder a la carpeta 'OdooSetup'. Y desde esta correr los siguientes comandos:

``` bash
cd OdooSetup/
```

- Para levantar los contenedores: 
``` bash
docker compose up
```

- Para eliminar tanto contenedores como volúmenes en caso de error:
``` bash
docker compose down -v
```

5. En caso de que se quiera utilizar la base de datos con el set up inicial, se debe restaurar la base de datos desde la copia de seguridad:
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

6. Estando el contenedor levantado, se podrá acceder a la insterfaz de odoo a través del siguiente link: http://localhost:8069/