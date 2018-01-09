Capítulo 3.Sensor Kinect y herramientas software implicadas el sensado de fallas
================================================================================

Sensores 3D
-----------

.. TODO: DEFINICION, CARACTERÍSTICAS,FORMA DE REPRESENTACIÓN DE OBJETOS EN 3D, TIPOS DE SENSORES 3D, CARACTERÍSTICAS Y APLICACIONES. 

.. https://en.wikipedia.org/wiki/3D_scanner
.. https://en.wikipedia.org/wiki/Structured-light_3D_scanner
.. https://en.wikipedia.org/wiki/Field_of_view
.. https://en.wikipedia.org/wiki/Point_cloud
.. https://en.wikipedia.org/wiki/List_of_programs_for_point_cloud_processing


Los scanners o sensores 3D, son elementos de medición que se emplean con el fin de analizar objetos del mundo real o entornos y obtener información respecto a sus características físicas, tales como colores y/o forma, que posteriormente pueden emplearse para genera modelos 3D digitales de éstos. Estos modelo se representa por medio de una nube de puntos (Point Cloud), que es una estructura de puntos definidos  en algún sistema de coordenadas, estando éstos definidos por sus coordenas (X,Y,Z) en un sistema de coordenadas tridimensional. Estas representaciones pueden ser directamente renderizadas e inspeccionadas, sin embargo para su uso en aplicaciones comerciales de edición o modelado deben ser convertidas en mallas poligonales o modelos triangulados, modelos NURBS (modelo matemático empleado para la representación de superficies y curvaturas) o modelos compatibles con el diseño asistido por computadora (CAD).

Estos sensores son similares a las camaras digitales, ya que cuentan con un campo de visión cónico y solamente pueden recolectar información respecto del entorno en lugares que cuentan con suficiente iluminación. Sin embargo, a diferencia de éstas  que unicamente capturan información respecto de los colores de la superficie, los scanners 3D son capaces de recolectar información acerca de la distancia de cada punto en la imagen  dentro de su rango de visión, por lo que la coordenada de cada punto puede ser precisada. Aunque la imagen proporcionada por un scanner 3D incluya información de posicionamiento de los puntos que componen una imagen, una única captura del objeto no bastará para brindar un modelo tridimensional completo de las caracaterísticas de éste, por lo que si se desea obtener éste resultado, se deben realizar varias capturas desde distintos puntos de vista del mismo objeto y luego realizar la unión final de todas estas capturas en una captura final.



.. Clases de sensores 3D y descripción general de C/U

.. APLICACIONES de estos sensores

Sensor Kinect
+++++++++++++
.. terminos de busqueda google -->
.. "developing libraries kinect"
.. https://www.google.com.ar/search?q=developing+libraries+kinect&safe=off&ei=SylUWpf3KIiawASF96vQBA&start=40&sa=N&biw=1183&bih=616

.. TODO: FUNCIONAMIENTO Y CARACTERISTICAS, DRIVERS EN WINDOWS Y LINUX, ENUMERAR LIBRERÍAS PARA EL DESARROLLO DE APLICACIONES DESDE WINDOWS Y LINUX. 


.. https://en.wikipedia.org/wiki/Kinect

.. Libro Beginning Programming with Microsoft SDK Kinect -->
.. http://droppdf.com/v/IBzJ5
.. https://books.google.com.ar/books?id=Cfxnzjf9phAC&pg=PA29&lpg=PA29&dq=developing+libraries+kinect&source=bl&ots=phpg5X6rp_&sig=XD4KMR3pfCUE8ACGCtDE81-MBto&hl=es&sa=X&ved=0ahUKEwi_luTe5MnYAhXGEZAKHbgbB6I4ChDoAQglMAA#v=onepage&q=developing%20libraries%20kinect&f=false



.. Libro Hacking the kinect -->
.. http://pdf.th7.cn/down/files/1312/hacking_the_kinect.pdf


.. ZigFu con Unity y Kinect -->
.. https://forum.unity.com/threads/connecting-kinect-unity-with-official-sdk.162075/




Kinect for Windows SDK(Xbox Development Kit)
----------------------------------------------

.. https://developer.microsoft.com/en-us/windows/kinect
.. https://developer.microsoft.com/en-us/windows/kinect/tools
.. https://msdn.microsoft.com/library/dn799271.aspx

.. http://dailydotnettips.com/2016/01/17/developing-kinect-for-windows-v2-0-app-with-visual-studio-2015-on-windows-10/

.. Libro Kinect for Windows SDK Programming Guide -->
.. https://books.google.com.ar/books?id=7XqIvRDHVzkC&pg=PT173&lpg=PT173&dq=wpf+kinect&source=bl&ots=ECZpK_Tctb&sig=E8t0Ntgqy7DpvtqqzhRdesxBIs0&hl=es&sa=X&ved=0ahUKEwjUrZSX6snYAhWEIJAKHbVGB4Q4HhDoAQgoMAE#v=onepage&q=wpf%20kinect&f=false

.. WPF with Kinect -->
.. http://dotneteers.net/blogs/vbandi/archive/2013/03/25/kinect-interactions-with-wpf-part-i-getting-started.aspx

Librería Java For Kinect(J4K)
-----------------------------

.. http://research.dwi.ufl.edu/ufdw/j4k/faq.php
.. http://research.dwi.ufl.edu/ufdw/index.php




Librería PCL
------------
.. https://openkinect.org/wiki/Main_Page
.. https://openkinect.org/wiki/Getting_Started

.. https://en.wikipedia.org/wiki/3D_scanner
.. https://en.wikipedia.org/wiki/Point_cloud
.. http://cmuems.com/excap/readings/forsyth-ponce-computer-vision-a-modern-approach.pdf
.. http://szeliski.org/Book/drafts/SzeliskiBook_20100903_draft.pdf
.. 
.. Tipos de feature descriptors -->
.. https://arxiv.org/pdf/1102.4258.pdf
.. 

.. TODO: QUE ES PCL, CARACTERISTICAS, Tipos de ALGORITMOS PARA PROCESAMIENTO DE NUBES. 
..  ALgoritmos de pre-procesamiento de nube: 
..    -Estimacion de features (procesamiento de normales)
..    -Estructuración de la nube (Descomposicion: kd-tree y octree)
..    -Filtrado con passthrough filter y outlier removal (radius-based y statistical)
..    -Resampling ya sea empleando downsampling (voxel grid y uniform sampling) y upsampling (moving least squares)
..    -Segmentation (empleando tanto las normales como el color)

.. Algoritmos de procesamiento de descriptores:
  - Descriptores locales (empleando color o normales)
  - Descriptores globales(empleando color o normales)






