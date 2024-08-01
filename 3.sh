y=$#
i=1
if [ $y -eq 0 ]
then
	echo "MAKE SURE TO ENTER THE ARGUMENTS!!"
else
    while [ $i -le $y ]
    do 
       loginname=$1
       grep $loginname /etc/passwd>s
       if [ $? -eq 0 ]
       then 
            echo "LOGINNAME: $loginname"
            echo "HOME DIRECTORY"
            cut -d \: -f 6 s
        else
            echo "ERROR--LOGINNAME IS ABSENT"
         fi
    shift
     i=`expr $i+1`
     done
fi
