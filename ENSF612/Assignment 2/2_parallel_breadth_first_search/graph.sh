#!/bin/bash

INPUT=/user/input.txt
OUTPUT=/output/


clear="/usr/local/hadoop/bin/hdfs dfs -rm -r hdfs://10.1.3.106:9000/output"

mapred="/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar -D mapred.reduce.tasks=2 -input $INPUT -output $OUTPUT -file map2.py -file reduce2.py -mapper map2.py -reducer reduce2.py 2>&1 | grep NON_BLACK | cut -d "=" -f2"

get_output="/usr/local/hadoop/bin/hadoop fs -getmerge /output/ result.txt"
remove_input="/usr/local/hadoop/bin/hdfs dfs -rm hdfs://10.1.3.106:9000/user/input.txt"
put_input="/usr/local/hadoop/bin/hdfs dfs -moveFromLocal result.txt hdfs://10.1.3.106:9000/user/input.txt"

/usr/local/hadoop/bin/hdfs dfs -cp hdfs://10.1.3.106:9000/user/graph.txt hdfs://10.1.3.106:9000/user/input.txt

iteration(){
echo ITERATION $i
non_black=$(eval $mapred)
eval $remove_input
eval $get_output
eval $clear
eval $put_input
}

i="1"
non_black="-1"
iteration
while [ $non_black -ne "0" ]
do
echo UNVISITED NODES LEFT: $non_black
i=$[$i+1]
iteration
done

/usr/local/hadoop/bin/hdfs dfs -copyToLocal hdfs://10.1.3.106:9000/user/input.txt result.txt

eval $remove_input

echo DONE

