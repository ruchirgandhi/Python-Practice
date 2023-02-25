#

import zipfile
import shutil

# zip file
zipfile1 = zipfile.ZipFile("zip-file.zip","w")
zipfile1.write("document1.txt", compress_type=zipfile.ZIP_DEFLATED)
zipfile1.write("document2.txt", compress_type=zipfile.ZIP_DEFLATED)
zipfile1.close()


# uncompress

zip_obj = zipfile.ZipFile("zip-file.zip", "r")
zip_obj.extractall("extracted_content")


##

import shutil

path = "/Users/rucgandh/Desktop/Python/Practice/extracted_content"

output_filename = "example"

shutil.make_archive(output_filename,"zip", path)

shutil.unpack_archive('example.zip','final_unzip','zip')