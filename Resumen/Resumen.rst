Resumen
=======

Resumen
-------

.. El objetivo de la presente tesina consiste en estudiar el software disponible para registro de distintos tipos de fallas sobre senderos viales, dispositivos hardware y herramientas de software asociadas al sensado de las mismas, y técnicas para el reconocimiento y clasificación de las muestras de fallas capturadas.

El objetivo de la presente tesina consiste en incorporar a un sistema de detección de fallas, funcionalidad para el sensado tridimensional de fallas viales, exponiendo software disponible para registro de distintos tipos de fallas sobre senderos viales, dispositivos hardware y herramientas de software asociadas al sensado de las mismas, y técnicas para el reconocimiento y clasificación de las muestras de fallas capturadas.

Con respecto al software para el registro de fallas sobre senderos viales, se expondrá de manera breve la terminología relacionada a los distintos tipos de fallas, y  desarrollos software relacionados con el sensado y registro de fallas en sistemas de información.

En cuanto a dispositivos hardware, se estudiarán distintos tipos de sensores para el relevamiento de superficies, características principales y funcionamiento.
Asimismo,se investigarán los lenguajes de programación disponibles, librerías, herramientas y disponibilidad en distintos sistemas operativos.Adicionalmente, se incluirán las utilidades de software para obtención de latitud y longitud con un dispositivo compatible con GPS, y las librerías web que permiten obtener datos de la dirección estimada asociada a dichas coordenadas.

Además, se expondrán las técnicas de filtrado y clasificación empleadas para el análisis de distintos tipos de falla, antecedentes históricos, y proyectos de similares características.      

Finalmente,se realizarán modificaciones a una aplicación web previamente desarrollada, con el fin de incluir la visualización de distintos tipos de falla en un navegador, el filtrado de distintos tipos de fallas sobre una calle determinada, y la estimación de la dirección aproximada de una falla, basándose en la latitud y longitud.
Además,se realizará el desarrollo de una aplicación cliente que permita la captura de distintos tipos de fallas por medio del sensor Kinect. Ésta será capaz de interactuar con la aplicación web, para obtener información respecto de la ubicación de las fallas registradas anteriormente por sus usuarios, lo que le permitirá asociar archivos de capturas a las mismas.
También, la aplicación cliente permitirá registrar en la aplicación web aquellas fallas descubiertas durante un recorrido (sin registro previo),obteniendo la latitud y longitud de la falla por medio de un GPS, para luego realizar una estimación de la dirección en la aplicación web. Posteriormente, se podrá realizar una selección de las todas las fallas capturadas y realizar la subida de las mismas con sus archivos de capturas al servidor, desde la aplicación cliente.
Por último, se desarrollará un script separado, que utilizará los filtros y mecanismos de machine learning ofrecidos por la librería Point Cloud Library(PCL), para el aislamiento y la clasificación de los tipos de fallas "Bache" y "Grieta".

