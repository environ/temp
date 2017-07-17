import os
import glob
import time
import urllib2,json
import requests
import time

 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'

# defineeri andurid

device1_folder = base_dir + '/10-000802cc01ce'
device1_file = device1_folder + '/w1_slave'


device2_folder = base_dir + '/10-0008028ccd4a'
device2_file = device2_folder + '/w1_slave'

###############################################


# esimene andur

 
def read_temp1_raw():
    f = open(device1_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp1():
    lines = read_temp1_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp1_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        
        return temp_c

# teine andur


def read_temp2_raw():
    f = open(device2_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp2():
    lines = read_temp2_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp2_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0

        return temp_c


# saada serverile
	
while True:
	r = requests.get('http://192.168.1.251/input/post.json?node=101&json={t_kuur:'+str(read_temp1())+'}&apikey=INSERT_API_KEY')
        r = requests.get('http://192.168.1.251/input/post.json?node=101&json={t_sahver:'+str(read_temp2())+'}&apikey=INSERT_API_KEY')

#	print(read_temp1())
#       print(read_temp2())
	
	time.sleep(60)