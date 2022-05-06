# Práctica 3. Experimentación con Arduino
## Grado en Ingeniería Informática. Prácticas para la asignatura Periféricos y Dispositivos de Interfaz Humana

**Autor: Antonio Galera Gázquez**
**Contacto: agalera13@correo.ugr.es ó @galera115 en GitHub**

# Índice
1. [Introducción](#introducción)
2. [Instalación](#instalación)
3. [Arduino](#arduino)
4. [Led Básico](#led-básico)
5. [Semáforo](#uso-de-mediapipe)
6. [Semáforo con botón](#resultados)
7. [El Coche Fantástico](#conclusiones)
8. [Pantalla LCD]()

## Introducción
Arduino es una compañía que se dedica a la producción de software y hardware libres, su principal producto son las placas de microcontoladores, aunque al ser libres ellos las diseñan para que cualquier persona o empresa sea capaz de fabricar las placas de Arduino. Detrás de la compañía se encuentra una gran comunidad de desarrolladores que crean numerosas aplicaciones con estas placas ya que las posibilidades que ofrecen son casi infinitas. Tendremos tantas posibilidades ya que si bien las placas y el lenguaje de programación que utilizan son bastante sencillos, poseen una larga lista de complementos para utilizar con las placas.

Una de sus mayores ventajas es que son sumamente accesibles, tienen precios competitivos, suelen venir en packs con todos los componentes y complementos necesarios para realizar una gran cantidad de proyectos, y sobre todo que es muy sencillo de utilizar, es solamente instalar el IDE, escribir código en un lenguaje sumamente sencillo para alguien nuevo en el mundillo, conectar los componentes en una placa de conexiones y tras conectarla por USB al ordenador ver cómo funciona. Esta sencillez de uso también tiene que ver con la gran comunidad que hay detrás de ella ya que si buscamos por internet veremos que hay numerosos tutoriales de proyectos para realizar.

## Instalación

Para la mayoría de Sistemas Operativos encontraremos el software en la página de [Arduino](https://www.arduino.cc/en/software)

+ Windows. Instalar el fichero .exe

+ En MacOs. Descargamos el fichero para MacOS y ejecutamos este mismo, una vez hecho esto nos especificará las instrucciones.

+ Familia de Linux. Tenemos una AppImage para poder instalarlo en cualquier sistema operativo de la familia o un script de shell para ejecutar desde la terminal. En estos sistemas operativos será importante añadir el usuario a un grupo de usuarios y luego reiniciar el equipo. Para añadirlo escribiremos en la terminal:
    `
    sudo usermod -a -G dialout <username>
    `
Donde \<username\> será nuestro usuario

## Arduino
Tenemos:
+ Una placa Arduino Uno.
+ Bastantes resistencias de distintos valores
+ LEDs
+ Pantalla LCD
+ Potenciómetro de 10k
+ "Altavoz"

Con estos componentes y código podremos crear numerosos proyectos que se muestran a continuación

## Led Básico

## Semáforo
En este proyecto conectaremos tres LEDs de los siguientes colores: rojo, amarillo y verde. Estos LEDs tendrán que estar conectados a una resistencia y a tierra(GND). La idea es simular el funcionamiento de un semáforo para ello se iluminarán los LEDs de forma alternativa. El código para este funcionamiento es el siguiente:

