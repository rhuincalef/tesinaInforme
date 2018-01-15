Capítulo 3.Sensor Kinect y herramientas software implicadas el sensado de fallas
================================================================================

Sensores 3D
-----------

.. https://en.wikipedia.org/wiki/3D_scanner
.. https://en.wikipedia.org/wiki/Structured-light_3D_scanner
.. https://en.wikipedia.org/wiki/Field_of_view
.. https://en.wikipedia.org/wiki/Point_cloud
.. https://en.wikipedia.org/wiki/List_of_programs_for_point_cloud_processing
.. https://en.wikipedia.org/wiki/Lidar
.. https://es.wikipedia.org/wiki/Esc%C3%A1ner_3D


Los scanners o sensores 3D, son elementos de medición que se emplean con el fin de analizar objetos del mundo real o entornos y obtener información respecto a sus características físicas, tales como colores y/o forma, que posteriormente pueden emplearse para genera modelos 3D digitales de éstos. Estos modelo se representa por medio de una nube de puntos (Point Cloud), que es una estructura de puntos definidos  en algún sistema de coordenadas, estando éstos definidos por sus coordenadas (X,Y,Z) en un sistema de coordenadas tridimensional. Estas representaciones pueden ser directamente renderizadas e inspeccionadas, sin embargo para su uso en aplicaciones comerciales de edición o modelado deben ser convertidas en mallas poligonales o modelos triangulados, modelos NURBS (modelo matemático empleado para la representación de superficies y curvaturas) o modelos compatibles con el diseño asistido por computadora (CAD).

Estos sensores son similares a las cámaras digitales, ya que cuentan con un campo de visión cónico y solamente pueden recolectar información respecto del entorno en lugares que cuentan con suficiente iluminación. Sin embargo, a diferencia de éstas  que unicamente capturan información respecto de los colores de la superficie, los scanners 3D son capaces de recolectar información acerca de la distancia de cada punto en la imagen  dentro de su rango de visión, por lo que la coordenada de cada punto puede ser precisada. Aunque la imagen proporcionada por un scanner 3D incluya información de posicionamiento de los puntos que componen una imagen, una única captura del objeto no bastará para brindar un modelo tridimensional completo de las características de éste, por lo que si se desea obtener éste resultado, se deben realizar varias capturas desde distintos puntos de vista del mismo objeto y luego realizar la unión final de todas estas capturas en una captura final.

Existen diferentes tipos de sensores 3D que emplean distintas técnicas para la obtención del objeto 3D, aunque de manera general se clasifican en: Técnicas de contacto, donde las características del objeto se obtienen por medio del contacto físico, sosteniéndolo por medio un brazo robótico que puede ser manipulado para escanear la superficie completa de un objeto o, manteniéndolo apoyado sobre una plataforma fija; Y técnicas sin contacto, donde se detecta radiación (rayos infraroja o X) o luz solar sobre el objeto con el propósito de adquirir información de éste.  Dentro de los tipos de sensores sin contacto, éstos se pueden subdividir en activos y pasivos. Los activos son aquellos sensores que emiten algún tipo de radiación o luz sobre un objeto y absorben su reflexión con el fin de inspeccionar el objeto. Las aproximaciones existentes para medir esta radiación se pueden subdividir en tres clases generales: Time of Flight(ToF), Diferencia de fase (Phase Shift) y triangulación por láser.

Los tipos de láser ToF emiten varios impulsos láser hacia un objeto y miden el tiempo que requiere alcanzar el objeto y ser reflejado de vuelta al sensor emisor y, por medio de la siguiente fórmula computan la distancia:

.. math:: D = c * t/ 2
   :label: ecuacionDistanciaToF

