Capítulo 5. Herramientas GPS y Geocoding
===============================================================

El objetivo principal del siguiente capítulo será la determinación de posiciones sobre la superficie terrestre. Para poder alcanzar este objetivo, se describirá el contexto matemático básico para expresar un punto sobre la Tierra, además, de los sistemas de coordenadas y las proyecciones cartográficas.

Geodesia. Forma y representación de la Tierra
---------------------------------------------

La Geodesia es la ciencia que se encarga del estudio de la figura, las dimensiones y el campo gravitatorio de la Tierra, así como su variación a través del tiempo.

Friedrich Robert Helmert (1880) define la Geodesia como "la ciencia de la medida y representación de la Tierra".

El diccionario de la Real Academia Española define la Geodesia como "Ciencia matemática que tiene por objeto determinar la figura y magnitud del globo terrestre o de gran parte de él, y construir los mapas correspondientes".

La razón de estudiar la forma de la Tierra se debe a que esta es redonda, aunque no por completo, por lo que debe estudiarse su figura realmente cómo es para obtener mapas precisos. Los mapas ayudan a comprender los tipos de información de la que disponemos.

En la actualidad, el ámbito de la Geodesia es mucho más amplio que la definición clásica de Helmert, dado que como se mencionó anteriormente incluye el campo gravitatorio de la Tierra y su variación en el tiempo.

La Geodesia se puede dividir en varias ramas:

* Geodesia Física
Constituida por las teorías y modelos para la determinación de la figura del geoide mediante gravimetría, determinación del geoide mediante el campo gravitatorio y sus anomalías.

* Geodesia Geométrica
Determina la figura terrestre a través de mediciones en su aspecto geométrico, incluyendo la determinación de coordenadas de puntos en su superficie.

* Astronomía Geodésica
Constituida por métodos astronómicos, los cuales permiten la determinación de coordenadas geográficas sobre la superficie terrestre a partir de mediciones de los astros (se tiene en cuenta una serie de puntos fundamentales a partir de los cuales se arman redes geodésicas, se mencionarán más adelante).

* Geodesia Espacial
Determina de coordenadas geográficas mediante mediciones tomadas a través de satélites artificiales, objetos naturales o artificiales exteriores a la Tierra.

Las superficies de referencia de la Tierra utilizadas por la geodesia clásica son la elipsoide y geoide.

Geoide
^^^^^^

Es el objeto geométrico irregular utilizado para hacer referencia a la Tierra. Se define como una superficie en la que todos los puntos experimentan la misma atracción gravitatoria siendo esta equivalente a la experimentada al nivel del mar.

