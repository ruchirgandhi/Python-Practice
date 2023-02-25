import re

with open("config_file.txt", "r") as f:
    output = f.read()
    output = output.split()
    print(output)
    f.close()

regex = "^(((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1[0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))$"

#regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

# list = re.findall(r"[0-9]|[10-99]|[100-199]|[200-255]\.[0-9][10-99][100-199][200-255]\.[0-9][10-99][100-199][200-255]\.[0-9][10-99][100-199][200-255]", output)

# list = re.findall(r"([0-9]|[10-99]|[100-199]|[200-255]\.){3}[0-9]|[10-99]|[100-199]|[200-255]", output)
for each in output:

	list = re.findall(regex,each)
	if len(list) > 0:

		print(list[0][0])