Dado que la velocidad de la luz en la atmósfera *c* es una constante se conoce, solamente se debe calcular el tiempo de viaje y de retorno *t*, por lo que la precisión con la que un láser ToF detecta un objeto, depende en gran medida de la precisión con la que se mide el tiempo. Por lo tanto, la detección de este tipo de dispositivos consiste en emitir varios rayos de luz sobre un objeto y en base a éstos computar las distancias a partir de las cuales se computarán las coordenadas de los puntos. Existen diferentes métodos para emisión de los lasers, entre ellos las aproximaciones más comunes son las que emplean los sensores Lidar y las Cámaras ToF. El sensor Lidar (Light Detection And Ranging) emplea un pulso laser para medir la distancia a un objeto que varía rápidamente su dirección  por medio de un sistema de espejos rotativos, modificándose los ángulos horizontales y verticales, de manera que se puedan captar las distancias de todos puntos del objeto que se encuentra en el campo de visión. Una vez obtenidas las distancias y conociendo los ángulos horizontales y verticales, se pueden computar la posición X,Y,Z para cada uno de los puntos. Así, partiendo de la diferencia entre los tiempos y longitudes de onda producen un modelo tridimensional del objetivo. Estos dispositivos se empelan principalmente en satélites para la generación de mapas terrestres de alta resolución, topografía, documentación histórica de objetos antiguos y en la detección de objetos en vehículos autónomos.             

.. figure:: ../figs/Cap3/sensor_lidar_esquema.png
   :scale: 60%

   Ejemplo de laser tipo Lidar. En la figura superior, se puede observar el rayo proyectado (línea roja) que es desplazado para escanear una escena entera por medio de un espejo rotativo. En la figura central se denota con azul el laser, con una círculo verde un objeto esférico y un rectángulo verde que constituye las paredes del entorno en el que se ubica el dispositivo. Finalmente, en la figura inferior se muestra el sensor representado como un punto negro, y los puntos azules simbolizan cada uno de los puntos capturados por el dispositivo durante el escaneo.


.. figure:: ../figs/Cap3/robot_lidar.jpg
   :scale: 50%
   
   Robot móvil con un láser Lidar SICK Laser Rangefield.

Por otro lado, la cámara ToF no escanea individualmente cada uno de los puntos en el campo de visión, sino que emite varios pulsos de radiación simultáneamente capturando la escena completa en cada emisión. Luego una cámara sensible a la radiación captura la imagen producida por la reflexión del conjunto de pulsos (cuyas características variarán dependiendo de la distancia entre el sensor y el objeto), finalmente se filtra la radiación cuya longitud de onda coincide con la del tipo que fue emitida y se genera la imagen final. Estos dispositivos se emplean en: Aplicaciones automovilísticas para detección de peatones y prevención de colisiones, interfaces humanas donde se captura la interacción con el usuario tales como en televisores y videojuegos donde se emplea el dispositivo para capturar movimientos y gestos que son utilizados como gamepads, tales como la segunda generación del sensor Kinect (Kinect V2), en robótica en robots que se desplazan en un entorno donde deben esquivar obstáculos o seguir una persona, o en visión por computadora en entornos industriales para tareas automatizadas de medición, o detección de objetos que serán empleados por un robot para realizar una tarea.


.. figure:: ../figs/Cap3/sensor_kinect_v2_cam_tof.png
   :scale: 50%

   Kinect V2 con cámara ToF desarrollada por Microsoft. 


Este tipo de sensor, tienen la ventaja de ser rápidos para el muestreo, de alta precisión,aptos para trabajos de medición en monumentos o elementos de construcción, con una alta densidad de puntos por captura, una velocidad de captura entre 10.000 y 100.000 puntos por segundo y un rango de medición alto entre 200 y 300 m. Sin embargo, estos dispositivos no cuentan con una resolución de profundidad alta, la precisión del modelo generado es aproximadamente 1 cm y no se cuenta con información de color.  

.. http://floridalaserscanning.com/3d-laser-scanning/how-does-laser-scanning-work/

Los lasers de diferencia de fase funcionan emitiendo un haz de luz continuo y de potencia modulada, con una longitud de onda específica sobre el objeto o superficie, para posteriormente medir la diferencia entre las longitudes de onda del haz de luz emitido y el reflejado, y a partir de ésta diferencia computar la distancia. Este proceso es similar a la técnica de tiempo de vuelo, excepto que la fase del láser reflejado refina la precisión respecto de la detección de la distancia. El alcance de este tipo de sensores se encuentra limitado por las características de la longitud de onda, por lo que el rango de la  medición es la mitad de la modulación de la longitud de onda del haz de luz, mientras que la precisión de la medición es inversamente proporcional a la frecuencia empleada, por lo que medir con una alta frecuencia brinda distancias precisas pero menor rango de medición. Este tipo de dispositivo cuenta con una velocidad de adquisición alta (ubicándose ésta entre 100.000 y 1.000.000 de puntos por segundo) y un alcance de captura intermedio entre 70-100 m. Sin embargo, aunque la velocidad de captura es considerablemente superior a los scanners ToF, las nubes de puntos generadas por el método de diferencia de fase suelen contener más ruido. 


