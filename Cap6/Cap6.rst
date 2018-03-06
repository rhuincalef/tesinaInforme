
Capítulo 6. Caso de aplicación
==============================


Arquitectura global del sistema de administración de fallas
-----------------------------------------------------------

.. TODO: Se da una explicación de la estructura general de las 3 aplicaciones y como éstas interactúan mutuamente para conseguir el objetivo de la tesina.

La arquitectura general del sistema de registro y administración de fallas sobre circuitos viales, se compone de tres aplicaciones independientes: Aplicación web, aplicación de captura y aplicación de clasificación, con diferentes funcionalidades, que por medio de la interacción permiten llevar a cabo el registro, clasificación y obtención de información inherente a distintos tipos de fallas. La forma en que éstas interactúan y la frecuencia de ejecución se encuentra predefinida por medio de archivos de configuración específicos de cada una y, el lugar de ejecución (cliente o servidor) se encuentra condicionada por la funcionalidad que proporcionan al sistema global de administración de fallas. Así, las interacciones definen flujos de trabajo que involucran tanto a la máquina cliente de captura de fallas como al servidor que las procesa, siendo los flujos principales los siguientes:

* Flujo de trabajo para fallas Confirmadas
* Flujo de trabajo para fallas Informadas


El flujo de trabajo para fallas confirmadas se describe en la siguiente figura:


.. figure:: ../figs/Cap6/FlujoTrabajo_confirmada.png
   :scale: 100%

   Flujo de trabajo para fallas con estado "Confirmada".


1. En esta etapa la aplicación de captura fue configurada previamente en una notebook/netbook/ultrabook o algún dispositivo con espacio suficiente y conexión USB para interactuar con el dispositivo Kinect y un GPS. Así, en esta etapa se realiza la  captura de fallas en algún vehículo en distintas ubicaciones y para cada falla se computan su latitud y longitud. 
2. Una vez realizada la captura de un conjunto de fallas a lo largo de una calle completa, se las puede almacenar de manera persistente en un recorrido. Un recorrido o archivo de recorrido, es un archivo con extensión .rec que permite almacenar un conjunto de fallas en disco, registrando para cada falla la siguiente información: geolocalización, capturas asociadas a la falla, tipo de falla, nivel de criticidad y tipo de material, siendo éstos últimos tres especificados por el usuario de la aplicación al momento de posicionarse sobre la falla. 
3. Luego de haber almacenado varios recorridos en disco y de contar con conexión a Internet, estos se cargan nuevamente desde la aplicación y se envían al servidor web, para la computación de la información faltante de la falla.   
4. Durante este paso, con la latitud y longitud obtenidas por cada falla, se realiza reverse geocoding a Google Maps con el fin de obtener los datos de la dirección principal (nombre de calle y rango de altura) y, debido a que Google Maps no provee la información respecto de los nombres de las calles que forman parte de la intersección más cercana a la ubicación, ésta se solicita a los servidores de Geonames.org que ofrece dicha funcionalidad. 
5. De esta forma, con la información obtenida por ambos servidores, se realiza una validación de los datos obtenidos, se los adapta al formato de la base de datos del sistema y finalmente, se los registra en sistema de administración y registro de fallas.  
6. La aplicación de clasificación o clasificador, se encuentra alojada en el mismo servidor donde reside la aplicación web, configurada como un cron job (o tarea programada) que se ejecuta con una frecuencia de 5 min., por lo que la información de clasificación de una falla puede demorar un tiempo extra y no estar disponible de manera instantánea, al contrario de lo que ocurre con la información de las fallas subidas en un recorrido. Debido a que en la práctica algunas fallas no cuentan con una único patrón que los distinga como un bache o una grieta, sino que pueden contener deformaciones de ambos tipos, el clasificador se encuentra configurado para aislar varias clases de fallas en una captura, aislando por cada clase de falla encontrada en una captura, uno o más clusters, mostrando la información de cada cluster junto con el nombre de la captura a la que pertenece.   
7. Finalmente, una vez que el demonio de clasificación se haya ejecutado, serán visibles en cada falla de la aplicación web el tipo al que pertenece, determinado por el clasificador, y sus dimensiones (altura, ancho y profundidad para baches y grosor, largo y profundidad para grietas).


Por otro, lado el flujo de trabajo de fallas informadas varía con respecto a la obtención de información relativa a las coordenadas de la falla y se describe en la siguiente figura:



.. figure:: ../figs/Cap6/FlujoTrabajo_informada.png
   :scale: 100%

   Flujo de trabajo para fallas con estado "Informada". 



