from cryptography import fernet
import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet
import json

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("AGV")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global message
    decr = cipher.decrypt(msg.payload)
    message = json.loads(decr)
    with open('newOrder.json', 'w') as outfile:
        json.dump(message, outfile)
    print(msg.topic+" "+str(message))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#cipher_key = Fernet.generate_key()
#print(cipher_key)

cipher = Fernet(b'dk4e-Wbojtlq4iyENFjo1lc4BchKWGgdS5Cjgryjtd4=')

client.connect("test.mosquitto.org", 1883 , 60)
client.loop_forever()
