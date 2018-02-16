Capítulo 5. Herramientas GPS y Geocoding
===============================================================

El objetivo principal del siguiente capítulo será la determinación de posiciones sobre la superficie terrestre. Para poder alcanzar este objetivo, se describirá el contexto matemático básico para expresar un punto sobre la Tierra, además, de los sistemas de coordenadas y las proyecciones cartográficas.

Sistemas de Información Geográfica
----------------------------------

/*/*/*/*/*/
Un SIG es un caso particular de SI en el que la información aparece georreferenciada, es decir, incluye su posición en el espacio utilizando un sistema de coordenadas estandarizado resultado de una proyección cartográfica. Se lo puede definir como un conjunto de herramientas diseñadas para la obtención, almacenamiento, recuperación y despliegue de datos espaciales.
Básicamente, un SIG ha de permitir la realización las siguientes operaciones:
Lectura, edición, almacenamiento y, en términos generales, gestión de datos espaciales.
Análisis de dichos datos. Esto puede incluir desde consultas sencillas a la elaboración de complejos modelos, y puede llevarse a cabo tanto sobre la componente espacial de los datos (la localización de cada valor o elemento) como sobre la componente temática (el valor o el elemento en sí).
Generación de resultados tales como mapas, informes, gráficos, etc.

En función de cual de estos aspectos se valore como más importante, encontramos distintas definiciones formales del concepto de un SIG. Una definición clásica es la de [Tomlin1990Prentice], para quien un SIG es un elemento que permite «analizar, presentar e interpretar hechos relativos a la superficie terrestre». El mismo autor argumenta, no obstante, que «esta es una definición muy amplia, y habitualmente se emplea otra más concreta. En palabras habituales, un SIG es un conjunto de software y hardware diseñado específicamente para la adquisición, mantenimiento y uso de datos cartográficos».
/*/*/*/**/**/*/

Un sistema de información geográfica (SIG) es un sistema empleado para describir y categorizar la Tierra y otras geografías con el objetivo de mostrar y analizar la información a la que se hace referencia espacialmente. Este trabajo se realiza fundamentalmente con los mapas.

El objetivo de SIG consiste en crear, compartir y aplicar útiles productos de información basada en mapas que respaldan el trabajo de las organizaciones, así como crear y administrar la información geográfica pertinente.

Los mapas representan colecciones lógicas de información geográfica como capas de mapa. Constituyen una metáfora eficaz para modelar y organizar la información geográfica en forma de capas temáticas. Asimismo, los mapas SIG interactivos ofrecen la interfaz de usuario principal con la que se utiliza la información geográfica.
/*/*/*/*/*/
Se entiende por "Sistema de Información" la conjunción de información con herramientas informáticas, es decir, con programas informáticos o software. Si el objeto concreto de un sistema de información (información+software) es la obtención de datos relacionados con el espacio físico, entonces estaremos hablando de un Sistema de Información Geográfica o SIG (GIS en su acrónimo inglés, Geographic Information Systems).

Así pues, un SIG es un software específico que permite a los usuarios crear consultas interactivas, integrar, analizar y representar de una forma eficiente cualquier tipo de información geográfica referenciada asociada a un territorio, conectando mapas con bases de datos.

El uso de este tipo de sistemas facilita la visualización de los datos obtenidos en un mapa con el fin de reflejar y relacionar fenómenos geográficos de cualquier tipo, desde mapas de carreteras hasta sistemas de identificación de parcelas agrícolas o de densidad de población. Además, permiten realizar las consultas y representar los resultados en entornos web y dispositivos móviles de un modo ágil e intuitivo, con el fin de resolver problemas complejos de planificación y gestión, conformándose como un valioso apoyo en la toma de decisiones.
/*/**/**/*/*//*/*/*/

Componentes de un SIG
Datos
Métodos
Software
Hardware
Personas

Forma y representación de la Tierra
-----------------------------------

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
* Constituida por métodos astronómicos, los cuales permiten la determinación de coordenadas geográficas sobre la superficie terrestre a partir de mediciones de los astros (se tiene en cuenta una serie de puntos fundamentales a partir de los cuales se arman redes geodésicas, se mencionarán más adelante).

* Geodesia Espacial
Determina de coordenadas geográficas mediante mediciones tomadas a través de satélites artificiales, objetos naturales o artificiales exteriores a la Tierra.

Las superficies de referencia de la Tierra utilizadas por la geodesia clásica son la elipsoide y geoide.

Geoide
^^^^^^
Es el objeto geométrico irregular utilizado para hacer referencia a la Tierra. Se define como una superficie en la que todos los puntos experimentan la misma atracción gravitatoria siendo esta equivalente a la experimentada al nivel del mar.

