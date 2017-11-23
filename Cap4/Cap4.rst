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
    - Ensamble Shape of Functions(ESF)(Global)

* Algoritmos que emplean el color RGB en los puntos de la captura:

    - Rotation Invariant Feature Transform(RIFT)(Local)
      

FPFH
++++
.. TODO: PONER EXPLIACIÓN DE ALGORITMO ACÁ!


VFH
+++
.. TODO: PONER EXPLIACIÓN DE ALGORITMO ACÁ!




ESF
+++
.. TODO: PONER EXPLIACIÓN DE ALGORITMO ACÁ!


GRSD
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
   


Una vez aplicado del pipeline de cropeado para todas las muestras, se debe realizar la extracción de keypoints. Los keypoints o puntos de interés, son los puntos en una nube de puntos que se destacan por ser:

* Estables con respecto a interferencias locales y globales en el dominio de la imagen, como variaciones de iluminación y brillo.
* Distintivos para la caracterización efectiva de una superficie, y ricos en contenido en terminos de color y textura.
* Tienen una posición claramente definida y se pueden obtener repetidamente con respecto a ruido y variaciones en el punto de visión.
* No es afectado por variaciones de escala, por lo que son ideales para procesamiento en tiempo real como también, procesamiento en distintas escalas. 


Así para comenzar con el procesamiento de cada muestra, como primer paso se aplica el algortimo de Uniform Sampling, que es una variación del downsampling de Voxel Grid, donde se retornan los índices de los puntos. Esto reducirá la cantidad de puntos de la nube de entrada y estos puntos serán los keypoints principales, que aporten mayor información para la SVM. Esta nube se utilizará para generar el descriptor seleccionado.


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

Como primera medida, se  procedió a realizar el cálculo de la cantidad de muestras que se dedicarán para traning y testing del total de las muestras que se capturaron, siendo éste de 1002 muestras entre baches y grietas. Se decidió que se decidió seleccionar un 76,75% de las muestras para training (766) y el 33% para testing (236). Una vez hecha la división, se decidió que se aplicaría un Pipeline de Cropeado que consistirá de varios pasos que abarcan desde la limpieza y asilamiento de la muestra hasta la clasificación, con el fin de disgregar el tipo de falla del plano en el que ésta se encuentra y obtener sólo features inherentes a la falla.

Con respecto a la computación de features de baches y grietas, se optó por investigar cuales de los features de PCL se enfocaban en capturar las diferencias entre distintos tipos formas en superficies semejantes a planos, y debido al tamaño promedio de las nubes de puntos capturadas por el sensor, se seleccionaron aquellos cuyas dimensiones del histograma no sean de una magnitud que prolongue el tiempo de procesamiento de manera excesivo.    


Una vez cropeadas todas las muestras de training, se comenzó con las pruebas de clasificación que consisten generar los descriptores FPFH del archivo de training que emplea la SVM, tomando para este archivo, como muestras positivas los baches y como muestras negativas las grietas, con el fin de intentar clasificar solo entre baches y grietas. Una vez entrenada, la SVM se probó con diversos archivos de entrenamiento: Un conejo, un bache, una grieta y un archivo de training mixto (que consistía de 7 baches y 28 elementos que no son baches). El resultado de esta prueba fue negativo, debido a que la muestra de bache no fue reconocida como tal, la del conejo resulto positiva y la del archivo de training mixto proporcionó resultos positivos para muestras que no eran baches. Posteriormente, se aplicó la misma prueba para el descriptor VFH y GRSD, obteniéndose resultados positivos para muestras que no eran baches y negativos para baches, logrando un accuracy considerablemente inferior al esperado.Luego, se testeó escalando los valores de las features con el mismo dataset, y la misma SVM y no se consiguió un aumento de precisión, para los 3 descritpores que emplean normales (FPFH,GRSD,VFH).

Dado que las diferencias entre los descriptores de los distintos tipos de muestra no eran significativas, se realizó una comparación gráfica de los descriptores pertenecientes al mismo conjunto de muestras, observando que el descriptor GRSD contenia mayor diferencia entre distintos tipos de muestra, por lo que se continuo experimentando sólamente con este descriptor y se procedió a cambiar el enfoque, distinguiendo baches de planos y por otro lado, grietas y planos, necesitando clasificadores independientes. Con esta aproximación, la precisión aumentó considerablemente. 

