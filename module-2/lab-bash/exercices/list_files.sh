#!/bin/bash

echo Hello world
mkdir new_dir 
rmdir new_dir #rm -r new_dir
cp ../lorem/sed.txt ../lorem-copy/ #"cp <origen><destino>"
cp ../lorem/* ../lorem-copy/ #"cp <origen>* <destino>"
cat ../lorem-copy/sed.txt #cat file.txt 
cat ../lorem-copy/at.txt ../lorem-copy/lorem.txt #cat file1.txt file2.txt
head -n 3 ../lorem-copy/sed.txt
tail -n 3 ../lorem-copy/sed.txt
echo Homo homiini lupus. >> ../lorem-copy/sed.txt #echo "Text" >> file.txt
tail -n 3 ../lorem-copy/sed.txt
sed 's/et/ET/g' ../lorem-copy/at.txt #sed 's/unix/linux/g' geekfile.txt
who
pwd
ls ../lorem/*.txt
wc -l ../lorem/sed.txt
find .. -iname 'lorem*' -type f | wc -l 
grep -r et ../lorem/at.txt
grep -o et ../lorem/at.txt | wc -l
grep -o et ../lorem/* | wc -l


#BONUS
name=Maria
echo $name
mkdir $name
rmdir $name

#i
for f in $(ls ../lorem);
do
echo ${f%%.*}
done
#ii
for f in $(ls ../lorem);
do
echo ${#f%%.*}
done
#iii
for f in $(ls ../lorem);
do
echo ${f%%.*} has ${#f%%.*} characters lenght
done

top
ps -ef
lscpu
alias w="who"
alias p="ps -ef"
alias l="lscpu"

cat ~/.bashrc >>
alias w="who"
alias p="ps -ef" 
alias l="lscpu"

tar -zcvf lorem-compressed.tar.gz ../lorem ../lorem-copy/

tar --list --file lorem-compressed.tar.gz 
mkdir lorem-uncompressed
tar -xzvf  lorem-compressed.tar.gz -C lorem-uncompressed 
