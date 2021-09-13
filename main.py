from machine import I2C,Pin
from ssd1306 import SSD1306_I2C
import utime as time
i2c=I2C(0,sda=Pin(16),scl=Pin(17))
oled = SSD1306_I2C(128,64,i2c)
T=0.6
led = Pin(25)
led.on()
oled.fill(1)
oled.show()
oled.fill(0)
oled.show()
time.sleep(1)
oled.text('Hello world!Hello world!Hello world!',0,9,1)
oled.show()
time.sleep(1)
oled.pixel(20,20,1) #x20 y20处画点
oled.show()
time.sleep(1)
oled.line(10,10,20,20,1)# 画线
oled.show()
time.sleep(1)
oled.vline(30,30,20,1) # 画竖线
oled.show()
time.sleep(1)
oled.hline(30,30,20,1) #画横线
oled.show()
time.sleep(1)
oled.fill(1)
oled.show()
oled.fill(0)
oled.show()