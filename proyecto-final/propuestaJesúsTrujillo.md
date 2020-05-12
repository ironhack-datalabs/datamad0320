## TerracitAPP

### Descripción

API para realizar búsquedas de bares con terraza de acuerdo a las horas de sol disponibles. La metodología:
- Extraer la localización de los bares con terraza dentro de un radio fijado por el/la usuari@ de la aplicación.
- Calcular la altura de los edificios a través de Open Street Map y crear mapa de alturas de edificios
- Calcular la posición del sol mediante SunCalc.
- Crear mapas de zonas soleadas y sombreadas en función de la fecha y la hora a través de la posición del sol y el mapa de alturas de los edificios.
- [Si da tiempo] Ruta de la localización a la terraza.

### APIS, modulos, librerías

- Overpass API para extraer datos de Open Street MAP
- FourSquare API 
- Google Places API
- Shadow Mapper --> https://github.com/perliedman/shadow-mapper
- Flask + Heroku + Folium / Leaflet para servir los mapas



## Twitter moquea: Predecir picos de alergia a través de tweets

### Descripción

Estimación de niveles de polen a través de los síntomas/lamentos de los alérgicos en Twitter y las búsquedas en Google Trends. Se extraerán tweets que contengan palabras relacionadas con la sintomatología de las alergias principales (gramíneas, olivo, plátanos de sombra) mediante NLP, así como búsquedas de síntomas, remedios y medicamentos en Google Trends. Estos resultados se compararán con los datos de niveles de polen en aire reportados por la Sociedad Española de Alergología e Inmunología Clínica, para ver si existe correlación entre lo estimado y lo observado.
[Si da tiempo] Servir en una web un dashboard con los resultados.

### APIS, modulos, librerías

- Twitter API
- pyTrends
- Tweepy
- NLTK
- Gensim
- Skicit Learn (para los modelos)

Idea original
- https://dl.acm.org/doi/pdf/10.1145/2896338.2896342
- https://bmcmedinformdecismak.biomedcentral.com/track/pdf/10.1186/s12911-019-0921-x 
Base da datos para comparar los niveles de polen observados
- https://www.polenes.com/
