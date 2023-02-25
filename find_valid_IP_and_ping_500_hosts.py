import os
import ipaddress
import re


a = "config_file1.txt"

def find_ip(a):
    with open(a,"r") as file:
        output = file.read()
        output = output.split()
        print(output)

        result = []
        for each in output:

            """
            
            regex = re.search(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}",each)
            print(regex)

            if regex is not None:
                res = regex.group()
                print(res)
                result.append(res)

            """
            regex = re.search(r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$",each)

            if regex is not None:
                res = regex.group()
                print(res)
                result.append(res)


            for i in range(0,1):

                ip_addr = ipaddress.IPv4Address(res)+i

                ping = os.popen(f"ping {ip_addr} -c 2").read()
                print(ping)

                if "Request timeout" in ping:
                    f = open("IP4.txt", "a")
                    f.write(str(ip_addr) + "\t" + "DOWN" + "\n")
                    f.close()
                elif "Destination unreachable" in ping:
                    f = open("IP4.txt","a")
                    f.write(str(ip_addr) + "\t" + "DOWN" + "\n")
                    f.close()
                else:
                    f = open("IP4.txt","a")
                    f.write(str(ip_addr) + "\t" + "UP" + "\n")
                    f.close()


    return "number of valid IP addresses are ",result


print(find_ip(a))


