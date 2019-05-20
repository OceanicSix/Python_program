import os
#ffI
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.0 pyspark-shell'

import sys
import time
import json
from pymongo import MongoClient
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


def sendDataToDB(iter):
    client = MongoClient()
    db = client.fit5148_db
    week12 = db.week12
    # join_result = set()
    # join_list = []
    for record in iter:
        join_result = set()
        # join_list = []
        # print(record[1])
        # print(123)
        for result in record[1]:
            join_result.add(result)
            print(join_result)

        print(123)
        #     join_result.add(i.split(",")[1])
        #     join_list.append(i)
        # print(join_resuIlt)
        # if len(join_esult)>1:
        #     join_list.insert(0,record[0])
        #     print(join_list)




    client.close()


n_secs = 10
topic = "TaskC-2"

conf = SparkConf().setAppName("KafkaStreamProcessor").setMaster("local[2]")
sc = SparkContext.getOrCreate()
if sc is None:
    sc = SparkContext(conf=conf)
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, n_secs)

kafkaStream = KafkaUtils.createDirectStream(ssc, [topic], {
    'bootstrap.servers': '127.0.0.1:9092',
    'group.id': 'week12-group',
    'fetch.message.max.bytes': '15728640',
    'auto.offset.reset': 'largest'})
# Group ID is completely arbitrary

joined_data = kafkaStream.groupByKey()
#lines = kafkaStream.foreachRDD(lambda rdd: rdd.foreachPartition(sendDataToDB))
lines = joined_data.foreachRDD(lambda rdd: rdd.foreachPartition(sendDataToDB))

ssc.start()
time.sleep(600)  # Run stream for 10 minutes just in case no detection of producer
# ssc.awaitTermination()I
ssc.stop(stopSparkContext=True, stopGraceFully=True)
