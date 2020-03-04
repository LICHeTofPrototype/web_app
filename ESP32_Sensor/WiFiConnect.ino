
#include <WiFi.h>

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
