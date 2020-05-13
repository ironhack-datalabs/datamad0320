#**IDEAS PROYECTOS**

(He puesto ideas de proyectos más complicadas y más sencillas pero estoy un poco bloqueada. Así que añado ideas)

##**Nutritional information**

Entrenar un modelo que distinga la comida de una foto y te de la informacion nutricional aproximada segun grupo de alimentos
Lleve un recuento aproximado de las kcal que llevamos ingeridas, aproximadas.
Recomendaciones dietéticas segun peso y edad. 
Identificación de tipo de comida y buscar restaurantes cercanos donde pueda encontrar ese tipo de comida.


- MongoDB base de datos para almacenar la información nutricional
- Entrenar el modelo sklearn o redes neuronales para procesar las imagenes(TensorFlow-...). 
- Api de google para localizar restaurantes
- Flask

Posibles mejoras:
- Mi idea inicial es entrenar el modelo por grupos de comida pero quizás pueda afinarlo más.
- Presentación en js

Urls/dataset:

https://www.kaggle.com/kmader/food41 
https://www.tensorflow.org/datasets/catalog/food101

##**Recomendador de series Netflix:**

Crear una api con un sistema recomendador que recomiende series que ver.
https://www.kaggle.com/chasewillden/netflix-shows Es el dataset más limpio que he encontrado para series. Hay otros pero incluyen demasiadas peliculas y quiero enfocarme en series.
Habría que completar este dataset con información actual con webscrapping porque aquí dudo de que funcione al ser una web muy dinámica o con una api alternativa a la de Netflix que he encontrado https://rapidapi.com/unogs/api/uNoGS que a su vez las coge de https://unogs.com/
Posibles mejoras: que el recomendador busque en alguna otra plataforma, hbo, amazon prime, disney+
- MongoDB para almacenar los datos del usuario, de series vistas y gustos.
- Flask

##**rock-paper-scissors**

Jugar una partida de piedra-papel-tijeras a partir de un dataset de fotos de manos.
Enseñarle el modelos ampliado del juego(lagarto-spock)
* OpenCV para la obtencion de imagenes de la camara

* dataset
https://www.kaggle.com/drgfreeman/rockpaperscissors

* Posibles variaciones: Otros juegos. 
Por ejemplo que averigue un objeto:
http://cocodataset.org/#download (tiene una api para seleccionar el tipo de objetos de los que quiero obtener el dataset)



