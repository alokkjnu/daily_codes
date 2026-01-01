"""
Write a python program get flat list:
1. include all datasets
2. get flat flat list.
3. split string and store individual
    in list
"""

class FlatNestedList:

    def __init__(self,inp):

        self.inp = inp

    def get_flat_list(self):

        res = []

        for i in self.inp:
            if  type(i) == list or type(i) == set or type(i) == tuple:
                for j in i:
                    if type(j) == str:
                        for k in j:
                            res.append(k)
                    else:
                        res.append(j)
            else:
                res.append(i)

        return res


if __name__ == "__main__":

    inp = [[1,2,3],(4,5,6),{"AD","BF","CE"},7,8]
    cls_obj = FlatNestedList(inp)
    res = cls_obj.get_flat_list()
    print(res)