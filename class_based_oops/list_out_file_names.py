""" 
Write a Python program to list out all the files from a directory.
"""

import os

class GetFiles:

    def __init__(self,inp_path):

        self.inp_path=inp_path

    def get_files_list(self):

        try:

            files_name = os.listdir(self.inp_path)

            return files_name
        except Exception as e:
            return "Files does not exists at this path"

if __name__ == "__main__":

    inp_path = "/home/shivalok/Desktop/Daily Code/daily_codes/class_based_oops"
    class_ob = GetFiles(inp_path)
    get_files_name = class_ob.get_files_list()

    print(get_files_name)

