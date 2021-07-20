import pandas as pd

df = pd.read_excel("D:\Python Scripts\subnets.xlsx", sheet_name=0)
# insert the name of the column as a string in brackets
list1 = list(df['Subnt']) 


NETWORKS = list1

ADDRESSES = input(' Please enter ip: ')

for ip in ADDRESSES:
    for net in NETWORKS:
        if ip in net:
            print('{}\nis on {}'.format(ip, net))
            break
    else:
        print('{}\nis not on a known network'.format(ip))
    print()
