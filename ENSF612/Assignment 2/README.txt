Adam Kerr - 10146363

Input files should be placed on HDFS in directory /user/

A script is provided to run the second part iteratively

The commands for each part are as follows:

Matrix transpose:
/usr/local/hadoop/bin/hadoop \
jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar \
-D mapred.reduce.tasks=2 \
-input /user/matrix.txt \
-output /output/ \
-file map1.py -file reduce1.py \
-mapper map1.py -reducer reduce1.py

Parallel Breadth First Search:
./graph.sh

Normalized word co-occurrence matrix:
/usr/local/hadoop/bin/hadoop \
jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar \
-D mapred.reduce.tasks=2 \
-D stream.num.map.output.key.fields=2 \
-D mapred.text.key.partitioner.options=-k1 \
-input /user/retail.dat \
-output /output/ \
-file map3.py -file reduce3.py \
-mapper map3.py -reducer reduce3.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner