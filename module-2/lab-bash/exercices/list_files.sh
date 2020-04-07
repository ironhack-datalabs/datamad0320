# OS: "Ubuntu 18.04.4 LTS"

# CREAR UN ARCHIVO .sh:
# code exercices/list_files.sh # code es el editor y list_files.sh el nombre del archivo

# EJECUTARLO POR TERMINAL:
# bash list_files.sh



# EJERCICIOS 

# Imprime en consola Hello World
# printf "%s\n" "hello world" # Mensaje y nueva línea de consola a parte
# printf "hello world" # Mensaje y nueva línea de consola todo seguido
# echo "Hello world" # Mensaje y nueva línea de consola a parte



# Crea un directorio nuevo llamado new_dir
# mkdir new_dir



# Elimina ese directorio
# rmdir new_dir



# Copia el archivo sed.txt dentro de la carpeta lorem a la carpeta lorem-copy
# cp lorem/sed.txt lorem-copy



# Copia los otros dos archivos de la carpeta lorem a la carpeta lorem-copy 
# en una sola línea mediante ;.
# cp lorem/at.txt lorem/lorem.txt lorem-copy # No hace falta poner ;



# Muestra el contenido del archivo sed.txt dentro de la carpeta lorem.
# cat lorem/sed.txt # todo seguido con la siguiente línea de comando en la misma línea
# cat lorem/sed.txt \n # incluyo \n para que la siguiente línea de comando vaya a parte.



# Muestra el contenido de los archivos at.txt y lorem.txt dentro de la carpeta lorem
# cat lorem/at.txt lorem/lorem.txt # Muestra el contenido todo seguido. He probado \n y no funciona



# Visualiza las primeras 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy
# cat lorem-copy/sed.txt |head -n3 # head indica primeras líneas y n3 especifica el número



# Visualiza las ultimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy
# cat lorem-copy/sed.txt |tail -n3



# Añade Homo homini lupus. al final de archivo sed.txt dentro de la carpeta lorem-copy.
# echo "Homo homini lupus." >> lorem-copy/sed.txt



# Visualiza las últimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy. 
# Deberías ver ahora Homo homini lupus..
# cat lorem-copy/sed.txt |tail -n3 



# Sustituye todas las apariciones de et por ET del archivo at.txt dentro de la carpeta 
# lorem-copy. Deberás usar sed.
# cat lorem-copy/at.txt # Abrimos el archivo primero (no es necesario)
# sed 's/et/ET/g' lorem-copy/at.txt # Hace el reemplazo y muestra el texto con los cambios



# Encuentra al usuario activo en el sistema
# w      # Muestra los usuarios activos y lo que están haciendo
# who    # Usuarios activos (versión más resumida que la anterior)
# users  # Muestra sólo el nombre del usuario
# whoami # Igual que users



# Encuentra dónde estás en tu sistema de ficheros.
# pwd



# Lista los archivos que terminan por .txt en la carpeta lorem
# ls lorem/*.txt



# Cuenta el número de líneas que tiene el archivo sed.txt dentro de la carpeta lorem
# wc -l lorem/sed.txt # Muestra el n. líneas y el nombre del archivo
# cat lorem/sed.txt | wc -l



# Cuenta el número de archivos que empiezan por lorem que están en 
# este directorio y en directorios internos.
# find "lorem" | wc -l
# ls -R | grep "lorem" | wc -l # Lista las carpetas que contengan "lorem" y lista el path 
                               # ./lorem con los ficheros que se llaman "lorem", de modo
                               # que cuenta dos veces cada carpeta "lorem"



# Encuentra todas las apariciones de et en at.txt dentro de la carpeta lorem
# cat lorem/at.txt | grep "et" # Escribiéndolo directamente por consola, muestra el texto 
                             # con el strin "et" en rojo (incluyendo las palabras que 
                             # contengan "et")



# Cuenta el número de apariciones del string et en at.txt dentro de la carpeta lorem.
# cat lorem/at.txt | grep "et" | wc -l



# Cuenta el número de apariciones del string et en todos los archivos del directorio lorem-copy.
# cat lorem-copy/*.txt | grep "et"| wc -l




# BONUS

# Almacena en una variable name tu nombre.
# name="Bea" # No puede ir con espacios!



# Imprime esa variable
# echo $name



# Crea un directorio nuevo que se llame como el contenido de la variable name
# mkdir $name



# Elimina ese directorio
# name="Bea"   
# rmdir $name   # Para eliminarlo por el nombre de la variable, hay que definirla de nuevo



#Por cada archivo dentro de la carpeta lorem imprime el número de carácteres que tienen sus 
# nombres. Intenta primero mostrar los archivos mediante un bucle for:

    #Imprime los ficheros
    #Imprime las longitudes de los nombres de los ficheros
    #Imprime outputs con la siguiente estructura: lorem has 5 characters lenght

"""
for file in "lorem/*.c" #*.c
    do 
    echo "Processing file.." 
    done
"""
#Muestra los procesos de forma jerárquica que se están ejecutando en tu ordenador:

    #Usando el comando top o htop
    #Usando el comando ps con argumentos

#Muestra información sobre tu procesador por pantalla
# top # Muestra los procesos que se están llevando a cabo en el ordenador



#Crea 3 alias y haz que estén disponibles cada vez que inicias sesión
# alias gs="git status"



#Comprime las carpetas lorem y lorem-copy en un archivo llamado lorem-compressed.tar.gz
# tar -czvf lorem-compressed.tar.gz lorem lorem-copy



#Descomprime el archivo lorem-compressed.tar.gz en la carpeta lorem-uncompressed
# tar -xvf lorem-compressed.tar.gz lorem-uncompressed # Muestra las carpetas y archivos