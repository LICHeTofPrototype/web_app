
#include <HTTPClient.h>
#define SensorPin 25

volatile int SampleCount = 0;
char buffer[1000];
HTTPClient httpClient;


//[Wi-Fi環境・サーバ]が変更される場合は以下を変更
//*********************************************
const char* ssid = "elecom-58179b";
const char* password = "cmp574fn3em4";
const String host ="192.168.2.105";
#define PORT 8000
//*********************************************

void setup() {
  Serial.begin(115200); 
  while (!Serial);
  pinMode(SensorPin, INPUT);
  
  WiFiConnect();
  HttpConnect();
  
  CreateJson();
  
  HttpDisConnect();
  WiFiDisConnect();
}
 
void loop() {
  //None
}
