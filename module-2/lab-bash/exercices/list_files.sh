
# Imprime en consola Hello World.
echo 'Hello World'

#Crea un directorio nuevo llamado new_dir.
mkdir ../new_dir

#Elimina ese directorio.
rm -r ../new_dir #Remove recursevely
#Or using rmdir if it is empty: rmdir new_dir

#Copia el archivo sed.txt dentro de la carpeta lorem a la carpeta lorem-copy.
cp ../lorem/sed.txt ../lorem-copy/

#Copia los otros dos archivos de la carpeta lorem a la carpeta lorem-copy en una sola línea mediante ;.
cp ../lorem/at.txt ../lorem-copy/ ; cp ../lorem/lorem.txt ../lorem-copy/

#Muestra el contenido del archivo sed.txt dentro de la carpeta lorem.
cat ../lorem-copy/sed.txt

#Muestra el contenido de los archivos at.txt y lorem.txt dentro de la carpeta lorem.
cat ../lorem-copy/lorem.txt ../lorem-copy/at.txt #cat puede concatenar varios archivos.

#Visualiza las primeras 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy
cat ../lorem-copy/sed.txt | head -n3

#Visualiza las ultimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy
cat ../lorem-copy/sed.txt | tail -n3

#Añade Homo homini lupus. al final de archivo sed.txt dentro de la carpeta lorem-copy.
echo " Homo homini lupus." >> ../lorem-copy/sed.txt

#Visualiza las últimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy. Deberías ver ahora Homo homini lupus..
cat ../lorem-copy/sed.txt | tail -n3

#Sustituye todas las apariciones de et por ET del archivo at.txt dentro de la carpeta lorem-copy. Deberás usar sed.
sed -i 's/et/ET/g' ../lorem-copy/at.txt 
#s es el indicador de 'replace', et es el patrón a reemplazar y ET por lo que quieres reemplazarlo. 
# g indica que se reemplazen todas las ocurrencias en una línea
# El argumento i indica 'inline changes'. Para escribirlos permanentemente en el fichero

#Encuentra al usuario activo en el sistema.
w 
#Or the command who -a

#Encuentra dónde estás en tu sistema de ficheros.
pwd

#Lista los archivos que terminan por .txt en la carpeta lorem.
ls ../lorem/*txt

#Cuenta el número de líneas que tiene el archivo sed.txt dentro de la carpeta lorem.
wc -l ../lorem/sed.txt
#wc cuenta lineas, palabras or caracteres usando -l, -w o -m respectivamente

#Cuenta el número de archivos que empiezan por lorem que están en este directorio y en directorios internos.
find ../ -name 'lorem*.*' | wc -l
# Find command usa un patrón regex para encontrar cualtquier archivo con cualquier extensión que empieze por lorem
# El wc -l cuenta las líneas del output de find.

#Encuentra todas las apariciones de et en at.txt dentro de la carpeta lorem.
grep 'et' ../lorem/at.txt

#Cuenta el número de apariciones del string et en at.txt dentro de la carpeta lorem.
grep -o 'et' ../lorem/at.txt | wc -l 
# La flag -o de grep hace que te devuelva solamente los matches.

#Cuenta el número de apariciones del string et en todos los archivos del directorio lorem-copy.
grep -o 'et' ../lorem-copy/*.* | wc -l
# Como antes, solo que incluimos * como wildcard para que busque en todos los archivos. No encuentra los de at.txt porque 
# anteriormente los cambié de et a ET.


#Bonus

#Almacena en una variable name tu nombre.
name=david

#Imprime esa variable.
echo $name

#Crea un directorio nuevo que se llame como el contenido de la variable name.
mkdir ../$name

#Elimina ese directorio.
rm -r ../$name

#Por cada archivo dentro de la carpeta lorem imprime el número de carácteres que tienen sus nombres. Intenta primero mostrar los archivos mediante un bucle for
    #Imprime los ficheros
for file in $(ls ../lorem); do echo $file; done
    #Imprime las longitudes de los nombres de los ficheros
for file in $(ls ../lorem); do echo ${#file%.txt}; done
    #Imprime outputs con la siguiente estructura: lorem has 5 characters lenght
for file in $(ls ../lorem); do echo $file has ${#file%.txt} words; done
#Esto me funciona en la terminal, pero al correr el script me da error, no se por qué.


#Muestra los procesos de forma jerárquica que se están ejecutando en tu ordenador:
    #Usando el comando top o htop
    top
    #Usando el comando ps con argumentos
    ps -ef

#Muestra información sobre tu procesador por pantalla
lscpu
#or less /proc/cpuinfo para información individual por core

#Crea 3 alias y haz que estén disponibles cada vez que inicias sesión
echo -e 'alias py="python3"\n' >> ../../../../../../.bash_aliases
##Insertando una nueva linea en tu bashrc file o en un bash_aliases ya es accesible en cada sesión. 
# Solo voy a crear este por lo pronto. No soy muy amigo de los alias :P

#Comprime las carpetas lorem y lorem-copy en un archivo llamado lorem-compressed.tar.gz
tar -czvf ../lorem-compressed.tar.gz ../lorem ../lorem-copy

#Descomprime el archivo lorem-compressed.tar.gz en la carpeta lorem-uncompressed
mkdir ../lorem-uncompressed ; tar -xzvf ../lorem-compressed.tar.gz -C ../lorem-uncompressed