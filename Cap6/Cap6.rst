
Capítulo 6. Caso de aplicación
==============================

El objetivo principal del presente capítulo será la exposición de las herramientas utilizadas y las etapas necesarias para la captura, procesamiento, clasificación y visualización de fallas. Cabe aclarar que del conjunto de tipos de falla existentes detallados anteriormente (Ver :doc:`../Cap2/Cap2`), únicamente se considerarán los tipos de falla bache y grieta sobre pavimento rígido.


Arquitectura global del sistema de administración de fallas
-----------------------------------------------------------

Antes de comenzar a detallar los diferentes componentes del sistema de administración de fallas, es necesario tener en cuenta que los tipos de fallas administrados por ésta, desde que son notificadas hasta que concluye su reparación, atraviesan por un conjunto de estados que son secuenciales, excluyentes y una vez superado un estado, la falla no puede regresar a un estado previo. Estos tipos de estado son:

* **Informado**: Son aquellas fallas que fueron cargadas por usuarios desde la aplicación web.
  
* **Confirmado**: Son aquellas fallas que realmente fueron cargadas por personal autorizado o aquellas fallas informadas que fueron validadas por los mismos y modificadas en el sistema.
  
* **En reparación**: Son aquellas fallas a las que se les ha asignado una fecha de finalización estimada y un procedimiento de reparación.
  
* **Reparado**: Son aquellas fallas que realmente han sido reparadas y que poseen un costo real de reparación y una fecha de finalización efectiva de la reparación.
  

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
4. Se envían las fallas que forman parte del recorrido al servidor, enviando junto con las propiedades el identificador con el que se encuentran registradas en la aplicación web, para su posterior búsqueda.
5. Se realiza el aislamiento y clasificación de la falla análogamente a como se realiza en el flujo de trabajo de fallas confirmadas.
6. Se visualizan las fallas aisladas correctamente desde la aplicación web con estado Informada.    


En las siguientes secciones se describirán en detalle la arquitectura, características  y modo de uso de cada una de las aplicaciones que componen el sistema de registro y administración de fallas. 


Aplicación web
--------------

.. TODO: Incluir:
..				-Requerimientos funcionales, no funcionales
..              -Diseño: Arquitectura de la aplicación.Incluir Diagrama de Clases Software. Descripción breve de la funcionalidad que proporcionan los módulos principales. 
..              -Librerías empleadas para el desarrollo
..              -Funcionalidad de la aplicación: Descripción respecto de como emplear las funcionalidades.
..                                 *Funcionalidades heredadas: Incluir funcionalidad realizada durante el proyecto de investigación (previo a la tesina).
..                                 *Funcionalidades agregadas: Incluir funcionalidad que fue desarrollada como parte de la tesina. 


Requerimientos funcionales
^^^^^^^^^^^^^^^^^^^^^^^^^^

* Incorporar visualizador de características geométricas inherentes a los distintos tipos de fallas.
* Agregar información respecto al resultado de clasificación y dimensiones obtenidas para una falla en particular.
* Añadir capacidad de filtrado de distintos tipos de fallas a partir de información de la dirección.
 


Requerimientos no funcionales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Manipulación del archivo que contiene información de la geometría de la falla de manera intuitiva.
* Ayuda de fácil acceso para entender los comandos para interactuar con el visualizador.
* Indicación clara de las fallas filtradas en una calle, remarcadas de manera que se trace una ruta sobre ésta. 

.. _disenioApp:

Diseño de la aplicación
^^^^^^^^^^^^^^^^^^^^^^^

En primer lugar, esta aplicación consistía en la georeferenciación de fallas sobre un mapa interactivo, cuyo objetivo principal era la visualización del estado de la fallas informadas por usuarios y características que los mismos aportaban vía web. Esta aplicación fue pensada para ser utilizada por diferentes tipos de usuarios entre los que se encontraban:

* Usuarios anónimos
* Usuarios registrados (administradores)
  
Los usuarios anónimos disponen de las siguientes funciones:

* **Informar de una falla**: Esta funcionalidad permite especificar la calle y altura donde se encuentra localizada una falla, la clase a la que la falla pertenece (Ver :doc:`../Cap2/Cap2`), una pequeña observación (opcional) y una o más imágenes de la falla notificada. Esta información luego se envía y se registra en el sistema de administración de fallas.
   
* **Visualización de la información asociada a una falla previamente informada**: Permite visualizar información sobre las especificaciones de la falla previamente notificada por otro usuario y los comentarios que otras personas hicieron sobre ésta.

Por otro lado, los usuarios registrados pueden realizar las siguientes operaciones en la aplicación web:

* **Informar de una falla**: Ésta funcionalidad se encuentra extendida acorde a los conocimientos técnicos del personal que opera el sistema, proveyendo las mismas funcionalidades que las que se encuentran disponibles para el perfil de usuario anónimo y adicionalmente, vocabulario específico de cada tipo de falla.

* **Ver fallas reparadas**: Esta función es exclusiva del usuario registrado y permite visualizar de manera veloz sobre el mapa las fallas que se encuentran reparadas o las que no.

* **Agregar tipos de fallas**: Brinda la posibilidad de añadir un nuevo tipo de falla al sistema e incorporando todos aquellos atributos y características técnicas inherentes a la misma.