Debido a la necesidad de utilizar dos clasificadores diferentes por cada clase de muestra, se hizo un análisis de las curvaturas (Principal Curvatures Estimation) de las muestras con objetivo de encontrar un parámetro que, sumado al descriptor GRSD, permitiera la diferenciación entre ambos tipos de muestra empleando un único clasificador.




LUEGO SE AÑADIÓ LA ESTIMACIÓN DE CURVATURAS DE LA SUPERFICIE EN PCL A TRAVÉS DEL ALGORTIMO DE "PrincipalCurvatureEstimation", para las carpetas de grietas y baches de TRAINING que mas capturas contenian, empleando los valores de curvatura maximo(pc1) y minimo(pc2) promedio de cada nube.Luego se comparó este valor,por medio de un diagrama de dispersión y uno de densidad, observandose que el rango de curvatura promedio de las grietas estaba contenida dentro del rango de los baches, por lo que los baches contenian valores de curvatura mayores en general. 


PROBAMOS EL PIPELINE HASTA LA PARTE DE SEGMENTACION QUE INCLUYE FILTRADO POR CANTIDAD DE PUNTOS Y POR VALORES DE CURVATURA DE MUESTRAS, con dos baches downsampleados, una muestra de bunny, una grieta downsampleada (sin curvatura apreciable, con poca profundidad respecto del plano) y se pudieron generar clusters solo para los baches, lo que significa que asila correctamente estos, y no la grieta debido a que no tiene un valor de curvatura.Adicionalmente,se probaron con muestras 7 con downsampling generandose clusters para el bache completo o para la mayor parte del mismo. 
Todas estas pruebas se hicieron con algoritmo "planar_segmentation_and_euclidean" con -threshold 0.005 y -max_it 1000.Este threshold es más bajo a los utilizados durante la etapa de cropeo de muestras (anteriormente -threshold 0.014). Con el valor de curvatura se pudo observar una considerable mejora.
Debido a que se debieron ajustar los valores de curvatura maxima y minima tanto para baches como para grietas, se aplico el algoritmo de "principal_curvatures_estimation" en modo batch (donde se lee un archivo .batch con los listados de todos los directorios de captura) y se obtuvieron datos estadísticas acerca del promedio de curvaturas maximas y minimas para baches y grietas de TRAINING por directorio y en total, y luego se ajustaron los limites considerando estos valores de los archivos de TRAINING  cropeados.


Valores finales tentativos:
	tolerance = 0.023f
	min_cluster_size=220
	distance_threshold = 0.07 

Resultados:

	testeados/Baches_2.pcd  --> OK
	testeados/bunny.pcd --> OK
	testeados/bachecitos_tw_1.pcd --> OK
	testeados/una_grieta/grietas_12.pcd --> OK
	12-04-2017/bache_1.pcd --> OK
	12-04-2017/bache_2.pcd --> OK
	12-04-2017/bache_3.pcd --> OK
	12-04-2017/bache_4.pcd --> M'OK
	12-04-2017/bache_5.pcd --> OK
	12-04-2017/baches_1.pcd --> OK
	12-04-2017/baches_2.pcd --> OK


	Las muestras cropeadas en la carpeta de 7planos_separados fueron cropeadas con un distance_threshold de 0.014, por lo que en los planos se detecta una mayor superficie
	7planos_separados/bache_1_1_planePoints.pcd --> OK      
	7planos_separados/bache_2_1_planePoints.pcd --> OK      
	7planos_separados/bache_3_1_planePoints.pcd --> OK      
	7planos_separados/bache_5_1_planePoints.pcd --> OK      
	7planos_separados/baches_1_1_planePoints.pcd --> OK      
	7planos_separados/baches_2_1_planePoints.pcd --> OK      




Se realizó una prueba con todos los baches capturados del dataset (sin downsampling ni cropeados), y se compararon los valores de curvatura maxima o minimo para los clusters y, ajustandose en base a los valores que se dejaban afuera del clusterizado, se lograron segmentar en base a curvatura y RANSAC SAC_PLANE con una precisión aproximada a 97,55%(159 /163 baches,). 
Se realizó otra prueba para grietas con los mismos parámetros, y se obtuvo una precisión del 69,4% (91/131).


