Introducción
============

Objetivo general
----------------

Extender un sistema de notificación y administración de información pertinente a irregularidades en superficies viales, por medio del censado visual tridimensional semiautomático de información vial, con el fin de contribuir a la toma de decisiones respecto del estado de los circuitos viales.

Objetivos específicos
---------------------

* Desarrollar un servicio web para el almacenamiento de capturas realizadas por el sensor desde el aplicativo de captura.
* Procesar la información tridimensional contenida en un archivo con el fin de identificar las diferentes propiedades  y clasificar el tipo de falla capturada.
* Implementar una aplicación que permita la captura tridimensional, en un formato especificado por el sensor Kinect, y su posterior carga por medio del servicio web.
* Integrar el servicio web de almacenamiento de capturas a la aplicación web de gestión de fallas para su visualización en línea.


Motivación
------------

El sensor Kinect desarrollado por Microsoft, es un sensor de detección de movimiento que permite la interacción usuario-dispositivo sin la necesidad de controles adicionales. Este sensor, ofrece una amplia gama de características entre las que se destacan una cámara RGB de 640x480 px a 30 FPS, un emisor y un  sensor infrarrojos, que le permiten obtener información acerca de la profundidad, capacidades de reconocimiento de voz y reconocimiento facial.  Esta amplia variedad de características, sumadas al bajo costo de adquisición, y la disponibilidad de paquetes de código abierto disponibles,  hacen que este dispositivo sea apropiado para la explotación en innovaciones.

Las nuevas tecnologías web y la amplia variedad de dispositivos y conectividad  actual, hacen de Internet una  plataforma computacional  con una gran incidencia en la operación y acceso a la información por parte de las personas. Estas características, sumadas al crecimiento en el uso de estas tecnologías en dispositivos móviles actuales, permiten aumentar la facilidad con la que los usuarios pueden acceder e informar de manera intuitiva, acerca de problemas relacionados a irregularidades en las calles de la ciudad.

La librería Point Cloud Library (PCL), es una herramienta libre, potente y con un gran conjunto de algoritmos para el procesamiento de imágenes y nubes de puntos en 2D/3D. Esta librería reúne investigadores, universidades, compañías e individuos de todo el mundo y se está convirtiendo rápidamente en una referencia para cualquier interesado en el procesamiento 3D y robótica. 

El núcleo de PCL está estructurado en pequeñas librerías y algoritmos para áreas específicas del procesamiento 3D que pueden ser combinadas para resolver problemas como el reconocimiento de objetos, registro de nubes de puntos, segmentación y reconstrucción de superficies facilitando la reutilización de código.

Las irregularidades son una característica común en las rutas y calles pavimentadas de una ciudad lo que genera problemas en el flujo del tráfico y puede ocasionar situaciones de conducción potencialmente peligrosas. Debido a la constante degradación de los diferentes tipos de fallas, estas deben ser detectadas y reparadas tan pronto como sea posible. Existen diferentes formas para la detección de la ubicación y las propiedades de las irregularidades como forma, tamaño, profundidad y volumen,lo que juega un rol importante con respecto a la reparación de las mismas.

La reciente introducción de programación de aplicaciones web en la carrera, requirió introducir personal especializado de la Universidad Nacional del Sur (UNS), y por medio de las prácticas realizadas en esta asignatura, se inició con el desarrollo de un trabajo final que inicialmente georeferenciaba fallas. Ésto dio pie a un proyecto de investigación dirigido por Gabriel Ingravallo (UNPSJB Trelew), y asesorado por Diego C. Martínez (UNS Bahía Blanca)  para la recolección y análisis de fallas viales y que hacía uso del sensor Kinect, del que participaron desde su inicio los presentes tesistas. Sin embargo, el proyecto no cuenta con un mecanismo de análisis y clasificación de diferentes tipos de fallas.

