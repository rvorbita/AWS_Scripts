#create a python script that will print the
#file type of the PATH

import os 
import pprint

print("Enter the PATH")
req_path = input(": ")
print("Enter the Extension")
req_ext = input(": ")

dir_path = os.listdir(req_path)
#iterate to the dir_path to check if the extension exist 
#in the directory.
req_extension=[]

for i in dir_path:

    if req_ext in i:
        req_extension.append(i)


if len(req_extension) == 0:

    print("No file extension found on the directory")
else:
    
    print("Extension found on the directory")
    for j in req_extension:
        print(j)      