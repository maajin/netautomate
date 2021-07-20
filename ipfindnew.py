import openpyxl
import ipaddress

path = "D:\Python Scripts\subnets.xlsx"
 
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

ADDRESSES = input(' Please enter ip: ')

for ip in ADDRESSES:
    for net in sheet_obj:
        if ip in net:
            print('{}\nis on {}'.format(ip, net))
            break
    else:
        print('{}\nis not on a known network'.format(ip))
    print()