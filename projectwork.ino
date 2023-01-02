#include<WiFi.h>
#include<HTTPClient.h>

const char* ssid = "WIFI_SSID_NAME";
const char* password = "WIFI_PASSWORD";

void setup()
{
  pinMode(14, OUTPUT);
  pinMode(25, OUTPUT);
  pinMode(26, OUTPUT);
  pinMode(27, OUTPUT);
  Serial.begin(115200);
  WiFi.disconnect();
  Serial.print("\nsetup done.....\n");
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.print("connecting to wifi..");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print('.');
    delay(500);
  }

  Serial.println("\nConnected to the wifi network");
  Serial.print("Local ESP32 IP: ");
  Serial.println(WiFi.localIP());
  Serial.print("RSSI: ");
  Serial.println(WiFi.RSSI());
}

void loop()
{
  
  if ((WiFi.status()== WL_CONNECTED))
  {
    HTTPClient http;

    http.begin(" IP-ADDRESS ");
    int httpCode = http.GET();

    if(httpCode > 0)
    {
      String payload = http.getString();
      Serial.println(httpCode);
      Serial.println(payload);

         digitalWrite(14, LOW);
         digitalWrite(25, LOW);
         digitalWrite(26, LOW);
         digitalWrite(27, LOW);

        if(payload == "1")
       {
         digitalWrite(14, HIGH);
         digitalWrite(25, HIGH);
       }

       if(payload == "2")
       {
         digitalWrite(27, HIGH);
         digitalWrite(25, HIGH);
         delay(500);
       }

       if(payload == "3")
       {
         digitalWrite(14, HIGH);
         digitalWrite(26, HIGH);
         delay(500);
       }

       if(payload == "4")
       {
         digitalWrite(27, HIGH);
         digitalWrite(26, HIGH);
       }

       if(payload == 0)
       {
         digitalWrite(14, LOW);
         digitalWrite(25, LOW);
         digitalWrite(26, LOW);
         digitalWrite(27, LOW);         
       }
    }

    else
    {
      Serial.println("Error on HTTP request");
    }

  http.end();  
  }

  delay(100);
}
