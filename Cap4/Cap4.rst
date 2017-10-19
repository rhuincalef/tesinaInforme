Capítulo 4.Técnicas de reconocimiento y procesamiento de fallas
===============================================================


¿Qué es Machine Learning(ML)?
-----------------------------

.. TODO: Concepto de machine learning, entrenamiento supervisado vs no supervisado
.. TODO: Etapa de preprocesamiento de datos
.. TODO: Usos y aplicaciones de ML



Mecanismos para Machine Learning(ML)
------------------------------------


Maquinas de sporte de Vectores(SVM)
+++++++++++++++++++++++++++++++++++

.. TODO: Completar!!!

Redes Neuronales(NN)
++++++++++++++++++++

.. TODO: Completar!!!

Árboles de decisión(Tree)
+++++++++++++++++++++++++

.. TODO: Completar!!!



Selección de features para ML en PCL
------------------------------------

Inicialmente se investigó si PCL ofrecía funciones para obtener features de cada punto, de manera que se conozca información respecto de la geometría alrededor de un punto a través del procesamiento de sus vecinos, y se averiguó que PCL ofrecía una variedad de algoritmos que permiten computar "descriptores" que estan pensados para ser empleados en el reconocimiento de objetos 3D dentro de una captura. PCL ofrece dos tipos de descriptores: Descriptores locales que se emplean para describir la geometría alrededor de cada punto, sin considerar la geometría total del objeto que cada punto compone, por lo que cuando se emplean estos descriptores se deben seleccionar los puntos clave del objeto o keypoints que se desean procesar. Estos descriptores se emplean para el reconocimiento de objetos y para la registración(registration), que consiste en alinear dos nubes de puntos y por medio de transformaciones lineales, detectar si existen áreas comunes en ambas nubes de puntos.
Por otro lado, PCL ofrece descriptores globales que describen la geometría de un cluster de puntos que representa un objeto, por lo que para emplear estos descriptores se requiere preprocesar una nube de puntos, con el fin de aislar el objeto. Estos descriptores se aplican para el reoconocimiento de objetos y clasificación, estimación de posición y análisis de geometría (tipo de objeto, forma, etc.). Los descriptores locales que emplean un radio de busqueda, mayormente pueden ser usados como globales, si se computa un solo punto en el cluster y se modifica el radio de busqueda de puntos vecinos, de manera que se abarquen todos los puntos que componen el objeto.

De este conjunto, se seleccionó un subconjunto acorde a las capacidades de computo disponibles y a las características de curvatura y profundidad que son propias de fallas tipo bache y grieta. Con respecto a los baches, se optó por seleccionar aquellos algoritmos que computan features llamadas normales( vectores unidad que son tangentes a un punto en una superficie y perpendiculares al plano en que se encuentra dicho punto).

Debido a que las grietas recolectadas poseen una diversidad de profundidades y algunas de estas no pueden ser detectadas por el sensor, se decidió realizar una 
subdivisión en dos grupos: Aquellas que poseen profunidad y, por lo tanto pueden procesarse con las normales, y aquellas que no poseen una profundidad suficiente como para ser detectadas a traves de normales y, deben ser detectadas empleando algún mecanismo que utilice la diferencia de color entre la región interior y el resto del pavimento. Teniendo ésto en cuenta, se filtraron los siguientes algoritmos:

* Algoritmos que hacen uso de las normales de los puntos de la captura:

    - Fast Point Feature Histogram(FPFH)(Local)
    - ViewPoint Feature Histogram(VFH)(Local)
    - Global Radious-based Surface Descriptor(GRSD)(Global)

* Algoritmos que emplean el color RGB en los puntos de la captura:

    - Rotation Invariant Feature Transform(RIFT)(Local)
      

FPFH
++++
.. TODO: PONER EXPLIACIÓN DE ALGORITMO ACÁ!


VFH
+++
.. TODO: PONER EXPLIACIÓN DE ALGORITMO ACÁ!


GRSD
++++

.. TODO: PONER EXPLIACIÓN DE ALGORITMO ACÁ!


RIFT
++++

.. TODO: PONER EXPLIACIÓN DE ALGORITMO ACÁ!




Metodología de preprocesado de muestras (Pipeline de Cropeado)
--------------------------------------------------------------

Debido a la cantidad numerosa de puntos que se encuentran en una captura realizada por el sensor (aproximadamente 300.000 puntos) y, a que se deseaba abstraer solo aquellas caracaterísticas propias de cada tipo de falla, se procedió a aplicar una serie de algoritmos como parte del preprocesado de datos en machine learning o "Pipeline de Cropeado", con el fin de reducir la cantidad de puntos de cada muestra y de solo calcular el descriptor con los puntos principales de un bache.Este Pipleline de cropeado, se compone de los siguientes pasos:

