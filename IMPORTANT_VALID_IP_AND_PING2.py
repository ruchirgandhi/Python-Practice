

import os
import ipaddress
import re


a = "config_file1.txt"


def find_ip(a):
    with open(a) as file:
        output = file.read()
        output = output.split()
        file.close()
        print(output)
        #return (output)

        result = []
        for each in output:
            regex = re.search(r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)",each)

            if regex is not None:
                res = regex.group()
                print("Valid IP Address is {}".format(res))
                result.append(res)
                ping = os.popen(f" ping {res} -c 2").read()

                if "Request timeout" in ping:
                    print(ping)
                    f = open("IP3.txt","a")
                    f.write(str(res) + "\t" + "DOWN" + "\n")
                    f.close()

                elif "Destination unreachable" in ping:
                    f = open("IP3.txt","a")
                    f.write(str(res) + "\t" + "DOWN" + "\n")
                    f.close()
                else:
                    f = open("IP3.txt","a")
                    f.write(str(res) + "\t" + "UP" + "\n")
                    f.close()

        for num in result:
            for i in range(0,100):

                ip = ipaddress.IPv4Address(num)+i
                print(ip)
                ping1 = os.popen(f"ping {ip} -c 2").read()
                if "Request timeout" in ping:
                    print(ping)
                    f = open("IP3.txt","a")
                    f.write(str(ip) + "\t" + "DOWN" + "\n")
                    f.close()

                elif "Destination unreachable" in ping:
                    f = open("IP3.txt","a")
                    f.write(str(ip) + "\t" + "DOWN" + "\n")
                    f.close()
                else:
                    f = open("IP3.txt","a")
                    f.write(str(ip) + "\t" + "UP" + "\n")
                    f.close()

    return (result)

print(find_ip(a))
