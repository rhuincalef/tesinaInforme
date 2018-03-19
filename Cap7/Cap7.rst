
Capítulo 7. Conclusiones y líneas futuras
=========================================

Este capítulo tiene como objetivo plantear los resultados logrados en la investagación realizada, como así también aquellos resultados obtenidos de la implementación del caso de aplicación. Además, se exponen las posibles líneas futuras de investigación que podrían llevarse a cabo y posibles funcionalidades que permitan enriquecer el comportamiento.

Conclusiones
------------

En la presente tesina, se ha realizado una investigación en profundidad de la estructura de datos empleada para la organización de nubes de puntos tridimensionales y la administración de éstas; los algoritmos de segmentación ofrecidos por la librería Point Cloud Library (PCL) que son de utilidad durante el proceso de clasificación de fallas viales. 

Adicionalmente, se ha estudiado los distintos tipos de descriptores que ofrece PCL teniendo las características propias de cada uno y su contribución al proceso de clasificación de las fallas viales, exponiendo en detalle aquellos mejor representaban la forma objeto en estudio.

Por otro lado, se realizó una investigación respecto a distintos tipos de mecanismos de aprendizaje automático que pueden ser utilizados en conjunto con los descriptores de PCL, encontrando que el mecanismo que mejores resultados brinda y requiere menor cantidad de muestras para su construcción es la SVM, ya que, la obtención de las muestras presenta una considerable dificultad. Una vez hecho esto, se efectuaron varios experimentos empleando este mecanismo y distintos tipos de descriptores, para finalmente realizar una comparación de los tres mejores descriptores con respecto a la precisión y seleccionar aquel de mayor precisión.

En cuanto al caso de aplicación, cabe señalar que se construyó una aplicación de captura que utiliza el sensor Kinect para el relevamiento de fallas viales utilizadas para la generación del modelo de clasificación, la cual permite interacturar con la aplicación web previamente desarrollada, tanto para el envío de fallas como para la obtención de fallas registradas a priori. Además, se agregó las posibilidad de persistir un conjunto de fallas en un formato propio de la aplicación para evitar la posibles pérdidas de las mismas (ya que al momento de su captura sólo se almacenan en memoria RAM) y brindar la comodidad de posponer el envío de dichas fallas a la aplicación web hasta que se disponga de una conectividad con un ancho de banda suficiente para esta tarea.

Además, se consiguió el objetivo de gestionar y visualizar el tipo de falla que fue obtenida desde la aplicación de captura en la aplicación web.

Finalmente, se cumplió con el objetivo de realizar la identificación y clasificación de los dos tipos de fallas seleccionados (baches y grietas) a través un pipeline que emplea los algoritmos de PCL previamente estudiados. Además, se logró que este clasificador se ejecute de manera automática e interactúe con los datos de la aplicación web (muestras de fallas viales 3D) y genere información que pueda ser procesada por esta. Por otro lado, además del tipo de falla se logró obtener propiedades inherentes a esta que pueden ser de interés, como son el alto, largo y profundidad.

Líneas futuras
--------------

Con respecto a posibles líneas de investigación, se puede considerar la captura en tiempo real de muestras sin necesidad de detener por completo el vehículo, íncorporando algún tipo de mecanismo que permita mitigar el ruido de la captura y detectar posibles depresiones asociadas a baches.

Por otro lado, la aplicación de captura puede ser extendida para soportar diferentes tipos de sensores tridimensionales que empleen distintos tipos de formato, realizando para ésto una comprobación al inicio para identificar el tipo de dispositivo actualmente conectado. 

Respecto a la funcionalidad de la aplicación web, se puede añadir la posibilidad de superponer sobre la muestra original los distintos segmentos clasificados de la falla, con el fin de contrastar la ubicación de los segmentos obtenidos.

En lo que respecta al tipo de falla y de material sobre los que se realiza la clasificación, ésta puede ser ampliada para realizarse sobre distintos tipos de fallas sobre otros tipos de materiales, debiendo para esto investigarse los algoritmos propuestos en este trabajo, además de los ofrecidos en PCL, para posteriormente, realizar una obtención de muestras que permita encontrar parámetros de segmentación apropiados para cada tipo de muestra a clasificar y llevar a cabo una experimentación que posibilite encontrar el/los descriptor/es más apropiados para el tipo de muestra en cuestión.

Finalmente, el modelo empleado para realizar la clasificación puede ser modificado para incorporar otros mecanismos de aprendizaje automático, tales como CART o Redes Neuronales.   
