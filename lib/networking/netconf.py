import network
from machine import Pin

def isAp():
    # Uncomment these lines after wiring both pins
    # selectButton = Pin(14, Pin.IN)
    # confirmButton = Pin(12, Pin.IN)

    ssid = "comms"
    password = "komunikace be like"

    global isAccessPoint

    isSelecting = True
    while isSelecting:
        
        # Comment these lines and uncomment other two lines after wiring pin 14 and 12
        selectValue = 1
        confirmValue = 1
        # selectValue = selectButton.value()
        # confirmValue = confirmButton.value()
        
        if confirmValue == 1:
            if selectValue == 1:
                isAccessPoint = True
                break
            else:
                isAccessPoint = False
                break

    # Different settings for each mode
    if isAccessPoint:
        ap = network.WLAN(network.AP_IF)
        ap.config(authmode=3, essid=ssid, password=password)
        ap.active(True)
        ap.ifconfig(["192.168.0.69", "255.255.255.0", "192.168.0.69", "127.0.0.1"])
    else:
        sta = network.WLAN(network.STA_IF)
        sta.connect(ssid, password)
        sta.active(True)
        sta.ifconfig(["192.168.0.22", "255.255.255.0", "192.168.0.69", "127.0.0.1"])
        
    return isAccessPoint