.. figure:: ../figs/Cap3/ejemplo_phase_shift.jpg
   :scale: 60%
   
   Comparación gráfica de laser ToF y Phase Shift 


Los scanners 3D de triangulación, consisten en emitir una luz láser sobre un objeto y por medio de una cámara detectar la posición del haz en el campo de visión de la cámara, de manera que dependiendo de que tan lejano el objeto se encuentre el punto, aparecerá en distintas posiciones del campo de visión de la cámara. Posteriormente empleando la distancia entre el emisor láser y los ángulos del emisor láser y la cámara, se forma un triángulo que es empleado para calcular la ubicación del punto.


.. figure:: ../figs/Cap3/ejemplo_triangulacion.jpg
   :scale: 60%
   
   Esquema gráfico de scanners de triangulación

Los sensores de Holografía Conoscópica (Conoscopic Holography), consisten en proyectar un rayo láser en una superficie y luego emplear la reflexión del mismo, haciendo que éste atraviese un cristal con forma cónica y genere un patrón de luz que se proyecta en una cámara y posteriormente es analizado para medir la distancia.

Los sensores de luz estructurada 3D (Structured Light 3D), proyectan un patrón de luz sobre un objeto o superficie y captan la deformación producida por el objeto, pudiendo ser éste de unidimensional (una línea de luz) o bidimensional (una grilla o patrón de lineas). Un sensor que se encuentra desplazado del emisor de luz, se emplea para captar la deformación y luego se computa la distancia. Este tipo de dispositivos se caracterizan por ser veloces, ya que en lugar de escanear un punto a la vez, los sensores escanean múltiples puntos en campo de visión con una sola emisión, lo que elimina la posibilidad de distorsión por movimiento. La resolución y velocidad de estos sensores es similar a la de las cámaras VGA, y su precisión es similar a las ToF (aproximadamente 1 cm), contando con un alcance máximo entre 3 m y 6 m, sin embargo estos dispositivos tienen dificultades para captar objetos pequeños menores a 1 cm.   

.. figure:: ../figs/Cap3/ejemplo_luz_estructurada.jpg

   Ejemplo de sensor ASUS Xion Pro con luz estructurada.

  
En los scanners de luz modulada (Moduled Light), la luz emitida por el emisor se modifica variando la amplitud de la radiación emitida en base a un patrón establecido (generalmente una onda sinusoidal) y una cámara detecta la diferencia entre la amplitud del patrón y la diferencia de radiación reflejada, empleándose ésta para detectar la distancia del objeto y computar las posiciones. 
  

Por otro lado, la técnica de scanners sin contacto pasivos, no emiten ningún tipo de radiación sino que su funcionamiento se basa en capturar la radiación reflejada del ambiente, como la luz solar o la luz infraroja. Estos tipos de scanners se caracterizan por ser económicos, ya que no requieren de hardware  especializado para la emisión de un tipo de radiación. Dentro de esta categoría de dispositivos, se encuentran los siguientes:

* Scanners estereoscópicos (Stereoscopic Scanners): Estos dispositivos emplean dos cámaras de video en posiciones diferentes (desplazadas algunos centímetros) enfocadas hacia el mismo objeto, que captarán imágenes distintas del mismo y, por medio del análisis de estas diferencias, se puede calcular la distancia de cada punto punto en las imágenes. Un ejemplo de este tipo de dispositivos son las cámaras estéreo, que cuentan con la ventaja de ser económicas, sin embargo requieren una perfecta calibración de ambas cámaras de video y son sensibles a las malas condiciones de iluminación. 
 
.. figure:: ../figs/Cap3/ejemplo_de_camara_estereo.png
   :scale: 60%

   Cámara estéreo


* Silhouette scanners: Estos scanners capturan una secuencia de imágenes para generar un contorno alrededor de un objeto que contrasta con el fondo, que posteriormente son superpuestos para formar un hull visual y generar una aproximación del objeto.
  

