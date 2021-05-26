import paho.mqtt.client as mqtt
import time
import json
#import bot

requested = False

# def sendFlag(data):
#     global requested
    
#     if requested:
#         client1.publish("AGV_receive", json.dumps(data), qos=2)
#         requested = False
            


def on_msg(client, userdata, message):

    global requested

    print(json.loads(message.payload))


    if message.topic == "destReached_Flag" and bool(requested) :
        client1.publish("AGV_receive", json.dumps(True), qos=2)
        requested = False

    if message.topic == "AGV_send":
        requested = True


# MQTT broker IP address
broker_address = "broker.mqttdashboard.com"

# client instance
client1 = mqtt.Client("AGV", transport='websockets')

client1.on_message = on_msg

client1.connect(broker_address, 8000, 60)

client1.subscribe("AGV_send")
client1.subscribe("destReached_Flag")
client1.loop_forever() 

    
    