1. El primer paso en este flujo de trabajo consiste en solicitar las fallas que se encuentren localizadas en una calle, enviando para éste fin el nombre de la calle desde la aplicación de captura. De esta forma, la aplicación web realiza un filtrado de los nombres de calles registrados, asociados a fallas informadas previamente y retorna aquellas que se encuentren en la calle solicitada.
2. A continuación, se realiza la captura de la falla informada registrando solamente información relativa a las propiedades de ésta, obviando sus coordenadas.
3. Se almacenan las fallas en un recorrido de la misma forma que en el flujo de trabajo para fallas confirmadas.
4. Se envían las fallas que forman parte del recorrido al servidor, enviando junto con las propiedades el *id* con el que se encuentran registradas en la aplicación web, para su posterior búsqueda.
5. Se realiza el aislamiento y clasificación de la falla análogamente a como se realiza en el flujo de trabajo de fallas confirmadas.
6. Se visualizan las fallas aisladas correctamente desde la aplicación web con estado Informada.    


En las siguientes secciones se describirán en detalle la arquitectura, características  y modo de uso de cada una de las aplicaciones que componen el sistema de registro y administración de fallas. 


Aplicación web
--------------

.. TODO: Incluir:
..				-Requerimientos funcionales, no funcionales
..              -Diseño: Arquitectura de la aplicación.Incluir Diagrama de Clases Software. Descripción breve de la funcionalidad que proporcionan los módulos principales. 
..              -Funcionalidad de la aplicación: Descripción respecto de como emplear las funcionalidades.
..                                 *Funcionalidades heredadas: Incluir funcionalidad realizada durante el proyecto de investigación (previo a la tesina).
..                                 *Funcionalidades agregadas: Incluir funcionalidad que fue desarrollada como parte de la tesina. 
..              -Librerías empleadas para el desarrollo


Aplicación de captura(appCliente)
---------------------------------


.. TODO: Incluir:
..				-Requerimientos funcionales, no funcionales
..              -Diseño: Arquitectura de la aplicación.Incluir Diagrama de Clases Software. Descripción breve de la funcionalidad que proporcionan los módulos principales. 
..              -Librerías empleadas para el desarrollo
..              -Funcionalidad de la aplicación: Descripción respecto de como emplear las funcionalidades 

.. h4 -->


Requerimientos funcionales
^^^^^^^^^^^^^^^^^^^^^^^^^^

Los requerimientos funcionales que fueron determinados para la aplicación de captura de fallas fueron los siguientes:

* *Capturar información relativa a fallas confirmadas en la ubicación de la misma*: La aplicación debe permitir capturar fallas nuevas sin registro previo en la aplicación web(fallas confirmadas) detectadas durante una exploración, registrando información  respecto de las propiedades de la falla (tipo de falla, tipo de material, criticidad, características geométricas) y de la ubicación donde ésta se encuentra, de manera que posteriormente la aplicación web pueda computar datos de la dirección de la misma. 

* *Obtención de fallas informadas en una calle desde el servidor*: La aplicación debe permitir la obtención de fallas informadas que fueron previamente registradas desde la aplicación web, según el nombre de la calle donde éstas se encuentran. De esta forma, la aplicación de captura debe poder comunicarse con la aplicación web, que buscará la calle solicitada de entre conjunto de calles registradas y retornará los resultados, para proceder con la captura de las fallas informadas.  
  
* *Captura de información relativa a fallas informadas en la ubicación de la misma*: Una vez solicitadas las fallas desde el servidor, se debe poder registrar información de las propiedades de cada falla.  
  
* *Almacenar/Leer de manera persistente un conjunto de fallas*: Las fallas informadas y confirmadas capturadas se deben poder almacenar en un archivo que contenga el recorrido hecho con las fallas (archivo de recorrido), para ser posteriormente cargado y enviado a la aplicación web.  
  
* *Enviar una o varias fallas a servidor remoto*: Se deben poder enviar una o más fallas informadas y/o confirmadas cargadas en memoria, desde la aplicación de captura hacia la aplicación web. 


Requerimientos no funcionales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Por otro lado, los requerimientos no funcionales que fueron determinados para la aplicación de captura de fallas fueron los siguientes:

