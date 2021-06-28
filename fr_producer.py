import sys
import time
import json
import os
from random import choice
from random import seed
from random import randint
from random import uniform
from kafka import KafkaProducer
from datetime import datetime

topic = "TOP22_05_FACE_RECO_DONE"

# Start up producer
producer = KafkaProducer(bootstrap_servers='172.31.29.6:9092')

seed(1)
data = {}

data['header'] = {}
data['header']['caseId'] = "d5f97fe2-ab74-4ffd-8036-a3709f5953ae"
data['header']['msgId'] = "Message Id"
data['header']['msgType'] = "Data"
data['header']['scope'] = "Private"
data['header']['sender'] = "WAT"
data['header']['sentUtc'] = "2020-11-05T14:12:17.5767851Z"
data['header']['topicName'] = "TOP22_05_FACE_RECO_DONE"
data['header']['topicVer1'] = 1
data['header']['topicVer2'] = 0
data['header']['source'] = "WAT Face recognition module"
data['header']['status'] = "System"

data['body'] = {}
data['body']['camID'] = "Cam1234"
data['body']['level'] = "high"
data['body']['camID'] = "Cam1234"
data['body']['reason'] = "watch-list"
data['body']['sourceURL'] = "https://www.crest.org/images/image1.jpg"
data['body']['timestamp'] = "1970-01-01 00:00:00"

data['body']["faceRecognized"] = {}
data['body']["faceRecognized"]["bbox"] = ["5", "10", "120", "121"]
data['body']["faceRecognized"]["confidence"] = "0.789"
data['body']["faceRecognized"]["dataStoreId"] = "5f22c0f20c0afda939169007"
data['body']["faceRecognized"]["leaURL"] = "https://www.crest.org/images/image1.jpg"
data['body']["faceRecognized"]["subjectDesc"] = "suspect recognized"
data['body']["faceRecognized"]["subjectID"] = "Donald Duck"
data['body']["faceRecognized"]["subjectName"] = "suspect"

while True:
	# print(data['coordinates'][0])
	data['body']['faceRecognized']["confidence"] = uniform(0, 1)
	# data = {}
	# data['coordinates'] = [uniform(0.0, 50.0), uniform(0.0, 50.0)]

	
	json_data = json.dumps(data)
	print(json_data)
	producer.send(topic, json.dumps(data).encode('utf-8'))
	time.sleep(7)