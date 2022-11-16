# Heavily unfinished

import machine
from machine import Pin, I2C
from lib.lcd.lcd_api import LcdApi
from lib.lcd.machine_i2c_lcd import I2cLcd
from lib.networking.netconf import isAp
from lib.networking.comms import *
from lib.essential.communication import *

isAp()

sock = serverInit()

i2c = I2C(sda=Pin(21), scl=Pin(22), freq=10000)
lcd = I2cLcd(i2c, 39, 4, 20)