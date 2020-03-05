
#include <HTTPClient.h>

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