La falta de innovación con respecto al registro y análisis del estado de las vías de circulación de la ciudad y la necesidad de un mecanismo de análisis y clasificación de distintos tipos de fallas en el proyecto de investigación, conforman la principal motivación de esta tesina, que busca extender la funcionalidad de éste, agregando la visualización de las dimensiones de la falla, incluyendo el procesamiento de nubes de puntos para las irregularidades, la clasificación y extracción de sus propiedades relevantes.

Marco teórico
-------------

.. PONER ACA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


Desarrollos propuestos
----------------------

Se propone el desarrollo de una aplicación que haciendo uso de las tecnologías web actuales, permitirá a los actores involucrados en el proceso de mantenimiento de vías de circulación recolectar, procesar y visualizar los diferentes tipos de fallas sobre las distintas calles de la ciudad. Así como, permitir a los habitantes de la ciudad informar y mantenerse informados respecto del estado de las calles.

Con respecto al proceso de recolección  se propone implementar un pequeño aplicativo desarrollado en Python, que junto al sensor Kinect, posibilitará almacenar la nube de puntos censada (que representa una porción de un sendero vial) por el dispositivo. En cuanto al procesamiento, se investigará y experimentará con las técnicas ofrecidas por la librería PCL, que contribuyan a la identificación y delimitación de un tipo de irregularidad dentro de la captura realizada. Una vez identificado el método más conveniente, se desarrollarán varios módulos en C++, interconectados que permitirán la identificación y clasificación del tipo de falla y la extracción de sus propiedades. 

Por último, con respecto a los mecanismos de notificación y visualización, se hará uso de distintas tecnologías web del lado del cliente (Javascript, CSS3, HTML5) que darán el formato a las herramientas ofrecidas para visualizar las fallas, y operará en conjunto con framework PHP (CodeIgniter 2) del lado del servidor.


Resultados esperados
--------------------

Con el desarrollo de la presente tesina, se espera obtener una plataforma que permita mantener informados a los habitantes locales con respecto al estado de las calles de la ciudad a través del acceso a una aplicación web que indique la ubicación de las fallas y el estado actual en el que se encuentran las mismas. Esta a su vez, permitirá a los habitantes informar la localización falla sobre una calle determinada.

Por otro lado, se producirá un módulo de software, que mediante el procesamiento de nubes de puntos tridimensionales posibilite la obtención de una medida objetiva que caracterice distintos tipos de falla. Para ello, se investigará acerca de las estructuras ofrecidas con la librería PCL, y se experimentará con el sensor Kinect, para lograr comprender la estructura interna de una captura realizada por el dispositivo y el funcionamiento de los algoritmos que procesan dicha captura (algoritmos que eliminan el ruido y filtran dicha captura).


Cronograma de actividades
-------------------------

Las actividades que se efectuarán para cumplir con el objetivo de la tesina se detallan enumeradas junto a su número de tarea:

1. Documentar la información técnica durante el desempeño de las tareas.
2. Investigar acerca del funcionamiento del sensor Kinect y los distintos módulos ofrecidos por su SDK bajo Linux.
3. Investigar la librería de procesamiento PCL.
4. Investigar acerca métodos de detección de fallas sobre vías de circulación.
5. Investigar sobre la utilización del sensor Kinect para detección de objetos.
6. Experimentar con la librería PCL y el sensor Kinect acerca de distintos métodos de procesamiento y análisis de nubes de puntos tridimensionales.
7. Desarrollar un módulo en Python para la captura de nubes de puntos.
8. Documentar los pasos requeridos para sanear y detectar una falla en el archivo de nube de puntos.
9. Documentar las técnicas requeridas para delimitar y clasificar un tipo de falla a partir de una nube de puntos.
10. Desarrollar módulos en C++  para el análisis de fallas (el saneamiento, la detección, delimitación y clasificación de los tipos de fallas).
11. Investigar el renderizado de archivos de nubes de puntos con WebGL.
12. Integrar la funcionalidad de la aplicación web con los módulos de procesamiento de nubes de puntos desarrollados.
13. Defensa de la tesina ante mesa examinadora.
