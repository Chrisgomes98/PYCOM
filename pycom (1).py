import pycom
import time
import machine
from machine import Pin
from network import LoRa
import socket

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868,frequency= 867000000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
print("start")

def parking_system():
    while True:
        pin1 = Pin('P12', mode=Pin.IN, pull=Pin.PULL_UP)
        pin2 = Pin('P11', mode=Pin.IN, pull=Pin.PULL_UP)
        pin3 = Pin('P10', mode=Pin.IN, pull=Pin.PULL_UP)
        pin4 = Pin('P2', mode=Pin.IN, pull=Pin.PULL_UP)
        pin5 = Pin('P3', mode=Pin.IN, pull=Pin.PULL_UP)
        pin6 = Pin('P4', mode=Pin.IN, pull=Pin.PULL_UP)
        data=str(pin1())+str(pin2())+str(pin3())+str(pin4())+str(pin5())+str(pin6())
        print("sending the data")
        print(type(data))
        print(data)
        s.setblocking(True)
        s.send(data.encode())
        time.sleep(1)

def main():
    parking_system()

if __name__=="__main__":
    main()
