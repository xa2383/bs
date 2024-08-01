if [ $# -eq 0 ];
then
		echo "no arguments"
		exit
fi
if [ $# -eq 2 ];then
		dir=$2
else
		dir=`pwd`
fi
inode=`stat -c %i $1`
count=0
for link in `find $dir -inum $inode`
do
		echo $link
		count=`expr $count + 1`
done
if [ $count -eq 0 ];
then
		echo "$1 has no link in the directory $dir"
else
		echo "$1 has $count links in the directory $dir"
fi
