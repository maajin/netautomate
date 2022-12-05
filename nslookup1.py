import csv
import socket

# read the file with the list of URLs and IPs
with open('urls_and_ips.txt', 'r') as file:
    # store the URLs and IPs in a list
    urls_and_ips = file.readlines()

# create a CSV file for the nslookup results
with open('nslookup_results.csv', 'w') as csvfile:
    # create a writer object for the CSV file
    writer = csv.writer(csvfile)
    
    # write the header row for the CSV file
    writer.writerow(['URL/IP', 'Result'])

    # loop through the URLs and IPs
    for url_or_ip in urls_and_ips:
        try:
            # perform the nslookup
            result = socket.gethostbyname(url_or_ip)
        except socket.gaierror:
            # handle any errors that occur during the nslookup
            result = 'Unable to perform nslookup'
        
        # write the URL/IP and the nslookup result to the CSV file
        writer.writerow([url_or_ip, result])