Con respecto a los scanners de contacto, un ejemplo de su funcionamiento son las cámaras de medidas de coordenadas(Coordinate Measuring Machine) empleadas para la medición de las características geométricas de partes o productos industriales ensamblados. Este dispositivo se compone de tres ejes X,Y,Z ortogonales entre si, donde cada uno se mantiene una escala para registrar las coordenadas del elemento que se analiza. Así, este tipo de scanner desplaza uno de los ejes (ya sea automáticamente o manualmente) mientras que el resto se mantiene fijo, y graba cada una de las coordenadas del objeto.  


Existen varias áreas donde se aplican los scanners 3D, entre las más comunes se encuentran:

* Control de calidad industrial. Una de las principales aplicaciones de los scanners 3D consisten en la digitalización de partes producidas, tanto en el diseño como en la producción de la parte final. Estos dispositivos deben ser precisos y versátiles, con el fin de obtener la mayor cantidad de información acerca del proceso de construcción de partes.
 
* Registros históricos. En esta rama se emplean dispositivos 3D sin contacto que permitan el análisis de restos animales o artefactos antiguos sin dañarlos, con el fin de generar un modelo a mayor o menor escala, para ser exhibido en museos.
  
* Ciencias médicas. Dentro de las ciencias médicas, los scanners 3D se emplean por ejemplo en la rama de construcción de piezas dentales, ya que por su precisión y adquisición sin contacto, permiten generar de manera satisfactoria piezas cuyas dimensiones serían complejas de adquirir.
   
* Gráficos por computadora. Debido a que con las tecnologías actuales en la industria de videojuegos permiten la creación de entornos con mayor nivel gráfico de detalle, actualmente se recurre a los scanners 3D para la construcción de éstos en el entorno del videojuego, ya que escanear estos objetos consume menos tiempo que la creación a mano con herramientas digitales.  



Sensor Kinect
+++++++++++++
.. TODO: FUNCIONAMIENTO Y CARACTERISTICAS, DRIVERS EN WINDOWS Y LINUX, ENUMERAR LIBRERÍAS PARA EL DESARROLLO DE APLICACIONES DESDE WINDOWS Y LINUX. 

.. https://en.wikipedia.org/wiki/Kinect

.. Libro Beginning Programming with Microsoft SDK Kinect -->
.. http://droppdf.com/v/IBzJ5

.. Libro Hacking the kinect -->
.. http://pdf.th7.cn/down/files/1312/hacking_the_kinect.pdf

.. https://www.jameco.com/jameco/workshop/howitworks/xboxkinect.html
.. https://electronics.howstuffworks.com/microsoft-kinect2.htm

.. https://en.wikipedia.org/wiki/Range_imaging
.. https://web.archive.org/web/20100620012436/http://www.microsoft.com/Presspass/press/2010/mar10/03-31PrimeSensePR.mspx?rss_fdn=Press%20Releases
.. https://venturebeat.com/2009/09/05/how-many-vendors-does-it-take-to-make-microsofts-project-natal-game-control-system/


.. Componentes del Kinect -->
.. https://msdn.microsoft.com/en-us/library/jj663790.aspx
.. https://msdn.microsoft.com/en-us/library/jj131033.aspx
.. https://msdn.microsoft.com/en-us/library/jj131023.aspx
.. https://msdn.microsoft.com/en-us/library/hh973078.aspx

.. http://www.cs.upc.edu/~virtual/RVA/CourseSlides/Kinect.pdf
.. http://www.laserfocusworld.com/articles/2011/01/lasers-bring-gesture-recognition-to-the-home.html
.. https://bbzippo.wordpress.com/2010/11/28/kinect-in-infrared/
.. http://www.depthbiomechanics.co.uk/?p=100



El sensor Kinect es un dispositivo de juego compatible con las plataformas Xbox y PC, desarrollado por las compañías Microsoft y Primesense, pensado para la interacción del usuario sin la necesidad de controles físicos de juego, empleándose para la interacción una interfaz de gestos y comandos hablados.Este dispositivo es una cámara de rango que genera imágenes de rango (Range Images), que son aquellas que por cada pixel de la imagen tienen asociada la información de distancia de cada uno hacia el punto de captura. Este dispositivo fue lanzado en dos versiones,  la versión Kinect V1 para la consola Xbox 360 y la versión Kinect V2 para la consola Xbox One. 

