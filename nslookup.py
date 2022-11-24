import socket


file =open ('dns.txt', 'r')
domain_list = []

for x in file.readlines():
    domain_list.append(x.rstrip())

for y in domain_list:
    try:
        print (socket.gethostbyname(y))
    except:
        print ("Unable to resolve")

