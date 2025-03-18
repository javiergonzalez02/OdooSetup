# Entorno de Desarrollo de Odoo con Vagrant

Esta guía te mostrará cómo configurar tu entorno de desarrollo para Odoo utilizando Vagrant y VirtualBox.

---

## 1. Instalación de Vagrant

- Descarga e instalación: 
  Accede a la [guía oficial de Vagrant](https://developer.hashicorp.com/vagrant/downloads) y selecciona la versión adecuada para tu sistema operativo (macOS, Windows o Linux).

![Instalación Vagrant](./vagrantInstall.png)

---

## 2. Instalación de VirtualBox

- Descarga:
  Visita la [página oficial de VirtualBox](https://www.virtualbox.org/wiki/Downloads) y descarga la versión correspondiente a tu sistema operativo.

![Instalación VirtualBox](./virtualBoxInstall.png)

---

## 3. Levantar la Máquina Virtual

1. Ubicación del Vagrantfile:
    Dirígete a la carpeta **VagrantDev** (donde se encuentra el archivo ``Vagrantfile``).

   ```bash
     cd VagrantDev/
   ```

2. Iniciar la máquina virtual:
    Ejecuta:
   ```bash
   vagrant up
   ```
Nota: La primera ejecución puede tardar varios minutos. En algunos casos, puede ser necesario abrir VirtualBox manualmente.

3. Acceder a la máquina virtual:
    Conéctate mediante SSH:
   ```bash
   vagrant ssh
   ```

4. Cerrar la sesión:
    Cuando termines, escribe:
    ```bash 
     exit
   ```

5. Apagar la máquina virtual:
    Desde el host, ejecuta:
    ```bash 
    vagrant halt
    ```
Alternativamente, puedes apagarla desde la interfaz de VirtualBox: haz clic derecho sobre la máquina, selecciona parar > apagar.

![apagarMaquinaVirtual](/docs/apagarMaquinaVB.png)


En caso de que se necesite más información sobre el uso de Vagrant, se puede referir a la [documentación oficial](https://developer.hashicorp.com/vagrant/docs).

---

## 4. Acceso al Entorno de Odoo

Una vez dentro de la máquina virtual, navega hasta la carpeta `OdooSetup` para continuar la configuración:

   ```bash
     cd OdooSetup/
   ```

Para conocer en detalle el uso y mantenimiento, consulta la sección 
[Uso y mantenimiento](UsoYMantenimiento.md)
