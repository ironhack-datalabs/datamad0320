# 1. Print Hello World:
    echo Hello World    

# 2. Create dir called new_dir:
    mkdir new_dir

# 3. Delete new_dir:
    rmdir new_dir

# 4. Copy sed.txt from lorem to lorem-copy:
    cp lorem/sed.txt lorem-copy

# 5. Copy the other 2 files:
    cp lorem/at.txt lorem/lorem.txt lorem-copy

# 6. Show lorem/sed.txt:
    cat lorem/sed.txt

# 7.Show at.txt and lorem.txt from lorem:
    cat lorem/at.txt lorem/lorem.txt

# 8. Print 1st 3 lines of lorem-copy/sed.txt:
    head -3 lorem-copy/sed

# 9. Print last 3 lines of lorem-copy/sed.txt:
    tail -3 lorem-copy/sed

# 10. Add Homo homini lupus at the end of lorem-copy/sed.txt:
    echo Homo homini lupus >> lorem-copy/sed.txt

# 11. Visualize last 3 lines of lorem-copy/sed.txt, you should see "Homo homini lupus":
    #este punto no concuerda con el punto previo; antes te dice simplemente que añadas "Homo.." al final del archivo
    #sin embargo, aqui dice que usando tail -3 deberia aparecer solo "Homo homini lupus"
    #por tanto, para conseguir este punto he intentado en el punto 10 los siguientes comandos:
    sed -i '10i\Homo\nhomini\nlupus' lorem-copy/sed.txt
    sed -i '10 i\Homo\nhomini\nlupus' lorem-copy/sed.txt
    #sin embargo, a pesar de creo que son correctos no funcionan

# 12.Sub any et with ET in lorem-copy/at.txt:
    sed 's/et/ET/' lorem-copy/at.txt

# 13. Find active users right now:
    w

# 14. Find where you are:
    pwd

# 15. List .txt files in lorem:
    ls lorem/*.txt

# 16. Count #lines in in sed.txt:
    wc -l lorem/sed.txt

# 17. Find all files starting with lorem in the main dir and sub dirs
    find lorem | wc -l

# 18. Find all et in lorem/at.txt:
    grep 'et' lorem/at.txt

# 19. Count all et in lorem/at.txt:
    grep -o 'et' lorem/at.txt | wc -l 

# 20. Count et in all lorem-copy files:
    grep -o 'et' lorem-copy/* | wc -l 


#BONUS

# 1. Create var name with your name:
    name = diego

# 2. Print name:
    echo $name

# 3 Create dir with same name as the content in var name:
    mkdir diego

# 4. Delete the previous dir:
    rmdir diego

# 5.1 List all files inside lorem, with for loop
for f in lorem/*;do
    echo $f | cut -d '/' -f2 | cut -d '.' -f1
done

# 5.2 List the lenght:
for f in lorem/*;do
    ff=`echo $f | cut -d '/' -f2 | cut -d '.' -f1`
    echo ${#ff}
done

# 5.3 Print like "lorem has 5 characters lenght":
for f in lorem/*;do
    ff=`echo $f | cut -d '/' -f2 | cut -d '.' -f1`
    echo $ff has ${#ff} characters lenght
done

# 6 Show process with top and then sort with ps
top
ps aux

# 7. Show processor info:
lsblk

# 8. Create 3 alias:
alias la='ls -a'
alias lal='ls -als'
alias lah='ls -alsh'

# 9. Compress lorem and lorem-copy in tar.gz file:
tar -czvf lorem-compressed.tar.gz lorem lorem-copy

# 10. Descompress it in lorem-uncompressed:
tar -xzvf lorem-compressed.tar.gz -C lorem-uncompressed