1 - Eliminación de ruido con Statistical Removal: Debido a que la densidad de puntos de una captura puede variar, bajo diversas condiciones tales como: La cantidad de luz solar presente o la posición del sensor con respecto al pavimento, es necesario eliminar para cada captura aquellos valores extremos o outliers, que pueden interferir con la computación features de la muestra. Para ello, PCL ofrece un algoritmo de filtrado denominado Statistical Outlier Removal, el cual para cada punto en la nube de entrada computa la distancia media de éste hacia todos sus vecinos, y asumiendo que las distancias siguen una distribución estadística Gaussiana con una media y desvío estándar, elimina de la nube aquellos puntos cuyas distancias esten fuera del intervalo definido por la media y el desvío estándar de la distribución.
|


.. figure:: statistical_removal_ejemplo.png
   :scale:	70 %

	Izquieda: Ejemplo de nube de puntos sin el filtro Statistical Outlier Removal. Derecha: Ejemplo de nube de puntos con el filtro de Statistical Outlier Removal.
|

2 - Downsampling con Voxel Grid: Se conoce con el nombre de vóxel a un conjunto de puntos que forman una mínima unidad cubica (grilla en 3D) de un objeto tridimensional, de la misma forma que un pixel es la minima unidad en una imagen en 2D. El algoritmo de Voxel Grid en PCL, permite reducir la cantidad de elementos de una nube, realizando una división de una nube de puntos en voxels, y computando en base a éstos el centroide (centro del voxel grid), que representa al resto de los puntos en el voxel grid.


.. figure:: voxel_grid_estructura.png
   :scale:	60 %

	Estructura de un voxel y voxel grid en 3D


|
3 - Segmentación con algoritmo de Planar Segmentation: La segmentación en PCL consiste en dividir una nube de puntos de entrada en varios clusters, donde cada cluster representa un objeto de la captura, que puede ser procesado independientemente. El algoritmo empleado  para la segmentación en PCL fue RANSAC (Random Sample Consensus), este algoritmo considera que en la nube de puntos de entrada existen puntos que pueden ser ajustados al modelo,con un margen de error especificado (inliers), y puntos que no se ajustan al modelo de RANSAC(outliers). Este algoritmo es una algortimo no determinístico, y consiste en realizar N iteraciones, donde en cada una:  
	
		1. Se toma un subconjunto de puntos aleatorios de la nube de entrada y partiendo de un modelo establecido y, utilizando los puntos empleados como muestra, se realiza la computación de parámetros del modelo.
		
		2. A continuación, el algoritmo verifica cuales puntos del la nube de entrada completa son consistentes con el modelo generado, con los parametros tomados como muestra en el paso anterior, empleando una función de costo o función de pérdida(loss function). Los puntos que no se ajusten al modelo instanciado con un margen de error se consideran outliers, mientras que el resto de puntos que se ajustan al modelo se consideran inliers, y forman parte del conjunto de consenso(consensus set).

De esta forma, el algoritmo RANSAC se repite una serie de veces hasta que se tengan suficientes inliners como para ser considerada confiable la estimación. PCL ofrece varios modelos geométricos predefinidos para emplear con RANSAC, entre los que se encuentran: Circulo 2D, Circulo 3D, Cono, Cilindro, Linea, Esfera, Vara(Stick) y Plano. Debido a la características geormétrica de los senderos viales, se empleó para este paso RANSAC en combinación con el modelo de plano.  

|
4 - Filtrado de puntos con Statistical Removal luego de segmentación: Debido a que la segmentación puede producir en la práctica valores espurios, se aplica nuevamente Statistical Outliers Removal con el fin de eliminar valores extremos que puedan haber permanecido en la muestra. 


Metodología para clasificación de muestras con ML
-------------------------------------------------

Dado que PCL ofrece facilidades para emplear el mecanismo de SVM a través de la librería libsvm (implementada en C y con bindings a python y compatibilidad con Scikit Learn), se optó por seleccionar ésta técnica, en combinación con los descriptores producidos por los algoritmos de ML seleccionados, para las pruebas de clasificación de fallas detalladas en la sección vitácora de pruebas. La metodología de trabajo inicial para el procesamiento de muestras para la etapa de training consistió en: 


1. Aplicar "pipeline de cropeado" para cada muestra
2. Extracción de keypoints
3. Computación de descriptor (FPFH | VFH | GRSD | RIFT)
4. Extracción de features (valores del histograma) del descriptor seleccionado 
5. Almacenamiento de las feautes en formato svmlight en archivo de training
6. Entrenamiento y almacenamiento del modelo entrenado con archivo de training
   


Una vez aplicado del pipleline de cropeado para todas las muestras, se realizó la extracción de keypoints...

.. TODO: AGREGAR SAMPLING y KEYPOINTS!




