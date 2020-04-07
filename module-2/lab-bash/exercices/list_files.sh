

# Ejercio 1
echo "Hello World"

# Ejercicio 2
mkdir new_dir

# Ejercico 3
rmdir new_dirls

# Ejercicio 4
cp lorem/sed.txt lorem-copy/

#Ejercicio 5
cp lorem/lorem.txt lorem-copy; cp lorem/at.txt lorem-copy

# Ejercicio 6
cat lorem/sed.txt

#Ejercicio 7
cat lorem/{sed.lorem}.txt

# Ejercicio 8
cat lorem-copy/sed.txt|head -n 3 

# Ejercicio 9
cat lorem-copy/sed.txt|tail -n 3

# Ejercicio 10
echo 'Homo homini lupus' >> lorem-copy/sed.txt

# Ejercico 11
cat lorem-copy/sed.txt | tail -n 3

# Ejercicio 12 
sed -i 's/\bet\b/ET/g' lorem-copy/at.txt


# Ejercicio 13
getent passwd {1000..60000}
# tambien he encontado estas para el ejercicio 13
whoami
id

# Ejercico 14
getent passwd{1000..60000}

# Ejercicio 15
ls lorem/*.txt

# Ejercicio 16
wc -l lorem/sed.txt

# Ejercicio 17
ls -1q lorem* | wc -l

# Ejercicio 18
cat lorem/at.txt |grep et  

# Ejercicio 19
cat lorem/at.txt |grep et | wc -l 

# Ejercicio 20
 cat lorem-copy/*.txt |grep et | wc -l 