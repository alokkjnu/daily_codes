""" 
write a program to list out files from a directory
"""

import os

path = "/home/shivalok/Desktop/Daily Code/daily_codes"

def get_file_name(path):
    
    file_names = os.listdir(path)
    return file_names


print(get_file_name(path))