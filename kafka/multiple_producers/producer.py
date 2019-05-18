# import statements
from time import sleep
from json import dumps
from kafka import KafkaProducer
import random
import datetime as dt


def publish_message(producer_instance, topic_name, data):
    try:
        producer_instance.send(topic_name, value=data)
        print('Message published successfully. Data: ' + str(data))
    except Exception as ex:
        print('Exception in publishing message.')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                  value_serializer=lambda x: dumps(x).encode('ascii'),
                                  api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka.')
        print(str(ex))
    finally:
        return _producer


if __name__ == '__main__':

    topic = 'Scenario05'
    print('Publishing records..')
    producer01 = connect_kafka_producer()
    producer02 = connect_kafka_producer()
    producer03 = connect_kafka_producer()

    for e in range(100):
        datetime = str(dt.datetime.now().strftime("%X"))[-5:]
        data1 = {'datetime': datetime, 'producer05-1': random.randrange(0, 100)}
        publish_message(producer01, topic, data1)
        data2 = {'datetime': datetime, 'producer05-2': random.randrange(0, 100)}
        publish_message(producer02, topic, data2)
        data3 = {'datetime': datetime, 'producer05-3': random.randrange(0, 100)}
        publish_message(producer03, topic, data3)
        sleep(1)