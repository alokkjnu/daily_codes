"""
Write a python program to get flat list,
from nested list using list comprehension.

input: _list = [1, 2,[3], 4, 5,[6, 7]]
output: [1, 2, 3, 4, 5, 6, 7] 
"""

class GetFlat:

    def __init__(self,inp_list):

        self.inp_list = inp_list

    def get_flat_list(self):

        list_a = self.inp_list

        flat_list = [

            item
            for subitem in list_a
            for item in (subitem if isinstance(subitem,list) else [subitem])

        ]

        return flat_list


if __name__ == "__main__":

    inp = [1, 2,[3], 4, 5,[6, 7]]
    class_obj = GetFlat(inp)
    res = class_obj.get_flat_list()
    print(res)