#Example program to read a text file from HDFS and
#output the word count of the text in the file
#
from operator import add
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
lines = spark.read.text("./myTest.txt").rdd.map(lambda r: r[0])
counters = lines.flatMap(lambda x: x.split(' ')) \
             .map(lambda x: (x, 1)) \
             .reduceByKey(add)

coll = counters.collect()
sortedCollection = sorted(coll, key = lambda r: r[1], reverse = True)

for i in range(0, 5):
     print(sortedCollection[i])

print("Test outputa")