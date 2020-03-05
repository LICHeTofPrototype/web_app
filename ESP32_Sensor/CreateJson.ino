
#include <ArduinoJson.h>

//***********************************
int timeInterval = 50;  //ms
int arrayNum = 100;  //配列に入れる要素数
//arrayNum * 2 以上の数値をJSON_ARRAY_SIZE(**)に入れてね
//***********************************

void CreateJson(){

  StaticJsonDocument<JSON_ARRAY_SIZE(200) + JSON_OBJECT_SIZE(2)> root;
  JsonArray Time = root.createNestedArray("time");
  JsonArray Beat = root.createNestedArray("beat");
  
  for(int i=1 ; i <= arrayNum; i++){
    SampleCount += timeInterval;
    float Signal = analogRead(SensorPin);  
      
    Time.add(SampleCount);
    Beat.add(Signal);
    
    delay(timeInterval);
  }
  
  Serial.println("****************************");
  
  serializeJson(root, Serial);
  Serial.print("\n");
  serializeJson(root, buffer, sizeof(buffer));

  int postCode = httpClient.POST((uint8_t*)buffer, strlen(buffer));

  if( postCode == 200 ){
    Stream* resp = httpClient.getStreamPtr();

    DynamicJsonDocument json_response(255);
    deserializeJson(json_response, *resp);

    serializeJson(json_response, Serial);
    Serial.println("");
  }else{
    Serial.print("Error on sending POST: ");
    Serial.println(postCode); 
  }

  Serial.println("****************************");
}