La versión Kinect V1, empleada para la captura de muestras de la presente tesina, se basa en la técnica de proyección de luz estructurada 3D con luz infraroja(IR) constituyéndose por: Un emisor IR, una camara IR o sensor de profundidad IR, una cámara RGB de video, un conjunto de micrófonos en la parte inferior para la captura de comandos de voz, un acelerómetro y un motor de inclinación. Para realizar la captura de objetos en el campo de visión, el sensor captura constantemente varias imágenes o frames por segundo(fps) paralelamente, correspondientes a la cámara IR y la cámara de video.  En cada frame, el emisor IR emite un patrón de puntos infrarojos con distintas intensidades en 830nm, que son capturados por la cámara IR que funciona a 30 fps y produce imágenes en una resolución de 1280x960 pixeles, la cual se encarga de filtrar únicamente las señales IR, evitando que otro tipos de señales del entorno (tales como las señales de control remoto o condiciones de iluminación interior), interfieran con el funcionamiento del sensor. De esta forma, la cámara IR captura la señal IR, que se representa como una imagen en escala de grises, donde cada pixel contiene la distancia Cartesiana en milímetros hacia la coordenada de ese pixel desde el dispositivo de captura. El sensado de objetos se encuentra delimitado por un rango de distancia entre 0.8 m y 0.4 m por defecto, para la versión de Xbox 360, mientras que para la versión de Windows se incluye además un rango cercano de 0.4m y 3 m. 


.. figure:: ../figs/Cap3/funcionamineto_stream_profundidad.png
   :scale: 60%

   Funcionamiento del stream de profundidad


.. .. figure:: ../figs/Cap3/ejemplo_patron_puntos.jpg
.. figure:: ../figs/Cap3/ejemplo_patron_puntos_2.png
   :scale: 60%

   Patrón de puntos proyectados sobre una superficie


Luego, se analizan las diferencias entre el patrón emitido y la información de profundidad sensada por la cámara IR, se realiza una reducción de los datos capturados y se combina esta información con los datos de la cámara RGB de video para generar la nube de puntos final.



.. figure:: ../figs/Cap3/esquema_general_kinect.gif

   Esquema general de funcionamiento del Kinect V1



La cámara RGB opera a 30 fps en una resolución de 640x480 pixeles y puede ampliar su resolución a una definición de 1280x1024 pixeles, la cual se ajusta para concordar con la cámara IR de profundidad. Adicionalmente, la cámara RGB posee algunas características para optimizar la calidad del video tales como balanceo de blancos automático, saturación de color, corrección de defectos y eliminación de parpadeo.


.. figure:: ../figs/Cap3/sensorKinectEstructura.png
   :scale: 60%

   Diagrama externo del sensor Kinect V1


.. figure:: ../figs/Cap3/componentesKinectV2.png
   :scale: 60%

   Representación externa de los componentes de hardware del sensor Kinect V1


El acelerómetro del dispositivo se emplea para conocer la orientación del sensor con respecto a la gravedad, y se encuentra ubicado en el centro del dispositivo, de manera que el eje Z apunta a la dirección en la que el sensor apunta.

.. figure:: ../figs/Cap3/acelerometro_sensor.png
 
    Ejes del dispositivo


Este sensor contiene un campo de de visión de 43º horizontalmente y 57º verticalmente, que puede ser variado verticalmente a través del motor de inclinación en +- 27º, siendo éste el área de interacción con el dispositivo, donde se capturarán todos aquellos elementos que se encuentren en frente del sensor y no se encuentren bloqueados por algún otro objeto.   

.. figure:: ../figs/Cap3/extension_inclinacion.png
   :scale: 60%

   Extensión de inclinación


La versión Kinect V2, fue lanzada para Xbox One y en lugar del sensor de luz estructurada 3D desarrollada por Primesense, esta versión emplea una versión de cámara Time-of-Flight desarrollado por Microsoft, que cuenta con mayor precisión para capturar los movimientos, capacidad de detección de mayor esqueletos (articulaciones de usuario) y mayor distancia de detección.   


Microsoft Kinect SDK(Xbox Development Kit)
------------------------------------------