Luego se agregaron las features de curvatura maxima y minima para cada muestra a las features del descriptor GRSD, y se entreno una SVM con capacidad para multiclase o multi labels, dividiendo las muestras entre 3 clases: Baches, Grietas y Planos, obteniendose una precisión de 100% contra si mismo y 89.9 % con otras grietas con planar. 


Posteriormente, se confeccionó el archivo de training final con baches con histogramas GRSD similares, grietas y planos cropeados, empleando un kernel linear con un gamma -g 0.0008 y un -c 1 y logranod una precisión del 85.5% y de 70% emplenando un cross validation de 5 iteraciones, y empleando un archivo de testing con baches y grietas sin cropear. Sin embargo, al emplearlo con las muestras de testing reales cropeadas por medio del script automatico de planar_segmentation_and_euclidean, y el mismo archivo de training, se redujo la precisión al 55% debido a que los clusters generados por éste, mayormente no tienen una curvatura adecuada al rango de baches, por lo que muchos de los baches se clasificaron como grietas, distinguiéndose así de los planos, pero no de las grietas.

Luego,como la precisión era muy baja con el descriptor global, adicionalmente se probó con el descriptor local FPFH que calcula un histograma por punto, agregando los valores de curvatura y, al probarlo con dos subconjuntos de muestras del set de testing (carpetas: testing_cropeadas_graches/ y testing_cropeadas_graches_alternativo/) se logró una precisión del 56,47%, observando que los descriptores y la curvatura de los puntos introducían ruido en el clasificador.

Debido a esto se decidió volver a emplear el descriptor global ESF en una SVM multiclase, logrando una precisión del 54.4444% (49/90) empleando uno de los set de prueba (TESTING/testing_cropeadas_graches_alternativo/), pudiendo distinguir las grietas y baches de los planos, pero sin lograr distinguir baches de grietas, clasificando el resto de las muestras(41 restantes) como grietas cuando en realidad eran baches.




Con el fin de descartar que el script automático de cropeo, estuviera produciendo clusters que no fueran parte de la falla, se probó cropeando el mismo dataset de muestras de training(testing_cropeadas_graches/) manualmente solo con descriptores globales GRSD,ESF, VFH y, empleando para training los baches similares, las grietas y los planos.Esto retorno los siguientes resultados:


Descriptores + curvaturas: 
GRSD -->
	- Con kernel RBF -->

		+ 42.10 % de accuracy para dataset de testing.

	- Con kernel Linear -->

	    + 57.9% de accuracy para dataset de testing.


ESF -->
	- Con kernel RBF -->
	
		+ 42.10 % de accuracy para dataset de testing

	- Con kernel Linear -->

	    + 42.10 % de accuracy para dataset de testing


VFH -->
	- Con kernel RBF -->

	    + 42.10 % de accuracy para dataset de testing


	- Con kernel Linear -->

	    + 57.9 % de accuracy para dataset de testing

FPFH -->
	- Con kernel RBF -->

	    + 42.10 % de accuracy para dataset de testing


	- Con kernel Linear -->

	    + 47.30 % de accuracy para dataset de testing



Descriptores + sin curvaturas: 
GRSD -->
	- Con kernel RBF -->

		+ 42.10 % de accuracy para dataset de testing.
		+ 47.5 % de accuracy con -c 10 y gamma 0.000004

	- Con kernel Linear -->

	    + 79% de accuracy para dataset de testing.
	    + 69.1% de accuracy con cross_validation de 5 iteraciones


ESF -->
	- Con kernel RBF -->
	
		+ 42.10% de accuracy para dataset de testing

	- Con kernel Linear -->

	    + 42.10% de accuracy para dataset de testing


VFH -->
	- Con kernel RBF -->

	    + 42.10% de accuracy para dataset de testing


	- Con kernel Linear -->

	    + 57.9% de accuracy para dataset de testing


FPFH -->
	- Con kernel RBF -->

	    + 42.10 % de accuracy para dataset de testing


	- Con kernel Linear -->

	    + 47.36 % de accuracy para dataset de testing




- Realizando una prueba con planar_segmentation_and_euclidean aplicado a todos el set de testing, y se realizo una comparación con los archivos de training con el descriptor GRSD, obteniendo una precisión del 40.25 % (19/47).

