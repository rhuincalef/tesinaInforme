Resumen
=====

Resumen
------------

La presente tesina expondrá los antecedentes con respecto a la recolección semi-automática de fallas en senderos viales por medio del empleo de sensores, y se presentará de manera breve la  terminología relacionada a éstas. Adicionalmente, serán presentados antecedentes históricos y desarrollos, relacionados con el sensado y el registro en sistemas de información de fallas sobre calles y autopistas.

Además, se estudiarán distintos tipos de sensores para el relevamiento de superficies, su funcionamiento, como así también el software disponible para su manipulación.
Asimismo,se investigarán los lenguajes de programación disponibles, librerías, herramientas y el soporte multiplataforma de éstos.       

Adicionalmente, se expondrán distintos mecanismos de filtrado y clasificación usados en distintos estudios, para el saneamiento y reconocimiento de distintos tipos de fallas,en distintos entornos de desarrollo.   

Finalmente, se realizará el desarrollo de una aplicación cliente que permita la captura de distintos tipos de fallas (registrados previamente en un servidor),por medio del sensor Kinect. Esta aplicación será capaz de interactuar con una aplicación web para obtener información respecto de la ubicación de las fallas informadas por usuarios en la misma.Ésto le permitirá realizar capturas asociadas a tipos de fallas informadas previamente, y posteriormente, cargarlas en la misma para su visualización.
También, esta aplicación permitirá registrar en la aplicación web aquellas fallas descubiertas durante un recorrido (sin registro previo),obteniendo la latitud y longitud de la falla y enviándolas a la aplicación web, para la estimación de su dirección aproximada.
Por último, se emplearán filtros y mecanismos de machine learning ofrecidos por por la librería Point Cloud Library(PCL), para el aislamiento y la clasificación de los tipos de fallas "Bache" y "Grieta".