Luego de computarse los descriptores de las muestras, se procede a realizar la conversión de las muestras a formato svmlight. Para la clasificación de muestras con svmlight, el formato consiste en especificar cada muestra como una combinación de un numero que especifica la clase a la que petenece la misma separado por un espacio en blanco <SPACE> de sus features <FEATURE_N> con sus respectivos valores <VALOR> y, separada de otras muestras por caracteres de nueva linea <NEW_LINE>:

<LABEL> <FEATURE_1>:<VALOR> <FEATURE_2>:<VALOR> ... <FEATURE_N>:<VALOR><NEW_LINE>
<LABEL> <FEATURE_1>:<VALOR> <FEATURE_2>:<VALOR> ... <FEATURE_N>:<VALOR><NEW_LINE>
"..."

Para el modo de clasificación, la clase a la que la muestra petenece se especifica como un valor positivo (1) si la muestra pertenece a la clase del tipo de elementos que se busca clasificar o, negativo (-1) si ésta no petenece a la clase del tipo de elementos que se desean clasificar. Los features se especifican como una sucesión de valores numéricos que representan las características propias de cada muestra, y que varía según el tamaño del histograma del descriptor que se emplee. Con el fin de realizar la conversión se eempleo un script de generacion de muestras que por medio de un archivo de configuración (.cfg), genera los descriptores para cada muestra y lo almacena en un archivo de testing o training según se haya especificado.


.. TODO: AGREGAR LA ETAPA DE TRAINING DEL MODELO!



Con respecto a la etapa de testing, los pasos inicialmente fueron los siguientes:

1. Downsampling de la muestra
2. Conversión de capturas a formato svmlight para archivo de testing
3. Prueba del clasificador con archivo de testing y obtención de métricas


Luego de realizar el downsampling con Voxel Grid y la conversión de capturas de testing a formato svmlight, se procede a probar el clasificador...

.. TODO: CONTINUAR CON LA CLASIFICACIÓN.



Vitácora de pruebas para clasificación
--------------------------------------

Como primera medida, se  procedió a realizar el calculo de la cantidad de muestras que se dedicarán para traning y para testing del total de las muestras que se capturaron, siendo éste de 1002 muestras entre baches y grietas. Se decidió que se seleccionarían un 76,75% de las muestras para training(766) y el 33% para testing(236). Una vez hecha esta división, se procedió a  aplicar la metodología de cropeado(Pipeline de Cropeado), de las muestras de training con el fin de disgregar el tipo de falla del plano en el que ésta se encuentra y obtener solo features inherentes a la falla.

Una vez cropeadas todas las muestras de training, se comenzaron con las pruebas de clasificación, comenzando por generar los descriptores FPFH del archivo de training que emplea la SVM, tomando para este archivo como muestras positivas los baches y como muestras negativas las grietas, con el fin de intentar clasificar solo entre baches y grietas. Una vez entrenada, la SVM se probó con diversos archivos de entrenamiento que incluían:  Un conejo, un bache, una grieta y un archivo de training mixto (7 baches y 28 elementos que no son baches). El resultado de esta prueba fue negativo, debido a que la muestra de bache dio negativa, la del conejo dio positiva y la del archivo de training mixto dió positiva para muestras que no eran baches.

Posteriormente, se aplico la misma prueba para el descriptor VFH y GRSD, obteniéndose resultados positivos para muestras que no eran baches y negativos para baches, logrando un accuracy considerablemente inferior al esperado.

LUEGO SE ESCALARON LOS VALORES DE LAS FEATURES, Y NO SE LOGRÓ NADA PARA LOS 3 METODOS DE ML.


SE COMPARARON LOS HISTOGRAMAS DE LOS BACHES DE TRAINING PARA FPFH, VFH Y GRSD, SIENDO EL DE GRSD EL MÁS SIMILAR DENTRO DEL MISMO TIPO DE MUESTRAS, Y DESCARTANDO LOS OTROS DOS MÉTODOS.


SE PROCEDIÓ A CAMBIAR EL ENFOQUE Y EN VEZ DE CLASIFIACAR CON BACHES Y GRIETAS AL MISMO TIEMPO, SE PROCEDIO A CLASIFICAR SOLO BACHES CON GRSD, COLOCANDO COMO NO BACHES GRSD CAPTURAS DE PLANOS. SE APLICA EL PIPELINE DE CROPEADO A CADA MUESTRA DE TRAINING .PCD, CONSERVANDO BACHES Y PLANOS PARA LA SVM. EN ESTE CASO, AL EJECUTAR LA SVM ENTRENADA CON UN ARCHIVO DE TRAINIGN CON ESTOS DATOS, LA PRECISIÓN MEJORA LOGRANDO UNA CLARA DISTINCIÓN ENTRE BACHES Y PLANOS.








































