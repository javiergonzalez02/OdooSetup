# ENTORNO DE DESARROLLO DE ODOO CON VAGRANT

1. INSTALACIÓN DE VAGRANT.
Guía de instalación oficial: https://developer.hashicorp.com/vagrant/docs/installation

2. INSTALACIÓN DE VIRTUAL BOX. Link oficial: https://www.virtualbox.org/wiki/Downloads

3. En la carpeta en la que se encuentra el archivo 'Vagrantfile', ejecutar los siguientes comandos:

- Este comando levantará la Máquina virtual
``` bash
vagrant up
```

- Este comando dará acceso a la terminal
``` bash
vagrant up
```

4. Una vez dentro, se deberá acceder a la carpeta 'OdooSetup'. Y desde esta correr los siguientes comandos:

- Para levantar los contenedores: 
``` bash
docker compose up
```

- Para eliminar tanto contenedores como volúmenes en caso de error:
``` bash
docker compose down -v
```

5. Estando el contenedor levantado, se podrá acceder a la insterfaz de odoo a través del siguiente link: http://localhost:8069/