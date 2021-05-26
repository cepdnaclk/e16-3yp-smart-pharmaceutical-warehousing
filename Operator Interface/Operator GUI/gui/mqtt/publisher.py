import sys
import paho.mqtt.client as mqtt
import threading
from cryptography.fernet import Fernet


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

cipher = Fernet(b'dk4e-Wbojtlq4iyENFjo1lc4BchKWGgdS5Cjgryjtd4=')



def mqtt( X):

    client.connect("test.mosquitto.org", 1883, 60)
    client.loop_start()
    message = b'testing 1 2 3'
    encryted = cipher.encrypt(message)
    out_message = encryted.decode()
    infot = client.publish("AGV", out_message , qos=2)
    infot.wait_for_publish()




t1 = threading.Thread(target=mqtt, args={55})
t1.start()
