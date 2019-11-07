import RPi.GPIO as GPIO
import time
f=open('a.txt','r')
l=f.readline()
a=[float(x) for x in l.split()]
#print(a)
a=[int(x) for x in a] # Or floor it to get an integer
print(a)
lane_green=[31,33,35,37]
lane_red=[11,15,19,23]

GPIO.setwarnings(False)
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

def lights_off():
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

def set_lights(i,t):
	lights_off()
	GPIO.output(lane_green[i],True)
	for x in range(0,4):
                if(x!=i):
                        GPIO.output(lane_red[x],True)
                else:
                        GPIO.output(lane_red[x],False)

	time.sleep(t)

set_lights(a[0],a[1])
lights_off()


