#coding:utf-8

import RPi.GPIO
 as GPIO
import time

#サーボの設定
# BOARDでpinで指定
GPIO.setmode(GPIO.BOARD)

# PIN12を制御パルスの出力に設定
gp_out = 12
GPIO.setup(gp_out, GPIO.OUT)

servo = GPIO.PWM(gp_out, 50)
servo.start(0)

def trun():

    GPIO.setup(gp_out, GPIO.OUT)
    time.sleep(0.5)

    servo.ChangeDutyCycle(7.25)
    time.sleep(0.5)

    servo.ChangeDutyCycle(5.5)
    time.sleep(0.5)

    servo.ChangeDutyCycle(7.25)
    time.sleep(0.5)

    GPIO.cleanup(gp_out)
