"""
Write a Python program to sort the following
list of dictionaries by the key name:

users = [
    {"name": "Alok", "age": 25},
    {"name": "Rahul", "age": 30},
    {"name": "Priya", "age": 28}
]
"""

class SortList:

    def __init__(self,inp):

        self.inp = inp

    def sort_list(self):

        self.inp.sort(key = lambda x:x['name'])

        return self.inp
    

if __name__ == "__main__":

    users = [
    {"name": "Alok", "age": 25},
    {"name": "Rahul", "age": 30},
    {"name": "Priya", "age": 28}
]   
    cls_obj = SortList(users)
    res = cls_obj.sort_list()
    print(res)