* Respuesta rápida ante la solicitud de efectuar una captura, debido a que ésta tarea debe realizarse sobre un vehículo con tiempos de ejecución que pueden estar limitados por la fuente de alimentación del dispositivo, sobre el cual se ejecuta la aplicación.  
* Interfaz intuitiva, con terminología e iconos afines al dominio del problema, que agilicen la interacción con el usuario.
* Interacción entre aplicación de captura y aplicación web a través de un protocolo de comunicación sencillo, que permita rastrear por medio de códigos de estado posibles errores en la obtención o envío de información.
* Visualización de las fallas tanto con luz solar como en ausencia de ésta. Debido a que la luz solar interfiere con el tipo de ondas emitidas por el sensor, la aplicación debe contemplar la visualización de las fallas tanto de día, en horas previas al anochecer, como así también la captura de noche. 

Diseño de la aplicación
^^^^^^^^^^^^^^^^^^^^^^^

Arquitectura de la aplicación
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





Librerías empleadas en la aplicación
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Funcionalidad de la aplicación
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Aplicación de clasificación
---------------------------

.. TODO: Incluir:
..				-Requerimientos funcionales, no funcionales
..              -Diseño: Arquitectura de la aplicación.Incluir Diagrama de Clases Software. Descripción breve de la funcionalidad que proporcionan los módulos principales. 
..              -Librerías empleadas para el desarrollo
..              -Funcionalidad de la aplicación: Descripción respecto de como emplear las funcionalidades 

Requerimientos funcionales
^^^^^^^^^^^^^^^^^^^^^^^^^^

* *Clasificación de fallas*: La aplicación debe leer los parámetros utilizados en los algoritmos relacionados con la clasificación desde un archivo de configuración, procesar capturas en formato .pcd desde un directorio específico y producir uno o más clusters, con información respecto de las dimensiones de la falla aislada, en un directorio de salida accesible por la aplicación web.


Requerimientos no funcionales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Capacidad para ser configurado y ejecutado en múltiples plataformas.
* Utilizar los mecanismos de paralelización en el procesamiento provistos por las librerías empleadas, con el fin de minimizar el tiempo de clasificación de fallas.
* Disponibilidad de capacidad de almacenamiento persistente alto para computar las muestras.
* Contar con un mecanismo de configuración que sea minimalista y amigable.
* Capacidad de realizar un rastreo de las muestras previamente procesadas, para reducir tiempo de cómputo.
* Versatilidad con respecto al modelo de Machine Learning empleado, el algoritmo de segmentación, el descriptor y el tipo de punto para la clasificación de fallas.
* Obligatoriedad de ejecución como tarea programada periódica y en segundo plano.


Diseño
^^^^^^
La estructura de la aplicación de clasificación esta integrada por los siguientes componentes software principales:

* **MainPipeLine**: Es la clase principal de procesado, que realiza las configuraciones globales iniciales, analiza el directorio de muestras, instancia objetos Nube y comienza con el procesamiento de cada una. 
 
* **Nube**: Representa una nube de puntos y todas aquellas nubes resultantes de haber sido procesadas por los algoritmos que intervienen en la clasificación. Contiene una colección de clusters que se derivaron del procesamiento de la misma.
  
* **Cluster**: Nube de puntos resultado de la aplicación de estrategia de segmentación. Esta clase contiene la información sobre las dimensiones aproximadas del mismo, por ejemplo alto, ancho, profundidad.

* **EstrategiaSegmentationAbstract**: Clase que representa la estrategia que será empleada para segmentar la nube de puntos. Puede consistir en uno o varios algoritmos de segmentación concretos. 

* **PointFeature**: Esta clase representa el feature personalizado que se compone de uno de los features ofrecidos por PCL y la diferencia entre ancho y alto calculados a partir de un cluster.


.. TODO: Hacer una referencia a capitulo 3.

* **EstrategiaDescriptorAbstract**: Esta clase genera el PointFeature a partir de un cluster y puede ser extendida para distintos tipos de descriptores provistos por PCL.
  
.. TODO: Hacer una referencia a capitulo 4.
  
* **EstrategiaClasificacionMLAbstract**: Esta clase representa la estrategia de clasificación que se puede adoptar para clasificar a que clase el cluster pertenece. Puede ser extendida para ser utilizada con distintos modelos de Machine Learning.

* **DBManager**: Esta clase engloba el comportamiento relacionado con la interacción de MainPipeLine con una base de datos que mantiene un registro de las fallas previamente clasificadas. Todas las fallas procesadas y clasificadas con o sin éxito, se agregan a dicha base. 



.. figure:: ../figs/Cap6/Final_Diagrama_de_clases_clasificador.png
   :scale: 100%

   Diagrama de clases software de la aplicación de clasificación


