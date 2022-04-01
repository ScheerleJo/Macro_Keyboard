#include <SPI.h>
#include "LCD_Driver.h"
#include "GUI_Paint.h"
#include "image.h"

void setup() {
  DIN = pinMode(10, OUTPUT);
  CLK = pinMode(8, OUTPUT);
  CS = pinMode(9, OUTPUT);
  DC = pinMode(11, OUTPUT);
  RST = pinMode(12, OUTPUT);
  BL = pinMode(13, OUTPUT);


  
}

void loop() {


}
