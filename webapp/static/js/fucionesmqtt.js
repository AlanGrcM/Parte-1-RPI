function onConnectionLost(){
	console.log("connection lost");
	connected_flag=0;
}

function onFailure(message) {
    console.log("Failed");
    setTimeout(MQTTconnect, reconnectTimeout);
}

function onMessageArrived(r_message){
    out_msg="Message received "+r_message.payloadString+"<br>";
    out_msg=out_msg+"Message received Topic "+r_message.destinationName;
    //console.log("Message received ",r_message.payloadString);
    console.log(out_msg);
}
		
function onConnected(recon,url){
    console.log(" in onConnected " +reconn);
}

function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    connected_flag=1
    console.log("on Connect "+connected_flag);
    //mqtt.subscribe("sensor1");
    //message = new Paho.MQTT.Message("Hello World");
    //message.destinationName = "sensor1";
    //mqtt.send(message);
}

function MQTTconnect(host, port) {
	console.log("connecting to "+ host +" "+ port);
	mqtt = new Paho.MQTT.Client(host,port,"clientjsaaa");
	//document.write("connecting to "+ host);
	var options = {
        timeout: 3,
		onSuccess: onConnect,
		onFailure: onFailure,
      
     };
	
    mqtt.onConnectionLost = onConnectionLost;
    mqtt.onMessageArrived = onMessageArrived;
    mqtt.onConnected = onConnected;
	mqtt.connect(options);
	return false;
}

function sub_topics(stopic){
    if (connected_flag==0){
        out_msg="<b>Not Connected so can't subscribe</b>"
        console.log(out_msg);
        return false;
    }
    console.log("Subscribing to topic ="+stopic);
    mqtt.subscribe(stopic);
    return false;
}

function send_message(topic, msg){

    if (connected_flag==0){
        out_msg="<b>Not Connected so can't send</b>"
        console.log(out_msg);
        return false;
    }
    console.log(msg);

    message = new Paho.MQTT.Message(JSON.stringify(msg));
    if (topic=="")
        message.destinationName = "test-topic"
    else
        message.destinationName = topic;
    mqtt.send(message);
    return false;
}