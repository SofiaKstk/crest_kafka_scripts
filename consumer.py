import sys
import time
import json
import os
from random import seed
from random import uniform
from kafka import KafkaConsumer
# from json import loads

consumer_face = KafkaConsumer('TOP22_05_FACE_RECO_DONE',bootstrap_servers ='172.31.29.6:9092', auto_offset_reset='earliest')
# consumer_obj = KafkaConsumer('TOP22_02_OBJECT_RECO_DONE',bootstrap_servers ='172.31.29.6:9092', auto_offset_reset='earliest')
# consumer_concObj = KafkaConsumer('TOP10_02_COD_ALERT',bootstrap_servers ='172.31.29.6:9092', auto_offset_reset='earliest')

for message in consumer_face:
    message = message.value
    print(message)
    # mess = json.loads(message.value)
    # print(json.dumps(mess["header"]["source"]))
    # if mess["header"]["sender"] == "UoA":
    #     continue
    # mess["header"]["source"] = "UoA Threat Assessment module"
    # mess["header"]["sender"] = "UoA"
    # if mess["body"]["faceRecognized"]["confidence"] <=0.5:
    #   mess["body"]["level"] = "low"
    # elif mess["body"]["faceRecognized"]["confidence"] <=0.75:
    #   mess["body"]["level"] = "medium"
    # else:
    #   mess["body"]["level"] = "high"
    
# for message in consumer_obj:
#   message = message.value
#   mess = json.loads(message.value)
#   print(json.dumps(mess["header"]["source"]))
#     if mess["header"]["sender"] == "UoA":
#             continue
    # mess["header"]["source"] = "UoA Threat Assessment module"
    # mess["header"]["sender"] = "UoA"
    # if mess["body"]["class_names"].length <=1:
    #   mess["body"]["threatLevel"] = "low"
    # elif mess["body"]["class_names"].length <=2:
    #   mess["body"]["threatLevel"] = "medium"
    # else:
    #   mess["body"]["threatLevel"] = "high"

# for message in consumer_concObj:
#   message = message.value
#   mess = json.loads(message.value)
#   print(json.dumps(mess["header"]["source"]))
#     if mess["header"]["sender"] == "UoA":
#             continue
    # mess["header"]["source"] = "UoA Threat Assessment module"
    # mess["header"]["sender"] = "UoA"
    # if mess["body"]["concealedObjects"].length <=1:
    #   mess["body"]["threatLevel"] = "low"
    # elif mess["body"]["concealedObjects"].length <=2:
    #   mess["body"]["threatLevel"] = "medium"
    # else:
    #   mess["body"]["threatLevel"] = "high"