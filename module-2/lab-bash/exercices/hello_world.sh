 #!/bin/bash         

#Print Hello World
echo "Hello World"

#Crear nuevo directorio
mkdir new_dir

#Elimina ese directorio
rmdir new_dir

#Copia el archivo sed.txt dentro de la carpeta lorem a la carpeta lorem-copy
#Forma: cp [nombre de fichero] [ruta]
cp sed.txt /home/carolina/Desktop/IRONHACK/datamad0320/module-2/lab-bash/lorem-copy

#Copia los otros dos archivos de la carpeta lorem a la carpeta lorem-copy en 
#una sola línea mediante ;.
cp -r /home/carolina/Desktop/IRONHACK/datamad0320/module-2/lab-bash/lorem /home/carolina/Desktop/IRONHACK/datamad0320/module-2/lab-bash/lorem-copy

#Muestra el contenido del archivo sed.txt dentro de la carpeta lorem.
cat sed.txt

#Muestra el contenido de los archivos at.txt y lorem.txt dentro de la carpeta lorem.
cat at.txt , lorem.txt 

#Visualiza las primeras 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy.
head -n3 sed.txt 

#Visualiza las ultimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy.
tail -n3 sed.txt

#Añade Homo homini lupus. al final de archivo sed.txt dentro de la carpeta lorem-copy.
sed -i '$a Homo homini lupus' sed.txt

#Visualiza las últimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy.
# Deberías ver ahora Homo homini lupus..
tail -n3 sed.txt

#Sustituye todas las apariciones de et por ET del archivo at.txt dentro de la carpeta lorem-copy. 
#Deberás usar sed.
sed 's/et/ET/g' at.txt

#Encuentra al usuario activo en el sistema.
who

#Encuentra dónde estás en tu sistema de ficheros.
df –Th

#Lista los archivos que terminan por .txt en la carpeta lorem.
ls | grep '.txt'

#Cuenta el número de líneas que tiene el archivo sed.txt dentro de la carpeta lorem.
cat sed.txt| wc -l

#Cuenta el número de archivos que empiezan por lorem que están en este directorio
#y en directorios internos.
ls | grep 'lorem' | wc -l 

#Encuentra todas las apariciones de et en at.txt dentro de la carpeta lorem.
cat at.txt | grep et | wc -l

#Cuenta el número de apariciones del string et en at.txt dentro de la carpeta lorem.
cat at.txt | grep 'et' | wc -l

#Cuenta el número de apariciones del string et en todos los archivos del directorio lorem-copy.
grep 'et' * | wc -l

