En la actualidad se dice que el Geoide es una superficie equipotencial [#e1]_ del campo de gravedad terrestre ajustado a determinaciones del nivel medio del mar corregidas por los mejores modelos de circulación oceánica, de las perturbaciones atmosféricas y toda influencia no periódica que afecte el nivel del agua.

Se trata de una superficie que no es totalmente estable debido a los ajustes incorporados determinados, por lo cual ciertas descargas fluviales o desprendimientos de barreras de hielo pueden influir en el cálculo de la superficie del mismo Geoide. Aunque esta concepción es muy reciente (1980), se encuentra apoyada por detalladas investigaciones que surgen de sensores montados en satélites artificiales.

.. figure:: ../figs/Cap5/geoide_elipsoide.png
   :scale: 50%

   Elipsoide y geoide.

.. rubric:: Footnotes

.. [#e1] Una superficie equipotencial es el lugar geométrico de los puntos de un campo escalar en los cuales el "potencial de campo" o valor numérico de la función que representa el campo, es constante.

Elipsoide
^^^^^^^^^
Es el objeto regular utilizado para hacer referencia a la Tierra. Se encuentra definido por dos parámetros: el semieje mayor y el semieje menor.

En el caso de la Tierra estos ejes se corresponden con el readio ecuatorial y el radio polar. La relación existente entre estas dos medidas define el grado de achatamiento del elipsoide, dado por:

.. math:: f = \frac {r_{1} - r_{2}} {r_{1}}

.. figure:: ../figs/Cap5/elipsoide.png
   :scale: 50%

   Elipsoide. http://volaya.github.io/libro-sig/chapters/Fundamentos_cartograficos.html


Datum
^^^^^
Conjunto formado por los parámetros *a* y *b* del *elipsoide*
Es el conjunto formado por una superficie de referencia (el elipsoide) y un punto en el que «enlazar» este al geoide. Este punto se denomina punto astronómico fundamental (para su cálculo se emplean métodos astronómicos), o simplemente punto fundamental, y en él el elipsoide es tangente al geoide. La altura geoidal en este punto es, como cabe esperar, igual a cero. La vertical al geoide y al elipsoide son idénticas en el punto fundamental.
Para un mismo elipsoide pueden utilizarse distintos puntos fundamentales, que darán lugar a distintos datum y a distintas coordenadas para un mismo punto.

.. Asigna a cada punto sobre el geoide un par de coordenadas angulares único.
.. Conjunto formado por los parámetros *a* y *b* del *elipsoide*, las coordenadas geográficas, latitud y longitud, del punto fundamental y la dirección que define el Norte.
Todos sabemos que la tierra no es esférica. Pero, no solo eso, ni siquiera es un cuerpo regular achatado por los polos. Esta irregularidad hace que cada pais, o incluso cada región, escoja el modelo de cuerpo (definible matemáticamente) que mas se ajuste a la forma de la tierra en su territorio. 
Cada Datum esta compuesto por:

a) un elipsoide,
b) por un punto llamado "Fundamental" en el que el elipsoide y la tierra son tangentes. De este punto se han de especificar longitud, latitud y el acimut de una dirección desde él establecida.

En el punto Fundamental, las verticales de elipsoide y tierra coinciden. También coinciden las coordenadas astronómicas (las del elipsoide) y las geodésicas (las de la tierra).

Definido el Datum, ya se puede elaborar la cartografía de cada lugar, pues se tienen unos parámetros de referencia.

Coordenadas geográficas
-----------------------

El sistema de coordenadas natural de un esferoide o elipsoide es el de coordenadas angulares (latitud y longitud) que suele denominarse coordenadas geográficas.
Para poder definir latitud y longitud, es necesario identificar el eje de rotación terrestre.

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

Azimuth
"""""""
Es el ángulo formado por la línea une el punto de partida y el Norte y la línea que une el punto de partida con el de llegada.

