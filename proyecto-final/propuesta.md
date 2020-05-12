**Título del proyecto:** Detección de microsatélites en tumores gastrointestinales.

**Descripción del proyecto**

La inmunoterapia es una estrategia eficaz para el tratamiento de pacientes de diferentes tumores. Sin embargo, en el caso de los pacientes con tumores gastrointestinales solo responden bien a esta terapia aquellos cuyo tumor pertenece al grupo de tumores con microsatélites inestables (MSI).
La detección de estos microsatélites con diferentes técnicas es muy costosa. Por tanto, lo que se propone es generar un modelo que distinga estos dos tipos de tumores (con MSI y sin MSI) a partir de imágenes de biopsias teñidas.

Para ello, el dataset se compone de 192312 imagenes de biopsias de tumores gastrointestinales teñidas: 117273 imagenes de tumores no MSI y 75039 de tumores MSI → problema de clasificación de 2 clases.

Etapas:

1) Preparar las imágenes y entrenar diferentes modelos de clasificación de ML y redes neuronales. Analizar los scores de los modelos: accuracy, precision, recall, f1.
Plotear la confusion matrix
¿Puedo separar desde el principio el dataset en 2 y entrenar secuencialmente?
2) Generar una API en Flask para pedir al usuario una imagen y devolver la predicción para esa imagen (con la probabilidad de que sea de ese tipo)
3) Hacer una Docker image
4) Hacer el deploy de la API a Heroku

**Info sobre dataset y módulos y librerías de python a usar**

- url del dataset en kaggle: https://www.kaggle.com/joangibert/tcga_coad_msi_mss_jpg

- modulos:
    - pandas
    - numpy
    - seaborn 
    - matplotlib
    - glob → para obtener los paths de todas las imágenes 
    - pillow, cv2 → para tratamiento de imagenes
    - sklearn → modelos de clasificación de ML y módulos de estadística
    - keras → redes neuronales
    - pickle → guardar un modelo entrenado
    - flask → para la API

- referencias:

glob  https://docs.python.org/2/library/glob.html

pillow https://pillow.readthedocs.io/en/stable/

OpenCV https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

scikit-learn https://scikit-learn.org/stable/supervised_learning.html#supervised-learning

keras https://keras.io/api/preprocessing/image/

pickle https://docs.python.org/3/library/pickle.html

flask https://flask.palletsprojects.com/en/1.1.x/
