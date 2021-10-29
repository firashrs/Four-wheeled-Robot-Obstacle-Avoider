import RPi.GPIO as GPIO          
from time import sleep

#Left Motor Pins
L_in1 = 16
L_in2 = 20
L_en = 21


#Left Motor Pins
#L_in1 = 23
#L_in2 = 24
#L_en = 25

#Right Motor Pins
R_in1 = 27
R_in2 = 17
R_en = 22

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
GPIO.output(L_en,GPIO.HIGH)


#Initialize Right Motor
GPIO.output(R_in1,GPIO.LOW)
GPIO.output(R_in2,GPIO.LOW)
GPIO.output(R_en,GPIO.HIGH)

#p=GPIO.PWM(en,1000)
#p.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):
    sleep(3)
    print("F O R W A R D")
    GPIO.output(L_in1,GPIO.HIGH)
    GPIO.output(L_in2,GPIO.LOW)
    
    GPIO.output(R_in1,GPIO.HIGH)
    GPIO.output(R_in2,GPIO.LOW)
    sleep(5)
    
    print("S T O P P E D")
    GPIO.output(L_in1,GPIO.LOW)
    GPIO.output(L_in2,GPIO.LOW)
    
    GPIO.output(R_in1,GPIO.LOW)
    GPIO.output(R_in2,GPIO.LOW)
    sleep(3)
    
    print("B A C K W A R D")
    GPIO.output(L_in1,GPIO.LOW)
    GPIO.output(L_in2,GPIO.HIGH)
    
    GPIO.output(R_in1,GPIO.LOW)
    GPIO.output(R_in2,GPIO.HIGH)
    sleep(5)
    
    
    print("S T O P P E D")
    GPIO.output(L_in1,GPIO.LOW)
    GPIO.output(L_in2,GPIO.LOW)
    
    GPIO.output(R_in1,GPIO.LOW)
    GPIO.output(R_in2,GPIO.LOW)
    sleep(3)