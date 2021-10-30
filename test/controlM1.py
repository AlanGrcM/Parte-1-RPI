import time
import paho.mqtt.client as paho
import serial
import json

broker="localhost"
port= 9001
sub_topic="movimiento/#"
ser = serial.Serial('/dev/ttyACM0', 115200)

def movement(x, y):
    #print(x, y)
    if(y == 0):
        command = 'STOP'
    elif(y >= -10 and y < 0 ):
        command = 'FI'
    elif(y >= -30 and y < -10 ):
        command = 'FII'        
    elif(y >= -50 and y < -30 ):
        command = 'FIII'
    elif(y < -50 ):
        command = 'FIV'
    else:
        command = 'STOP'
    #print ("Se envio un: ", command + "\n")
    ser.write(str.encode(command + "\n"))

    #ser.write(str.encode("FI\n"))

def on_subscribe(client, userdata, mid, granted_qos):   #create function for callback
   print("subscribed with qos",granted_qos, "\n")
   pass

def on_message(client, userdata, message):
    m_decode=str(message.payload.decode("utf-8"))
    print("message received  "  , m_decode)
    m_in=json.loads(m_decode)
    movement(int(m_in["x"]), int(m_in["y"]))

def on_publish(client,userdata,mid):   #create function for callback
   print("data published mid=",mid, "\n")
   pass

def on_disconnect(client, userdata, rc):
   print("client disconnected ok") 

client= paho.Client("client-socks",transport='websockets')       #create client object
client.on_subscribe = on_subscribe       #assign function to callback
client.on_publish = on_publish        #assign function to callback
client.on_message = on_message        #assign function to callback
client.on_disconnect = on_disconnect
print("connecting to broker ",broker,"on port ",port)
client.connect(broker,port)           #establish connection
#client.loop_start()
print("subscribing to ",sub_topic)
client.subscribe(sub_topic)

while True:
  client.loop()
  #print ("Se recibio un: ", ser.readline())
  time.sleep(0.5) # Delay for one tenth of a second