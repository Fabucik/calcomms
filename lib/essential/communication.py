from lib.networking.comms import *
import machine
from machine import Pin
import uasyncio
from time import sleep
import _thread

# temporary variables
######################
enter = 26 #Pin(26, Pin.IN)
delete = 27 #Pin(27, Pin.IN)
# mode pin is used for setting access point mode or station mode on boot
# and for viewing last message
modePin = 28 #Pin(28, Pin.IN)
# message alert led
led = 29 #Pin(29, Pin.IN)
######################

# 26 pins required to get all letters, shift register / pin expander needed
pinLetterMapping = {
    "0": "A",
    "1": "B",
    "2": "C",
    "3": "D",
    "4": "E",
    "5": "F",
    "6": "G",
    "7": "H",
    "8": "I",
    "9": "J",
    "10": "K",
    "11": "L",
    "12": "M",
    "13": "N",
    "14": "O",
    "15": "P",
    "16": "Q",
    "17": "R",
    "18": "S",
    "19": "T",
    "20": "U",
    "21": "V",
    "22": "W",
    "23": "X",
    "24": "Y",
    "25": "Z"
}

# UPDATE AFTER WIRING EXPANDERS AND BUTTONS
# map numbers to physical pins
pinPhysicalMapping = {
    "0": "",
    "1": "",
    "2": "",
    "3": "",
    "4": "",
    "5": "",
    "6": "",
    "7": "",
    "8": "",
    "9": "",
    "10": "",
    "11": "",
    "12": "",
    "13": "",
    "14": "",
    "15": "",
    "16": "",
    "17": "",
    "18": "",
    "19": "",
    "20": "",
    "21": "",
    "22": "",
    "23": "",
    "24": "",
    "25": ""
}
###########################################################
#        Only viewLastMessage function is tested          #
###########################################################

def mainLoop(lcd, sock):
    text = ""
    
    _thread.start_new_thread(recvLoop, (sock, lcd))
    while True:
        if modePin.value() == 1:
            viewLastMessage(lcd)
            continue
        
        for i in range(0, 25, 1):
            # UPDATE AFTER WIRING EXPANDERS AND BUTTONS
            letterPin = Pin(int(pinPhysicalMapping[str(i)]), Pin.IN)
            if letterPin.value() == 1:
                letter = letter + pinLetterMapping[str(i)]
                
                lcd.clear()
                lcd.putstr(text)
        
        if enter.value() == 1:
            socketSend(text)

            text = ""

            break
        
        if delete.value() == 1:
            text = text[:-1]
            
            lcd.clear()
            lcd.putstr(text) 

def ledMessageAlert(ledPin):
    for i in range(0, 5, 1):
        ledPin.value(1)
        
        sleep(0.5)
        
        ledPin.value(0)
        
        sleep(0.5)
        
def viewLastMessage(lcd):
    dataFile = open("/data/last-message.txt", "r")
    data = dataFile.read()
    dataFile.close()
    
    lcd.clear()
    lcd.putstr(data)

# recvLoop runs in independend thread
def recvLoop(sock, lcd):
    while True:
        data = socketRecv(sock)
        
        lcd.clear()
        lcd.putstr(data)
        
        uasyncio.run(ledMessageAlert(led))
        
        dataFile = open("/data/last-message.txt", "w")
        dataFile.write(data)
        data.close()