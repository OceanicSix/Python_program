import os

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
    week11 = db.week11
    for record in iter:
        data = record[1].split(":")
        jsonData = {}
        if data[1] is "":
            jsonData[data[0]] = "*"
        else:
            jsonData[data[0]] = data[1]
        try:
            week11.insert(jsonData)
        except Exception as ex:
            print("Exception Occured. Message: {0}".format(str(ex)))
    client.close()


n_secs = 1
topic = "Scenario061"

conf = SparkConf().setAppName("KafkaStreamProcessor").setMaster("local[2]")
sc = SparkContext.getOrCreate()
if sc is None:
    sc = SparkContext(conf=conf)
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, n_secs)

kafkaStream = KafkaUtils.createDirectStream(ssc, [topic], {
    'bootstrap.servers': '127.0.0.1:9092',
    'group.id': 'week11-group',
    'fetch.message.max.bytes': '15728640',
    'auto.offset.reset': 'largest'})
# Group ID is completely arbitrary

lines = kafkaStream.foreachRDD(lambda rdd: rdd.foreachPartition(sendDataToDB))

ssc.start()
time.sleep(600)  # Run stream for 10 minutes just in case no detection of producer
# ssc.awaitTermination()
ssc.stop(stopSparkContext=True, stopGraceFully=True)