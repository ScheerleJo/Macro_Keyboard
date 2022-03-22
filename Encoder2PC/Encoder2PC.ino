int encoderPinA = 5;
int encoderPinB = 6;
int encoderPos = 0;
int encoderPinALast = LOW;
int encoderPinANow = LOW;
bool clicked = false;
bool klick = true;

void setup()
{
  pinMode(3, INPUT_PULLUP);
  pinMode (encoderPinA, INPUT_PULLUP);
  pinMode (encoderPinB, INPUT_PULLUP);
  Serial.begin(9600);
  Serial.println("System successfully booted");
}

void loop()
{
  encoderPinANow = digitalRead(encoderPinA);
  if ((encoderPinALast == HIGH) && (encoderPinANow == LOW)) {
    if (digitalRead(encoderPinB) == HIGH) {
      encoderPos++;
      delay(50);
    } else {
      encoderPos--;
      delay(50);
    }
    Serial.println(encoderPos);
  }
  encoderPinALast = encoderPinANow;

  klick = digitalRead(3);

  if (klick == LOW && clicked == false)
  {
    clicked = true;
    Serial.println("Switch Klicked");
  }
  if (klick == HIGH) clicked = false;
}
