Capítulo 4.Técnicas de reconocimiento y procesamiento de fallas
===============================================================


.. Header H3 -->
¿Qué es Machine Learning(ML)?
-----------------------------

.. TODO: Concepto de machine learning, entrenamiento supervisado vs no supervisado.Clasificacion y regresion.
.. TODO: Usos y aplicaciones de ML
.. TODO: Etapa de pre-procesamiento de datos
.. TODO: Metricas empleadas en cada uno de los metodos para la clasificación


La Inteligencia Artificial(IA) es una disciplina que abarca todos aquellos mecanismos(reglas if-then, árboles de decisión, redes neuronales,etc.) que posibilitan a las computadoras imitar la inteligencia humana con el fin de realizar tareas tales como: la toma de decisiones, resolver problemas y el aprendizaje; Considerándose un comportamiento inteligente, a aquél que involucra percibir o deducir información de un contexto y almacenarla en forma de conocimiento, de manera que pueda ser aplicado en futuras situaciones o contextos. Así, Machine Learning(ML) es una rama dentro de IA y consiste en aquellos mecanismos que se basan en identificar patrones en un conjunto de datos, para generar conocimiento de estas relaciones que puede ser aplicado en futuras predicciones, mientras que Deep Learning es un subconjunto de algoritmos de ML, donde el aprendizaje se realiza por medio de sucesivas capas que representan el problema que son generadas automáticamente por medio de la exposición a datos de entrada, y permiten que una máquina aprenda conceptos complicados a través de su descomposición en conceptos más simples. Estas representaciones en Deep Learning se generan por medio de modelos denominados Redes Neuronales expuestas a enormes cantidades de datos, y cuyo funcionamiento se inspira en el funcionamiento del cerebro humano. 



.. figure:: ../figs/Cap4/Diferencia_AI_ML_DL.jpg

   Comparación de AI, ML y Deep Learning



.. TODO: PONER EL FLUJO DE TRABAJO DE ML -->
..  https://livebook.manning.com/#!/book/real-world-machine-learning/chapter-1/104

De esta forma, ML se diferencia del paradigma de programación clásico donde un equipo de desarrollo programa instrucciones que procesan datos y se generan salidas en base a estructuras predefinidas, en que para esta metodología solamente se ingresan datos (y opcionalmente sus respuestas),y se obtienen reglas de salida que pueden ser aplicadas a nuevos datos para realizar predicciones. Por lo tanto en ML, se considera que dado un programa cuyo rendimiento en la predicción sobre un conjunto de datos(o dataset) que se encuentra medido por medio de alguna métrica (que indica que tan precisas son sus predicciones sobre ese conjunto de datos), éste aprende de la experiencia si su rendimiento mejora al adquirir más experiencia.

.. figure:: ../figs/Cap4/ML_paradigma.jpg

   Paradigma de ML vs paradigma de programación tradicional.

Flujo de trabajo en ML
^^^^^^^^^^^^^^^^^^^^^^

Así, el flujo de trabajo en ML para la generación y prueba de un modelo de predicción se puede subdividir en las siguientes fases:

1. Pre-procesamiento de datos(feature extraction). 
2. Etapa de entrenamiento del modelo (training). Se genera un modelo por medio de elementos que son relevantes a una tarea, lo que permite que el modelo identifique patrones que permitan automatizar la tarea. 
3. Evaluación y optimización del modelo.
4. Etapa de validación (testing). (TODO: INCLUIR CROSS-VALIDATION)
   

.. TODO: TRADUCIR ESTA IMAGEN DE FLUJO DE TRABAJO

.. figure:: ../figs/Cap4/workflow_ML.png

   Flujo de trabajo general en ML


Debido a que los datos en el mundo real frecuentemente no son aceptables para ser procesados por un algoritmo de ML, debido a que contienen valores incorrectos, erróneos o nombres escritos de manera distinta aunque se refieren a la misma entidad, y dado los algoritmos de ML tienen como finalidad descubrir asociaciones y relaciones en un conjunto de datos de entrenamiento históricos (training dataset) para generar un modelo de predicción,  el primer paso para lograr ésto, consiste en realizar el pre-procesado de los datos de manera que se puedan producir datos de alta calidad, ruido leve y correlaciones fácilmente deducibles que permitan generar un modelo predictivo de alta fidelidad. De esta manera, el pre-procesamiento involucra aplicar técnicas y algoritmos para el saneamiento, visualización y transformación de datos a otro rango de valores, de forma que se reduzca la redundancia de features, la variabilidad de valores y el tiempo de procesamiento, conservando únicamente aquellas features con información relevante para el modelo. Durante esta fase se descarta información, por lo que se debe realizar con cautela ya que si atributos relevantes al modelo se descartan, puede verse afectada la capacidad de predicción de éste. En general, el pre-procesamiento de datos basa en considerar la presencia de las siguientes características en el dataset y aplicar los pasos mencionados:

* Features categóricas: Las features categóricas son aquellos valores no numéricos a los que se les puede asignar un valor numérico, con el fin de que sean de utilidad para los algoritmos, tales como los días de la semana o el género. En general, los algoritmos de machine learning necesitan datos numéricos (salvo algunos casos concretos derivados de los árboles de decisión), por lo que es necesario codificar las features categóricas a través de la creación de clases con valores binarios que representan cada categoría, y luego asignar a cada muestra del dataset un valor (0 o 1) indicando si ésta pertenece o no a una determinada categoría. A continuación, se muestra un ejemplo donde para las categorías de hombre o mujer, se crea una clase binaria y se un valor 1 a la categoría donde se ubica la muestra:
  

.. figure:: ../figs/Cap4/ejemploFeatureCategorica.png

   Ejemplo de conversión de feature categórica

* Datos faltantes: En general la información faltante en datasets, debido ya sea porque no pudo ser recolectada o porque no pudo ser medida, puede suceder que estos datos sean significativos para el algoritmo de ML, en cuyo caso se debe asignar un valor no valido entre -1 y -999 y proceder a probar el modelo, mientras que en caso contrario, se puede proceder a eliminar aquellas muestras de datos en las que el valor del atributo no se encuentre. Si la cantidad de muestras descartadas son suficientes como para disminuir la capacidad de predicción del modelo, se puede simplemente reemplazar aquellos valores faltantes por la media o la mediana del resto de valores de ese feature.

* Datos en distintas escalas de valores(Normalización de datos): Algunos algoritmos de ML requieren que las features se normalicen, de manera que residan en el mismo rango de numérico, debido a que el rango de una feature puede influenciar la importancia de la feature con respecto a otras. La normalización consiste en ajustar los valores para que se distribuyan entre un valor mínimo y máximo, generalmente ubicado entre [-1,1] o [0,1]. Existen varias maneras de realizar ésto, una de ellas es rescaling aunque la mas sencilla consiste en restar al valor mínimo a cada valor del rango de valores y dividir ésto sobre el rango total de valores, lo que brinda valores en el intervalo [0,1] o [-1,1] aplicando la siguiente fórmula:
  
.. figure:: ../figs/Cap4/formula_rescaling.png

   Fórmula Rescaling


Alternativamente, se puede aplicar la fórmula anterior reemplazando la resta del valor mínimo por la media de los valores:



