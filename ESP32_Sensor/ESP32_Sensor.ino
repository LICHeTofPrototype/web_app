
#include <HTTPClient.h>
#include <WiFi.h>
#define SensorPin 34

volatile int SampleCount = 0;
char buffer[1000];
int time_m =0;
HTTPClient httpClient;


//[Wi-Fi環境・サーバ]が変更される場合は以下を変更
//*********************************************
const char* ssid = "elecom-58179b";
const char* password = "cmp574fn3em4";
const String host ="192.168.2.105";
#define PORT 8000
int Switch = 0;
//*********************************************




void setup() {
  
  Serial.begin(115200); 
  while (!Serial);
  pinMode(SensorPin, INPUT);
  
  if ( Switch == 0 ){
    WiFiDisConnect();
    HttpDisConnect();
    
    WiFiConnect();
    HttpConnect();
    
    for (int j=1 ; j <= 5; j++){
      CreateJson();
      delay(30000);
    }
    HttpDisConnect();
    WiFiDisConnect();
  }
  
}
 
void loop() {
  
  if ( Switch == 1 ){
    WiFiConnect();
    HttpConnect();
    CreateJson();
    HttpDisConnect();
    WiFiDisConnect();
  }
  
}
