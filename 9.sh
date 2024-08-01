clear 
if [ $# -lt 1 ] 
then 
echo " GIVE THE INPUT STRING"
exit 
fi 
echo "INPUT THE WORD TO DELETE" 
read word 
for file in $* 
do 
grep -iv "$word" $file|tee /dev/null $file 
done 
echo done
