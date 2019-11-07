import RPi.GPIO as GPIO
import time
f=open('t.txt','r')
l=f.readline()
a=[float(x) for x in l.split()]
print(a)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.OUT)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.OUT)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(23,GPIO.OUT)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35,GPIO.OUT)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)

lane_red=[11,15,19,23]
lane_green=[31,33,35,37]

GPIO.output(11,False)
GPIO.output(15,False)
GPIO.output(19,False)
GPIO.output(23,False)
GPIO.output(37,False)
GPIO.output(35,False)
GPIO.output(33,False)
GPIO.output(31,False)
GPIO.output(3,False)
GPIO.output(5,False)
GPIO.output(7,False)
GPIO.output(8,False)

def fun(x):
	for i in range(0,4):
		if(i==x):
			GPIO.output(lane_red[i],False)
		else:
			GPIO.output(lane_red[i],True)

for i in range(0,4):
	GPIO.output(lane_green[i],True)
	fun(i)
	time.sleep(a[i])
	GPIO.output(lane_green[i],False)
GPIO.cleanup()
