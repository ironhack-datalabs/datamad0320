# Imprime en consola Hello World
echo "Hello World"

# Crea un directorio nuevo llamado new_dir
mkdir new_dir

# Elimina ese directorio
    # para directorios vacíos
rmdir new_dir
    # para directorios con contenido. OJO! no pregunta, borra diretamente
rm -r new_dir
    # rm new_dir me da error. Es solo para archivos, no directorios

# Copia el archivo sed.txt dentro de la carpeta lorem a la carpeta lorem-copy
cp lorem/sed.txt lorem-copy

# Copia los otros dos archivos de la carpeta lorem a la carpeta lorem-copy en una sola línea mediante ;
    # cp -r lorem lorem-copy --> con este comando copio todo el directorio, incluido el directorio, no solo los archivos
cp lorem/at.txt lorem-copy; cp lorem/lorem.txt lorem-copy

# Muestra el contenido del archivo sed.txt dentro de la carpeta lorem
cat lorem/sed.txt

# Muestra el contenido de los archivos at.txt y lorem.txt dentro de la carpeta lorem.
# los concatena
cat lorem/at.txt; cat lorem/lorem.txt

# Visualiza las primeras 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy
cat lorem-copy/sed.txt | head -n 3
    # cat lorem-copy/sed.txt | head -n -3 --> te imprime todo menos las 3 últimas líneas

# Visualiza las ultimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy
cat lorem-copy/sed.txt | tail -n 3
    # cat lorem-copy/sed.txt | tail -n +3 --> con el + delante del número te muestra el archivo empezando por la línea 3

# Añade Homo homini lupus. al final de archivo sed.txt dentro de la carpeta lorem-copy.
# lo concatena 
echo "Homo homini lupus." >> lorem-copy/sed.txt

# Visualiza las últimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy. Deberías ver ahora Homo homini lupus.
cat lorem-copy/sed.txt | tail -n 3

# Sustituye todas las apariciones de et por ET del archivo at.txt dentro de la carpeta lorem-copy. Deberás usar sed.
sed 's/et/ET/' lorem-copy/at.txt

# Encuentra al usuario activo en el sistema.
logname # imprime el nombre del usuario actual
whoami # imprime el nombre asociado con el ID del actual usuario  the current effective user ID
id # imprime el usuario e info del usuario que se introduce (si no se introduce ninguno, pues del actual)

# Encuentra dónde estás en tu sistema de ficheros.
pwd 

# Lista los archivos que terminan por .txt en la carpeta lorem.
ls lorem/*.txt

# Cuenta el número de líneas que tiene el archivo sed.txt dentro de la carpeta lorem.
wc -l lorem/sed.txt # imprime el número de líneas (empezando por 0) y el path del archivo
cat lorem/sed.txt | wc -l # imprime solo el número de líneas (empezando por 0)
    # cat lorem/sed.txt -n --> te imprime todo el texto, pero numerando cada línea (empezando por 1)

# Cuenta el número de archivos que empiezan por lorem que están en este directorio y en directorios internos.
ls -l lorem | wc -l # obtengo un resultado de 4
    # ls -l lorem* | wc -l obtengo un resultado de 11 ?? El asterisco era para 
    #que encontrase archivos cuyo nombre empezara por lorem y siguiera por lo que sea

# Encuentra todas las apariciones de et en at.txt dentro de la carpeta lorem.
tr -s ' ' '\n' < lorem-copy/at.txt | grep -c 'et'  # es sensible a mayusculas y minusculas, pero no a estar concatenado a otro string. 
                                                    #Si está la palabra dos veces concatenada solo cuenta una
    # grep -c "et" lorem/at.txt --> cuenta las líneas donde hay match
grep -o "et" < lorem-copy/at.txt | wc -l

# Cuenta el número de apariciones del string et en at.txt dentro de la carpeta lorem.
# No he conseguido que me busque solo el string "et"

# Cuenta el número de apariciones del string et en todos los archivos del directorio lorem-copy.
cat lorem-copy/*.txt | grep -o "et" | wc -l  # busca todos los et, pero no el string "et"

# BONUS
#Almacena en una variable name tu nombre.
name=Flori

# Imprime esa variable.
echo $name

# Crea un directorio nuevo que se llame como el contenido de la variable name.
mkdir $name

# Elimina ese directorio.
rmdir $name

# Por cada archivo dentro de la carpeta lorem imprime el número de carácteres que tienen sus nombres. 
# Intenta primero mostrar los archivos mediante un bucle for
    #Imprime los ficheros
for e in $(ls lorem); do echo $e; done
for e in $(ls lorem); do echo ${e%.*}; done #eliminando los .txt
    #Imprime las longitudes de los nombres de los ficheros
for e in $(ls lorem); do echo ${#e}; done
    #Imprime outputs con la siguiente estructura: lorem has 5 characters lenght
for e in $(ls lorem); do echo $e has ${#e} characters lenght; done
for e in $(ls lorem); do echo ${e%.*} has ${#e} characters lenght; done # eliminando los .txt del nombre

# Muestra los procesos de forma jerárquica que se están ejecutando en tu ordenador:
    #Usando el comando top o htop
top
    #Usando el comando ps con argumentos
ps #los procesos actuales
ps r # para los procesos que están corriendo
ps -e # para todos los procesos

# Muestra información sobre tu procesador por pantalla
lscpu
cat /proc/cpuinfo

# Crea 3 alias y haz que estén disponibles cada vez que inicias sesión
# No lo he entendido. Alias como usuarios o alias para los comandos?

# Comprime las carpetas lorem y lorem-copy en un archivo llamado lorem-compressed.tar.gz
tar -czvf lorem-compressed.tar.gz lorem lorem-copy

# Descomprime el archivo lorem-compressed.tar.gz en la carpeta lorem-uncompressed
tar -xzvf lorem-compressed.tar.gz --directory lorem-uncompressed
tar -xzvf lorem-compressed.tar.gz -C lorem-uncompressed # en caso de que el directorio estuviese en otro path


