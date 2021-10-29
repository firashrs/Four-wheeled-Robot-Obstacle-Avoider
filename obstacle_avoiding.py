import RPi.GPIO as GPIO          
from time import sleep
import time

low_speed = 30

#Left Motor Pins
R_in1 = 20
R_in2 = 16
R_en = 21


#Right Motor Pins
L_in1 = 27
L_in2 = 17
L_en = 22

 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins

#trans
GPIO_TRIGGER = 23

#receive
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
        
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 



GPIO.setmode(GPIO.BCM)

#Setup Left Motor
GPIO.setup(L_in1,GPIO.OUT)
GPIO.setup(L_in2,GPIO.OUT)
GPIO.setup(L_en,GPIO.OUT)

#Setup Right Motor
GPIO.setup(R_in1,GPIO.OUT)
GPIO.setup(R_in2,GPIO.OUT)
GPIO.setup(R_en,GPIO.OUT)

#Initialize Left Motor
GPIO.output(L_in1,GPIO.LOW)
GPIO.output(L_in2,GPIO.LOW)
#GPIO.output(L_en,GPIO.HIGH)

L_p=GPIO.PWM(L_en,1000)
L_p.start(100)

#Initialize Right Motor
GPIO.output(R_in1,GPIO.LOW)
GPIO.output(R_in2,GPIO.LOW)
#GPIO.output(R_en,GPIO.HIGH)

R_p=GPIO.PWM(R_en,1000)
R_p.start(100)
def forward():
    print("F O R W A R D")
    GPIO.output(L_in1,GPIO.HIGH)
    GPIO.output(L_in2,GPIO.LOW)
    L_p.start(100)
        
    GPIO.output(R_in1,GPIO.HIGH)
    GPIO.output(R_in2,GPIO.LOW)
    R_p.start(100)

def backward():
    print("B A C K W A R D")
    GPIO.output(L_in1,GPIO.LOW)
    GPIO.output(L_in2,GPIO.HIGH)
    L_p.start(100)
        
    GPIO.output(R_in1,GPIO.LOW)
    GPIO.output(R_in2,GPIO.HIGH)
    R_p.start(100)

def stopped():
    print("S T O P P E D")
    GPIO.output(L_in1,GPIO.LOW)
    GPIO.output(L_in2,GPIO.LOW)
    L_p.start(100)
    
    GPIO.output(R_in1,GPIO.LOW)
    GPIO.output(R_in2,GPIO.LOW)
    R_p.start(100)
    
def turn_left():
    print("L E F T")
    GPIO.output(L_in1,GPIO.HIGH)
    GPIO.output(L_in2,GPIO.LOW)
    L_p.start(low_speed)
    
    GPIO.output(R_in1,GPIO.HIGH)
    GPIO.output(R_in2,GPIO.LOW)
    R_p.start(100)

def turn_right():
    print("R I G H T")
    GPIO.output(L_in1,GPIO.HIGH)
    GPIO.output(L_in2,GPIO.LOW)
    R_p.start(100)
        
    GPIO.output(R_in1,GPIO.HIGH)
    GPIO.output(R_in2,GPIO.LOW)
    R_p.start(low_speed)


while(1):
    if distance() < 10:
        stopped()
        sleep(1) 
        backward()
        sleep(1)
        turn_left()
        sleep(2)
        stopped()
        sleep(1)
        turn_right()
        sleep(2)
        stopped()
        sleep(1)
        turn_right()
        sleep(2)
        stopped()
        sleep(1)
        turn_left()
        sleep(2)
        stopped()
        sleep(1)
    else:
        forward()
    sleep(0.5)
    
GPIO.cleanup()