.. figure:: ../figs/Cap4/formula_mean_normalization.png

   Fórmula normalización por media


Otro método para la normalización de features, es la estandarización que consiste en calcular la media y su desvío estándar para los valores de una feature determinada, y luego por cada valor de esa feature substraer la media y dividir por el desvío estándar

.. figure:: ../figs/Cap4/formula_estandarizacion.png

   Fórmula de estandarización


* Verificación de representatividad de los datos(Visualización de datos): Antes de realizar el entrenamiento puede ser necesario realizar la verificación de la relación y validez en las features que componen los datos de entrenamiento (por ejemplo en entrenamiento supervisado revisar como se relacionan las muestras y los resultados), necesitándose para ésto representaciones gráficas que indiquen que tan significativos son las muestras de que disponen y los tipos de muestras que podrían estar faltando.

Una de las herramientas empleadas para ésto son los gráficos de mosaicos, donde se representan las proporciones de instancias y los porcentajes de cada clase respecto del total, entre dos features del dataset. Este diagrama consiste en seleccionar dos features y realizar una subdivisión vertical entre las dos clases generando una columna para cada clase, donde el ancho de cada columna es equivalente a la proporción de los datos de esa clase respecto del total de datos. Luego se realiza la división de estos rectángulos por una línea horizontal, donde la altura de cada rectángulo depende de la cantidad de muestras que pertenecen a esa clase. Así, si la línea horizontal que separa ambos rectángulos se encuentra separada de manera considerable, ambas features se encontrarán fuertemente relacionadas, mientras que si por el contrario, se encuentran juntas significará que ambas features no se encuentran relacionadas. A continuación, se muestra un ejemplo para un dataset con información de pasajeros del Titanic, donde se demuestra que el género y la supervivencia se encuentran relacionadas:



.. figure:: ../figs/Cap4/ejemplo_moisac_plot.png
 
    Ejemplo de gráfico de mosaicos del dataset del Titanic
 

Otra herramienta utilizada para este fin son los gráficos de densidad, que permiten mostrar la distribución de alguna de las features, creando para ésto un estimado de la distribución de probabilidad basándose en los valores de esa feature, considerando que los valores proporcionados son una muestra aleatoria que representa la población de valores.Para esto, se utilizando una técnica estadística conocida como kernel de suavizado (kernel smoothing) que dado un conjunto *p* de valores reales, produce un valor real de salida que es un promedio ponderado de los datos vecinos observados. A continuación, la distribución de grafica como una curva que muestra los valores que la variable probablemente puede adoptar. De esta forma, creando un gráfico de densidad por cada categoría que una feature puede adoptar, se pueden visualizar diferencias en el rango de los valores en cada categoría. 


.. figure:: ../figs/Cap4/ejemplo_diagrama_densidad.png

   Ejemplo de diagrama de densidad para las millas por galon (MPG) que consumen autos fabricados por diferentes países, siendo las clases o categorías las siguientes: USA,Europa o Asia. Este gráfico ilustra la densidad de MPG vs el país del fabricante.


Alternativamente, se pueden emplear diagramas de dispersión (scatter plots), donde se grafican los valores de dos features, agregando un punto por cada instancia, lo que permite revelar tanto relaciones lineares como no lineares entre features y determinar si existe una relación útil entre ambas features son para el entrenamiento modelo. 


.. figure:: ../figs/Cap4/ejemplo_diagrama_dispersion.png

   Ejemplo de diagrama de dispersión. En la izquierda se muestra que la relación entre las features de MPG y el peso del vehículo no siguen una relación linear, mientras que en la imagen a la derecha se muestra que MPG y año de fabricación siguen una relación linear. De estas figuras, se deduce que ambas features se encuentran relacionadas a MPG y sirven para la predicción de MPG.



.. TODO: Incluir Matriz de covarianza gráfico y PCA!!!
.. https://en.wikipedia.org/wiki/Covariance
.. https://en.wikipedia.org/wiki/Covariance_matrix
.. https://en.wikipedia.org/wiki/Correlation_and_dependence#Correlation_matrices
.. https://machinelearningmastery.com/visualize-machine-learning-data-python-pandas/

Otro mecanismo empleado para visualizar la relación entre features de un dataset es la matriz de correlación (o matriz de covarianza) que es una matriz simétrica que consiste en, dadas *n* features del dataset, generar una matriz de *n x n* que relaciona cada feature con el resto y donde el elemento (i,j) de la matriz representa la correlación entre ambas features, siendo esta la relación linear que existe entre ambas variables. Así, si la variabilidad de una feature se encuentra asociada a la variabilidad de la otra, el elemento (i,j) de la matriz contendrá un valor positivo y cuanto más sea esta relación más alto será este valor. Por el contrario, si no existe una relación linear entre ambas features, tenderán a estar negativamente correlacionadas, siendo estos valores inferiores y negativos. 


.. figure:: ../figs/Cap4/Correlation-Matrix-Plot.png

   Ejemplo de gráfico de matriz de correlación para features relacionadas con personas que padecen diabetes. 


.. https://es.wikipedia.org/wiki/An%C3%A1lisis_de_componentes_principales
.. https://es.wikipedia.org/wiki/Teorema_de_descomposici%C3%B3n_espectral
.. https://es.wikipedia.org/wiki/Descomposici%C3%B3n_en_valores_singulares
.. http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA

Adicionalmente, durante la etapa de pre-procesamiento se puede aplicar un análisis de componentes principales (Principal Component Analysis,PCA) que es un algoritmo que consiste en realizar la transformación de un conjunto de datos con o sin correlación a un espacio de menor dimensión sin correlación, denominadas componentes principales. Para ello aplica a la matriz de correlación la descomposición de valores singulares, que es una factorización donde se computan los eigenvalores(o autovalores) y en base éstos se computa su raíz cuadrada, dando como resultado los valores singulares de la matriz. De esta forma, se busca que al reducir la dimensionalidad de los datos, se conserven solamente aquellos elementos que tengan mayor varianza y por lo tanto, sean los que aporten mayor información al modelo a construir.   

Una vez pre-procesados los datos, se lleva a cabo la etapa de entrenamiento donde se exponen los algoritmos de ML a los datos pre-procesados y se ajustan las configuraciones del modelo para controlar el comportamiento de éste ante los datos(hyperparametros del modelo). Estos hyperparametros no son ajustados por el modelo automáticamente, ya que en algunos casos éstos pueden ser difíciles de determinar y para aquellos que controlan la capacidad de predicción del modelo, si se aprenden para el dataset en particular, siempre brindarán la máxima capacidad de predicción para esos datos, lo que no implica que la capacidad de predicción del modelo sea la misma con otro conjunto de datos. Debido a ésto, los hyperparametros se suelen ajustar manualmente y, durante esta fase el dataset completo se suele subdividir en datos de entrenamiento (entre 70% y 80% del total de muestras) y datos de testing (30%-40% del total de las muestras). Generalmente los datos del dataset son previamente estructurados durante el pre-procesamiento en vectores vectores o matrices, separando los datos que contienen features en matrices y, las respuestas a éstos(también denominadas labels o targets), si se dispone de ellas, en un vector cuyos resultados se corresponden con la cantidad de muestras y se encuentran ordenados.  


