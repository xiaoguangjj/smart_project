MFRC522-python
==============

A small class to interface with the NFC reader Module MFRC522 on the Raspberry Pi.

This is a Python port of the example code for the NFC module MF522-AN.

##Requirements
This code requires you to have SPI-Py installed from the following repository:
https://github.com/lthiery/SPI-Py

##Examples
This repository includes a couple of examples showing how to read, write, and dump data from a chip. They are thoroughly commented, and should be easy to understand.

## Pins
You can use [this](http://i.imgur.com/y7Fnvhq.png) image for reference.

| Name | Pin # | Pin name   |
|------|-------|------------|
| SDA  | 24    | GPIO8      |
| SCK  | 23    | GPIO11     |
| MOSI | 19    | GPIO10     |
| MISO | 21    | GPIO9      |
| IRQ  | None  | None       |
| GND  | Any   | Any Ground |
| RST  | 22    | GPIO25     |
| 3.3V | 1     | 3V3        |

##Usage
Import the class by importing MFRC522 in the top of your script. For more info see the examples.


LED灯
==============

#功能说明
一个灯的接口函数，实现了，调用改函数，就可以控制灯的“开”与“关”。

#调用接口
调用led_on()函数，可以打开灯。
调用led_off()函数，可以关闭灯。
调用led(time)函数，可以控制灯的闪烁，time为闪烁的时间，注意函数内包含sleep 需要防止阻塞。

#Pins

| Name | Pin # | Pin name   |
|------|-------|------------|
|  +   | 2     | 5V         |
|  -   | 11    | GPIO.1     |

蜂鸣器
==============

#功能说明
有源蜂鸣器的蜂鸣功能

#调用接口
调用buzz(time)函数，实现蜂鸣time时间，注意函数内包含sleep 需要防止阻塞，

#Pins

| Name | Pin # | Pin name   |
|------|-------|------------|
|  GND |   9   |    GND     |
|  I/O |   16  |   GPIO.4   |
|  VCC |   17  |    3.3V    |


