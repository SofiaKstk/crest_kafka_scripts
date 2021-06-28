import sys
import time
import json
import os
from random import seed
from random import uniform
from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import loads

topic_obj = "TOP22_02_OBJECT_RECO_DONE"

producer = KafkaProducer(bootstrap_servers='172.31.29.6:9092')

consumer_obj = KafkaConsumer(topic_obj, bootstrap_servers ='172.31.29.6:9092')


for message in consumer_obj:
    message = message.value
    mess = json.loads(message)
    if mess["header"]["sender"] == "UoA":
        continue
    mess["header"]["source"] = "UoA Threat Assessment module"
    mess["header"]["sender"] = "UoA"
    if len(mess["body"]["objectsDetected"]["class_names"]) <=1:
        mess["body"]["threatLevel"] = "low"
    elif len(mess["body"]["objectsDetected"]["class_names"]) <=2:
        mess["body"]["threatLevel"] = "medium"
    else:
        mess["body"]["threatLevel"] = "high"
    # print("obj " + mess["body"]["threatLevel"])
    producer.send(topic_obj, json.dumps(mess).encode('utf-8'))