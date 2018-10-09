#coding: utf-8
import smbus

global switch_status
global room_status

switch_status = 15
room_status = 100

bus = smbus.SMBus(1)

addr = 0x23 #内側
addr1 = 0x5c #外側 #ADDR Vcc in

def get_lux():
    lux = bus.read_i2c_block_data(addr,0x10)
    lux1 = bus.read_i2c_block_data(addr1,0x10)

    switch = round(((lux[0]*256+lux[1])/1.2),1)
    room = round(((lux1[0]*256+lux1[1])/1.2),1)

    print ("電源:"+ str(switch))
    print ("部屋:"+ str(room))

    return switch,room
