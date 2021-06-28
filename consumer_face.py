import sys
import time
import json
import os
from random import seed
from random import uniform
from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import loads

topic_face = "TOP22_05_FACE_RECO_DONE"

producer = KafkaProducer(bootstrap_servers='172.31.29.6:9092')

consumer_face = KafkaConsumer(topic_face, bootstrap_servers ='172.31.29.6:9092')

for message in consumer_face:
    message = message.value
    mess = json.loads(message)
    if mess["header"]["sender"] == "UoA":
        continue

    mess["header"]["source"] = "UoA Threat Assessment module"
    mess["header"]["sender"] = "UoA"

    if mess["body"]["faceRecognized"]["confidence"] <=0.6:
        mess["body"]["level"] = "low"
    elif mess["body"]["faceRecognized"]["confidence"] <=0.7:
        mess["body"]["level"] = "medium"
    else:
        mess["body"]["level"] = "high"
    # print("fr " + mess["body"]["level"])
    producer.send(topic_face, json.dumps(mess).encode('utf-8'))