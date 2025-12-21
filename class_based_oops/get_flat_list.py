"""
Write a python program to get flat list from a nested list.
input: _list = [1, 2,[3], 4, 5,[6, 7]]
output: [1, 2, 3, 4, 5, 6, 7] 
"""

class GetFlat:

    def __init__(self,inp):

        self.inp = inp

    def get_flat_list(self):

        try:
            res = []
            for i in self.inp:
                if type(i) == list:
                    for j in i:
                        res.append(j)

                else:

                    res.append(i)
            return res

        except Exception as e:
            return (str(e))

if __name__=="__main__":

    inp = [1, 2,[3], 4, 5,[6, 7]]

    cls_obj = GetFlat(inp)
    res = cls_obj.get_flat_list()

    print(res)

