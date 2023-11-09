#include <Mouse.h>

const int buttonPin = 2; // Change this to the pin where your button is connected
unsigned long lastDebounceTime = 0;
unsigned long doubleClickInterval = 250; // Adjust this value as needed
int buttonState = HIGH; // The current reading from the input pin
int lastButtonState = HIGH; // The previous reading from the input pin
bool singleClick = false;
bool doubleClick = false;

void setup() {
  pinMode(buttonPin, INPUT);
  Mouse.begin();
}

void loop() {
  int reading = digitalRead(buttonPin);
  
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > doubleClickInterval) {
    if (reading != buttonState) {
      buttonState = reading;

      if (buttonState == LOW) {
        singleClick = true;
      }
    }
  }

  if (singleClick) {
    // Send a single mouse click event
    Mouse.click();
    singleClick = false;
  }

//Edit to add Close button and Text to Speech

  if (doubleClick) {
    // Send a double mouse click event
    Mouse.click(MOUSE_LEFT);
    Mouse.click(MOUSE_LEFT);
    doubleClick = false;
  }

  lastButtonState = reading;
}
