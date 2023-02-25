
"""
f = open("opening_file_prac.txt", "w+")
f.write("MY NAME IS SAMMY")
f.close()

"""



import os

print(os.getcwd())

print(os.listdir("/Users/rucgandh/Desktop/Python"))

import shutil

# Move file from one Dir to other

shutil.move("opening_file_prac.txt","/Users/rucgandh/Desktop/")

# Move file back

shutil.move("/Users/rucgandh/Desktop/opening_file_prac.txt","/Users/rucgandh/Desktop/Python/Practice")


for folders, subfolders, files in os.walk("/Users/rucgandh/Desktop/Python/Practice"):

    print(f"\t These are folders in {folders}")


    for subfold in subfolders:
        print(f"\t these are subfolders in {subfold}")
    print("\n")

    for f in files:
        print(f"\t these are files in {f}")
    print("\n")