- Realizando una prueba agregando los valores de area + volumen con el descriptor GRSD con SVM con kernel Linear, se obtuvo una precisión 52.94% con el set de testing de baches similares y grietas, sin planos. 

Posteriormente, se incluyeros aquellos atributos que son referentes a las dimensiones de  las grietas y baches de training, obteniendo : Ancho,alto , profundidad y volumen, y con éstos se realizó una comparación con el fin de obtener valores que permitieran diferenciar entre baches y grietas. Así, se optó por emplear el descriptor GRSD con la diferencia en valor de absoluto de ancho y alto de las fallas,clasificando por este limite a los baches que tienen diferencia |alto-ancho| > 40 como grietas y, los que tienen menor diferencia como baches (Limite alternativo > 30). De esta manera se opto por reclasificar las muestras según este valor como bache o grieta y, se realizaron las siguientes pruebas obteniendo como resultado:

- Al agregar los valores de alto,profundidad y ancho, con el descriptor GRSD se obtuvo un score de 79.8 % para el set de testing.

- Al agregar al GRSD la diferencia entre ancho y alto al descriptor GRSD, se logró un accuracy de 100% con archivo de testing(8/8).
  
- Agregando volumen y profundidad al descriptor GRSD con la diferencia entre  ancho y alto, se redujo la precisión al 75%.

- Haciendo pruebas con profundidad y volumen para comprobar el accuracy: 

-->Sin volumen y con profundidad (ajustada dividiendo por 2):
    - RBF: 75% (6/8) de accuracy con grieta de dataset de testing corregido.
    - Linear: 87.5 (7/8) de accuracy con grieta de dataset de testing corregido.



- Al agregar al GRSD la diferencia entre ancho y alto al descriptor GRSD y solamente con el descritpor GRSD, se logró un accuracy de 75%(6/8) kernel Linear y 87.5(7/8) con kernel RBF (con -c 2 -g 0.00000002) con archivo de testing.



- Debido a que al analizar la diferencia entre alto-ancho entre algunos archivos de baches y grietas era similar, por lo que existian muestras (baches y grietas) que tenian una relación similar entre alto-ancho, se decidió realizar un recropeado y clasificador limpiando las muestras y reclasificandolas como baches o grietas. Y luego probar nuevamente la SVM con el archivo de training generado a partir de estas muestras, obteniendo un score de precisión del 87.5% con RBF si se reclasifican las muestras con el mismo valor que el que se reclusterizo el conjunto de datos de training(para las pruebas -lim 0.5) y un 100% para 7 planos.
  
  NOTA: - Es necesario realizar el cropeo por lotes de los sets de training y reclasificar todas las muestras de testing con el mismo parametro que empleamos para reclasificación de los elementos de training.
        - Al hacer cross_validation sobre el set de testing, se logra una precisión del 75%.

  
Log de prueba RBF----->

rodrigo@rodrigo-asus:~/TESINA-2016-KINECT/MACHINE_LEARNING/algoritmos_parametrizados/lib_svm_svm_modificado$ ./svm-train trainDescrPropio_diff_alto_ancho_v3.dat modelo.dat salida.txt
.*.*
optimization finished, #iter = 1565
nu = 0.711409
obj = -324.046284, rho = -0.447172
nSV = 745, nBSV = 265
Total nSV = 745
rodrigo@rodrigo-asus:~/TESINA-2016-KINECT/MACHINE_LEARNING/algoritmos_parametrizados/lib_svm_svm_modificado$ ./svm-predict testDescrPropio_diff_alto_ancho_v3.dat modelo.dat salida.txt
pred_result: 1.000000
predict_label: 1.000000 and real_label: 2.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 2.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 2.000000
pred_result: 2.000000
predict_label: 2.000000 and real_label: 2.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 2.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 2.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
Accuracy = 37.5% (3/8) (classification)             -------> VALOR SIN RECLASIFICAR EL TESTING SET CON -lim 0.5 de separacion

