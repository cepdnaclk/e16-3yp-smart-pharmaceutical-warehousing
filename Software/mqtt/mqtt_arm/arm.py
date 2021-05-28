
from time import sleep
import paho.mqtt.client as mqtt
from prettytable import PrettyTable
from os import system
import os
import sys
from progress.bar import Bar
# delet single line
# sys.stdout.write("\033[F")

station_number = 0

dict = {'Name':None}

t = PrettyTable(['Type', 'value'])
S = PrettyTable(['Station',''])



def table(label , value ):
    
    dict[label] = value
    t.clear_rows()
    for key,value in dict.iteritems():
         t.add_row([key , value ])

    

    bar = Bar(label, max=100)
    for i in range(100):
        # Do some work
        bar.next()
        sleep(0.01)
    bar.finish()

    os.system('cls' if os.name == 'nt' else 'clear')
    print(t)
    print(S)

def station(station_number):
    
    bar = Bar('Station', max=100)
    for i in range(100):
        # Do some work
        bar.next()
        sleep(0.1)
    bar.finish()
    os.system('cls' if os.name == 'nt' else 'clear')
    S.add_row([station_number,'Null'])

    station_number += 1 

    print(t)
    print(S)

            




            

auth = {
    'username':'parveen',
    'password':'password'
}

def on_connect(mqttc, obj, flags, rc):
    print("Connected with result code "+str(rc))



def on_message(mqttc, obj, msg):
    
   
    text = msg.payload.decode("utf-8") 
    #print(text)
    if( text.startswith('Type:') ):
        table('Name',text.replace('Type:', ""))
  
        
    elif( text.startswith('IP:') ):
       # os.system('cls' if os.name == 'nt' else 'clear')
       table('IP addres',text.replace('IP:', ""))
       #t.add_row(['IP address', text.replace('IP:',"")])
       # print(t)
    elif(text.startswith('ID:')):
       table('ID',text.replace('ID:', ""))
       # os.system('cls' if os.name == 'nt' else 'clear')
        #t.add_row(['ID', text.replace('ID:',"")])
        #print(t)

    elif(text.startswith('LCD')):
        table('LCD',text.replace('LCD:', ""))

    elif(text.startswith('stepper:')):
        table('stepper',text.replace('stepper:', ""))

    
    elif(text.startswith('Motors:')):
        table('Motors',text.replace('Motors:', ""))

    elif(text.startswith('limit stwitch:')):
        table('limit stwitch',text.replace('limit stwitch:', ""))


    elif(text.startswith('Station:')):
        station(station_number)


    

        
            


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.username_pw_set("praveen","Pra350een")
client.connect("192.168.1.3", 1883, 60,)
client.subscribe("SERVER",qos=2)
#client.loop_start()

os.system('cls' if os.name == 'nt' else 'clear')
bar = Bar('loading', max=100)
for i in range(100):
    # Do some work
    bar.next()
    sleep(0.01)
bar.finish()

message = 'SERVER'
infot = client.publish("ARM1", message , qos=0 )
infot.wait_for_publish()



client.loop_forever()