import paho.mqtt.client as paho
import time

broker="192.168.1.77"

port= 9001

sub_topic="movimiento/#"

def on_subscribe(client, userdata, mid, granted_qos):   #create function for callback
   print("subscribed with qos",granted_qos, "\n")
   pass

def on_message(client, userdata, message):
    print("message received  "  ,str(message.payload.decode("utf-8")))

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

client.loop_forever()

# time.sleep(3)
# client.publish("house/bulb1","on")    #publish
# time.sleep(4)

# client.disconnect()