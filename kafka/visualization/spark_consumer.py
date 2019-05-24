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
    week12 = db.week12
    for record in iter:
        data = json.loads(record[1])
        jsonData = {}
        jsonData["_id"] = data.get("bay_id")
        jsonData["latitude"] = data.get("lat")
        jsonData["longitude"] = data.get("lon")
        jsonData["status"] = data.get("status")
        try:
            week12.replace_one({"_id": data.get("bay_id")}, jsonData, True)
        except Exception as ex:
            print("Exception Occured. Message: {0}".format(str(ex)))
    client.close()


n_secs = 5
topic = "week12"

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

lines = kafkaStream.foreachRDD(lambda rdd: rdd.foreachPartition(sendDataToDB))

ssc.start()
time.sleep(600)  # Run stream for 10 minutes just in case no detection of producer
# ssc.awaitTermination()
ssc.stop(stopSparkContext=True, stopGraceFully=True)