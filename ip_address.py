import re
 
a = "config_file.txt"



def return_ip(a):
  file1 = open('config_file.txt', 'r')
  #Lines = file1.readlines()
  Lines = file1.read()
  Lines = Lines.split()
  print(Lines)
  ip_list=[]
  for line in Lines:
    #250-255 or 200-249 or 100-199 or 10-99 or 0-9
    #output = re.search(r'\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b',line)
    output = re.search(r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])',
      line)
    output = re.search(r'([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])',
      line)
    if output is not None:
      ip_addr = output.group()
      ip_list.append(ip_addr)
 
  return ip_list
 
ip_List = return_ip(a)
for ip in ip_List:
  print("Valid ipv4 addr : {0} \n".format(ip))
