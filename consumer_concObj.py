import sys
import time
import json
import os
from random import seed
from random import uniform
from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import loads

topic_concObj = "TOP10_02_COD_ALERT"

producer = KafkaProducer(bootstrap_servers='172.31.29.6:9092')

consumer_concObj = KafkaConsumer(topic_concObj, bootstrap_servers ='172.31.29.6:9092', auto_offset_reset='earliest')
#consumer_concObj = KafkaConsumer(topic_concObj, bootstrap_servers ='172.31.29.6:9092')

for message in consumer_concObj:
    message = message.value
    mess = json.loads(message)
    if mess["header"]["sender"] == "UoA":
        continue
    mess["header"]["source"] = "UoA Threat Assessment module"
    mess["header"]["sender"] = "UoA"
    if len(mess["body"]["concealedObjects"]) <=1:
        mess["body"]["threatLevel"] = "low"
    elif len(mess["body"]["concealedObjects"]) <=2:
        mess["body"]["threatLevel"] = "medium"
    else:
        mess["body"]["threatLevel"] = "high"
    # print("conc " + mess["body"]["threatLevel"])
    print("Alert level updated.")
    producer.send(topic_concObj, json.dumps(mess).encode('utf-8'))