rodrigo@rodrigo-asus:~/TESINA-2016-KINECT/MACHINE_LEARNING/algoritmos_parametrizados/lib_svm_svm_modificado$ ./svm-predict testGRSD_7_baches.dat modelo.dat salida.txt
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
Accuracy = 100% (7/7) (classification)
rodrigo@rodrigo-asus:~/TESINA-2016-KINECT/MACHINE_LEARNING/algoritmos_parametrizados/lib_svm_svm_modificado$ 
rodrigo@rodrigo-asus:~/TESINA-2016-KINECT/MACHINE_LEARNING/algoritmos_parametrizados/lib_svm_svm_modificado$ ./svm-predict testGRSD_8_Reclasificadas.dat modelo.dat salida.txt
pred_result: 2.000000
predict_label: 2.000000 and real_label: 2.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 2.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
Accuracy = 87.5% (7/8) (classification)
rodrigo@rodrigo-asus:~/TESINA-2016-KINECT/MACHINE_LEARNING/algoritmos_parametrizados/lib_svm_svm_modificado$


CROSS VALIDATION RBF (10 iteraciones) --->

Cross Validation Accuracy = 64.4295%
rodrigo@rodrigo-asus:~/TESINA-2016-KINECT/MACHINE_LEARNING/algoritmos_parametrizados/lib_svm_svm_modificado$ ./svm-train  -v 10 trainDescrPropio_diff_alto_ancho_v3.dat modelo.dat salida.txt





 Log de prueba LINEAR -->


rodrigo@rodrigo-asus:~/TESINA-2016-KINECT/MACHINE_LEARNING/algoritmos_parametrizados/lib_svm_svm_modificado$ ./svm-train -t 0 trainDescrPropio_diff_alto_ancho_v3.dat modelo.dat salida.txt
..............................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................*
WARNING: reaching max number of iterations
optimization finished, #iter = 10000000
nu = 0.280052
obj = -290.578210, rho = -7.316579
nSV = 230, nBSV = 188
Total nSV = 230
rodrigo@rodrigo-asus:~/TESINA-2016-KINECT/MACHINE_LEARNING/algoritmos_parametrizados/lib_svm_svm_modificado$ ./svm-predict testGRSD_7_baches.dat modelo.dat salida.txt
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
Accuracy = 100% (7/7) (classification)
rodrigo@rodrigo-asus:~/TESINA-2016-KINECT/MACHINE_LEARNING/algoritmos_parametrizados/lib_svm_svm_modificado$ ./svm-predict testGRSD_8_Reclasificadas.dat modelo.dat salida.txt
pred_result: 1.000000
predict_label: 1.000000 and real_label: 2.000000
pred_result: 2.000000
predict_label: 2.000000 and real_label: 2.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 2.000000
predict_label: 2.000000 and real_label: 1.000000
pred_result: 2.000000
predict_label: 2.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
pred_result: 1.000000
predict_label: 1.000000 and real_label: 1.000000
Accuracy = 62.5% (5/8) (classification)


CROSS VALIDATION LINEAR (10 iteraciones) --->

Cross Validation Accuracy = 87.5168%
rodrigo@rodrigo-asus:~/TESINA-2016-KINECT/MACHINE_LEARNING/algoritmos_parametrizados/lib_svm_svm_modificado$ ./svm-train -t 0 -v 10 trainDescrPropio_diff_alto_ancho_v3.dat modelo.dat salida.txt





-       3. Crear achivo test final con training y testing (ajustados con misma diff. alto y ancho) para el cross validation.(Con kernel RBF cross_val da 62.4% de accuracy y con LINEAR se obtiene 87.46% con 10 iteraciones)

-       4.Las grietas con region_growing_rgb no se pueden aislar empleando intensidad, por lo que hay que ejecutar planar_segmentation_and_euclidean y  que éste descarte las muestras que no tengan un valor preestablecido. 
  


ULTIMO TEST -->

- Se limpiaron algunas que contenian demasiados outliers, filtrando de un total de 1000, 797 muestras (744 para training y 53 para testing) y se procedió a calcular empleando los puntos que brinda el mecanismo Oriented Bounding Box de PCL, el cual se ajusta y se orienta al tamaño de la muestra, y observando las estadisticas de dimensiones del dataset de fallas de training, se seleccionó un limite para divirlas segun el tipo (grieta o bache) de 0.49, que se calcula como una diferencia entre alto y ancho, ya que al obtener las estadisticas se observaba que las grietas contenian una longitud considerablemente mayor al grosor, situación que no ocurría en baches. Al ejecutar nuevamente las pruebas con dataset de training y testing divididos por este limite, se obtuvo  91%  de accuracy con kernel Linear y 61% con kernel RBF empleando un cross validation de 5 iteraciones. 





