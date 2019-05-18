# import statements
from time import sleep
from json import dumps
from kafka import KafkaProducer
import random
import datetime as dt


def publish_message(producer_instance, topic_name, data):
    try:
        value_bytes = bytes(data, encoding='utf-8')
        producer_instance.send(topic_name, value=value_bytes)
        print('Message published successfully. ' + data)
    except Exception as ex:
        print('Exception in publishing message.')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],
                                  api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka.')
        print(str(ex))
    finally:
        return _producer


if __name__ == '__main__':

    topic = 'Scenario061'
    print('Publishing records..')
    producer06 = connect_kafka_producer()

    for e in range(100):
        if e % 10 != 0:
            data = "data:" + str(random.randrange(0, 100))
        else:  # every 10th record will have missing data
            data = "data:"
        publish_message(producer06, topic, data)
        sleep(1)