

import re

file = open('config_file.txt','r')
lines = file.readlines()
ip_add = []

for line in lines:
    output = re.search(r"\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b",line)
    if output is not None:
        output = output.group()
        ip_add.append(output)


for ip in ip_add:
    print("Valid IP address is {}".format(ip))

