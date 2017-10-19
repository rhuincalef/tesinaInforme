Pruebas con Machine Learning(ML)
================================


¿Qué es Machine Learning(ML)?
-----------------------------

.. TODO: Completar!!!



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

Inicialmente se investigó si PCL ofrecía funciones para obtener features de cada punto, de manera que se conozca información respecto de la geometría alrededor de un punto a través del procesamiento de sus vecinos, y se descubrió que PCL ofrecía una variedad de algoritmos que permiten computar "descriptores" que se emplean como features para el reconocimiento de objetos en 3D. 

De este conjunto, se seleccionó un subconjunto acorde a las capacidades de computo disponibles y a las características de curvatura y profundidad que son propias de fallas tipo bache y grieta. Con respecto a los baches, se optó por seleccionar aquellos algoritmos que computan features llamadas normales( vectores unidad que son tangentes a un punto en una superficie y perpendiculares al plano en que se encuentra dicho punto).

Debido a que las grietas recolectadas poseen una diversidad de profundidades y algunas de estas no pueden ser detectadas por el sensor, se decidió realizar una 
subdivisión en dos grupos: Aquellas que poseen profunidad y, por lo tanto pueden procesarse con las normales, y aquellas que no poseen una profundidad suficiente como para ser detectadas a traves de normales y, deben ser detectadas empleando algún mecanismo que utilice la diferencia de color entre la región interior y el resto del pavimento. Teniendo ésto en cuenta, se filtraron los siguientes algoritmos:

* Algoritmos que hacen uso de las normales de los puntos de la captura:

    - Fast Point Feature Histogram(FPFH)
    - ViewPoint Feature Histogram(VFH)
    - Global Radious-based Surface Descriptor(GRSD)

* Algoritmos que emplean el color RGB en los puntos de la captura:

    - Rotation Invariant Feature Transform(RIFT)
      


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


Selección de Mecanismo de ML
----------------------------

Dado que PCL ofrece facilidades para emplear el mecanismo de SVM a través de la librería libsvm(implementada en C y con bindings a python y compatibilidad con Scikit Learn), se optó por seleccionar ésta técnica en combinación con los descriptores producidos por los algoritmos de ML seleccionados, para las pruebas de clasificación de fallas detalladas en la sección vitácora de pruebas. La metodología de trabajo seleccionada consiste en emplear un script para la generación de muestras que, por medio de un archivo de configuración, realiza la conversión de un conjunto de muestras capturadas con Kinect, convirtiendo cada uno de los histogramas obtenidos en cada captura al formato que requiere libsvm. Este formato consiste en especificar tanto para los archivos de tranining como de testing de la SVM, el label o clase a la que pertenece la cada muestra siendo una muestra positiva (1) si pertenece a la clase que se busca clasificar, o siendo una muestra negativa(-1) si el elemento no pertenece al tipo de elementos que clasifica la actual SVM.

.. TODO: TERMINAR! A VER SI USAMOS EL SVM BINARIO o MULTICLASE. 



Metodología de cropeado de muestras (Pipeline de Cropeado)
----------------------------------------------------------

Debido a la cantidad numerosa de puntos que se encuentran en una captura realizada por el sensor (aproximadamente 300.000 puntos) y, a que se deseaba abstraer solo aquellas caracaterísticas propias de cada tipo de falla, se procedió a aplicar una serie de algoritmos como parte del preprocesado de datos en machine learning o "Pipeline de Cropeado", con el fin de reducir la cantidad de puntos de cada muestra y de solo calcular el descriptor con los puntos principales de un bache.


.. TODO: Completar la descripción del pipeline de cropeado!!!

Este Pipleline de Cropeado, se compone de los siguientes pasos:

1 - Statistical Removal:

2 - DownSampling con Voxel Grid:

3 - Statistical Removal:

4 - Segmentación:



Vitácora de pruebas
-------------------

Como primera medida, se  procedió a realizar el calculo de la cantidad de muestras que se dedicarán para traning y para testing del total de las muestras que se capturaron, siendo éste de 1000 muestras entre baches y grietas. Se decidió que se seleccionarían un 77% de las muestras para training(735) y el 33% para testing(PONER CANTIDAD). Una vez hecha esta división, se procedió a  aplicar la metodología de cropeado(Pipeline de Cropeado), de las muestras de training con el fin de disgregar el tipo de falla del plano en el que ésta se encuentra.

Una vez cropeadas todas las muestras de training, se comenzaron con las pruebas de clasificación, comenzando por generar los descriptores FPFH del archivo de training que emplea la SVM, tomando para este archivo como muestras positivas los baches y como muestras negativas las grietas, con el fin de intentar clasificar solo entre baches y grietas. Una vez entrenada, la SVM se probó con diversos archivos de entrenamiento que incluían:  Un conejo, un bache, una grieta y un archivo de training mixto (7 baches y 28 elementos que no son baches). El resultado de esta prueba fue negativo, debido a que la muestra de bache dio negativa, la del conejo dio positiva y la del archivo de training mixto dió positiva para muestras que no eran baches.

Posteriormente, se aplico la misma prueba para el descriptor VFH y GRSD, obteniéndose resultados positivos para muestras que no eran baches y negativos para baches, logrando un accuracy considerablemente inferior al esperado.

LUEGO SE ESCALARON LOS VALORES DE LAS FEATURES, Y NO SE LOGRÓ NADA PARA LOS 3 METODOS DE ML.


SE COMPARARON LOS HISTOGRAMAS DE LOS BACHES DE TRAINING PARA FPFH, VFH Y GRSD, SIENDO EL DE GRSD EL MÁS SIMILAR DENTRO DEL MISMO TIPO DE MUESTRAS, Y DESCARTANDO LOS OTROS DOS MÉTODOS.


SE PROCEDIÓ A CAMBIAR EL ENFOQUE Y EN VEZ DE CLASIFIACAR CON BACHES Y GRIETAS AL MISMO TIEMPO, SE PROCEDIO A CLASIFICAR SOLO BACHES CON GRSD, COLOCANDO COMO NO BACHES GRSD CAPTURAS DE PLANOS. SE APLICA EL PIPELINE DE CROPEADO A CADA MUESTRA DE TRAINING .PCD, CONSERVANDO BACHES Y PLANOS PARA LA SVM. EN ESTE CASO, AL EJECUTAR LA SVM ENTRENADA CON UN ARCHIVO DE TRAINIGN CON ESTOS DATOS, LA PRECISIÓN MEJORA LOGRANDO UNA CLARA DISTINCIÓN ENTRE BACHES Y PLANOS.








