* **Filtrado de fallas por calle**: Permite trazar una ruta sobre el mapa de aquellas fallas pertenecientes a una calle en particular, con la posibilidad de establecer el tipo y el estado de la falla.

* **Cambio de estado de fallas**: Esta funcionalidad permite modificar el estado de una falla por el siguiente en la secuencia de estados, dependiendo los atributos del siguiente estado del estado actual de la misma.  



Estructura general del proyecto
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La aplicación web fue desarrollada con el lenguaje de programación PHP empleando el framework CodeIgniter, el cual emplea la arquitectura Model-View-Controller, para la funcionalidad backend, en combinación con Boostrap para las vistas del fontend. Por lo que, la arquitectura general de la aplicación web es la se conforma por los siguientes componentes:

.. figure:: ../figs/Cap6/appWebFlowChart.png

   Arquitectura de la aplicación


* **index.php**: Es el controlador principal de la aplicación e inicializa los recursos necesarios para la ejecución de CodeIgniter.
  
* **Routing**: Este módulo recibe las peticiones HTTP realizadas y se encarga de establecer el objetivo de la petición.
   
* **Security**: Realiza el saneamiento de la URL solicitada, comprobando que todas las configuraciones de seguridad establecidos en el servidor se cumplan y luego, realiza la carga del controlador de la aplicación.
   
* **Application Controller**: Es el controlador principal de la aplicación y carga todos aquellos recursos necesarios para el procesamiento de las peticiones, como son los modelos, las vistas, librerías, plugins y scripts.
  
* **Caching**: Este módulo realiza la administración de aquellas peticiones que ya han sido procesadas, por lo que, si una petición ya fue realizada no es necesario renderizarla nuevamente, sino que se retorna directamente por medio de éste módulo el resultado procesado anteriormente.
  
* **View**: Este componente mantiene la estructura general de las vistas, que serán renderizadas posteriormente ante una petición con información que responda a la misma. Si esta activada la posibilidad de caching, ésta será almacenada para responder a futuras peticiones.


La organización de directorios de la aplicación web se divide en dos carpetas: 

* Application
* System

La carpeta Application contiene aquellos elementos que componen la aplicación desarrollada, subdiviéndose en varias subcarpetas siéndo las principales las siguientes:

*  **Config**: Contiene todos aquellos archivos de configuración.
    
*  **Controllers**: Contiene los controladores de la aplicación, donde cada uno se encuentra asociado a una URL que puede ser solicitada. De esta forma, si existe un controlador Producto con un método consultar en midominio.com, el acceso a esta funcionalidad será realizado por la siguiente dirección http://www.midominio.com/index.php/producto/consultar.
    
*  **Core**: Esta carpeta agrupa las clases de base, sobre las que se construye la aplicación.
   
*  **Libraries**: Contiene archivos de librería desarrollados o incorporados para el funcionamiento de la aplicación.
   
*  **Models**: Contiene los modelos que reflejan la lógica de la aplicación, agrupando las clases tanto del problema especifico modelado como de las que acceden a la base de datos.
   
*  **Views**: Esta clase contiene los archivos templates HTML que representan la pagina web final que se enviará en respuesta a una petición. 


Por otro lado, la carpeta System contiene el código fuente propio del framework, donde se encuentran las clases nucleo del framework, los drivers para el acceso a diferentes DBMS, librerías empleadas por éstos y utilidades relacionadas con la manipulación de distintos atributos asociados a las páginas web (cookies, fechas y URL). 


Clases específicas agregadas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para el desarrollo de la funcionalidad incorporada a la aplicación web, se extendió el comportamiento de las clases preexistentes en la misma, siendo éstas las siguientes:

* **Falla**: Se agregó funcionalidad para creación y registro de fallas de peticiones provenientes de la aplicación de captura para fallas confirmadas e informadas, identificar la correspondencia entre una falla y los clusters que fueron clasificados  a partir de ésta.
* **Multimedia**: Esta clase se extendió para incluir el procesamiento de archivos de tipo PCD asociados a una falla, ya que anteriormente solo se permitía subir archivos multimedia de tipo imagen.
* **Calle**: Se añadió comportamiento relacionado con la obtención de sugerencias desde la aplicación de captura, y la obtención de fallas desde ésta a partir del nombre de una calle.
* **Dirección**: Se agregó comportamiento para realizar el geocodificación inversa (reverse geocoding) en las fallas confirmadas enviadas desde la aplicación de captura, y para la obtención de la intersección más próxima a una coordenada geográfica.
* **TipoFalla**: En esta clase se incorporó funcionalidad para obtener los tipos de reparación y el tipo de material asociados a un tipo de falla y disponer de esta información en la aplicación de captura.
* **TipoMaterial**: Se agregó funcionalidad para obtener los tipos de criticidades asociadas con un tipo de material desde la aplicación de captura.
* **Pcd_upload_model**: Esta clase se encarga de gestionar la subida de archivos asociados a capturas (archivos tipo PCD) desde la aplicación de captura.


Librerías empleadas
^^^^^^^^^^^^^^^^^^^

