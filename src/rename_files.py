import os
from string import digits

def rename_files():
    #get file name from folder
    file_list = os.listdir(r"C:\Users\ltbul\OneDrive\Desktop\prank\prank")
    print(file_list)
    path = os.getcwd()
    print("Current dir",path)
    os.chdir(r"C:\Users\ltbul\OneDrive\Desktop\prank\prank")
    
    #for each file, rename file name
    for file_name in file_list:

        remove_digits = str.maketrans('','',digits)
        new_name = file_name.translate(remove_digits)
        os.rename(file_name, new_name)

    os.chdir(path)

rename_files()