.. ZigFu con Unity y Kinect -->
.. https://forum.unity.com/threads/connecting-kinect-unity-with-official-sdk.162075/


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



.. Encabezado h3 -->

Librería Point Cloud Library(PCL)
---------------------------------

.. https://en.wikipedia.org/wiki/Point_cloud
.. https://openkinect.org/wiki/Main_Page
.. https://openkinect.org/wiki/Getting_Started
.. https://en.wikipedia.org/wiki/Point_Cloud_Library
.. https://en.wikipedia.org/wiki/Computer_vision
.. http://robotica.unileon.es/index.php/PhD-3D-Object-Tracking


.. http://cmuems.com/excap/readings/forsyth-ponce-computer-vision-a-modern-approach.pdf
.. http://szeliski.org/Book/drafts/SzeliskiBook_20100903_draft.pdf
.. 
.. Tipos de feature descriptors -->
.. https://arxiv.org/pdf/1102.4258.pdf
.. 


PCL es un proyecto que comenzó en 2010 por Willow Garage (compañía desarrolladora de la librería de imágenes OpenCV) y de la compañía desarolladora de Robotic Operating System(ROS), y cuya primera versión fue oficialmente liberada en 2011. Point Cloud Library(PCL) es una librería independiente, de código abierto, multiplataforma, escrita en C++, para la captura, el procesamiento geométrico y almacenamiento de nubes de puntos 3D, que ofrece algoritmos vinculados a tareas relacionadas a la visión artificial (o visión por computadora).  La visión artificial es un área de la inteligencia artificial, donde se busca que una computadora obtenga información y logre un entendimiento de alto nivel de las propiedades de ésta (tales como formas, iluminación,distribución de colores) a partir de un video o imagen del mundo real. Esta disciplina incluye aquellos métodos que permiten adquirir, analizar, procesar y extraer datos que puedan ser convertidos a información numérica y simbólica que pueda ser de utilidad durante la automatización de una tarea. Dentro del rango de aplicaciones en las que se emplea la visión artificial las más comunes son las siguientes:

* Reconocimiento óptico de caracteres(OCR) interpretando códigos escritos a mano.
* Inspección de máquinas, asesorando la calidad de partes empelando estéreo visión con iluminación especializada para medir tolerancias en partes de dispositivos aéreos o de automóviles.
* Seguridad automotriz, detectando obstáculos como peatones en los senderos viales, bajo condiciones donde las técnicas de visión activas como Lidar no funcionan correctamente.
* CGI(computer-generated imagery) en Cine-TV, donde la filmación real con actores se une con imágenes generadas por computadora rastreando puntos clave en el video origen, con el fin de estimar el movimiento de la cámara y la forma del entorno.
* Captura de movimiento, utilizando marcadores retro-reflectivos capturados desde distintas cámaras con el objetivo de capturar digitalmente el patrón de movimiento de actores para realizar una animación por computadora.
* Reconocimiento de huellas digitales para el acceso de personal autorizado automatizado.


.. TODO: QUE ES PCL, CARACTERISTICAS, Tipos de ALGORITMOS PARA PROCESAMIENTO DE NUBES. 
..  ALgoritmos de pre-procesamiento de nube: 
..    -Estimacion de features (procesamiento de normales)
..    -Estructuración de la nube (Descomposicion: kd-tree y octree)
..    -Filtrado con passthrough filter y outlier removal (radius-based y statistical)
..    -Resampling ya sea empleando downsampling (voxel grid y uniform sampling) y upsampling (moving least squares)
..    -Registración de dos nubes de puntos

..  ALgoritmos de segmentación de objetos: 
..    -Segmentation (empleando tanto las normales como el color)
..    -Reconstrucción(Triangulación)

.. Algoritmos de generación de descriptores:
  - Descriptores locales (empleando color o normales)
  - Descriptores globales(empleando color o normales)



