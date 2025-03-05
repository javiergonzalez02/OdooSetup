# Entorno de Desarrollo de Odoo con Vagrant

Esta guía te ayudará a configurar tu entorno de desarrollo para Odoo utilizando Vagrant. Sigue los pasos a continuación para instalar Vagrant, VirtualBox y levantar tu máquina virtual.

---

## 1. Instalación de Vagrant

- **Guía oficial de instalación:**  
  [Descargar Vagrant](https://developer.hashicorp.com/vagrant/downloads)  
  Selecciona la versión que se ajuste a tu sistema operativo (macOS, Windows o Linux).

![Instalación Vagrant](./vagrantInstall.png)

---

## 2. Instalación de VirtualBox

- **Página oficial de descargas:**  
  [Descargar VirtualBox](https://www.virtualbox.org/wiki/Downloads)  
  Elige la opción correspondiente a tu sistema.

![Instalación VirtualBox](./virtualBoxInstall.png)

---

## 3. Levantar la Máquina Virtual

1. Navega a la carpeta que contiene el archivo `Vagrantfile`.  
   En este proyecto, se encuentra en la carpeta **VagrantDev** (donde también está este documento).

2. Ejecuta el siguiente comando para iniciar la máquina virtual:  
   *La primera vez puede tardar unos minutos. Dependiendo de tu ordenador, es posible que debas abrir la aplicación de VirtualBox manualmente.*
   ```bash
   vagrant up
   ```

3. Una vez levantada la máquina, accede a ella a través de la terminal:
   ```bash
   vagrant ssh
   ```

---

## 4. Acceso al Entorno de Odoo

Dentro de la máquina virtual, accede a la carpeta `OdooSetup` para continuar con la configuración:
```bash
cd OdooSetup/
```

Para conocer en detalle el uso y mantenimiento, consulta:  
[Ver explicación de uso y mantenimiento](UsoYMantenimiento.md)
