import pygeohash as pgh
from time import sleep
from json import dumps
from kafka import KafkaProducer
import random
import datetime as dt

climate_streaming = open('/home/student/PycharmProjects/Python_program/Assignment/MongoDb_Ass2/streaming/climate_streaming.csv','r').readlines()


def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()

    except Exception as ex:
        print('Exception in publishing message.')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                  api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka.')
        print(str(ex))
    finally:
        return _producer


if __name__ == '__main__':

    topic = 'TaskC-2'

    print('Publishing records..')
    producer = connect_kafka_producer()

    while True:
        random_data = climate_streaming[random.randrange(1, len(climate_streaming))].strip()
        #     print(random_data)
        #     print(randoIm_data.split(",")[1])

        geo_hash = pgh.encode(float(random_data.split(",")[0]), float(random_data.split(",")[1]), precision=5)
        #    print(geo_hash)

        data = str(dt.datetime.now().strftime("%X")) + ',' + "producer-1" + ',' + str(random_data)
        print(geo_hash+","+data)
        publish_message(producer, topic, geo_hash, data)
        sleep(5)
