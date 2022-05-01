# Detección de Poses con Mediapipe y OpenCV en Python
## Grado en Ingeniería Informática. Trabajo de Teoría para la asignatura Periféricos y Dispositivos de Interfaz Humana

**Autor: Antonio Galera Gázquez**
**Contacto: agalera13@correo.ugr.es ó @galera115 en GitHub**

# Índice
1. [Introducción](#introducción)
2. [Instalación](#instalación)
3. [OpenCV](#opencv)
   
## Introducción

En este trabajo se utilizarán las APIs de Mediapipe y OpenCV para Python, con el objetivo de realizar detección de poses. 
A lo largo del documento se explicará como proceder a la instalación de los paquetes necesarios(que serán mínimos ya que nos apoyaremos en Google Colab) y el cómo poder obtener unos puntos que definan las poses realizadas por una persona en un vídeo o en una imagen.

Esta herramiento es sumamente interesante ya que puede ser aplicada en numerosos campos, como podría ser los gestos de los deportistas a la hora de realizar deporte, por ejemplo esta técnica es utilizada en corredores de sprint para poder analizar si sus movimientos son adecuados para obtener el mejor tiempo. Otro posible ejemplo son los deportistas de halterofilia, en este deporte es muy importante la postura en el ejercicio para poder llegar al máximo peso y evitar lesiones de gravedad.

Lo bueno de esta herramienta es que nos dará una serie de coordenadas en 3 dimensiones con los que podremos representar la pose de una persona en la imagen o vídeo que queramos. Esta utilidad puede ser de suma relevancia ya que podremos extraer de vídeos o imágenes esas poses, para poder realizar otra serie de tareas de aprendizaje automático.

## Instalación

Como en mi caso se ha utilizado Google Colab solo necesitaremos instalar Mediapipe. Pero en caso de que queramos ejecutarlo en nuestra máquina deberíamos instalar Jupyter y Python junto a su kernel de Jupyter, ya que son notebooks de python donde se encuentra el código.

+ Windows. Nos dirigimos a la página oficial de Python y vamos a [Descargas](https://www.python.org/downloads/windows/). Una vez estamos ahí descargamos el ejecutable de Python 3 que deseamos y lo ejecutamos. Será importante añadir Python al PATH de Windows. Lo siguiente será asegurarnos que tenemos python y pip instalados escribiendo en la terminal
  `
  python3 --version
  pip --version
  `
  
  Si está todo correcto procedemos a instalar jupyter:  `pip install jupyter` y para lanzar jupyter usaremos `jupyter notebook` que nos dará una dirección para abrir en el navegador como localhost.

+ En MacOs. Para instalarlo se va a suponer que se dispone de Homebrew(y si no tienes deberías) para gestionar los paquetes. La instalación de Python será muy sencilla `brew install python3`, para comprobar la instalación podemos hacer igual que con Windows y también para instalar jupyter ya que con pip será similar.

+ Familia de Linux. Lo más seguro es que tengamos alguna versión de Python3 instalada en el ordenador por defecto o que la hayamos instalado previamente, para comprobar esto:
    `
    python3 --version
    pip --version
    `
    Si no nos da ningún error podemos proceder con pip como se ha explicada para Windows y MacOs, en caso de error deberemos usar nuestro gestor de paquetes para instalarlo en sistemas Debian y derivados donde tenemos apt podemos hacer:
    
    `sudo add-apt-repository pp:deadsnakes/ppa`

    `sudo apt-get update`

    `sudo apt-get install python 3.7`


Aparte habrá que instalar las siguientes librerías y sus dependencias: mediapipe, openCV y numpy. Esto se puede realizar con pip de la siguiente forma, con la exclamación para instalarlos desde el notebook(si estamos en terminal serían el mismo comando pero sin esta exclamación):

`
!pip install opencv-python
!pip install mediapipe
!pip install numpy
`

Importante destacar también que si ya están estas librerías instaladas estas líneas no serían necesarias, estas se han dejado por el propio funcionamiento de Colaboratory de Google y es que esta herramiento cargará el Notebook, cada vez que conectemos una sesión ala máquina que nos ha sido asignada y por ello puede que no tengan los paquetes que necesitamos.

## OpenCV

OpenCV es una popular biblioteca libre de inteligencia artificial centrada en el campo de la visión. Se trata de una biblioteca programada en C y C++ con lo que es sumamente eficiente y conveniente ya que en Python poseemos una API que llamará a los métodos escritos en C y C++(más eficientes) y previamente compilados, con lo que tendremos unos resultados muy buenos sin necesidad de una cantidad exagerada de recursos, como ocurre en las redes neuronales más actuales que pueden llegar a necesitar semanas de entrenamiento.

Algunas de las herramientas que ofrece son sistemas de reconocimiento, tracking del movimiento(necesario en este proyecto) y detección y segmentación de objetos(también útiles en este proyecto). También ofrece numerosas herramientas para leer, mostrar y modificar imágenes y vídeos, las cuales utilizaremos para leer y mostrar nuestros resultados.

## MediaPipe

Se trata de una librería de Google que ofrece soluciones multimedia con machine learning fáciles de aplicar, es un producto muy reciente que aún se encuentra en alpha por lo que puede no ser del todo estable aún, aunque como adelanto obtiene muy buenos resultados. Es totalmente gratis y libre de uso y en su propia página encontraremos numerosos ejemplos de como usar la librería. Nos proporcionará numerosas herramientas como:

+ Detección de caras
+ Detección de poses
+ Tracking de objetos en movimiento
+ Tracking de manos

Aparte otras soluciones como segmentación. O algunas de las más recientes como el objectron que es capaz de detectar objetos 3D a partir de la imagen en directo obtenida con un dispositivo móvil. Esto puede ser muy importante en campos como la robótica o la conducción autónoma.

Un uso que podemos darle es el de poder entrenar un modelo en un dataset específico como puede ser las salidas en 100 metros lisos para luego obtener los pesos del entrenamiento y usarlos en una app de Android para que pueda ser utilizada por cualquiera y con un móvil pueda ver si ha realizado o no una buena salida.

## Uso de MediaPipe