De esta forma, PCL es una librería que ofrece diferentes módulos independientes que pueden ser combinados de distintas formas en un pipeline de instrucciones, con el fin de lograr el reconocimiento de distintos tipos de objetos en una nube de puntos. Los algoritmos de estos módulos están pensados para abarcar un  diverso rango de tareas que son necesarias para una correcta detección de objetos, tales como filtrado de puntos con valores atípicos distantes del resto en una nube (outliers en la nube), almacenamiento, lectura y conversión de nubes de puntos en distintos formatos, descomposición de la nube para realizar búsquedas, concatenar y fusionar dos nubes de puntos con los mismos o distintos campos, segmentar partes de una escena, extraer puntos clave y computar descriptores geométricos con el propósito de distinguir elementos del mundo real. De manera general, el pipeline de PCL para el reconocimiento de objetos se compone de las siguientes etapas:

* Pre-procesamiento de nube: Durante esta etapa se elimina el ruido de la nube, se aplican algoritmos para estructurar la nube y se estiman features que proporcionan información acerca de las características de la superficie que serán empleadas durante las siguientes etapas.

* Segmentación de objetos: En esta etapa se realiza la segmentación por medio de distintas técnicas con el fin de obtener clusters de interés, que serán utilizados para generar descriptores.

* Generación de descriptores: Durante esta fase, se computan los descriptores para el/los clusters aislados. Un descriptor es una estructura compleja que codifica información respecto de la geometría que rodea un punto, de manera que permiten identificar un conjunto de puntos a lo largo de varias nubes de puntos, sin importar el ruido, la resolución o las posibles transformaciones. Adicionalmente, algunos descriptores capturan información global respecto del objeto al que pertenecen, como el punto de visión que puede ser utilizado para computar la posición.   

A continuación, se enumeran y describen los algoritmos principales empleados durante cada fase.


Algoritmos de pre-procesamiento de nubes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Algoritmos de segmentación de objetos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Algoritmos para generación de descriptores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. Organización de features en PCL -->
.. http://pointclouds.org/documentation/tutorials/how_features_work.php
.. https://github.com/PointCloudLibrary/pcl/wiki/Overview-and-Comparison-of-Features
.. http://www.pointclouds.org/assets/icra2013/pcl_features_icra13.pdf

Con respecto a la generación de descriptores, PCL ofrece dos tipos de descriptores: Descriptores locales y descriptores globales. Los descriptores locales, se emplean para describir la geometría alrededor de cada punto, sin considerar la geometría total del objeto que cada punto compone, por lo que cuando se computan éstos, se debe hacer un filtrado previo de los puntos clave del objeto o keypoints que se desean procesar. Estos descriptores se emplean para el reconocimiento de objetos y para la registración(registration), que consiste en alinear dos nubes de puntos y por medio de transformaciones lineales, detectar si existen áreas comunes en ambas nubes de puntos. 

Por otro lado, PCL ofrece descriptores globales que describen la geometría de un cluster de puntos que representa un objeto, por lo que para emplear estos descriptores se requiere pre-procesar una nube de puntos, con el fin de aislar el objeto. Estos descriptores se aplican para el reconocimiento de objetos y clasificación, estimación de posición y análisis de geometría (tipo de objeto, forma, etc.). Los descriptores locales que emplean un radio de búsqueda, mayormente pueden ser usados como globales, si se computa un solo punto en el cluster y se modifica éste radio al de puntos vecinos, de manera que se abarquen todos los puntos que componen el objeto.

Existen varios tipos de descriptores en PCL, cada uno empleando su propia técnica, ya sea empleando los ángulos de las normales o las distancias Euclidianas entre puntos. Sin embargo, con el fin de reducir el tamaño de cada descriptor, todos se organizan en histogramas cuyos rangos de escala se corresponden con la característica que es parte el descriptor (por ejemplo, distancia entre puntos), asociándose cada una de las características del descriptor a un histograma, donde éstos se encuentran divididos en k subdivisiones y en cada rango del histograma se representan las ocurrencias de puntos dentro de ese rango. De esta forma, cada algoritmo para la generación de descriptores realiza su propia subdivisión del histograma, dependiendo del rango de valores que sea más representativo en la variable, es decir, que esto se genera dinámicamente y se producen más subdivisiones para los valores donde existen mayor cantidad de puntos con esa característica.

.. Ejemplo histograma -->
.. http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.324.3396&rep=rep1&type=pdf
 


 .. . Con respecto a los baches, se optó por seleccionar aquellos algoritmos que computan features llamadas normales( vectores unidad que son tangentes a un punto en una superficie y perpendiculares al plano en que se encuentra dicho punto).







