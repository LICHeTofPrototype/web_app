
#include <HTTPClient.h>
#include <WiFi.h>
#include <WiFiClient.h>
#include <ArduinoJson.h>

volatile float Signal;
volatile int SampleCount = 0;
volatile int data_num = 20;

const char* ssid = "elecom-58179b";
const char* password = "cmp574fn3em4";
//const String host ="192.168.2.105";
const String host ="24d43ba2.ngrok.io";

#define BlinkPin 26
#define SensorPin 25
#define PORT 8000
HTTPClient httpClient;
WiFiClient client;

//*************************************
//true  : ProductionDjangoに送る場合
//false : SerialMonitorに表示する場合
volatile boolean Production = false;
//*************************************






void setup() {
  Serial.begin(115200); 
  pinMode(BlinkPin, OUTPUT);
  pinMode(SensorPin, INPUT);
  while (!Serial);
  
  if(Production == true){
    WiFiConnect();
    HttpConnect();
    CreateJson();
    HttpDisConnect();
    WiFiDisConnect();
  }

  if(Production == false){
    CreateJson();
    Serial.println("test3");
  }
  
}
 
void loop() {
  //None
}






//*************************************************
// WiFiと接続
//*************************************************

void WiFiConnect(){
  
  WiFi.begin(ssid, password); 
  
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
  
  Serial.print("\n");
  Serial.println("WiFi Connected");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP()); 
  Serial.print("\n");
  
}

void WiFiDisConnect() {
  
  WiFi.disconnect();
  Serial.println("WiFi Disconnected!");
  
}

//*************************************************
// サーバとの接続と送信
//*************************************************

void HttpConnect(){
  
  String url = "http://";
  url += host;
//  url += ":";
//  url += PORT;
  url += "/api/calc_pnn/2/";
  
  Serial.print("Requesting URL = ");
  Serial.println(url);
  Serial.println("Http Connected");
  Serial.print("\n");
  
  httpClient.begin(url);

}

void HttpDisConnect(){
  
  int httpCode2 = httpClient.GET();

  if(httpCode2 > 0){
      String httpResponse2 = httpClient.getString();                   
      Serial.printf("Response: %d", httpCode2);  
      Serial.println(httpResponse2);  
    }else{
      Serial.print("Error on sending GET: ");
      Serial.println(httpCode2);  
    }
    
  httpClient.end();
  Serial.println("Http Disonnected");
  
}

//*************************************************
// Json形式でデータ整形
//*************************************************

void CreateJson(){

  const size_t buffer_size = JSON_ARRAY_SIZE(data_num) + JSON_OBJECT_SIZE(2);
  DynamicJsonBuffer jsonBuffer(buffer_size);

  JsonObject& root = jsonBuffer.createObject();
  JsonArray& Time = root.createNestedArray("time");
  JsonArray& Beat = root.createNestedArray("data");

 
  for(int i=1 ; i <= data_num; i++){
    digitalWrite(BlinkPin, HIGH);
    SampleCount += 50;
    float Signal = analogRead(SensorPin);
    
    Time.add(SampleCount);
    Beat.add(Signal/4);
    
    digitalWrite(BlinkPin, LOW);
    delay(50);
  }



  Serial.println("****************************");
  
  if(Production == true){

    char jsonChar[10000000];
    root.printTo(jsonChar);
    int httpCode = httpClient.POST(jsonChar);
    
    if(httpCode > 0){
      String response = httpClient.getString(); 
      Serial.printf("Response: %d", httpCode);  
      Serial.println(response);          
    }else{
      Serial.print("Error on sending POST: ");
      Serial.println(httpCode);
    }

    Serial.println();
  }

  if(Production == false){
    root.printTo(Serial);
    Serial.print("\n");
  }
  
  Serial.println("****************************");
}
