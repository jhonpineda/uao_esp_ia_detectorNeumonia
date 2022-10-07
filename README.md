# Herramienta de detección de Neumonía con Microservicios

## Integrantes:

Nombre: Jhon Harold Pineda Dorado
Cédula: 97435193
Código: 2220156

Nombre: Harold Muñoz
Cédula: 97397310
Código: 2221845


Definición: Herramienta para la detección rápida de neumonía con base en imagenes radiológicas.

## Diseño:

Lo compone una interfaz de usuario y dos microservicios (cada uno con un .proto). Todos se despliegan en un contenedor independiente.

La interfaz de usuario se diseñó para que la imagen se visualizara dentro de la ventana, dos textbox para que muestre el resultado y la predicción, asi como dos botones para Cargar la imagen y otro para Predecir.

En la imagen UI.JPG podrá visualizar el "look and feel".

Para un mejor entendimiento del funcionamiento se adjunta un diagrama de secuencia (Diagrama_Secuencia.jpeg)

## Requisitos:

- Docker

- Docker compose

## Instalación:

Se describen los pasos a seguir para la instalación en ambiente Windows:

1. Clonar el proyecto de esta rama desde github.

2. Crear o modificar la ruta de los volúmenes: Para este proyecto se usa la carpeta "D:\tmp" (internamente vinculada a home/images).

3. Abrir el programa "VcXsrv\xlaunch.exe" o sino instalarlo desde la siguiente ruta:

https://dev.to/darksmile92/run-gui-app-in-linux-docker-container-on-windows-host-4kde

4. Abrir una terminal (CDM) y ejecutar la sentencia de docker dentro de la carpeta del proyecto:

docker-compose up



# Creditos
Arturo Duque [repo GRPC_example](https://github.com/woodElec/grpc_example)