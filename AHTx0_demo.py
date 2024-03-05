# -*- coding: utf-8 -*-
#!/usr/bin/python3

# AHTx0_dataSave03.py
"""
2024/03/05  AHTのデータをOLEDに表示

AHTx0_demo.py
"""

# 補正値
temp_hosei  = 0
humdy_hosei = 0


import time
import board
import adafruit_ahtx0
import lib_oled

def data_read():
    i2c = board.I2C()  # uses board.SCL and board.SDA
    sensor = adafruit_ahtx0.AHTx0(i2c)
    temp  = sensor.temperature
    humdy = sensor.relative_humidity
    return temp,humdy

try:
    temp,humdy = data_read()
except:
    try:
        time.sleep(2)
        temp,humdy = data_read()
    except:
        print("AHTセンサーがありません")


print('測定値',end='', flush=True)
print("Temperature: %0.1f C" % temp, end='', flush=True)
print("   Humidity: %0.1f %%" % humdy)

print('補正値        ',end='', flush=True)
print('温度:',temp_hosei,'           湿度:',humdy_hosei)

print('補正後',end='', flush=True)
temp  = int((temp + temp_hosei)*10)/10
humdy = int(humdy + humdy_hosei)
print("Temperature: %0.1f C" % temp, end='', flush=True)
print("   Humidity: %0.1f %%" % humdy)

line1 = "temp :" + str(temp) +" c"
line2 = " "
line3 = "humd :" + str(humdy) +" %"
try:
    lib_oled.text(line1,line2,line3)
    time.sleep(6)
except:
    print("no OLED")