* **Three.js**:
* **Geocoder**:
* **Geonames**:
* **CodeIgniter**:
* **Boostrap**:
* **jQuery**:
* **GMaps**:
* **GeoComplete**:



Funcionalidad de la aplicación
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al ejecutar la aplicación configurada en un servidor web (Ver instrucciones de configuración en archivo "Pasos de instalación - BacheoServer.txt" adjunto al código fuente), se presentará en la pantalla principal un mapa interactivo de la ciudad de Trelew con todas las fallas registradas en el sistema, diferenciándose por colores las fallas con distinto estado.


.. figure:: ../figs/Cap6/pantalla_principal_web.png
   :scale: 100%

   Pantalla de inicio de la aplicación web

Esta pantalla inicial muestra las opciones ofrecidas para un tipo de usuario anónimo, y estas son:

* **Iniciar Sesión**: Esta opción se encuentra disponible para usuarios registrados que ya posean una cuenta en el sistema, y permite el logueo de los mismos.
* **Baches**: Dentro de esta opción se ofrece la función *Agregar* que permite informar una falla nueva. Ver :ref:`_disenioApp`. 
* **Ayuda**: Esta opción permite visualizar el el significado, con respecto al estado, de cada color de los marcadores.
* Barra de búsqueda. Esta barra se encuentra en el centro del conjunto de las opciones y permite buscar y posicionarse sobre una dirección.
* **Visualización de propiedades de falla**: Esta funcionalidad es accesible al hacer click sobre una falla posicionada sobre el mapa y redirige al usuario a una ventana donde se puede observar en el banner principal el identificador de la falla, conformado por el símbolo hashtag(#), la palabra *Falla* y el número de falla registrada. Dentro de esta pantalla se puede visualizar un submenú, donde se agrupan las siguientes opciones:
	
	* **Especificación de la falla**: Esta pestaña muestra un minimapa con la ubicación de la falla y ofrece información relacionada con las propiedades de la misma, mostrando el tipo de falla, criticidad, dirección (calle y altura), estado y fecha de establecimiento del último estado.   
	* **Comunidad social**: Permite a un usuario anónimo ver los comentarios hechos por otros usuarios relacionados con la falla, además de poder agregar comentarios. 


.. figure:: ../figs/Cap6/pantallaVisualizacionPropsUserAnonimo.png
   :scale: 100%

   Pantalla de visualización de propiedades de la falla (usuario anónimo)


Una vez autentificado un usuario este accede al siguiente conjunto de operaciones:

* Baches. Este menú ofrece las opciones:

    - Informar falla. Ver :ref:`_disenioApp`
    - Ver fallas reparadas. Ver :ref:`_disenioApp`
      
* TipoFalla

    - Agregar. Ver :ref:`_disenioApp`
      
* **Barra de búsqueda**: Idem para usuario anónimo.
  
* **Registrar Usuarios**: Esta opción permite a un administrador agregar nuevos usuarios al sistema, especificando para ello nombre, apellido, teléfono, mail, usuario y contraseña. Luego debe hacer presionar sobre la opción *Registrar* para proceder con el registro de éste.
    
* **Barra lateral de filtrado**: Esta barra se encuentra localizada en la parte superior izquierda del menú de opciones con un botón, y al acceder se despliega un sidebar donde el usuario debe seleccionar la opción *Filtrado de fallas por calle*. Una vez hecho esto, se abrirá un menú en la misma sidebar en el cual el usuario ingresará la calle, y seleccionara por medio de la opción "Seleccionar tipo de falla" el/los tipo/s de falla que desea filtrar. Además, deberá seleccionar el/los estados de falla. Una vez hecho esto se solicita el filtrado por medio del botón "Buscar", luego se trazará una ruta si existiesen ese tipo de fallas sobre la calle especificada. Con la opción *Limpiar Ruta* se puede realizar un borrado de la ruta trazada.  
  
* **Ayuda**: Idem para usuario anónimo.  
  
* **Visualización de propiedades de falla**: Esta opción cumple el mismo objetivo que la opción de visualización para un usuario anónimo, incluyendo las mismas funcionalidades y agregando las siguientes:
  
	* **Estado de falla**: Esta opción permite la modificación del estado asociado a una falla, permitiendo que se cambie el estado de la falla al estado siguiente en la secuencia de estados, y sus atributos dependen del tipo de estado en el que se encuentra actualmente la falla. Una vez completados todos los campos específicos del estado, el usuario deberá seleccionar la opción *Confirmar* para proceder con el cambio de estado.
	  
	* **Visor de nube de puntos**: Permite la visualización de el/los archivo/s de  nube de puntos PCD asociados a una falla. Para conseguir ésto, se debe posicionar el cursor sobre uno de los thumbnails que contienen imágenes miniatura con el logo de la universidad y seleccionar la opción *Ver*. Ésto desplegará el visor y permitirá rotar por medio del mouse la imagen y acceder a los comandos del mismo a través de la opción *Ayuda visor*.
	  
	* *Visor de clusters*: Esta funcionalidad muestra aquellos clusters asociados a una falla que fueron aislados y clasificados, indicando para cada cluster el tipo de falla que fue predicho por la aplicación de clasificación, nombre del archivo (nombre de la falla y número de cluster), largo, ancho y profundidad en centímetros.
	     

.. figure:: ../figs/Cap6/pantallaVisualizacionPropsUserRegistrado.png
   :scale: 100%

   Pantalla de visualización de propiedades de la falla (usuario registrado)



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

La arquitectura de la aplicación cliente esta formada por los siguientes componentes principales:

* **Dispositivo Kinect**: La interacción con el dispositivo Microsoft Kinect consiste únicamente en la obtención de frames de profundidad y de video, necesarios para la generación del archivo de nube de puntos. Estos frames se solicitan de manera continua y son renderizados y visualizados en tiempo real por la aplicación, en la ventana de captura. Ésta ventana se compone de dos visualizadores, uno que muestra una imagen de video a color y otro con una imagen de profundidad, con distintos colores asociados a las distancias entre el dispositivo de sensado y la falla. Ésto permite que se pueda corregir la orientación del dispositivo al momento de la captura.  
    
* **Geofencing**: El módulo de geofencing se incluye como parte de la aplicación y tiene la finalidad de computar y retornar las coordenadas donde se encuentra ubicada una falla desde el dispositivo GPS para fallas confirmadas. Éste brinda dos modos de operación, uno donde se leen coordenadas desde el dispositivo reales ("real-gps") y otro donde se lee un conjunto de coordenadas artificiales y se iteran de manera circular ("fake-gps"). Éste último, fue realizado por motivos de debugging entre la aplicación de captura y la aplicación web, en entornos cerrados donde no se dispone de conectividad GPS.
  
* **APIClient**: Este módulo es incluido junto con la aplicación contiene la clase principal encargada del intercambio de información de fallas entre la aplicación web y aplicación de captura.  
  
* **Aplicación cliente**: La aplicación cliente tiene como objetivo ofrecer tanto la captura, administración y envío al servidor de fallas, tanto informadas como confirmadas. Con respecto a la gestión de fallas confirmadas, la aplicación se comunica adicionalmente con el módulo GPS, para la obtención de las coordenadas de la falla, mientras que para las fallas informadas ésta interacción no es necesaria, debido a que las coordenadas de la dirección ya fueron especificadas en uno de los flujos de trabajo.    



.. figure:: ../figs/Cap6/arquitecturaAppCliente.png
   :scale: 100%

   Arquitectura general de aplicación cliente


De esta manera, la aplicación cliente se compone de las siguientes clases software:

* **Main**: Esta es la clase principal que efectúa la configuración inicial de la aplicación  y administra los capturadores asociados a fallas informadas y confirmadas.
  
* Capturador: Esta clase representa un objeto que realiza la captura de una falla con estado Confirmada, y se ejecutar todas aquellas operaciones inherentes a la administración de una falla Confirmada como son enviar fallas a la aplicación web, descartar fallas y solicitar a GeofencingAPI la computación de la latitud y longitud asociada a una falla.      
  
* CapturadorInformados: Representa al objeto encargado de realizar las operaciones de captura de fallas Informadas, ejecutando las operaciones relacionadas con la administración de fallas informadas, excluyendo de este conjunto las operaciones de computación de coordenadas de la falla. Adicionalmente, encapsula las operaciones de solicitud y carga de fallas informadas en memoria desde la aplicación web.
  
* ItemFalla: Esta clase representa a una falla confirmada o informada administrada por un capturador, y mantiene para cada falla el estado actual (Informada o Confirmada) y una colección de objetos Captura asociadas a ésta.
  
* Estado: Representa el estado actual de la falla y sus atributos depende del estado concreto que la falla tenga asociado. De esta superclase extienden dos subclases que son: Confirmada e Informada. Confirmada mantiene información respecto de las propiedades asociadas a la falla (tipo de falla, tipo de material y criticidad)coordenadas de la falla (latitud y longitud) y si es posible obtenerlos, información de la dirección. Por otro lado, Informada solamente mantiene información de la dirección (calle y altura) y el identificador con el que la falla se encuentra registrada.
  
* Captura: Esta clase contiene información propia de una captura individual para un objeto ItemFalla (nombre captura, extensión, directorio) y el comportamiento para almacenar esta persistentemente. 
  
* GeofencingAPI: Es la API principal de comunicación con el dispositivo GPS y principalmente contiene las operaciones de obtención de coordenadas.
  
* ApiClientApp: Esta clase representa la API que contiene la funcionalidad relacionada con la comunicación entre la aplicación cliente y la aplicación web, para la obtención de fallas informadas y envío de fallas (confirmadas e informadas) al servidor. Mantiene atributos relacionados con la conexión entre ambas aplicaciones, la cantidad de bytes enviados y bytes totales de las capturas a enviar.    
   

.. figure:: ../figs/Cap6/Final_Diagrama_clases_appCliente.png

   Diagrama de clases software de la aplicación de captura



Librerías empleadas en la aplicación
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Esta aplicación fue desarrollada en el lenguaje de programación Python 2.7 empleando las siguientes librerías:

.. https://kivy.org/docs/philosophy.html
.. https://kivy.org/docs/guide/basic.html
.. https://kivy.org/docs/guide/architecture.html
.. 

* **Kivy**: Kivy es una framework open-source en Python orientada al desarrollo rápido y sencillo de aplicaciones multiplataforma con widgets que soportan multi-touch, es decir, que proporciona soporte nativo para diferentes dispositivos táctiles que soportan la  detección de múltiples pulsaciones simultáneas. Esta librería se encuentra disponible en Android, Linux, OS X, iOS y Rasperry, por lo que permite que se desarrollen tanto aplicaciones para computadoras de escritorio como aplicaciones móviles. Kivy facilita el diseño de aplicaciones brindando interfaces gráficas escalables que no interfieran con el comportamiento de relacionado a validaciones necesarias en la aplicación, definiendo para ello un lenguaje declarativo de marcado denominado lenguaje KV (KVLang o KV languaje). Este lenguaje, permite especificar de manera declarativa una jerarquía de widgets y realizar bindeos entre distintos elementos de la GUI o, entre la aplicación y los widgets, separando el código relacionado con la construcción de interfaz gráfica del que es necesario para el funcionamiento de la aplicación web. Este lenguaje, se especifica en archivos con extensión .kv cuyo nombre es el mismo que el de la clase del widget. Este framework fue empleado para el desarrollo de la interfaz gráfica de la aplicación de captura.

.. https://kivy.org/docs/api-kivy.garden.html
.. https://github.com/kivy-garden/garden.xpopup

* **XpopUp**: Este módulo es un conjunto de widgets generados a partir de la clase Popup de Kivy para el desarrollo de diálogos de pregunta, díalogos de mensaje y diálogos con barras de progreso. Es parte de la extensión Kivy-Garden, que consiste en un conjunto de herramientas desarrolladas y mantenidas por la comunidad de usuarios de Kivy. Esta extensión fue empleada en combinación con el conjunto de widgets base de Kivy.
  

* **Requests**: Es una librería en Python para realizar solicitudes HTTP de una forma sencilla, permitiendo agregar encabezados, datos de un form, archivos multi-parte con diccionarios en Python y acceder a las respuestas del servidor de la misma manera, sin necesidad de formar completamente las Query Strings de las URL o codificar los datos enviados por POST. Esta librería emplea urllib3 para mantener las conexiones con el servidor activas y realizar consultas de manera automática. Esta librería fue empleada para desarrollar la API de comunicación entre la aplicación de captura y la aplicación web.
    
* **Pypcd**: Es un componente empleado para el almacenamiento y lectura de nubes de puntos en disco empleadas por PCL. Fue empleada para el almacenamiento de archivos de nubes de puntos(PCD) asociados con un objeto Captura.
   
* **Iconfonts**: Es una de las extensiones en Kivy-Garden para incorporar la utilización de icon fonts en widgets del tipo Labes y sus derivados en aplicaciones desarrolladas con Kivy. El funcionamiento de esta librería consiste en generar un archivo *.fontd* que pueda ser usado en combinación con un archivo de fuentes personalizado *.ttf* y su archivo *.css* asociado, dentro de la aplicación. Esta librería fue empleada para incluir iconos personalizados en la aplicación tales, como los que figuran en las opciones de obtención de fallas informadas, captura de fallas informadas y confirmadas, etc.
  

* **Tiny-db**: Es una librería de poco peso desarrollada en Python para el almacenamiento de documentos que puedan ser convertidos a un formato de diccionarios en Python, pensada para el almacenamiento local sin acceso concurrente, servidores HTTP o índices en tablas. Este elemento fue empleado para desarrollar funcionalidad de debugging para el registro global de las latitudes y longitudes, archivos de captura y fecha de cada conjunto de fallas, en formato json. 
  
* **ZODB/ZEO**:
* **gps**:


Funcionalidad de la aplicación
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _configAppCliente:

Configuración de la aplicación
""""""""""""""""""""""""""""""

.. TODO: PONER LA CONFIGURACIÓN DE LA APLICACION ACA!


Modo de uso de la aplicación
++++++++++++++++++++++++++++

Al iniciar la aplicación, se realizará una comprobación de conexión con sensor y se comprobará que exista el archivo de configuración de propiedades en el directorio de ejecución de la aplicación (Ver sección :ref:`_configAppCliente`) y se éstas se efectúa correctamente se visualizará un conjunto de submenus que agrupan las siguientes funcionalidades:

* **Seleccionar BD**: Este menú agrupa las opciones relacionadas con el registro de coordenadas geográficas asociadas a la captura de fallas. La funcionalidad de este módulo se realizó con fines de debugging para mantener un registro de la ubicación de las fallas ya capturadas en una base de datos JSON, evitar la recaptura de éstas y facilitar la organización de las mismas, registrando las coordenadas (latitud y longitud), el nombre del archivo de captura PCD y la fecha en que dicho conjunto de fallas fue capturada.

* **Captura de fallas**: Este módulo agrupa la funcionalidad de captura de fallas confirmadas e informadas y la obtención de fallas desde el servidor web.
  
* **Almacenar recorrido**: Contiene las funcionalidades relacionadas con la lectura/escritura de archivos de recorridos desde/hacia disco.
  
* **Subida de archivos**: Este menú abarca la opción de subida de archivos de captura a la aplicación web.


.. figure:: ../figs/Cap6/MenuPrincipalAppCliente.png
   :scale: 100%

   Menú principal de aplicación de captura

En el caso de que la conexión al sensor no pueda establecerse, no podrán realizarse capturas de ningún tipo y no se podrá emplear la funcionalidad de almacenamiento de recorridos. La aplicación mostrará un diálogo preguntando si se desea continuar con la ejecución de aplicación o si se desea terminar con la ejecución de la misma.


.. figure:: ../figs/Cap6/errorConexionIincial.png

   Error de conexión del sensor inicial

.. TODO: VER SI EXISTE ERROR DE PROPIEDADES EN JSON AL INICIAR!!!


Aunque el menú de selección de BD no forma parte de la funcionalidad de captura, ya que fue desarrollado previamente al desarrollo de la generación de archivos de recorridos, este módulo se conservo para conservar un registro global de las fallas y sus fechas de captura, por lo que no será explicado en detalle, sin embargo antes de comenzar la captura de fallas informadas y confirmadas, se debe seleccionar este menú y seleccionar sobre la opción *Comenzar BD nueva con la fecha actual(opción por defecto)*. Ésto producirá una BD JSON global (para todas las fallas de todos los recorridos) y permitirá continuar con la captura de fallas y la generación de recorridos.


.. figure:: ../figs/Cap6/capturarFallaNueva1.png
   :scale: 100%

   Inicialización de BD de registro de fallas


Con respecto al menú de captura de fallas, si esta pestaña es seleccionada se podrán observar las siguientes opciones:

* Capturar falla nueva
* Obtener falla informada
* Capturar falla informada

La opción de capturar falla nueva permite realizar la captura de fallas con estado confirmada, y al seleccionarse se mostrará una pantalla donde el usuario deberá seleccionar las propiedades de la falla que se está capturando siendo éstas: el tipo de falla, tipo de material de la calle donde la falla se localiza y nivel de criticidad específico para cada tipo de falla. Una vez confirmadas estas propiedades, se mostrará una vista con un explorador de archivos desde donde se podrá navegar la estructura de archivos de las carpetas locales a la ejecución de la aplicación y se podrá crear/eliminar un directorio de capturas y escribir en la barra de búsqueda un nombre de archivo para la captura. 


.. figure:: ../figs/Cap6/capturaFallaNueva2.png
   :scale: 100%

   Creación de un directorio en el explorador de archivos


.. figure:: ../figs/Cap6/capturaFallaNueva3.png
   :scale: 100%

   Establecimiento del nombre de la falla en el directorio creado anteriormente


Al confirmar el directorio y el nombre del archivo de captura, se mostrarán los visores de la imagen en video y de la imagen de profundidad, con la opción de generar una captura desde la opción *Capturar* o presionando SPACEBAR. 


.. figure:: ../figs/Cap6/capturaFallaNueva4.png
   :scale: 100%

   Visor de imagen RGB y de profundidad

Una vez capturada una falla, se mostrará un cuadro de diálogo que permitirá visualizar la falla a través de la herramienta *pcl_viewer* ofrecida por PCL y luego, al cerrar este cuadro de diálogo se proporcionará la opción de conservar o descartar dicha captura, si ésta no es de una calidad aceptable. Estos dos últimos pasos pueden repetirse, permitiendo la obtención de múltiples capturas asociadas a una falla confirmada. 

.. figure:: ../figs/Cap6/capturaFallaNueva5.png
   :scale: 100%

   Visualización de la falla capturada

Con respecto a la opción de *obtención de fallas*, ésta consiste en obtener desde el servidor fallas con estado informada en  una calle determinada y cargarlas en memoria, para su posterior captura. Al seleccionar esta opción, se una entrada de texto donde se deberá ingresar el nombre de la calle, cuyo valor será autocompletado con las calles que el servidor tiene registradas. Una vez ingresado el nombre de la calle se debe seleccionar la opción *Solicitar fallas servidor*, que enviará la petición a la aplicación web para su carga en memoria.      


.. figure:: ../figs/Cap6/obtencionDireccion1.png
   :scale: 100%

   Ingreso de nombre de calle 

Una vez obtenidas las fallas informadas desde la aplicación web, se puede proceder con la capturar de las mismas seleccionando la opción *Capturar falla informada*, que mostrará un listado con la información asociada a la falla informada: ID que es el identificador de la falla en el sistema, nombre de la calle y altura de la misma, donde el usuario deberá seleccionar una de las fallas de la lista y presionar sobre la opción *Realizar captura*. 

.. figure:: ../figs/Cap6/capturaFallaInforma1.png
   :scale: 100%
   
   Selección de una falla informada para su captura

Luego de seleccionar la falla, se mostrará el explorador de archivos para la selección de nombre  de falla y creación/eliminación de directorios de captura.

.. figure:: ../figs/Cap6/capturaFallaInforma2.png
   :scale: 100%

   Selección del nombre y directorio donde se almacenará la falla informada



Finalmente, se mostrará la pantalla que contiene los visores y se mostrarán los cuadros de diálogos para la visualización y conservación de la captura que son visualizados para las fallas confirmadas.


.. figure:: ../figs/Cap6/capturaFallaInforma3.png
   :scale: 100%

   Captura de falla informada

Con respecto al menú de *Almacenar recorrido* este ofrece las siguientes opciones:

* Guardar fallas capturadas
* Cargar fallas capturadas


La opción de *Guardar fallas capturadas* permite almacenar una o varias fallas (informadas y/o capturadas) previamente en un archivo de recorrido (archivos .rec), para ser leído posteriormente. Al seleccionar esta opción, se podrá abrirá una ventana que permitirá navegar la jerarquía de directorios de la aplicación para seleccionar un directorio. La jerarquía puede visualizarse en dos modos: Vista iconos y Vista lista; Si se selecciona vista iconos (opción por defecto) se puede visualizar los elementos en iconos de tamaño mediano, mientras que en vista lista se puede visualizar un listado con el nombre completo de cada uno de los archivos y directorios en una lista.  



.. figure:: ../figs/Cap6/menuAlmacenarRecorrido.png
   :scale: 100%
 
   Menú Almacenar recorrido

Una vez seleccionado el directorio (dentro del mismo), se debe ingresar en la barra inferior el nombre del archivo de recorrido (obviando la extension .rec) y elegir la opción *Guardar*. Una vez realizado el almacenamiento exitoso, las fallas informadas y confirmadas que se almacenarán en disco y se eliminarán de memoria, por lo que luego de haber realizado el guardado del recorrido, éstas no podrán subirse al servidor, debiendo ser cargadas nuevamente para este fin. 


.. figure:: ../figs/Cap6/almacenarFalla1.png
   :scale: 100%

   Almacenamiento de recorrido

Respecto de la opción *Cargar fallas capturadas*, esta permite cargar en memoria un conjunto de fallas almacenadas en un archivo de recorridos. Al momento de realizar la carga de un archivo de recorrido en memoria, es importante realizar un almacenamiento persistente de las fallas que puedan existir en memoria, ya que éstas serán eliminadas antes de proceder con la carga del recorrido. Al seleccionar esta opción, se mostrará un explorador para la navegación de archivos a partir del cual se localizará el archivo de recorrido. Una vez seleccionado éste, se debe confirmar su apertura seleccionando la opción *Abrir*, y la aplicación verificará la consistencia de todos los archivos PCD en las rutas en que se almacenaron al momento de guardar el recorrido, y cargará en memoria solo aquellas consistentes, indicando que existió un error al momento de realizar la carga con algunas capturas.


.. figure:: ../figs/Cap6/cargaFallas1.png
   :scale: 100%

   Carga de recorrido


.. figure:: ../figs/Cap6/cargaFallas2.png
   :scale: 100%

   Mensaje al realizar una carga exitosa de un recorrido consistente


Por último, el menú **Subida de archivos** contiene la funcionalidad de subida de fallas a la aplicación web, y ésta solo puede ser seleccionada si existe al menos una fallas capturada en la aplicación, ya sea por algunas de las opciones de captura de fallas o por la carga de un recorrido.

.. figure:: ../figs/Cap6/subirFalla1.png
   :scale: 100%

   Menú de subida de archivos


Luego de haber seleccionado esta opción, aparecerá un listado con las fallas informadas y confirmadas junto con su información asociada, mostrando para las fallas confirmadas la latitud y longitud, el campo ID se visualizará como "No disponible" ya que este campo es exclusivo de las fallas informadas y, opcionalmente si dispone de acceso a Internet, el nombre de la calle y el rango estimado de altura en el que la misma se encuentra. Mientras que para fallas informadas, se mostrará el ID con el que la falla se encuentra registrada en la aplicación web y en lugar de latitud y longitud se mostrará la calle y altura específica con que fue notificada previamente. En esta ventana se deben seleccionar una o más fallas para enviar y luego seleccionar la opción *Enviar fallas*, lo que mostrará una barra de progreso con respecto al envío de fallas.


.. figure:: ../figs/Cap6/subirFalla2.png
   :scale: 100%

   Selección de fallas para subir a la aplicación web


Al finalizar el envío de fallas, se mostrará un cuadro de dialogo consultando si las capturas se conservarán en disco y en caso de seleccionarse la opción afirmativa, se conservarán los archivos de captura en disco y en memoria, en caso de que se desee aún generar un recorrido con esas fallas en particular. En caso de desear eliminar las capturas subidas, éstas se descartarán de disco y de memoria, por lo que al retornar a la pantalla anterior no podrán seleccionarse nuevamente para ser enviadas y serán eliminadas permanentemente. En caso de haber sido cargadas desde un archivo de recorrido, este quedará inutilizado debido a que las fallas se borran desde disco y el archivo de recorrido una referencia a las fallas en disco.  


.. figure:: ../figs/Cap6/subirFalla3.png
   :scale: 100%

   Cuadro de diálogo




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


* **EstrategiaDescriptorAbstract**: Esta clase genera el PointFeature a partir de un cluster y puede ser extendida para distintos tipos de descriptores provistos por PCL. Ver :doc:`../Cap3/Cap3`.
  

* **EstrategiaClasificacionMLAbstract**: Esta clase representa la estrategia de clasificación que se puede adoptar para clasificar a que clase el cluster pertenece. Puede ser extendida para ser utilizada con distintos modelos de Machine Learning.Ver :doc:`../Cap4/Cap4`.

* **DBManager**: Esta clase engloba el comportamiento relacionado con la interacción de MainPipeLine con una base de datos que mantiene un registro de las fallas previamente clasificadas. Todas las fallas procesadas y clasificadas con o sin éxito, se agregan a dicha base. 



.. figure:: ../figs/Cap6/Final_Diagrama_de_clases_clasificador.png
   :scale: 100%

   Diagrama de clases software de la aplicación de clasificación


Librerías empleadas para el desarrollo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Boost**: Es una librería open-source que fue diseñada con el objetivo de extender las capacidades del lenguaje C++ e incluye varias funcionalidades entre las que se destacan el procesamiento de texto, operaciones de iteración sobre directorios del sistema operativo, operaciones de entrada/salida, programación concurrente, etc. Esta librería fue empleada principalmente para implementar la iteración, búsqueda y creación de elementos en la jerarquía de directorios del sistema operativo y el procesamiento de cadenas de texto asociadas a éstas.

* PCL: Librería descripta en el capítulo 4. Ver *Freenect y Librería Point Cloud Library (PCL)* en :doc:`../Cap4/Cap4`. 

* JSONCPP: Es una librería en C++ empleada para la manipulación de archivos con formato JSON y la serialización/deserialización de éstos hacia/desde disco. Fue empleada para funcionalidad relacionada con creación de los archivos .json que mantienen información de dimensiones respecto de la falla clasificada.
  
* SQLite3: Es un sistema de bases de datos relacional desarrollada en C, donde la aplicación cliente realiza consultas a la base de datos por medio de funciones, en lugar de comunicarse con un proceso independiente, lo que provoca una reducción de la latencia en la interacción. Esta base de datos fue utilizada para mantener un registro de las fallas que fueron procesadas, evitando procesamiento innecesario. 


Funcionalidad de la aplicación
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para el funcionamiento de esta aplicación, es necesario compilarla siguiendo las instrucciones en README.txt desde el repositorio https://github.com/rhuincalef/clasificadorFallas o, en el código fuente adjunto. Luego se debe realizar la configuración de los parámetros obligatorios de la aplicación, para ello se debe alterar el archivo *config_pipeline.json-default* cambiando la extensión a .json y modificando cada una de las siguientes entradas:

* **configuracion_global**: Esta entrada contiene el *dir_entrada* que es el directorio raíz desde el cual esta aplicación lee los archivos .pcd a procesar; *dir_salida* es el directorio raíz donde la aplicación almacenará los resultados obtenidos del procesamiento. Por último, cuenta con *database_muestras* que indica la ruta absoluta del archivo de base de datos con extensión .db, que se puede encontrar en el archivo base *fallas.db*.
      
* **clasificador**: Esta entrada consiste en aquellas configuraciones relativas al tipo de modelo de clasificación seleccionado. En *tipo* se debe especificar el modelo de clasificación a utilizar, siendo el único modelo implementado "svm". *path_modelo* especifica la ruta absoluta al modelo entrenado utilizado por el clasificador. 
 

* **estrategia_segmetador**: Esta entrada contiene aquellos valores empleados para la calibración del algoritmo de segmentación seleccionado. Estos valores fueron determinados por medio de pruebas de segmentación para baches y grietas y deben ser modificados con precaución según el tipo de objetos que desee aislar. No es necesario modificar estos valores para probar con grietas y baches. El único algoritmo implementado es Planar Euclidean que se encuentra especificado en la entrada *tipo*, el cual consta para planar segmentation de *distance_threshold*, *max_iterations* y de euclidean_segmentation (RANSAC) *tolerance*, *min_cluster_size* y *max_cluster_size*. Ver *Algoritmos de segmentación de objetos* en :doc:`../Cap3/Cap3`.


* **point_feature**: Esta entrada especifica el tipo de punto ofrecido por PCL a utilizar para la lectura, procesamiento y almacenamiento de nubes de puntos. Ver *Representación y almacenamiento de una nube de puntos* en :doc:`../Cap3/Cap3`.           


* **estrategia_descriptor**: Esta entrada representa el tipo de descriptor de PCL que se utilizará para generar el descriptor personalizado (PointFeature). *tipo_descriptor* determina el tipo de descriptor que puede ser "GRSD" o "ESF", aunque ESF es el descriptor que más precisión tiene para este desarrollo en concreto.
  
  Tener en consideración, que el tipo de modelo entrenado especificado en entrada **clasificador** tiene que estar entrenado con el tipo de estrategia descriptor seleccionada, por lo que si se selecciona ESF el *path_modelo* debe ser el de un modelo que este entrenado con éste feature de PCL. Ver *Selección de features para ML en PCL* en :doc:`../Cap4/Cap4`. 


Finalmente, para ejecutar la aplicación en segundo plano como una tarea programada, se deben seguir las instrucciones especificadas en README.txt, donde se detallan lapsos de ejecución de la tarea en intervalos de 5 minutos, todos los días. Esta configuración requiere el uso de *crontab* y únicamente fue probada bajo Linux (Ubuntu 16.14 y Manjaro Hakoila 17.16). 



