echo "Hello World"
mkdir new_dir
rmdir new_dir
cp -R -v ./lorem/sed.txt ./lorem-copy
cp -R -v ./lorem/{at,lorem}.txt ./lorem-copy
cat ./lorem/sed.txt
cat ./lorem/at.txt ./lorem/lorem.txt
head -n 3 ./lorem/sed.txt
tail -n 3 ./lorem/sed.txt
echo "Homo homini lupus." >> ./lorem-copy/sed.txt
tail -n 3 ./lorem-copy/sed.txt
sed 's/et/ET/' ./lorem-copy/at.txt
who
pdw
ls ./lorem/*.txt
wc -l ./lorem/sed.txt
ls | grep -v ^lorem | wc -l
grep -o -i et ./lorem-copy/at.txt | wc -l
grep -o -i et ./lorem-copy/*.txt  | wc -l
name=miriam
echo "$name"
mkdir "$name"
rmdir "$name"
for file in lorem/*;do
    ff=`echo $file | cut -d '/' -f2 | cut -d '.' -f1`
    echo ${ff} has ${#ff} character length
done
top
ps axu
sysctl -n machdep.cpu.brand_string
alias l='ls -lah'
zip -r lorem-compressed.tar.gz ./lorem ./lorem-copy







