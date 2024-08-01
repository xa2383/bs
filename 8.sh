if [ $# -lt 2 ] 
then        
    echo "USAGE:sh $0<pattern file><file1><file2>------"       
    exit 0; 
fi 
file=`cat $1` 
shift 
for word in $file 
    do      
        for file in $*      
        do         
        echo "occerence count of $word in file $file is:"         
        echo "`grep -iow $word $file | wc`"      
        done 
    done