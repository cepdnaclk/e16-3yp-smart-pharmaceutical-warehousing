import sys
import paho.mqtt.client as mqtt
import threading
from cryptography.fernet import Fernet
import json


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) +
          " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


cipher = Fernet(b'dk4e-Wbojtlq4iyENFjo1lc4BchKWGgdS5Cjgryjtd4=')



class MQTT:

    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.on_publish = on_publish

    def set(self, X):
        row = json.dumps(X)
        print(row)
        jsn = str.encode(row)
        #json_string = json.dumps(jsn)
       #message = bytearray( , "utf8")
        z = cipher.encrypt(jsn)
        self.msg = z.decode()

    def mqtt(self):

        cipher = Fernet(b'dk4e-Wbojtlq4iyENFjo1lc4BchKWGgdS5Cjgryjtd4=')


        self.client.connect("test.mosquitto.org", 1883, 60)
        self.client.loop_start()
        infot = self.client.publish("AGV", self.msg, qos=2)
        infot.wait_for_publish()
