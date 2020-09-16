Adam Kerr - 10146363


Assuming input file "shakespeare.txt" is located in hdfs in directory /user/
"shakespeare2.txt" is a copy of "shakespeare.txt"

The results for each part is also included

The following are the commands for each part of the assignment:

/usr/local/hadoop/bin/hadoop \
jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar \
-input /user/shakespeare.txt \
-output /output/ \
-file map1.py -file reduce1.py \
-mapper map1.py -reducer reduce1.py

/usr/local/hadoop/bin/hadoop \
jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar \
-input /user/shakespeare.txt \
-output /output/ \
-file map2.py -file reduce2.py \
-mapper map2.py -reducer reduce2.py

/usr/local/hadoop/bin/hadoop \
jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar \
-input /user/shakespeare.txt /user/shakespeare2.txt \
-output /output/ \
-file map3.py -file reduce3.py \
-mapper map3.py -reducer reduce3.py

/usr/local/hadoop/bin/hadoop \
jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar \
-D mapred.reduce.tasks=2 \
-D stream.num.map.output.key.fields=2 \
-D mapred.text.key.partitioner.options=-k1,2 \
-input /user/shakespeare.txt \
-output /output/ \
-file map4.py -file reduce4.py \
-mapper map4.py -reducer reduce4.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner