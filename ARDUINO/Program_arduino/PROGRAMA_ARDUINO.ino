  #include <SoftwareSerial.h>
  SoftwareSerial portOne(10, 11);// software serial #1: RX = pin digital 10, TX = pin digital 11
  #include <DynamixelSerial.h>
  String readString;  
  int m1a=3;
  int m1b=5;
  int m2a=6;
  int m2b=9;
  int vel=200;
  
  int pint2=2;
  int pint4=4;
  int pint7=7;
  int pint8=8;
  int valpin2=0;
  int valpin4=0;
  int valpin7=0;
  int valpin8=0;
  
  void setup() {
    Serial.begin(9600); 
    while (!Serial)
    {
     ; 
    }
    portOne.begin(9600);
    
    pinMode(m1a,OUTPUT);
    pinMode(m1b,OUTPUT);
    pinMode(m2a,OUTPUT);
    pinMode(m2b,OUTPUT);
    pinMode(pint2,INPUT);
    pinMode(pint4,INPUT);
    pinMode(pint7,INPUT);
    pinMode(pint8,INPUT);
    
  
  
  }
  
  void loop() 
  {
    valpin2=digitalRead(pint2);
    valpin4=digitalRead(pint4);
    valpin7=digitalRead(pint7);
    valpin8=digitalRead(pint8);
    Serial.print(valpin7);
    
    if(valpin2==0 && valpin4==0 && valpin7==0)
    {
      detener();
     
    }
    if(valpin2==0 && valpin4==0 && valpin7==1)
    {
      adelante();
       Serial.print(valpin7);
    }
      if(valpin2==0 && valpin4==1 && valpin7==0)
    {
      izquierda();
    }
    if(valpin2==0 && valpin4==1 && valpin7==1)
    {
      derecha();
    }
    if(valpin2==1 && valpin4==0 && valpin7==0)
    {
     atras();
    }
  movilidad_brazo();
    
  }
 
  
  
  
  void movilidad_brazo()
  {
    portOne.listen();
    while (portOne.available()) 
     {
       delay(3);
       char c = portOne.read();
       readString += c;
      }
     comunicacion_bluetooth();
   }

  void comunicacion_bluetooth()
  {
    Dynamixel.begin(1000000);
    Dynamixel.setEndless(9,ON); 
    Dynamixel.setEndless(10,ON);
    Dynamixel.setEndless(15,ON); 
    Dynamixel.setEndless(6,ON); 
    Dynamixel.setEndless(16,ON);

    if(readString.length()>0)  
    {
      Serial.println(readString);
//------------------------------------------------------------      
    if (  readString == "w")
       {
         Dynamixel.turn(10,RIGTH,600);
         delay(100);
         
       }
      else
        {
          Dynamixel.torqueStatus(10,ON);
           Dynamixel.turn(10,RIGTH,0);
        }
//------------------------------------------------------------       
         if (  readString == "s")
       {
         Dynamixel.turn(10,LEFT,400);
       }
      else
        {
           Dynamixel.turn(10,LEFT,0);
           Dynamixel.torqueStatus(10,ON);
        }
          
     
//------------------------------------------------------------      
      if (  readString == "a")
       {
         Dynamixel.turn(9,LEFT,200);
         delay(100);
       }
      else
        {
           Dynamixel.turn(9,LEFT,0);
        }
//------------------------------------------------------------       
      if (  readString == "d")
       {
         Dynamixel.turn(9,RIGTH,200);
         
       }
      else
        {
           Dynamixel.turn(9,RIGTH,0);
        }  
     readString="";  
    }  
  }
    
  void detener()
  {
    analogWrite(m1a,0);
    analogWrite(m1b,0);
    analogWrite(m2a,0);
    analogWrite(m2b,0);
  }
  
  void izquierda()
  {
    analogWrite(m1a,vel);
    analogWrite(m1b,0);
    analogWrite(m2a,vel);
    analogWrite(m2b,0);
  }
  void derecha()
  {
    analogWrite(m1a,0);
    analogWrite(m1b,vel);
    analogWrite(m2a,0);
    analogWrite(m2b,vel);
  }
  void adelante()
  {
    analogWrite(m1a,vel);
    analogWrite(m1b,0);
    analogWrite(m2a,0);
    analogWrite(m2b,vel);
  }
  void atras()
  {
    analogWrite(m1a,0);
    analogWrite(m1b,vel);
    analogWrite(m2a,vel);
    analogWrite(m2b,0);
  }
  

