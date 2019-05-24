from sodapy import Socrata
# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.melbourne.vic.gov.au", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.melbourne.vic.gov.au,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
result_list = client.get("dtpv-d4pf", limit=2000)
print(type(result_list))

for result in result_list:
    print(result)

# import statements

from time import sleep
from json import dumps
from kafka import KafkaProducer
import random
import datetime as dt


def publish_message(producer_instance, topic_name, key, data):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=data)
        producer_instance.flush()
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

    topic = 'week12'

    print('Publishing records..')
    producer = connect_kafka_producer()

    for data in result_list:
        publish_message(producer, topic, 'jsondata', data)
        sleep(1)