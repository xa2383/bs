echo "ENTER THE PATHNAME:"
read p
j=1
i=1
len=`echo $p | wc -c`  
while [ $i -le $len ]
do
    x=`echo $p | cut -d \/ -f $j`
	namelength=`echo $x | wc -c`
	mkdir -v $x
	cd $x
	j=`expr $j + 1`
    i=`expr $i + $namelength`
done

