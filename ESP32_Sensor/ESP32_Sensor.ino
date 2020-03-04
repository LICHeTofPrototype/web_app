
#include <HTTPClient.h>
#include <WiFi.h>
#include <ArduinoJson.h>

volatile int SampleCount = 0;

const char* ssid = "elecom-58179b";
const char* password = "cmp574fn3em4";
const String host ="192.168.2.105";


#define BlinkPin 26
#define SensorPin 25
#define PORT 8000

HTTPClient httpClient;
WiFiClient WiFiClient;

//*************************************
//true  : ProductionDjangoに送る場合
//false : SerialMonitorに表示する場合
int Production = 0;
//*************************************

void setup() {

  Serial.begin(115200); 
  while (!Serial);

  pinMode(BlinkPin, OUTPUT);
  pinMode(SensorPin, INPUT);
  
  WiFiDisConnect();
  WiFiConnect();
  HttpConnect();
  CreateJson();
  HttpDisConnect();
  WiFiDisConnect();
  
}
 
void loop() {
  //None
}






//*************************************************
// WiFiと接続
//*************************************************

void WiFiConnect(){
  
  WiFi.mode(WIFI_STA);
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
  Serial.print("\n");
  WiFi.disconnect();
  Serial.println("WiFi Disconnected");
  
}

//*************************************************
// サーバとの接続と送信
//*************************************************

void HttpConnect(){
  
  String url = "http://";
  url += host;
  url += ":";
  url += PORT;
  url += "/api/calc_pnn/2/";
  
  Serial.print("Requesting URL = ");
  Serial.println(url);
  Serial.println("Http Connected");
  Serial.print("\n");
  
  httpClient.begin(url);
  httpClient.addHeader("Content-Type", "application/json");

}

void HttpDisConnect(){
  
  int getCode = httpClient.GET();

  if(getCode > 0){
      String httpResponse = httpClient.getString();                   
      Serial.printf("Response: %d", getCode);  
      Serial.println(httpResponse);  
    }else{
      Serial.print("Error on sending GET: ");
      Serial.println(getCode);  
    }
    
  httpClient.end();
  Serial.println("Http Disonnected");
  
}

//*************************************************
// Json形式でデータ整形
//*************************************************

void CreateJson(){

  StaticJsonDocument<JSON_ARRAY_SIZE(50) + JSON_OBJECT_SIZE(2)> root;
  char buffer[1000];

  JsonArray Time = root.createNestedArray("time");
  JsonArray Beat = root.createNestedArray("beat");

  for(int i=1 ; i <= 20; i++){
    digitalWrite(BlinkPin, HIGH);
    SampleCount += 50;
    float Signal = analogRead(SensorPin);
    
    Time.add(SampleCount);
    Beat.add(Signal/4);
    
    digitalWrite(BlinkPin, LOW);
    delay(50);
  }


  Serial.println("****************************");
  
  serializeJson(root, Serial);
  Serial.println("");
  serializeJson(root, buffer, sizeof(buffer));

  int status_code = httpClient.POST((uint8_t*)buffer, strlen(buffer));

  if( status_code == 200 ){
    Stream* resp = httpClient.getStreamPtr();

    DynamicJsonDocument json_response(255);
    deserializeJson(json_response, *resp);

    serializeJson(json_response, Serial);
    Serial.println("");
  }else{
    Serial.print("Error on sending POST: ");
    Serial.println(status_code); 
  }

  
  Serial.println("****************************");
}
