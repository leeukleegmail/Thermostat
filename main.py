import BME280
from utime import sleep
import ssd1306
from machine import Pin, I2C

i2c = I2C(scl=Pin(5), sda=Pin(4))

bme = BME280.BME280(i2c=i2c)  # addr 118
display = ssd1306.SSD1306_I2C(128, 64, i2c)  # addr 60
pin = Pin(14, Pin.IN, Pin.PULL_UP)  # D5

while True:
    display.fill(0)
    display.show()
    if not pin.value():
        display.text('Temp:{}'.format(bme.temperature[:-1]), 10, 10)
        display.text('Hum:{}'.format(bme.humidity[:-1]), 10, 26)
        display.text('Pres:{}'.format(bme.pressure[:-3]), 10, 42)
        display.rect(0, 0, 128, 64, 1)
        display.show()
        sleep(5)