Librerías empleadas para el desarrollo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Boost**: Es una librería open-source que fue diseñada con el objetivo de extender las capacidades del lenguaje C++ e incluye varias funcionalidades entre las que se destacan el procesamiento de texto, operaciones de iteración sobre directorios del sistema operativo, operaciones de entrada/salida, programación concurrente, etc. Esta librería fue empleada principalmente para implementar la iteración, búsqueda y creación de elementos en la jerarquía de directorios del sistema operativo y el procesamiento de cadenas de texto asociadas a éstas.

.. TODO: Agregar referencia Capítulo 4.

* PCL: Librería descripta en el capítulo 4. 

* JSONCPP: Es una librería en C++ empleada para la manipulación de archivos con formato JSON y la serialización/deserialización de éstos hacia/desde disco. Fue empleada para funcionalidad relacionada con creación de los archivos .json que mantienen información de dimensiones respecto de la falla clasificada.
  
* SQLite3: Es un sistema de bases de datos relacional desarrollada en C, donde la aplicación cliente realiza consultas a la base de datos por medio de funciones, en lugar de comunicarse con un proceso independiente, lo que provoca una reducción de la latencia en la interacción. Esta base de datos fue utilizada para mantener un registro de las fallas que fueron procesadas, evitando procesamiento innecesario. 


Funcionalidad de la aplicación
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para el funcionamiento de esta aplicación, es necesario compilarla siguiendo las instrucciones en README.txt desde el repositorio https://github.com/rhuincalef/clasificadorFallas o, en el código fuente adjunto. Luego se debe realizar la configuración de los parámetros obligatorios de la aplicación, para ello se debe alterar el archivo *config_pipeline.json-default* cambiando la extensión a .json y modificando cada una de las siguientes entradas:

* **configuracion_global**: Esta entrada contiene el *dir_entrada* que es el directorio raíz desde el cual esta aplicación lee los archivos .pcd a procesar; *dir_salida* es el directorio raíz donde la aplicación almacenará los resultados obtenidos del procesamiento. Por último, cuenta con *database_muestras* que indica la ruta absoluta del archivo de base de datos con extensión .db, que se puede encontrar en el archivo base *fallas.db*.
      
* **clasificador**: Esta entrada consiste en aquellas configuraciones relativas al tipo de modelo de clasificación seleccionado. En *tipo* se debe especificar el modelo de clasificación a utilizar, siendo el único modelo implementado "svm". *path_modelo* especifica la ruta absoluta al modelo entrenado utilizado por el clasificador. 
 

.. TODO: Ver RANSAC y Euclidean

* **estrategia_segmetador**: Esta entrada contiene aquellos valores empleados para la calibración del algoritmo de segmentación seleccionado. Estos valores fueron determinados por medio de pruebas de segmentación para baches y grietas y deben ser modificados con precaución según el tipo de objetos que desee aislar. No es necesario modificar estos valores para probar con grietas y baches. El único algoritmo implementado es Planar Euclidean que se encuentra especificado en la entrada *tipo*, el cual consta para planar segmentation de *distance_threshold*, *max_iterations* y de euclidean_segmentation (RANSAC) *tolerance*, *min_cluster_size* y *max_cluster_size*. 

.. TODO: REFERENCIA "CAP3. Representación y almacenamiento de una nube de puntos"

* **point_feature**: Esta entrada especifica el tipo de punto ofrecido por PCL a utilizar para la lectura, procesamiento y almacenamiento de nubes de puntos.           

.. TODO: REFERENCIA "CAP4. Descriptores"

* **estrategia_descriptor**: Esta entrada representa el tipo de descriptor de PCL que se utilizará para generar el descriptor personalizado (PointFeature). *tipo_descriptor* determina el tipo de descriptor que puede ser "GRSD" o "ESF", aunque ESF es el descriptor que más precisión tiene para este desarrollo en concreto.
  
  Tener en consideración, que el tipo de modelo entrenado especificado en entrada **clasificador** tiene que estar entrenado con el tipo de estrategia descriptor seleccionada, por lo que si se selecciona ESF el *path_modelo* debe ser el de un modelo que este entrenado con éste feature de PCL. 


Finalmente, para ejecutar la aplicación en segundo plano como una tarea programada, se deben seguir las instrucciones especificadas en README.txt, donde se detallan lapsos de ejecución de la tarea en intervalos de 5 minutos, todos los días. Esta configuración requiere el uso de *crontab* y únicamente fue probada bajo Linux (Ubuntu 16.14 y Manjaro Hakoila 17.16). 



