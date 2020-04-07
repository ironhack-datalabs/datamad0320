1. #Imprime en consola Hello World.
print Hello World

2. #Crea un directorio nuevo llamado new_dir
mkdir new_dir

3. #Elimina ese directorio.
rmdir new_dir

4. #Copia el archivo sed.txt dentro de la carpeta lorem a la carpeta lorem-copy.
cp lorem/sed.txt lorem-copy

5. #Copia los otros dos archivos de la carpeta lorem a la carpeta lorem-copy en una sola línea mediante ;.
cp "lorem/at.txt" "lorem/lorem.txt" lorem-copy

6. #Muestra el contenido del archivo sed.txt dentro de la carpeta lorem.

lorem git:(lab-bash) ✗ cat sed.txt

7. #Muestra el contenido de los archivos at.txt y lorem.txt dentro de la carpeta lorem.
lorem git:(lab-bash) ✗ cat at.txt cat lorem.txt

8. #Visualiza las primeras 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy
cat sed.txt | head -n3

9. #Visualiza las ultimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy
cat sed.txt | tail -n3

10. #Añade Homo homini lupus. al final de archivo sed.txt dentro de la carpeta lorem-copy.

11. #Visualiza las últimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy. Deberías ver ahora Homo homini lupus..

12. #Sustituye todas las apariciones de et por ET del archivo at.txt dentro de la carpeta lorem-copy. Deberás usar sed.

13. #Encuentra al usuario activo en el sistema.

14. #Encuentra dónde estás en tu sistema de ficheros.

15 #Lista los archivos que terminan por .txt en la carpeta lorem.

16 #Cuenta el número de líneas que tiene el archivo sed.txt dentro de la carpeta lorem.

17. #Cuenta el número de archivos que empiezan por lorem que están en este directorio y en directorios internos.

18. #Encuentra todas las apariciones de et en at.txt dentro de la carpeta lorem.

19. #Cuenta el número de apariciones del string et en at.txt dentro de la carpeta lorem.

20. #Cuenta el número de apariciones del string et en todos los archivos del directorio lorem-copy