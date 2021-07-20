
import pandas as pd
import ipaddress

df = pd.read_excel("./subnets.xlsx", sheet_name=0)
list1 = list(df['Subnt']) 
tmp = input(' Please enter ip: ')

try:
        ADDRESSES = ipaddress.ip_address(tmp)
        for item in list1:
                val = ipaddress.ip_address(tmp) in ipaddress.ip_network(item)
                if val == True:
                        print(f'\nIP: {ADDRESSES} found on subnet -> {item}')
                        break
        else:
                print(f'\nIP: {ADDRESSES} NOT found in any subnet.')
except Exception as e:
        print(f'Error -> {str(e)}')
