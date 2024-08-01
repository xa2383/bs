clear 
echo "Enter the login name of the user:" 
read  name period=0 
echo "Enter the unit of time(min):" 
read min 
until who | grep -w "$name" > /dev/null 
do      
    sleep 60     
    period=`expr $period + 1` 
if [ $period -ge $min ] 
then         
    echo "$name has not logged in since $min minutes:"         
    exit 
fi 
done 
echo "$name has now logged in".