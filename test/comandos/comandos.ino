String command;
 
void setup() {
    Serial.begin(115200); 
}
 
void loop() {
    if(Serial.available()){
        command = Serial.readStringUntil('\n');
         
        if(command.equals("init")){
          Serial.println("init");
        }
        else if(command.equals("send")){
          Serial.println("send");
        }
        else if(command.equals("data")){
          Serial.println("data");
        }
        else if(command.equals("reboot")){
          Serial.println("reboot");
        }
        else{
          Serial.println("Invalid command");
        }
    }
}