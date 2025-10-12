import os

#first create images directory and keep some image/icon files here
path = "file_rename/images" 
list = os.listdir(path) #all files of the directory

print(f"Before renaming:\n {list}")
i = 1

for file in list:
    ext = file.split(".")[1]
    os.rename(f"{path}/{file}",f"{path}/{i}.{ext}") #rename with original file extension
    i+=1

list = os.listdir(path)
print(f"After renaming:\n {list}")


