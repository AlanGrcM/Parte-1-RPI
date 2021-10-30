#include "DualVNH5019MotorShield.h"

DualVNH5019MotorShield md;

int speedM1 = 0;
int speedM2 = 0;

String command;

void stopIfFault()
{
  if (md.getM1Fault())
  {
    Serial.println("M1 fault");
    while(1);
  }
  if (md.getM2Fault())
  {
    Serial.println("M2 fault");
    while(1);
  }
}

void printCurrent(){
  Serial.print("M1 current: ");
  Serial.print(md.getM1CurrentMilliamps());
  Serial.print(" M2 current: ");
  Serial.println(md.getM2CurrentMilliamps());  
}

void forward(int speed){
  //md.setM1Speed(100);
  md.setM2Speed(speed);
  stopIfFault();
  Serial.print("Forward: ");
  Serial.println(speed);
}

void backward(int speed){
  //md.setM1Speed(speed * -1);
  md.setM2Speed(speed * -1);
  stopIfFault();
  Serial.print("Backward: -");
  Serial.println(speed);

}

void setup() {
  Serial.begin(115200); 
  Serial.println("Ready");
  md.init();
}

void loop() {
  if(Serial.available()){
    command = Serial.readStringUntil('\n');
    if(command.equals("STOP")){
      forward(0);
    }
    else if(command.equals("FI")){
      forward(100);
    }
    else if(command.equals("FII")){
      forward(200);
    }
    else if(command.equals("FIII")){
      forward(300);
    }
    else if(command.equals("FIV")){
      forward(400);
    }
    else if(command.equals("BI")){
      backward(100);
    }
    else if(command.equals("BII")){
      backward(200);
    }
    else if(command.equals("BIII")){
      backward(300);
    }
    else if(command.equals("BIV")){
      backward(400);
    }
    else{
      forward(0);
      Serial.println("Invalid command");
    }        
  }
  Serial.println(command);
  //printCurrent();
  //delay(100); // delay for 1/10 of a second
}