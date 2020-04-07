1. #Imprime en consola Hello World.

print Hello World
echo Hello World

2. #Crea un directorio nuevo llamado new_dir

mkdir new_dir

3. #Elimina ese directorio.

rmdir new_dir

4. #Copia el archivo sed.txt dentro de la carpeta lorem a la carpeta lorem-copy.

cp lorem/sed.txt lorem-copy

5. #Copia los otros dos archivos de la carpeta lorem a la carpeta lorem-copy en una sola línea mediante ;.

cp "lorem/at.txt" "lorem/lorem.txt" lorem-copy
cp lorem/at.txt lorem-copy ; cp lorem/lorem.txt lorem-copy

6. #Muestra el contenido del archivo sed.txt dentro de la carpeta lorem.

cat lorem/sed.txt

7. #Muestra el contenido de los archivos at.txt y lorem.txt dentro de la carpeta lorem.

cat cat lorem/at.txt ; lorem/lorem.txt

8. #Visualiza las primeras 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy

cat lorem-copy/sed.txt | head -n3

9. #Visualiza las ultimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy

cat lorem-copy/sed.txt | tail -n3

10. #Añade Homo homini lupus. al final de archivo sed.txt dentro de la carpeta lorem-copy.

print "Homo homini lupus" >> lorem-copy/sed.txt
echo "Homo homini lupus" >> lorem-copy/sed.txt

11. #Visualiza las últimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy. Deberías ver ahora Homo homini lupus..

cat lorem-copy/sed.txt | tail -n3

12. #Sustituye todas las apariciones de et por ET del archivo at.txt dentro de la carpeta lorem-copy. Deberás usar sed.

sed -i "s/et/ET/g" lorem-copy/at.txt

13. #Encuentra al usuario activo en el sistema.

whoami

14. #Encuentra dónde estás en tu sistema de ficheros.

pwd

15 #Lista los archivos que terminan por .txt en la carpeta lorem.

ls lorem/*txt

16 #Cuenta el número de líneas que tiene el archivo sed.txt dentro de la carpeta lorem.

cat lorem/sed.txt | wc -l

17. #Cuenta el número de archivos que empiezan por lorem que están en este directorio y en directorios internos.

find . -name "lorem*.*" | wc -l

18. #Encuentra todas las apariciones de et en at.txt dentro de la carpeta lorem.

grep "et" lorem/at.txt

19. #Cuenta el número de apariciones del string et en at.txt dentro de la carpeta lorem.

grep -o "et" lorem/at.txt | wc -l

20. #Cuenta el número de apariciones del string et en todos los archivos del directorio lorem-copy

grep -o "et" lorem/* | wc -l

#Bonus

#Almacena en una variable name tu nombre.

name="Maca"

#Imprime esa variable.

echo $name

#Crea un directorio nuevo que se llame como el contenido de la variable name.

mkdir $name

#Elimina ese directorio.

rmdir $name

#Por cada archivo dentro de la carpeta lorem imprime el número de carácteres que tienen sus nombres. Intenta primero mostrar los archivos mediante un bucle for
#Imprime los ficheros
#Imprime las longitudes de los nombres de los ficheros
#Imprime outputs con la siguiente estructura: lorem has 5 characters lenght
 
 for file in lorem:
     print(file)

#Muestra los procesos de forma jerárquica que se están ejecutando en tu ordenador:
#Usando el comando top o htop
#Usando el comando ps con argumentos

pop
ps -am

#Muestra información sobre tu procesador por pantalla

#Crea 3 alias y haz que estén disponibles cada vez que inicias sesión

#Comprime las carpetas lorem y lorem-copy en un archivo llamado lorem-compressed.tar.gz

#Descomprime el archivo lorem-compressed.tar.gz en la carpeta lorem-uncompressed

