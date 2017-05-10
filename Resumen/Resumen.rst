Resumen
=====

Resumen
------------

El objetivo de la presente tesina consiste en estudiar el software disponible para registro de distintos tipos de fallas sobre senderos viales, dispositivos hardware y herramientas de software asociadas al sensado de las mismas, y técnicas para el reconocimiento y clasificación de las muestras de fallas capturadas.

Con respecto al software para el registro de fallas sobre senderos viales, se expondrá de manera breve la terminología relacionada a los distintos tipos de fallas, y  desarrollos software relacionados con el sensado y registro de fallas en sistemas de información.

En cuanto a dispositivos hardware, se estudiarán distintos tipos de sensores para el relevamiento de superficies, características principales y funcionamiento.
Asimismo,se investigarán los lenguajes de programación disponibles, librerías, herramientas y disponibilidad en distintos sistemas operativos.       

Además, se expondrán las técnicas de filtrado y clasificación empleadas para el análisis de distintos tipos de falla, antecedentes históricos, y proyectos de similares características.      

Finalmente, se realizará el desarrollo de una aplicación cliente que permita la captura de distintos tipos de fallas (registrados previamente en un servidor),por medio del sensor Kinect. Esta aplicación será capaz de interactuar con una aplicación web para obtener información respecto de la ubicación de las fallas informadas por usuarios en la misma.Ésto le permitirá realizar capturas asociadas a tipos de fallas informadas previamente, y posteriormente, cargarlas en la misma para su visualización.
También, esta aplicación permitirá registrar en la aplicación web aquellas fallas descubiertas durante un recorrido (sin registro previo),obteniendo la latitud y longitud de la falla y enviándolas a la aplicación web, para la estimación de su dirección aproximada.
Por último, se emplearán filtros y mecanismos de machine learning ofrecidos por por la librería Point Cloud Library(PCL), para el aislamiento y la clasificación de los tipos de fallas "Bache" y "Grieta".