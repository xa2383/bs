echo "Enter the First File Name:" 
read f1
echo "Enter the Second File Name:"
read f2
if [ ! -f $f1 ] || [ ! -f $f2 ]
then
      echo "Given File Name is not Exited"
      exit 0 ;
fi
ls -l $f1 2> /dev/null > t1
x=`cut -c 2-10 t1`
ls -l $f2 2> /dev/null > t2
y=`cut -c 2-10 t2`
echo "Permission of the First File is $x"
echo "Permission of the Second File is $y"
if [ $x = $y ]
then
       echo "Permission for both files are same"
       echo $x 
else 
        echo "Permissions are different"
        echo $x $f1 
        echo $y $f2
fi