Existen distintos tipos de métodos de entrenamiento según el objetivo perseguido con la generación del modelo entre los que se distinguen tres clases principales: Aprendizaje supervisado, aprendizaje no supervisado y aprendizaje por refuerzo. El aprendizaje supervisado, consiste en emplear las features y las respuestas de éstas(labels o clases) en un dataset para detectar relaciones entre los datos y sus resultados y así


.. TODO: Definir tipos de entrenamiento (supervisado vs no supervisado)




.. Header H4 -->

Aplicaciones de ML
^^^^^^^^^^^^^^^^^^

.. TODO: INCLUIR APLICACIONES DE ML -->

.. MIT-Machine Learning Book -cap5
.. Introduction to machine learning- alex smola,vishwanathan- cap1
.. Tom Mitchell - Machine learning - pag. 29.


Beneficios del uso de ML
^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO: TRADUCIR VENTAJAS DE MACHINE LEARNING -->

To wrap up our discussion of the microlending example, we list some of the most prominent advantages to using a machine-learning system, as compared to the most common alternatives of manual analysis, hardcoded business rules, and simple statistical models. The five advantages of machine learning are as follows:

* Accurate— ML uses data to discover the optimal decision-making engine for your problem. As you collect more data, the accuracy can increase automatically.
* Automated— As answers are validated or discarded, the ML model can learn new patterns automatically. This allows users to embed ML directly into an automated workflow.
* Fast— ML can generate answers in a matter of milliseconds as new data streams in, allowing systems to react in real time.
* Customizable— Many data-driven problems can be addressed with machine learning. ML models are custom built from your own data, and can be configured to optimize whatever metric drives your business.
* Scalable— As your business grows, ML easily scales to handle increased data rates. Some ML algorithms can scale to handle large amounts of data on many machines in the cloud.






En la siguiente sección, se resumen los mecanismos principales de ML y sus métricas relacionadas al ajuste del modelo para mejorar su precisión.



Mecanismos para Machine Learning(ML)
------------------------------------



.. Algoritmos de Pre-procesamiento de datos
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO: Incluir PCA, Normalización 


Maquinas de soporte de Vectores(SVM)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO: Completar!!!

Redes Neuronales(NN)
^^^^^^^^^^^^^^^^^^^^

.. TODO: Completar!!!

Árboles de decisión(Tree)
^^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO: Completar!!!