Rumbo
"""""
Es el ángulo agudo que forma las direcciones Norte o Sur desde el punto de partida y la línea que une ambos puntos.

.. figure:: ../figs/Cap5/rumbo-y-azimut.png
   :scale: 50%

   Rumbo y Azimut.

Sistemas de Proyección cartográfica
-----------------------------------

Una proyección cartográfica es la correspondencia matemática biunívoca entre los puntos de una esfera o elipsoide y sus transformados en un plano.
Una proyección cartográfica es el proceso de transformar las coordenadas geográficas del elipsoide en coordenas planas para representar una parte de la superficie del mismo en dos dimensiones.

Otras superficies pueden emplearse también para definir una proyección, de la misma forma que se hace con un plano.
Las superficies más habituales son el cono y el cilindro (junto con, por supuesto, el plano), las cuales, situadas en una posición dada en relación con el objeto a proyectar (esto es, la Tierra), definen un tipo dado de proyección. Por lo que se puede distinguir las siguientes proyecciones: cónicas, cilíndricas y planas azimutales.

* Cónicas

La superficie desarrollable es un cono, que se sitúa generalmente tangente o secante en dos paralelos a la superficie del elipsoide. En este último caso, la distorsión se minimiza en las áreas entre dichos paralelos, haciéndola útil para representar franjas que no abarquen una gran distancia en latitud, pero poco adecuada para representación de grandes áreas. Algunas de las proyecciones más conocidas de este grupo son la proyección cónica equiárea de Albers y la proyección conforme cónica de Lambert.

.. figure:: ../figs/Cap5/conicas.png
   :scale: 40%

   Proyecciones cónicas.

.. https://www.blinklearning.com/Cursos/c536159_c24567759__Metodos_de_representacion.php

* Cilíndricas

La superficie desarrollable es un cilindro. Al proyectar, los meridianos se convierten en lineas paralelas, así como los paralelos, aunque la distancia entre estos últimos no es constante.

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

Georreferenciación
------------------

La georeferenciación es un proceso de localización geográfica, dentro de un sistema de coordenadas. En términos más sencillos es ubicar una dirección dentro de un mapa digital, asociando al punto la coordenada...
Por ejemplo, Google Earth es un sistema de georreferenciación, el cual nos permite situar en un mapa puntos concretos de la geografía.

Geolocalización
------------------

geolocalización se define como la identificación de la ubicación de un dispositivo por ejemplo un radar, teléfono móvil o cualquier aparato tecnológico conectado a internet. Está relacionada con los sistemas de detección de posición, pero añade datos como información de la zona, calles, locales, etc.

La geolocalización por su parte tiene una característica muy específica: nos permite localizar un dispositivo en el mapa en tiempo real. Por ejemplo, lo que hace Google Maps es geolocalizar nuestro dispositivo, es decir, acceder a nuestra ubicación exacta y ofrecernos las diferentes funciones de la aplicación a partir de esto.

GPS (Global Positioning System)
-------------------------------

Es un sistema de localización, diseñado por el Departamento de Defensa de los Estados Unidos. Se encuentra en funcionamiento desde 1995, 

Funcionamiento
^^^^^^^^^^^^^^

Arquitectura del sistema GPS

Uso
^^^

Herramientas
^^^^^^^^^^^^

A continuación, se presenta a ShareGPS, aplicación utilizada en el marco de esta tesina como soporte de captura de datos de localización a través de un dispositvo móvil que cuente con un GPS integrado.

ShareGPS
""""""""

.. figure:: ../figs/Cap5/share-gps.png
   :scale: 40%

   ShareGPS.

Aplicación para el sistema operativo Android que permite compartir datos de localización en tiempo real desde un dispositivo móvil vía Bluetooth, 3G/4G, USB y TCP/IP.

Tipos de datos

Se trata del formato mediante el cual se comparte los datos de localización desde el aplicativo. Los tipos de datos son los siguientes:

NMEA 0183
KML PlaceMark (Keyhole Markup Language)

.. KML refrence: https://developers.google.com/kml/documentation/kmlreference?hl=es-419
.. A track describes how an object moves through the world over a given time period. This feature allows you to create one visible object in Google Earth (either a Point icon or a Model) that encodes multiple positions for the same object for multiple times. In Google Earth, the time slider allows the user to move the view through time, which animates the position of the object.

Para utilización de operaciones básicas de la aplicación, visitar el siguiente enlace: http://www.jillybunch.com/sharegps/user.html

Conexión vía USB
++++++++++++++++

Connecting NMEA data to a Linux PC via USB

.. http://www.jillybunch.com/sharegps/nmea-usb-linux.html


Conexión vía BlueTooth
++++++++++++++++++++++

Connecting NMEA data to a PC via Bluetooth

.. http://www.jillybunch.com/sharegps/nmea-bluetooth.html

Otros tipos de conecciones
++++++++++++++++++++++++++

Esta aplicación también permite otros tipos de conexiones para compartir los datos de localización. Estos tipos se van a nombrar a continuación, para más detalle visitar el enlace a aplicación ShareGPS.

TCP

SCP

GoogleDrive, Dropbox, LocalFile

SendTo


.. Sistemas de Información Geográfica - Un libro de Víctor Olaya - http://volaya.github.io/libro-sig/