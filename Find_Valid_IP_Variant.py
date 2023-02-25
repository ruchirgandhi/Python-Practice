

import os
import ipaddress


## Opening file and parse it
with open("IPaddress.txt","r") as file:
    dump = file.read()
    #print(dump)
    dump = dump.splitlines()
    print(dump)

# find only Valid IP addresses and nothing else








result = []
for j in range(1,500):
    x = ipaddress.IPv4Address(u"10.10.10.1")+j
    result.append(str(x))

print(result)

for i in result:
    ip =i.split()[0]
    ping= os.popen(f"ping {ip} -c 2").read()

    if "Request timeout" in ping:
        print(ping)
        f = open("IP2.txt", "a")
        f.write(str(ip) + "\t" + 'down' + "\n")
        f.close()

    elif "Destination host unreachable" in ping:
        print(ping)
        f = open("IP2.txt", "a")
        f.write(str(ip) + "\t" + 'down' + "\n")
        f.close()
    else:
        print(ping)
        f = open("IP2.txt", "a")
        f.write(str(ip) + "\t" + 'up' + "\n")
        f.close()

with open("IP2.txt") as file:
    output = file.read()

print(output)

with open("IP2.txt", "w"):
    pass

input("Press any key to quit")

for i in dump:
    ip = i.split()[1]
    print(ip)
    host = i.split()[0]
    print(host)

    res = os.popen(f"ping {ip} -c 2").read()
    print("res is {}".format(res))

    if "Request timeout" in res:
        print(res)
        f = open("IP1.txt", "a")
        f.write(str(host) + "\t" + str(ip) + "\t" + 'down' + "\n")
        f.close()

    elif "Destination host unreachable" in res:
        print(res)
        f = open("IP1.txt", "a")
        f.write(str(host) + "\t" + str(ip) + "\t" + 'down' + "\n")
        f.close()
    else:
        print(res)
        f = open("IP1.txt", "a")
        f.write(str(host) + "\t" + str(ip) + "\t" + 'up' + "\n")
        f.close()

with open("IP1.txt") as file:
    output = file.read()

print(output)

with open("IP1.txt", "w"):
    pass

input("Press any key to quit")









