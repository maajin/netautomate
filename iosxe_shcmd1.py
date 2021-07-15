from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

USERNAME = input('Input Username: ')
PASSWORD = getpass()

starttime = datetime.now()
print('Startime: ', starttime)

with open('device1.txt') as DEVICE_LIST:
	for DEVICE in DEVICE_LIST:
		RTR = {
    	  'device_type': 'cisco_xe',
    	  'ip' : DEVICE,
    		'username' : USERNAME,
    		'password' : PASSWORD,
    	}
		print('#'*80 + '\n')
		print('Connectig to device: ' + DEVICE)
		net_connect = ConnectHandler(**RTR)


		with open('commands.txt') as COMMANDS:
			output = ''
			for CMD in COMMANDS:
				output += CMD + net_connect.send_command(CMD) + '\n' + '+'*80 + '\n'

			print(output)
		

file = open()
		
endtime = datetime.now() - starttime
print('Total execution time: ', endtime)