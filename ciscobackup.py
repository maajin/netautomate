
import time
import paramiko 
import datetime


now = datetime.datetime.now().replace(microsecond=0)

username = input('Please enter username:')
password = input('Please enter password:')


DEVICE_LIST = open ('D:\Python Scripts\subnets1.txt')
for RTR in DEVICE_LIST:
    RTR = RTR.strip()
    print ('\n #### Connecting to the device ' + RTR + '####\n' )
    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SESSION.connect(RTR,port=22,
                    username=username,
                    password=password,
                    look_for_keys=False,
                    allow_agent=False)

    DEVICE_ACCESS = SESSION.invoke_shell()
    DEVICE_ACCESS.send(b'terminal len 0\n')
    DEVICE_ACCESS.send(b'show run\n')

    time.sleep(5)
    output = DEVICE_ACCESS.recv(65000)
    filename = "%s_%.2i%.2i%i_%.2i%.2i%.2i" % (RTR,now.year,now.month,now.day,now.hour,now.minute,now.second)
    f1 = open(filename, 'a')
    f1.write(output.decode("utf-8") )
    f1.close()

    SESSION.close()

    print ('backup is successful!')