En la actualidad se dice que el Geoide es una superficie equipotencial [#e1]_ del campo de gravedad terrestre ajustado a determinaciones del nivel medio del mar corregidas por los mejores modelos de circulación oceánica, de las perturbaciones atmosféricas y toda influencia no periódica que afecte el nivel del agua.

Se trata de una superficie que no es totalmente estable debido a varios ajustes incorporados, por lo cual ciertas descargas fluviales o desprendimientos de barreras de hielo pueden influir en el cálculo de la superficie del mismo Geoide. Aunque esta concepción es muy reciente (1980), se encuentra apoyada por detalladas investigaciones que surgen de sensores montados en satélites artificiales.

.. figure:: ../figs/Cap5/geoide_elipsoide.png
   :scale: 50%

   Elipsoide y geoide.

.. rubric:: Footnotes

.. [#e1] Una superficie equipotencial es el lugar geométrico de los puntos de un campo escalar en los cuales el "potencial de campo" o valor numérico de la función que representa el campo, es constante.

Elipsoide
^^^^^^^^^

Es el objeto regular utilizado para hacer referencia a la Tierra. Se encuentra definido por dos parámetros: el semieje mayor y el semieje menor. En el caso de la Tierra estos ejes se corresponden con el readio ecuatorial y el radio polar. La relación existente entre estas dos medidas define el grado de achatamiento del elipsoide, dado por:

.. math:: f = \frac {r_{1} - r_{2}} {r_{1}}

siendo :math:`r_{1}` el semieje mayor y :math:`r_{2}` el menor.

.. figure:: ../figs/Cap5/elipsoide.png
   :scale: 50%

   Elipsoide.
.. http://volaya.github.io/libro-sig/chapters/Fundamentos_cartograficos.html

+-----------------------+------------------+
|                                          |
+=======================+==================+
|      Elipsoide        |      WGS84       |
+-----------------------+------------------+
|      Eje Mayor        |      63781       |
+-----------------------+------------------+
| Inverso aplastamiento |   298.2572236    |
+-----------------------+------------------+
|     Aplastamiento     |   0.003352811    |
+-----------------------+------------------+
|      Eje Menor        |  6356752.314     |
+-----------------------+------------------+
|     Excentricidad     | 0.0818119190843  |
+-----------------------+------------------+

   Elipsoides de uso habitual

Datum
^^^^^

Es definido como aquel punto tangente al elipsoide y al Geoide, en el cual ambos son coincidentes.

Compuesto por:

* los parámetros *r1* y *r2* del elipsoide.

* un punto denominado fundamental. A este punto se le define sus coordenadas geográficas (latitud, longitud) y el acimut de una dirección con origen en este punto. Esta desviación se la denomina:


   * desviación de la vertical (Eta), dada por la no coincidencia de la vertical entre el geoide y el elipsoide.
   * desviación en el meridiano (Xi)

La altura geoidal en el punto fundamental es, como cabe esperar, igual a cero. La vertical al geoide y al elipsoide son idénticas en el punto fundamental.

Como ya hemos mencionado la superficie terrestre no es esférica. Por lo que dicha irregularidad, hace que cada país, región, escoja un modelo de cuerpo (definible matemáticamente) ajustado a la figura de la Tierra en su territorio.
Para un mismo elipsoide pueden utilizarse distintos puntos fundamentales, que darán lugar a distintos datum y a distintas coordenadas para un mismo punto.

+--------------------+------------------+----------------+----------------+---------------+
|      Datum         |      Area        |    Latitud     |    Longitud    |   Elipsoide   |
+====================+==================+================+================+===============+
|   Campo Inchauspe  |    Argentina     | 30 58 16.56 S  | 62 10 12.03 W  | Internacional |
+--------------------+------------------+----------------+----------------+---------------+
|   Corrego Alegre   |     Brasil       | 19 50 15.14 S  | 48 57 42.75 W  | Internacional |
+--------------------+------------------+----------------+----------------+---------------+
| Norte América 1927 |  Norte América   | 39 13 26.686 S | 98 32 30.506 W |  Clarke 1866  |
+--------------------+------------------+----------------+----------------+---------------+

   Datums de uso habitual

Coordenadas geográficas
-----------------------

El sistema de coordenadas natural de un esferoide o elipsoide es el de coordenadas angulares (latitud y longitud) que suele denominarse coordenadas geográficas.

**Coordenadas geodésicas**

Son aquellas coordenadas geográficas que están referidas al elipsoide de referencia.

**Coordenadas geocéntricas**

Son aquellas coordenadas geográficas que están definidas con respecto al centro de gravedad de la Tierra. Para poder definir latitud y longitud, es necesario identificar el eje de rotación terrestre.

Paralelos y latitud
^^^^^^^^^^^^^^^^^^^

El plano perpendicular al eje de rotación que corta la Tierra atravesándola por su centro define el Ecuador en su intersección con el esferoide. Por lo tanto, el resto de las líneas de intersección con la superficie terrestre de los infinitos planos perpendiculares al eje de rotación definen los diferentes *paralelos* o líneas de *latitud* constantes.
Latitud es la distancia angular entre el paralelo de un lugar y el Ecuador, se expresa en grados, minutos y segundos de arco y se mide de 0 a 90° hacia el Norte o el Sur.

Meridianos y longitud
^^^^^^^^^^^^^^^^^^^^^

Los meridianos pueden definirse como las líneas de intersección con la superficie terrestre de los infinitos planos que contiene al eje de rotación.
Longitud es la distancia angular entre el meridiano de un lugar y el de Greenwich, expresado en grados, minutos y segundos de arco y se mide de 0 a 180° hacia al Este o hacia el Oeste desde el meridiano de Greenwich.

Direcciones
^^^^^^^^^^^

Se denomina dirección de una recta, al ángulo horizontal existente esa recta y otra que se toma como referencia.

Hay dos formas para definir la dirección entre dos puntos:

**Azimuth o acimut**

Es el ángulo formado por la línea que une el punto de partida y el Norte y la línea que une el punto de partida con el de llegada.

**Rumbo**

Es el ángulo agudo que forma las direcciones Norte o Sur desde el punto de partida y la línea que une ambos puntos.

.. figure:: ../figs/Cap5/rumbo-y-azimut.png
   :scale: 50%

   Rumbo y Azimut.

Sistemas de Proyección cartográfica
-----------------------------------

La proyección cartográfica es el proceso de transformar los puntos de una esfera o elipsoide en sus transformados en una superficie definida, por ejemplo, un plano. Se trata de la aplicación de una función *f* que a cada par de coordenadas geográficas (puntos de la esfera o elipsoide) le hace corresponder un par de coordenadas cartesianas (punto en la superfice de proyección definida), dado por

.. math:: x = f(\theta,\lambda) ; y = f(\theta,\lambda)

De igual manera, a partir de las coordenadas cartesianas puede obtenerse las coordenadas geográficas según

.. math:: \theta = g(x,y) ; \lambda = g(x,y)

Otras superficies pueden ser utilizadas para definir una proyección. Las más habituales son el cono y el cilindro (junto con, por supuesto, el plano), las cuales, situadas en una posición dada en relación con el objeto a proyectar (esto es, la Tierra), definen un tipo dado de proyección. Por lo que se puede distinguir las siguientes proyecciones: cónicas, cilíndricas y planas azimutales.

* Cónicas

La superficie desarrollable que se utiliza es un cono, el cual se arrolla sobre la superficie del elipsoide y se poyecta los puntos sobre él. Se puede utilizar dos tipos de conos en contacto con la superficie definida. Cuando se utiliza un cono tangente, el eje que vincula a los polos es utilizado como vértice y se produce un paralelo llamado estándar a lo largo. Por otro lado, se puede utilizar un cono secante, para el cual se produce dos paralelos estándar.

En general, una proyección secante tiene menos distorsión total que una proyección tangente. Algunas de las proyecciones más conocidas de este grupo son la proyección cónica equiárea de Albers y la proyección conforme cónica de Lambert.

.. http://pdi.topografia.upm.es/mab/tematica/htmls/proyecciones.html

.. http://arquimedes.matem.unam.mx/PUEMAC/PUEMAC_2008/mapas/html/proyecciones/pconica.html

.. http://desktop.arcgis.com/es/arcmap/10.3/guide-books/map-projections/conic-projections.htm

.. figure:: ../figs/Cap5/conicas.png
   :scale: 40%

   Proyecciones cónicas.

.. https://www.blinklearning.com/Cursos/c536159_c24567759__Metodos_de_representacion.php

* Cilíndricas

La superficie desarrollable es un cilindro, el cual se circunscribe alrededor de la superficie del elipsoide. Se trata de un cilindro tangente, donde al proyectar, los meridianos se convierten en líneas paralelas, así como los paralelos, aunque la distancia entre estos últimos no es constante.

En su concepción más simple, el cilindro se sitúa de forma tangente al ecuador (proyección normal o simple), aunque puede situarse secante y hacerlo a los meridianos (proyección transversa) o a otros puntos (proyección oblicua).

La proyección de Mercator, la transversa de Mercator, la cilíndrica de Miller o la cilíndrica equiárea de Lambert son ejemplos relativamente comunes de este tipo de proyecciones.

.. figure:: ../figs/Cap5/cilindricas.png
   :scale: 40%

   Proyecciones cilíndricas.

.. https://www.blinklearning.com/Cursos/c536159_c24567759__Metodos_de_representacion.php

* Planas o azimutales

La superficie desarrollable es directamente un plano. Por lo que tenemos distintos tipos en función de la posición del punto de fuga.

.. figure:: ../figs/Cap5/planas.png
   :scale: 40%

   Proyecciones planas o azimutales.

* Sin superficie desarrollable

Algunas proyecciones no se ajustan exactamente al esquema planteado, y no utilizan una superficie desarrollable como tal sino modificaciones a esta idea. Por ejemplo, las proyecciones policónicas utilizan la misma filosofía que las cónicas, empleando conos, pero en lugar de ser este único, se usan varios conos, cada uno de los cuales se aplica a una franja concreta de la zona proyectada. La unión de todas esas franjas, cada una de ellas proyectada de forma distinta (aunque siempre con una proyección cónica), forma el resultado de la proyección.

Del mismo modo, encontramos proyecciones como la proyección sinusoidal, una proyección de tipo pseudocilíndrico, o la proyección de Werner, cuya superficie desarrollable tiene forma de corazón. Estas proyecciones son, no obstante, de uso menos habitual, y surgen en algunos casos como respuesta a una necesidad cartográfica concreta.

Otra forma distinta de clasificar las proyecciones es según las propiedades métricas que conserven. Toda proyección implica alguna distorsión (denominada anamorfosis), y según cómo sea esta y a qué propiedad métrica afecte o no, podemos definir los siguientes tipos de proyecciones: equiárea, conformes y equidistantes.

* Equiárea

En este tipo de proyecciones se mantiene una escala constante. Es decir, la relación entre un área terrestre y el área proyectada es la misma independientemente de la localización, con lo que la representación proyectada puede emplearse para comparar superficies.

* Conformes

Estas proyecciones mantienen la forma de los objetos, ya que no provocan distorsión de los ángulos. Los meridianos y los paralelos se cortan en la proyección en ángulo recto, igual que sucede en la realidad. Su principal desventaja es que introducen una gran distorsión en el tamaño, y objetos que aparecen proyectados con un tamaño mucho mayor que otros pueden ser en la realidad mucho menores que estos.

* Equidistantes

En estas proyecciones se mantienen las distancias.

Georreferenciación o Geocodificación
------------------------------------

La georeferenciación es un proceso de localización geográfica, dentro de un sistema de coordenadas. En términos más sencillos es asignar coordenadas geográficas a un objeto o estructura.

Este concepto puede ser aplicado a una imagen digital, a la cual aplicamos un conjunto de operaciones geométricas que permiten asignar a cada píxel de la misma un par de coordenadas *(x,y)* en un sistema de proyección. Por ejemplo, Google Earth [#e2]_ es un sistema de georreferenciación, el cual nos permite situar en un mapa puntos concretos de la geografía.

La plataforma web Google Maps nos permite georeferenciar direcciones como "650, 25 de Mayo, Trelew, Chubut" convirtiéndola en coordenadas geográficas. Por ejemplo, la dirección mencionada anteriormente se puede conertir en la siguiente coordenada geográfica latitud X y longitud Y, la cual se puede utilizar para disponer marcadores en un mapa o posicionarse en dicho mapa.

.. [#e2] plataforma web que permite ver y utilizar contenido de datos de mapas y de relieves, imágenes yotros datos proporcionados por Google.

Geocodificación inversa
-----------------------

Es el proceso mediante el cual se convierte coordenadas geográficas en direcciones en lenguaje natural. Se puede mencionar el sistema de geocodificación inversa de Google Maps que, a través del servicio Geocoding API permite realizar este procedimiento mediante solicitudes HTTP.

El ejemplo que sigue a continuación muestra la utilización del servicio de geocodificación inversa utilizando Google Maps JavaScript API:

::

   import math
   print 'import done'

Comentar API Google

Geolocalización
---------------

Se define como la identificación de la ubicación geográfica de cualquier tipo de objeto, por ejemplo un radar, teléfono móvil o cualquier aparato tecnológico conectado a internet. Está relacionada con los sistemas de detección de posición, pero añade datos como información de la zona, calles, locales, etc.

La geolocalización por su parte tiene una característica muy específica: nos permite localizar un dispositivo en el mapa en tiempo real. Por ejemplo, lo que hace Google Maps [#e3]_ es geolocalizar nuestro dispositivo, es decir, acceder a nuestra ubicación exacta y ofrecernos las diferentes funciones de la aplicación a partir de esto.

.. [#e3] servidor de mapas web. Ofrece mapas desplazables, además de fotografías satelitales.

.. figure:: ../figs/Cap5/google-maps.png
   :scale: 20%

   Ver ubicación actual del dispositivo en el mapa utilizando Google Maps.

GPS (Global Positioning System)
-------------------------------

Es un sistema de localización, diseñado por el Departamento de Defensa de los Estados Unidos. Se encuentra en funcionamiento desde 1995, el cual permite determinarla posición de un objeto en la Tierra (un dispositivo móvil, un vehículo) con una precisión de hasta centímetros utilizando GPS diferencial, aunque por lo general son unos pocos metros de precisión. Para poder determinar las posiciones en el globo, el sistema GPS se sirve de 24 satélites y utiliza la trilateración (Ver Trilateración Satelital).

Funcionamiento
^^^^^^^^^^^^^^

Trilateración Satelital
"""""""""""""""""""""""

Método por el cual obtener las coordenadas de un punto del que se ignora su posición a partir de mediciones de distancias a puntos de coordenadas conocidos previamente.

Se trata de un método matemático que determina las posiciones relativas de objetos utilizando geometría de triángulos de forma análoga a la triangulación. Para precisar la posición relativa de un punto mediante la trilateración se utiliza las localizaciones de tres o más puntos de referencia (a mayor puntos de referencia mayor precisión), y la distancia medida entre el sujeto y cada punto de referencia.

Teniendo en cuenta :num:`trilateracion`. Ubicándonos en el punto B, necesitamos conocer su posición relativa a los siguientes punntos de referencia *P1*, *P2* y *P3* en un plano bidimensional. Si se mide *r1* podemos reducir nuestra posición a una circunferencia. A continuación, si medimos *r2*, reducimos la posición a dos punto, *A* y *B*. Por último, si medimos, *r3*, podemos obtener nuestras coordenadas en el punto B. También, se puede realizar una cuarta medición para reducir y estimar el error.

.. _trilateracion:
.. figure:: ../figs/Cap5/trilateracion.png
   :scale: 50%

   Trilateración.

Arquitectura del sistema GPS
""""""""""""""""""""""""""""

El Sistema de Posicinamiento Global se encuentra conformada por 3 componentes básicos:

* Componente espacial formada por 24 satélites que conforman la red de GPS.
* Componente de control que cuenta con 10 estaciones de monitoreo encargadas de mantener en órbita los satélites y de la supervisión de su funcionamiento.
* Componente de usuario formado por aquellas antenas receptoras situadas en la Tierra.

Ubicación a través de GPS

Explicar cómo se calculan las coordenadas de un objeto utilizando el GPS.

.. http://www.mailxmail.com/curso-introduccion-gps/como-funciona-gps-trilateracion
Para determinar la ubicación de un receptor GPS se utiliza la trilateración satelital que tiene su base en el método matemático trilateración comentado previamente. Se denomina trilateración satelital ya que en este caso los puntos de referencia son satélites en el espacio. Para llevar a cabo este proceso, 

La base para determinar la posición de un receptor GPS es la trilateración a partir de la referencia proporcionada por los satélites en el espacio. Para llevar a cabo el proceso de trilateración, el receptor GPS calcula la distancia hasta el satélite midiendo el tiempo que tarda la señal en llegar hasta él. Para ello, el GPS necesita un sistema muy preciso para medir el tiempo. Además, es preciso conocer la posición exacta del satélite. Finalmente, la señal recibida debe corregirse para eliminar los retardos ocasionados.

Una vez que el receptor GPS recibe la posición de al menos cuatro satélites y conoce su distancia hasta cada uno de ellos, puede determinar su posición superponiendo las esferas imaginarias que generan.
Podemos comprender mejor esta explicación con un ejemplo. Imaginemos que nos encontramos a 21.000 km de un primer satélite. Esta distancia nos indica que podemos encontrarnos en cualquier punto de la superficie de una esfera imaginaria de 21.000 km de radio. Ahora, imaginemos que nos encontramos a 24.000 km de un segundo satélite. De este modo, también nos encontramos en cualquier punto de la superficie de esta segunda esfera imaginaria de 24.000 km de radio. La intersección de estas dos esferas generará un círculo que disminuirá las posibilidades de situar nuestra posición. Por otro lado, imaginemos que un tercer satélite se encuentra a 26.000 km. Ahora nuestras posibilidades de posición se reducen a dos puntos, aquellos donde se unen la tercera esfera y el círculo generado por las otras dos. Aunque uno de estos dos puntos seguramente dará un valor absurdo (lejos de la Tierra, por ejemplo) y puede ser rechazado sin más, necesitamos un cuarto satélite que determine cuál de ellos es el correcto, si bien no es necesario por la razón anteriormente mencionada. A pesar de su aparente falta de utilidad, este cuarto satélite tendrá una función crucial en la medición de nuestra posición, como se verá más adelante. 

Fuentes de error


Presentar las dificultades que atraviesan las señales entre el aparato emisor y el receptor.

Para el cálculo de su posición, se debe tener en cuenta las siguientes fuentes de error que pueden llegar a afectar a la señal en su recorrido desde el emisor al receptor.

Errores debido a la atmósfera.

Errores en el reloj del GPS.

Interferencias por la reflexión de las señales (multipath effect).

Errores de orbitales

Geometría de los satélites visibles

Uso del receptor GPS


Explicar acerca de la información obtenida desde el GPS y su clasificación.

Waypoint

Track

Ruta

Herramientas
^^^^^^^^^^^^

A continuación, se mencionará aquellas herramientas software utlizadas en el marco del presente trabajo.

A continuación, se presenta a ShareGPS, aplicación utilizada en el marco de esta tesina como soporte de captura de datos de localización a través de un dispositvo móvil que cuente con un GPS integrado.

ShareGPS
""""""""

.. figure:: ../figs/Cap5/share-gps.png
   :scale: 40%

   ShareGPS.

Aplicación para el sistema operativo Android que permite compartir datos de localización en tiempo real desde un dispositivo móvil vía Bluetooth, 3G/4G, USB y TCP/IP.

Para utilización de operaciones básicas de la aplicación ver :cite:`ShareGPS`.

Tipos de datos
""""""""""""""

Formato mediante el cual se comparte los datos de localización son compartidos desde el aplicativo. Los tipos de datos son los siguientes:

* NMEA 0183

Formato estándar para los datos GPS.

* KML PlaceMark (Keyhole Markup Language)

.. KML refrence: https://developers.google.com/kml/documentation/kmlreference?hl=es-419
.. A track describes how an object moves through the world over a given time period. This feature allows you to create one visible object in Google Earth (either a Point icon or a Model) that encodes multiple positions for the same object for multiple times. In Google Earth, the time slider allows the user to move the view through time, which animates the position of the object.

Conexión vía USB
################

Connecting NMEA data to a Linux PC via USB

En este apartado se explicará cómo establecer una conexión entre un computador bajo un sistema operativo Linux y un dispositivo móvil a través de cableado USB, para compartidor datos de localización utilizando NMEA como formato de datos.

Como primer paso, es necesario instalar el software ShareGPS en el dispositvo móvil a utilizar a través de alguna plataforma de distribución digital de aplicaciones como por ejemplo, Google Play Store, Uptodown, Aptoide.

Segundo paso, es necesario los siguientes paquetes de software en el dispositivo receptor (Linux PC en este caso):

GPS daemon
   Arch Linux:
      $ sudo pacman -S gpsd

Android Tools
   Arch Linux:
      $ sudo pacman -S android-tools
      $ sudo pacman -S android-udev

Opcional, para el caso del presente trabajo, se utilizó el siguiente módulo de Python [#e5]_ para capturar los datos obtenidos desde el GPS del dispositivo móvil.

.. [#e5] lenguaje de progamación interpretado.

Tercer paso, una vez instalado el software necesario, asegurarse que el dispositivo móvil al cual se conectará tenga habilitado la opción de depuración de USB. Luego, proceder a la conexiones a través del cable USB.
 
Cuarto paso, abrir la aplicación ShareGPS en el dispositivo móvil y crear una conexión NMEA USB.

$ adb devices

$ adb forward tcp:20175 tcp:50000

Utilizando netcat para verificar si se están compartiendo datos entre Linux PC y el dispositivo móvil.
$ nc localhost 20175

$ gpsd -D5 -N -n -b tcp://localhost:20175

$ gpsd -b tcp://localhost:20175

Por último, el consumo de los datos se utilizó...

.. http://www.jillybunch.com/sharegps/nmea-usb-linux.html


Conexión vía BlueTooth
######################

Connecting NMEA data to a PC via Bluetooth

En este apartado se explicará cómo establecer una conexión entre un computador bajo un sistema operativo Linux y un dispositivo móvil a través de Bluetooth, para compartidor datos de localización utilizando NMEA como formato de datos.

.. http://www.jillybunch.com/sharegps/nmea-bluetooth.html

Otros tipos de conexiones
#########################

La aplicación ShareGPS también permite otros tipos de conexiones para compartir los datos de localización diferentes a las mencionadas anteriormente. Estos tipos se van a nombrar a continuación, para más detalle visitar el siguiente enlace `ShareGPS <http://www.jillybunch.com/sharegps/index.html>`_.

* TCP/IP

Este tipo de conexión permite el envío de datos NMEA entre un computador y otro dispositivo que soporte este tipo de conexión. ShareGPS puede utilizarse tanto como servidor de datos así como cliente.

Para más detalles ver `TCP/IP RFC <https://www.rfc-es.org/rfc/rfc1180-es.txt>`_.


* SCP

Permite el envío de datos KMZ desde un computador y otro dispositivo que ejecute un servidor SSH.

Para más detalles ver `SSH RFC <https://www.ietf.org/rfc/rfc4251.txt>`_.

* GoogleDrive, Dropbox, LocalFile

Las plataformas Drive y Dropbox online que permite compartir y actualizar en tiempo real los archivos KMZ capturados.

A través de LocalFile, ShareGPS permite guardar los datos KMZ a la tarjeta de memoria (SD Card) del dispositivo móvil.

* SendTo

Esta opción se puede utilizar para compartir datos entre aplicaciones del dispositivo móvil. Por ejemplo, si se elige Gmail [#e6]_, los datos KMZ se enviarán como un mail.

.. [#e6] servicio de correo electrónico gratuito proporcionado por Google.

.. Sistemas de Información Geográfica - Un libro de Víctor Olaya - http://volaya.github.io/libro-sig/