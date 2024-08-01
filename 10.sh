for i in $*
do 
    echo "echo $i file is recreated"
     echo "cat > $i << *"
     cat $i
    echo "*"
done