Algoritmos para la validación (testing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO: Incluir cross-validation



Selección de features para ML en PCL
------------------------------------

.. TODO: ELIMINAR DE ESTE PARRAFO LA DESCRIPCIÓN DE LOS TIPOS DE DESCRIPTORES PCL,YA QUE VA EN CAP3.

.. Inicialmente se investigó si PCL ofrecía funciones para obtener features de cada punto, de manera que se conozca información respecto de la geometría alrededor de un punto a través del procesamiento de sus vecinos, y se averiguó que PCL ofrecía una variedad de algoritmos que permiten computar "descriptores" que estan pensados para ser empleados en el reconocimiento de objetos 3D dentro de una captura. PCL ofrece dos tipos de descriptores: Descriptores locales que se emplean para describir la geometría alrededor de cada punto, sin considerar la geometría total del objeto que cada punto compone, por lo que cuando se emplean estos descriptores se deben seleccionar los puntos clave del objeto o keypoints que se desean procesar. Estos descriptores se emplean para el reconocimiento de objetos y para la registración(registration), que consiste en alinear dos nubes de puntos y por medio de transformaciones lineales, detectar si existen áreas comunes en ambas nubes de puntos.
.. Por otro lado, PCL ofrece descriptores globales que describen la geometría de un cluster de puntos que representa un objeto, por lo que para emplear estos descriptores se requiere preprocesar una nube de puntos, con el fin de aislar el objeto. Estos descriptores se aplican para el reoconocimiento de objetos y clasificación, estimación de posición y análisis de geometría (tipo de objeto, forma, etc.). Los descriptores locales que emplean un radio de busqueda, mayormente pueden ser usados como globales, si se computa un solo punto en el cluster y se modifica el radio de busqueda de puntos vecinos, de manera que se abarquen todos los puntos que componen el objeto.


 .. . Con respecto a los baches, se optó por seleccionar aquellos algoritmos que computan features llamadas normales( vectores unidad que son tangentes a un punto en una superficie y perpendiculares al plano en que se encuentra dicho punto).

Con respecto a la elección de features para ML, debido a que únicamente algunas grietas podían ser aisladas aplicando la metodología de cropeado de muestras (Ver pipeline de cropeado), ya que durante la recolección de muestras se observó que en la práctica existían grietas que no poseían profundidad significativa para ser detectadas por el sensor, sino solamente grosor y largo suficiente para ser apreciadas como grietas. Por lo tanto, se optó por clasificar solo aquellos tipos de fallas que poseen profundidad necesaria para ser aisladas por descriptores que computan información geométrica relacionada con los ángulos entre las normales de la superficie. Debido a ésto, se seleccionó un subconjunto del rango completo de descriptores locales y globales que PCL ofrece, acorde a las capacidades de computo disponibles y a las propiedades de las normales que éstos computan, siendo los descriptores testeados los siguientes: 

* Fast Point Feature Histogram(FPFH)(Local)
* ViewPoint Feature Histogram(VFH)(Local)
* Global Radious-based Surface Descriptor(GRSD)(Global)
* Ensamble Shape of Functions(ESF)(Global)


PFH-FPFH
^^^^^^^^

Los puntos orientados, compuestos por el vector de coordenadas y el vector normal del punto, son computacionalmente eficientes y rápidos de generar, sin embargo, no son capaces de capturar  información geométrica significativa alrededor de un punto, por lo que se necesita un descriptor que sea capaz de capturar información geométrica respecto de la curvatura, en base a los vecinos de un punto. Para ello se diseño Point Feature Histogram(PFH), que permite generalizar la curvatura media en base a los k-vecinos de un punto, empleando histograma de múltiples valores, que se caracteriza por ser invariante a la posición que adopta la superficie, robusto ante ruido y diferentes tipos de densidades en las muestras, e invariante a las rotaciones y traslaciones 3D. La implementación de este descriptor en PCL, se basa en el trabajo en :cite:`FPFH1` donde se define formalmente la metodología para computar las características locales geométricas partiendo desde una malla de triángulos.

El funcionamiento de PFH consiste en representar las relaciones entre puntos en un k-vecindario dados los puntos y sus normales estimadas, de manera que se capture con la mayor precisión posible las variaciones en la superficie tomando en consideración todas las interacciones entre las direcciones de las normales estimadas. De esta forma, las features de un punto dependen en gran parte de las estimaciones de las normales para los puntos. Formalmente, PFH para cada punto *p*, perteneciente a una nube de puntos realiza los siguientes pasos:
* Primero, considera aquellos *k* vecinos que se encuentran a una distancia menor a un radio *r* para el procesamiento, ubicándose en el centro de la esfera el punto de entrada *p*, y produciendo un conjunto de puntos *P = {pj1,pj2,...,pjn}*, y un conjunto de normales asociadas a cada punto *N = {Nj1,Nj2,...,Njn}*:


.. figure:: ../figs/Cap4/pfh_k_vecinos.png

   Ejemplo de los pk-vecinos considerados como entrada al algoritmo

* Luego, para cada par de puntos en el conjunto P de vecinos e incluyendo el punto central *p*,*pj1* y *pj2*, y sus normales estimadas se selecciona un punto *ps* como origen  y un punto *pt* como objetivo, siendo el punto origen el que tiene el menor ángulo entre la normal de ese punto y un vector imaginario que conecta *ps* y *pt*; Matemáticamente hablando, se debe cumplir la siguiente ecuación: :math:`|n1 \cdot (p2-p1)| <= |n2 \cdot (p2-p1)| `. Posteriormente, para computar las diferencias entre los puntos y sus normales, se procede a definir 3 vectores base *u*, *v* y *w* alrededor del punto origen, siendo *u* el vector normal *ns* asociado al punto origen y definiéndose estos vectores por medio de las siguientes fórmulas, donde *x* es el producto cruz entre dos vectores y *|| . ||* es la norma Euclidiana del vector:
  

.. math:: U = ns
   :label: ecuacionVectorU

.. math:: v = u x (pt - ps)/ || pt - ps ||
   :label: ecuacionVectorV


.. math:: w = u x v
   :label: ecuacionVectorW


.. figure:: ../figs/Cap4/esquema_ejes_punto_origen.png

   Asignación de ejes al punto origen 

* A continuación, empleando los vectores *uvw* y las coordenadas y normales de los puntos se pueden calcular la diferencia entre las dos normales de la siguiente manera, siendo :math:`{\cdot}` el producto escalar entre dos vectores y *d* la distancia Euclidiana entre ps y pt, *d* = || ps-pt ||:
  
.. math:: {\alpha} = v \cdot nt
          {\phi}  = u \cdot (pt-ps)/d
          {\theta} = arctan( w \cdot nt, u \cdot nt)
   :label: ecuacionesFeatures


.. figure:: esquema_ejes_angulos.png

   Ángulos y sus correspondencias con las normales


* Finalmente, las frecuencias de las tuplas (:math:`{\alpha}`,:math:`{\phi}`,:math:`{\theta}`,*d*) por cada punto se organizan en un histograma, y se divide cada una de los rangos de las  características en *b* subdivisiones y se cuentan las frecuencias de valores en cada subdivisión. Así, el número de subdivisiones por cada feature del histograma, que se pueden formar utilizando las 4 features es *d^⁴*. La implementación PFH de PCL, emplea 5 subdivisiones de histograma por feature (cada uno de los 4 valores de features empleará estos 5 valores como rangos de intervalo) y no incluye las distancias, lo que resulta en 5^3 = 125 valores float de features.


Debido a que la complejidad computacional de PFH es del orden O(n), esto puede resultar en cuellos de botella de procesamiento para aplicaciones en tiempo real o con considerable cantidad de muestras, por lo que para solventar este inconveniente se puede emplear FPFH. FPFH consiste en calcular para cada punto *p* de la nube, los valores de (:math:`{\alpha}`, :math:`{\phi}`, :math:`{\theta}`) análogamente a como se realiza con PFH, solo que este cálculo se realiza solamente entre el punto *p* y los k-vecinos de éste, denominando este valor como SPFH(p). A continuación, el valor SPFH(p) es ponderado calculando los features para los puntos vecinos *pk*, SPFH(pk), y utilizando las distancias *wk* entre cada punto *pk* y el punto *p*, empleando la siguiente fórmula:


.. figure:: ../figs/Cap4/fpfh_formula_ponderacion.png

   Fórmula para calculo de descriptor FPFH(p) 


.. figure:: ../figs/Cap4/fpfh_relaciones.png

   Esquema relaciones que se consideran para calcular las features de FPFH. El punto central *p* o *pq* se encuentra en el centro, las relaciones entre *p* y sus k-vecinos empleados para computar SPFH(p) se encuentran resaltados en rojo y las relaciones entre los k-vecinos empleadas para ponderación se encuentran remarcadas en negro.   



VFH
^^^

VFH es una variación de FPFH que se emplea para la identificación y reconocimiento de posición, donde se aprovecha la velocidad de procesamiento y la potencia de este descriptor y, se agrega el componente de punto de visión, que no es afectado por variaciones en la escala de los datos. VFH   agrega el punto de visión  a FPFH, computando un histograma de ángulos con la diferencia de ángulos entre la normal del punto de visión y cada uno de los puntos de la superficie capturada:




.. figure:: ../figs/Cap4/VFH_punto_vision.jpg
 
    Representación gráfica del primer componente entre el punto de visión y cada uno de puntos de la superficie.


Además se agrega un componente de forma de superficie, generando para ésto un histograma FPFH extendido, donde se incorpora la computación de los ángulos relativos entre las normales en cada punto de la captura y el centroide del objeto (punto central):

.. figure:: VFH_segundo_componente.jpg

   Incorporación de la diferencia entre normales de puntos y centroide del objeto 


La implementación de PCL utiliza 45 subdivisiones para cada uno de los valores de FPFH extendido, además de 45 subdivisiones para las distancias entre cada punto y el centroide y 128 subdivisiones para el punto de visión, lo que da como resultado un arreglo de 308 valores.

GRSD
^^^^

Este descriptor emplea el descriptor local Radious-based Surface Descriptor (RSD), que se basa en la descripción geométrica de una superficie por medio del cálculo de información radial, computada a través de información inherente a los puntos vecinos. El funcionamiento de este algoritmo se basa en establecer una relación entre los ángulos de las normales :math:`{\lambda}`, la distancia entre éstas *d* y el radio de una superficie *r* por medio de la siguiente fórmula: 


.. math:: `d = r* {\alpha}`
   :label: ecuacionRadio


.. figure:: ../figs/Cap4/radio_rsd_entre_normales.png

   Representación gráfica el ángulo, el radio y la esfera


Por lo tanto, para un punto punto *p* dado y cada uno de sus puntos vecinos, se calcula la diferencia entre normales, por medio del cálculo del ángulo :math:`{\alpha}`, la distancia entre las normales *d*y con estos valores, se obtiene el radio *r* de la esfera que engloba tanto a *p*  y su normal como  a uno de sus puntos vecinos y su normal asociada. Este proceso genera un conjunto de radios de las esferas que contienen a *p* y cada uno de sus vecinos, y sólo se agregan al descriptor de ese punto los radios máximos y mínimos.

.. figure:: ../figs/Cap4/diagrama_densidad_grsd.png

   En el gráfico de densidad, se muestra un gráfico de número /densidad de puntos en un rango de 1cm para diferentes objetos, ejemplificando la delimitación del tipo de superficie (plano,esfera,cilindro,ruido) según el rango de radios mínimo y máximo.


Esta método cuenta con la ventaja de ser fácil de computar y aún así mantener su capacidad de descripción, y se emplea principalmente para la detección de puntos que pertenecen a distintas superficies.

GRSD consiste en generar agrupamiento de puntos(o voxels) en lugar de puntos individuales, donde cada voxel tiene un ancho de 2.5 cm, y se procede a computar los radios máximos y mínimos entre y a etiquetar cada uno de los voxels según su valor de radio, siendo un plano si el radio_minimo > 0.1, una superficie cilíndrica si no es un plano y radio_máximo > 0.175, un borde/esquina o ruido, si no es cilíndrico y radio_mínimo < 0.015, esférico si no es un borde y radio_maximo - radio_minimo < 0.05 y otra superficie si no es ninguna de las anteriores. Una vez etiquetados todos los voxels, se computa un histograma global que describe las relaciones entre los clusters, en base a las intersecciones de cada superficie con el resto.


ESF
^^^

Este descriptor no emplea ningún tipo de pre-procesamiento, como las normales, sino que inicialmente emplea un conjunto de voxeles de la superficie(voxel grid). Este algoritmo consiste en iterar a través de cada uno de los puntos de la nube y, en de cada punto seleccionado, se eligen 3 puntos aleatorios y se computan las funciones de forma: D2,proporción D2(D2 ratio), D3 y A3, donde cada función genera histogramas que describen la relación geométrica entre puntos de la figura, produciendo un total de 10 sub-histogramas cada uno de 64 divisiones, por lo que el tamaño del histograma final es de 640. A continuación se detallan las funciones de forma:

* La función D2, computa las distancias entre los 3 puntos elegidos, formando 3 pares distintos, y para cada par verifica si la linea que conecta ambos puntos yacen completamente dentro de la superficie, enteramente afuera de la figura (no formando parte del objeto) o, abarcando una porción del objeto y una porción del espacio libre. Dependiendo de esta condición, se asigna el valor de distancia a un histograma IN, OUT o MIXED respectivamente.
  

.. figure:: ../figs/Cap4/Funcion_D2.png

   Representación gráfica de la función D2


* La proporción D2, consiste en generar un histograma que represente la proporción entre partes de la línea dentro de la superficie y fuera de ésta, donde el valor será cero si la línea esta completamente afuera, uno si esta completamente adentro, y un valor intermedio si se encuentra tanto dentro como fuera.

* La función D3, computa la raíz cuadrada del área del triángulo formada por los 3 puntos, y es agrupado, al igual que D2, en 3 histogramas IN,OUT y MIXED independientes de los que emplea D2.
  

.. figure:: ../figs/Cap4/Funcion_D3.png

   Representación gráfica de la función D3
  
* Finalmente, la función A3 computa el ángulo formado por los puntos del triángulo, y luego este valor es asignado a un histograma IN,OUT o MIXED, dependiendo de que superficie abarca la línea que se encuentra opuesta al ángulo calculado. Estos 3 histogramas son independientes de los que se emplean en D2 y D3.


.. figure:: ../figs/Cap4/Funcion_A3.png

   Representación gráfica de la función A3




Metodología de pre-procesado de muestras (Pipeline de Cropeado)
---------------------------------------------------------------

Debido a la cantidad numerosa de puntos que se encuentran en una captura realizada por el sensor (aproximadamente 300.000 puntos) y, a que se deseaba abstraer solo aquellas características propias de cada tipo de falla, se procedió a aplicar una serie de algoritmos como parte del pre-procesado de datos en machine learning o Pipeline de Cropeado, con el fin de reducir la cantidad de puntos de cada muestra y de sólo calcular el descriptor con los puntos principales de una falla.Este Pipleline de cropeado, se compone de los siguientes pasos:

1 - Eliminación de ruido con Statistical Removal: Debido a que la densidad de puntos de una captura puede variar, bajo diversas condiciones tales como: La cantidad de luz solar presente o la posición del sensor con respecto al pavimento, es necesario eliminar para cada captura aquellos valores extremos o outliers, que pueden interferir con la computación features de la muestra. Para ello, PCL ofrece un algoritmo de filtrado denominado Statistical Outlier Removal, el cual para cada punto en la nube de entrada computa la distancia media de éste hacia todos sus vecinos, y asumiendo que las distancias siguen una distribución estadística Gaussiana con una media y desvío estándar, elimina de la nube aquellos puntos cuyas distancias estén fuera del intervalo definido por la media y el desvío estándar de la distribución.
|

.. figure:: ../figs/Cap4/statistical_removal_ejemplo.jpg
   :scale:	70 %

   Izquierda: Ejemplo de nube de puntos sin el filtro Statistical Outlier Removal. Derecha: Ejemplo de nube de puntos con el filtro de Statistical Outlier Removal.

2 - Downsampling con Voxel Grid(Extracción de Keypoints): Se conoce con el nombre de voxel a un conjunto de puntos que forman una mínima unidad cubica (grilla en 3D) de un objeto tridimensional, de la misma forma que un pixel es la mínima unidad en una imagen en 2D. El algoritmo de Voxel Grid en PCL, permite reducir la cantidad de elementos de una nube, realizando una división de una nube de puntos en voxels, y computando en base a éstos el centroide (centro del voxel grid) que se tomará como el punto que representa al resto de los puntos en el voxel grid. Estos puntos se denominan keypoints o puntos de interés y son aquellos  puntos principales que aportan mayor información respecto de la estructura del pavimento a la SVM. Éstos se caracterizan por ser:

* Estables con respecto a interferencias locales y globales en el dominio de la imagen, como variaciones de iluminación y brillo.
* Distintivos para la caracterización efectiva de una superficie, y ricos en contenido en términos de color y textura.
* Tienen una posición claramente definida y se pueden obtener repetidamente con respecto a ruido y variaciones en el punto de visión.
* No es afectado por variaciones de escala, por lo que son ideales para procesamiento en tiempo real como también procesamiento en distintas escalas. 


.. figure:: ../figs/Cap4/voxel_grid_estructura.png
   :scale:	60 %

   Estructura de un voxel y voxel grid en 3D

3 - Segmentación con algoritmo de Planar Segmentation: La segmentación en PCL consiste en dividir una nube de puntos de entrada en varios clusters, donde cada cluster representa un objeto de la captura, que puede ser procesado independientemente. El algoritmo empleado  para la segmentación en PCL fue RANSAC (Random Sample Consensus), este algoritmo considera que en la nube de puntos de entrada existen puntos que pueden ser ajustados al modelo,con un margen de error especificado (inliers), y puntos que no se ajustan al modelo de RANSAC(outliers). Este algoritmo es una algoritmo no determinístico, y consiste en realizar N iteraciones, donde en cada una:  
	
		1. Se toma un subconjunto de puntos aleatorios de la nube de entrada y partiendo de un modelo establecido y, utilizando los puntos empleados como muestra, se realiza la computación de parámetros del modelo.
    2. A continuación, el algoritmo verifica cuales puntos del la nube de entrada completa son consistentes con el modelo generado, particularmente con los parámetros tomados como muestra en el paso anterior, empleando una función de costo o función de pérdida(loss function). Los puntos que no se ajusten al modelo instanciado con un margen de error se consideran outliers, mientras que el resto de puntos que se ajustan al modelo se consideran inliers, y forman parte del conjunto de consenso(consensus set).
    3. Se repite de nuevo el paso 1. 

De esta forma, el algoritmo RANSAC se repite una serie de veces hasta que se tengan suficientes inliers como para ser considerada confiable la estimación. PCL ofrece varios modelos geométricos predefinidos para emplear con RANSAC, entre los que se encuentran: Circulo 2D, Circulo 3D, Cono, Cilindro, Linea, Esfera, Vara(Stick) y Plano. Debido a la características geométrica de los senderos viales y de las fallas, se empleó para este paso RANSAC en combinación con el modelo de plano.  


4 - Cálculo de curvaturas principales (Principal Curvatures Estimation): Una vez realizada la segmentación, se realiza el cálculo de curvaturas promedio para cada uno de los clusters aislados, de manera que se filtren solo aquellos que se ubican en un valor dentro del rango de las fallas, siendo estos valores establecidos a partir del análisis de valores de curvaturas para baches y grietas. PCL ofrece un algoritmo denominado Principal Curvatures Estimation (PCE) para calcular curvaturas principales mínimas y máximas de cada punto, empleando eigenvectores y eigenvalores asociados, en base a un conjunto de puntos y sus normales asociadas. Los eigenvectores (o vectores propios), son un concepto relacionado con el álgebra lineal, y son aquellos vectores no nulos tales que al ser transformados por un operador lineal,no modifican su escala o producen un vector múltiplo de si mismo,manteniendo su dirección; Siendo el escalar que los multiplica :math:`{\lambda}` el eigenvector asociado con este valor. Matemáticamente, dada una matriz *A* n dimensional, se dice que  un vector *v* es un eigenvector y :math:`{\lambda}` es un eigenvalor asociado al eigenvector, si se cumple la siguiente equivalencia:


.. math:: A*v = {\lambda}*v
   :label: ecuacionEigenVector


Así, las curvaturas principales se calculan como los eigenvalores para un eigenvector en un punto dado y permiten indicar el grado de torcedura en una superficie para un punto establecido. Gráficamente, las curvaturas principales se pueden visualizar como: Para un punto *p* sobre una superficie dada y un vector unidad normal asociado, este contendrá un plano tangente que entre el punto y el vector normal unidad y, existirán diversos planos que contendrán al vector normal unidad y que cortarán a la superficie de manera distinta, lo que generará diversas curvas con distintos valores por plano. De esta forma, los valores de curvatura seleccionados serán aquellos máximos y mínimos que representen mayor grado de variación de ese conjunto.


.. figure:: ../figs/Cap4/curvaturas-principales.png
   :scale: 60%

   Representación gráfica de las curvaturas principales


Por lo tanto, el algoritmo de PCE en PCL para el plano tangente a la normal de un punto dado, aplica PCA sobre las normales de los puntos en un área dada (tomando k-vecinos del punto), siendo primero estas normales trasladadas al plano tangente, y finalmente retorna la curvatura principal (eigenvector del máximo eigenvalor), junto con los valores de curvatura mínimos y máximos (eigenvalores).


.. 4 - Filtrado de puntos con Statistical Removal luego de segmentación: Debido a que la segmentación puede producir en la práctica valores espurios, se aplica nuevamente Statistical Outliers Removal con el fin de eliminar valores extremos que puedan haber permanecido en la muestra.


Metodología para el procesamiento de muestras con ML
----------------------------------------------------

Dado que PCL ofrece facilidades para emplear el mecanismo de SVM a través de la librería libsvm (implementada en C y con bindings a Python y compatibilidad con Scikit Learn), se optó por seleccionar este mecanismo en combinación con los descriptores producidos por los algoritmos de ML seleccionados, para las pruebas de clasificación de fallas (detalladas en la sección bitácora de pruebas). La metodología de trabajo para el procesamiento de muestras se dividió en dos fases:

* La fase de preparación del modelo, donde se debió realizar la conversión del descriptor de PCL y las características de la falla a un formato compatible con libsvm, el entrenamiento del modelo con dichos datos y el almacenamiento de éste para su posterior uso en la clasificación. Durante esta etapa, se realiza el entrenamiento de un modelo por cada tipo de descriptor probado. 
* La fase de clasificación de muestras, donde se realiza el aislamiento de la muestra empleando el pipeline de cropeado y se emplea el modelo entrenado previamente para un descriptor para clasificar la muestra aislada previamente.        

Con respecto a la fase de preparación del modelo, los pasos específicos para generar cada modelo en base un descriptor consistieron en los siguientes: 

1. Aplicar el pipeline de cropeado para cada muestra
2. Computación de descriptor (ESF | FPFH | VFH | GRSD | RIFT)
3. Extracción de features (valores del histograma) del descriptor seleccionado 
4. Almacenamiento de las features en formato svmlight en archivo de training
5. Entrenamiento y almacenamiento del modelo entrenado con archivo de training
   


Luego de aplicar el pipeline de cropeado y computarse los descriptores de las muestras, se procede a realizar la conversión de las muestras a formato svmlight. Para la clasificación de muestras con svmlight, el formato consiste en especificar cada muestra como una combinación de un numero que especifica la clase a la que pertenece la misma separado por un espacio en blanco <SPACE> de sus features <FEATURE_N> con sus respectivos valores <VALOR> y, separada de otras muestras por caracteres de nueva linea <NEW_LINE>:

<LABEL> <FEATURE_1>:<VALOR> <FEATURE_2>:<VALOR> ... <FEATURE_N>:<VALOR><NEW_LINE>
<LABEL> <FEATURE_1>:<VALOR> <FEATURE_2>:<VALOR> ... <FEATURE_N>:<VALOR><NEW_LINE>
"..."

Para el modo de clasificación, la clase a la que la muestra pertenece se especifica como un valor positivo (1) si la muestra pertenece a la clase del tipo de elementos que se busca clasificar o, negativo (-1) si ésta no pertenece a la clase del tipo de elementos que se desean clasificar. Los features se especifican como una sucesión de valores numéricos que representan las características propias de cada muestra, y que varía según el tamaño del histograma del descriptor que se emplee. Con el fin de realizar la conversión, se empleo un script de generación de muestras que por medio de un archivo de configuración (.cfg), genera los descriptores para cada muestra y lo almacena en un archivo de testing o training según se haya especificado.


Una vez generados ambos archivos de training y testing, se procede a entrenar el modelo empleando el archivo de training, utilizando una de las utilidades provistas por svm-light (svm-train), que permite generar un modelo de salida para distintos tipos de kernel y distintos tipos de SVM según la tarea para la que se emplee la misma(regresión o clasificación). Debido a que se debe realizar una división de muestras entre clases preestablecidas, se empleó una SVM para clasificación de muestras (SVC) y  debido a que el kernel que mejor precisión brindo fue Linear, éste fue empelado para generar el modelo, en combinación con distintos descriptores.         


Con respecto a la etapa de clasificación, los pasos a seguir fueron los siguientes:

1. Aplicación del pipeline de cropeado a una muestra individual
2. Lectura del modelo entrenado desde disco
3. Computación de las dimensiones de la falla
4. Generación del descriptor final, combinando el descriptor PCL y las dimensiones de la falla
5. Conversión del descriptor final a formato svmlight 
6. Clasificación de la muestra (bache o grieta) empleando el descriptor final
7. Almacenamiento en formato json de las propiedades de la falla
8. Lectura y muestra de las propiedades obtenidas desde la aplicación web


Luego de obtener los clusters válidos desde el pipeline de cropeado, se procede generar el descriptor final computando el descriptor seleccionado en PCL y a calcular las dimensiones (alto-ancho y profundidad para baches y largo-grosor y profundidad para las grietas) en los ejes X,Y y Z por medio de la OBB mínima que contiene a la falla. De esta forma, el descriptor final para cada cluster se compone del descriptor de PCL sumado a la diferencia entre alto y ancho y, posteriormente se adapta al formato que es utilizado por la SVC. 

Una vez obtenida la muestra, se levanta el modelo entrenado desde disco, y se le asigna la muestra para su clasificación, obteniendo el tipo de ésta, el cual, se almacena junto con las dimensiones de la falla según corresponda y el nombre del cluster(generado en base al nombre de la muestra) en formato json. Éste, posteriormente es leído por la aplicación web, que mostrará dicha información en una sección a parte, donde se visualizan las propiedades de la falla. 



Bitácora de pruebas para clasificación
--------------------------------------

Como primera medida, se  procedió a realizar el cálculo de la cantidad de muestras que se dedicarán para training y testing del total de las muestras que se capturaron, siendo éste de 1000 muestras entre baches y grietas. Se decidió seleccionar un 76,75% de las muestras para training (766) y el 33% para testing (234). Una vez hecha la división, se decidió que se aplicaría un Pipeline de Cropeado que consistirá de varios pasos que abarcan desde la limpieza y aislamiento de la muestra hasta la clasificación, con el fin de disgregar el tipo de falla del plano en el que ésta se encuentra y obtener sólo features inherentes a la falla.

Con respecto a la computación de features de baches y grietas, se optó por investigar cuales de los descriptores de PCL se enfocaban en capturar las diferencias entre distintos tipos formas en superficies semejantes a planos, y debido al tamaño promedio de las nubes de puntos capturadas por el sensor, se seleccionaron aquellos que se definían por un histograma cuyas dimensiones no eran de una magnitud que prolongue el tiempo de procesamiento de manera excesiva.

Una vez aisladas todas las muestras de training, se comenzó con las pruebas de clasificación que consisten generar los descriptores FPFH del conjunto de training que emplea la SVM, tomando para este conjunto, como muestras positivas los baches y como muestras negativas las grietas, con el fin de intentar clasificar sólo entre baches y grietas. Una vez entrenada, la SVM se probó con diversos conjuntos de entrenamiento: Un conejo, un bache, una grieta y un conjunto de muestras mixto (que consistía de 7 baches y 28 elementos que no son baches). El resultado de esta prueba fue negativo, debido a que la muestra de bache no fue reconocida como tal, la del conejo resultó positiva y la del conjunto de training mixto proporcionó resultados positivos para muestras que no eran baches. Posteriormente, se aplicó la misma prueba para el descriptor VFH y GRSD, obteniéndose resultados positivos para muestras que no eran baches y negativos para baches, logrando un accuracy considerablemente inferior al esperado. Luego, se testeó escalando los valores de las features con el mismo dataset, la misma SVM y no se consiguió un aumento de precisión, para los 3 descriptores que emplean normales (FPFH,GRSD,VFH).

Dado que las diferencias entre los descriptores de los distintos tipos de muestra no eran significativas, se realizó una comparación gráfica de los descriptores pertenecientes al mismo conjunto de muestras, observando que el descriptor GRSD contenía mayor diferencia entre distintos tipos de muestra, por lo que se continuó experimentando solamente con este descriptor y se procedió a cambiar el enfoque, distinguiendo baches de planos y por otro lado, grietas y planos, necesitando clasificadores independientes. Con esta aproximación, la precisión aumentó considerablemente. 

Dada la necesidad de utilizar dos clasificadores diferentes por cada clase de muestra, se hizo un análisis de los valores de las curvaturas (por medio del algoritmo de PCL Principal Curvatures Estimation) máximos y mínimos promedio por por cada muestra, con el objetivo de encontrar un parámetro que, sumado al descriptor GRSD, permitiera la diferenciación entre ambos tipos de muestra empleando un único clasificador, y se pudo observar que el rango de curvatura promedio de las grietas estaba contenida dentro del rango de los baches, por lo que los baches contenían valores de curvatura mayores en general. Por esta razón, se decidió emplear el valor de curvatura para mejorar el segmentador y aislar sólo aquellas capturas cuya curvatura promedio se aproxime a la de un bache/grieta.

Luego se agregaron las features de curvatura máxima y mínima promedio de cada muestra al descriptor GRSD, y se entrenó una SVM con capacidad para multiclase (multi-labels), dividiendo las muestras utilizadas entre 3 diferentes clases: Baches, Grietas y Planos (utilizados solamente para este experimento). Se confeccionó el conjunto de training final con baches con histogramas GRSD similares, grietas y planos cropeados, (empleando como parámetros para un kernel RBF gamma -g 0.0008 y un costo -c 1) obteniendo una precisión del 55% con un subconjunto de muestras del set de testing, aisladas con el segmentador mejorado, por lo que se observó que muchos de los baches se clasificaron como grietas, distinguiéndose así éstos de los planos, pero no de las grietas. Como la precisión obtenida con GRSD resultó ser muy baja, adicionalmente se probó con el descriptor local FPFH que calcula un histograma por punto, agregando los valores de curvatura y, al probarlo con las muestras de testing anteriores, se logró una precisión del 56,47%, observando que el descriptor en combinación con la curvatura, no mejoraba satisfactoriamente la precisión.

Debido a esto, se decidió utilizar otro descriptor global conocido como Ensemble Shape of Functions (ESF) en una SVM multiclase, alcanzándose una precisión del 54.4444% empleando el mismo set de testing, pudiendo conseguir que el clasificador distinguiera las grietas y baches de los planos, pero sin diferenciar baches de grietas, clasificando el resto de las muestras como grietas cuando en realidad eran baches.

Otra prueba realizada, consistió en computar y analizar el área y volumen de cada muestra de training, ya que si bien estos valores mostraban una diferencia inferior al feature de curvaturas, no era lo suficientemente ínfima para no lograr diferenciar baches y grietas.  Al agregar estas características al descriptor GRSD, con SVM con kernel Linear se obtuvo una precisión del 52.94% con el set de testing de baches y grietas, sin incluir planos. Además, se incluyeron aquellos atributos que son referentes a las dimensiones de las grietas y baches de training: ancho, alto, profundidad y volumen, y con éstos se realizó una comparación con el fin de obtener valores que permitieran diferenciar entre baches y grietas. Así, se optó por emplear el descriptor GRSD con la diferencia en valor absoluto de ancho y alto de las fallas, clasificando por este límite a los baches que tienen diferencia | alto - ancho | > 40 como grietas y, los que tienen menor diferencia como baches. De esta forma, se reclasificaron las muestras según este valor y se realizaron las siguientes pruebas con el subconjunto de testing seleccionado obteniendo como resultado:

- Al agregar los valores de alto, profundidad y ancho, con el descriptor GRSD se obtuvo un accuracy de 79.8%.

- Al agregar al GRSD la diferencia entre ancho y alto al descriptor GRSD se logró un accuracy de 100%.
  
- Agregando volumen y profundidad al descriptor GRSD con la diferencia entre ancho y alto, se redujo el accuracy al 75%.

- Al agregar al GRSD la diferencia entre ancho y alto y testeando únicamente con el descriptor GRSD, se logró un accuracy de 75% kernel Linear y 87.5 con kernel RBF (con costo -c 2 y gamma -g 0.00000002).



Ya que al analizar la diferencia entre alto-ancho en el dataset de training de baches y grietas ésta era similar entre el mismo tipo de muestra, por lo que existían muestras (baches y grietas) que poseían una relación similar entre alto-ancho, se realizó una reclasificación de baches y grietas según esta característica. Luego al probar nuevamente la SVM entrenada con el subconjunto de testing incluyendo solamente los valores del descriptor GRSD y la diferencia entre alto-ancho, se consiguió una precisión del 87.5% con kernel RBF y un 100% con kernel Linear.


Al observar que la precisión incrementó reclasificando el dataset de training, se aplicó el mismo procedimiento para el dataset de testing completo y debido a que el ancho y alto calculados se basan en valores máximos y mínimos que son brindados el mecanismo Oriented Bounding Box de PCL en los ejes X-Y, el cual se ajusta y se orienta al tamaño de la muestra, se eliminaron aquellas muestras que contenían outliers que introducían ruido en el cálculo de esta diferencia, filtrando con estos parámetros de un total de 1000 muestras, 806 muestras (753 para training y 53 para testing). Al analizar las estadísticas de dimensiones del dataset de fallas de training, se seleccionó un límite de diferencia entre alto y ancho para dividirlas según el tipo (grieta o bache) de 0.49, ya que las grietas contenían una longitud considerablemente mayor al grosor, situación que no ocurría en baches. Al ejecutar nuevamente las pruebas con dataset de training y testing divididos por este límite, se obtuvo 89%  de accuracy con kernel Linear y 71% con kernel RBF (con gamma 0.0000002 y costo C 1500) empleando un cross validation de 5 iteraciones con GRSD. Nuevamente se procedió a experimentar con la diferencia alto-ancho, cambiando únicamente el descriptor con ESF y FPFH, obteniendo para los mismos parámetros y la misma cantidad de iteraciones los siguientes resultados:

* Con FPFH 63% para un kernel Linear y 60% para un kernel RBF.
* Con ESF 98% para un kernel Linear y 54% para un kernel RBF.
 

Finalmente, se realizó una comparación de las métricas de clasificación respecto de los distintos descriptores para la división original de muestras(53 en total), con el fin de contrastar la efectividad de clasificación de éstos y comprobar la superioridad de ESF respecto al resto. Para ello, se calcularon los valores de F1-Score y Recall para ambas clases y la matriz de confusión para exponer la cantidad de elementos efectivamente asignados a cada clase. Los valores de F1-Score y Recall para la partición del dataset inicial, con los kernels linear y RBF, se puede observar a continuación: 


+------------------+----------------------------------------+------------------------------------+
|                  |              Kernel Linear             |             Kernel RBF             |
+------------------+-------------+---------+----------------+-------------+---------+------------+
| Tipo de muestra  | Precision   | Recall  |  F1-Score      | Precision   | Recall  |  F1-Score  |
+==================+=============+=========+================+=============+=========+============+
| Baches           |  1.0        | 1.0     |  1.0           |     0.0     |   0.0   |     0.0    | 
+------------------+-------------+---------+----------------+-------------+---------+------------+
| Grietas          |  1.0        | 1.0     |  1.0           |     0.17    |   1.0   |     0.29   |
+------------------+-------------+---------+----------------+-------------+---------+------------+
| avg/total        |  1.0        | 1.0     |  1.0           |     0.03    |   0.17  |     0.05   |
+------------------+-------------+---------+----------------+-------------+---------+------------+ 

*Métricas para descriptor ESF con Kernel Linear-RBF*


+------------------+----------------------------------------+------------------------------------+
|                  |              Kernel Linear             |             Kernel RBF             |
+------------------+-------------+---------+----------------+-------------+---------+------------+ 
| Tipo de muestra  | Precision   | Recall  |  F1-Score      | Precision   | Recall  |  F1-Score  |
+==================+=============+=========+================+=============+=========+============+ 
| Baches           |  0.83       | 1       |  0.91          |     0.00    |   0.00  |    0.00    |
+------------------+-------------+---------+----------------+-------------+---------+------------+   
| Grietas          |  0.23       | 0.78    |  0.36          |     0.17    |   1.00  |    0.29    |
+------------------+-------------+---------+----------------+-------------+---------+------------+ 
| avg/total        |  0.80       | 0.53    |  0.58          |     0.03    |   0.17  |    0.05    |
+------------------+-------------+---------+----------------+-------------+---------+------------+  

*Métricas para descriptor GRSD con Kernel Linear-RBF*


+------------------+----------------------------------------+------------------------------------+
|                  |              Kernel Linear             |             Kernel RBF             |
+------------------+-------------+---------+----------------+-------------+---------+------------+ 
| Tipo de muestra  | Precision   | Recall  |  F1-Score      | Precision   | Recall  |  F1-Score  |
+==================+=============+=========+================+=============+=========+============+ 
| Baches           |  0.91       | 0.48    |  0.63          |      1.00   |   0.09  |  0.17      |
+------------------+-------------+---------+----------------+-------------+---------+------------+  
| Grietas          |  0.23       | 0.78    |  0.36          |      0.18   |   1.00  |  0.31      |
+------------------+-------------+---------+----------------+-------------+---------+------------+  
| avg/total        |  0.80       | 0.53    |  0.58          |      0.86   |   0.25  |  0.19      |
+------------------+-------------+---------+----------------+-------------+---------+------------+  

*Métricas para descriptor FPFH con Kernel Linear-RBF*


La matriz de confusión para cada uno de los descriptores empleados, con la partición de datos inicial, fue la siguiente:


.. figure:: ../figs/Cap4/matriz_confusion_GRSD.png 
   :scale: 70%

   Matriz de confusión de SVM con descriptor GRSD


.. figure:: ../figs/Cap4/matriz_confusion_ESF.png 
   :scale: 70%

   Matriz de confusión de SVM con descriptor ESF


.. figure:: ../figs/Cap4/matriz_confusion_FPFH.png 
   :scale: 70%

   Matriz de confusión de SVM con descriptor FPFH


Finalmente, se realizó una comparación de la precisión promedio del k-folding de cada uno de los métodos con la precisión brindada por un clasificador Dummy, para comprobar realmente que la eficiencia de clasificación del clasificador (con kernel linear) sobrepasa la de un clasificador aleatorio:

+----------------------+----------------------------+------------------------------+---------------+ 
|   Tipo de descriptor |           ESF              |          GRSD                |     FPFH      |
+----------------------+----------------------------+------------------------------+---------------+ 
| Tipo de clasificador | ClasificadorESF | DummyESF | ClasificadorGRSD | DummyGRSD | ClasificadorFPFH | DummyFPFH |
+======================+==================+=========+==================+===========+==================+=========+ 
| Precision            |       0.98      |   0.45   |         0.89    |    0.516   |       0.63      | 0.494      |   
+----------------------+------------------+---------+------------------+-----------+-----------------+--------------+ 


