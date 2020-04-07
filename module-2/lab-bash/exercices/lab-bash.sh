# Imprime en consola Hello World.
echo "Hello World"
# Crea un directorio nuevo llamado new_dir.
mkdir new_dir
# Elimina ese directorio.
rm -r new_dir
# Copia el archivo sed.txt dentro de la carpeta lorem a la carpeta lorem-copy.
cp -R ../lab-bash/lorem/sed.txt ../lab-bash/lorem-copy
# Copia los otros dos archivos de la carpeta lorem a la carpeta lorem-copy en una sola línea mediante ;.
cp -R ../lab-bash/lorem/* ../lab-bash/lorem-copy
# Muestra el contenido del archivo sed.txt dentro de la carpeta lorem.
cat lorem/sed.txt
# Muestra el contenido de los archivos at.txt y lorem.txt dentro de la carpeta lorem.
cat lorem/at.txt lorem/lorem.txt
# Visualiza las primeras 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy
cat lorem-copy/sed.txt | head -n3
# Visualiza las ultimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy
cat lorem-copy/sed.txt | tail -n3
# Añade Homo homini lupus. al final de archivo sed.txt dentro de la carpeta lorem-copy.
echo -e "Homo homini lupus." >> lorem-copy/sed.txt
# Visualiza las últimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy. Deberías ver ahora Homo homini lupus..
cat lorem-copy/sed.txt | tail -n3
# Sustituye todas las apariciones de et por ET del archivo at.txt dentro de la carpeta lorem-copy. Deberás usar sed.
sed 's/et/ET/g' lorem-copy/at.txt
# Encuentra al usuario activo en el sistema.
w
who
users
# Encuentra dónde estás en tu sistema de ficheros.
pwd
# Lista los archivos que terminan por .txt en la carpeta lorem.
for f in lorem/*.txt
for> do
for> echo "$f"
for> done
# Cuenta el número de líneas que tiene el archivo sed.txt dentro de la carpeta lorem.
cat lorem/sed.txt | wc -l
# Cuenta el número de archivos que empiezan por lorem que están en este directorio y en directorios internos.
ls lorem*/ | wc -l
# Encuentra todas las apariciones de et en at.txt dentro de la carpeta lorem.
grep at lorem/at.txt
# Cuenta el número de apariciones del string et en at.txt dentro de la carpeta lorem.
grep et lorem/at.txt | wc -w
# Cuenta el número de apariciones del string et en todos los archivos del directorio lorem-copy.
grep et lorem-copy/* | wc -w

