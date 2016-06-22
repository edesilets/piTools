#!/usr/bin/env python  
# coding=utf-8  
import os  
import time
# At First we have to get the current CPU-Temperature with this defined function  
def getCPUtemperature():  
 res = os.popen('cat /sys/class/thermal/thermal_zone0/temp').readline()  
 math = float(res)/1000
 return math

# At First we have to get the current GPU-Temperature with this defined function  
def getGPUtemperature():  
 res = os.popen('vcgencmd measure_temp').readline()  
 return(res.replace("temp=","").replace("'C\n",""))

# Now we convert our value into a float number  
tempCpu = float(getCPUtemperature())
tempGpu = float(getGPUtemperature())

#print "GPU"
#print tempGpu
#print "CPU"
#print tempCpu

def sendmqttGpuC(temperature):
 passthis = str(temperature)
 run = os.system('mosquitto_pub -h node -t /home/computerRoom/PI2/thermometer/gpu/C -m ' + passthis)
 #print "mqttsend GPU in Celsius"
 return

def sendmqttCpuC(temperature):
 passthis = str(temperature)
 run = os.system('mosquitto_pub -h node -t /home/computerRoom/PI2/thermometer/cpu/C -m ' + passthis)
 #print "mqttsend CPU in Celsius "
 return

def sendmqttCpuF(temperature):
 this = (temperature*1.8)+32
 passthis = str(this)
 run = os.system('mosquitto_pub -h node -t /home/computerRoom/PI2/thermometer/cpu/F -m ' + passthis)
 #print "mqttsend CPU in Fahrenheit"
 return

def sendmqttGpuF(temperature):
 this = (temperature*1.8)+32
 passthis = str(this)
 run = os.system('mosquitto_pub -h node -t /home/computerRoom/PI2/thermometer/gpu/F -m ' + passthis)
 #print "mqttsend GPU in Fahrenheit"
 return

infinite = 1
while (infinite == 1):
# sendmqttGpuC(tempGpu)
# sendmqttCpuC(tempCpu)
 sendmqttGpuF(tempCpu)
 sendmqttCpuF(tempGpu)
 time.sleep(1);
# infinite = infinite + 1
#else:
# print "its dead"
