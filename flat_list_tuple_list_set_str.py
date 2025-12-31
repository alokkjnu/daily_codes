"""
Write a python program:
1. include all datasets
2. get flat flat list.
3. split string and store individual
    in list
"""

sl = [[1,2,3],(4,5,6),{"AD","BF","CE"},7,8]

def get_flat(sl):
    a = []

    for i in sl:
        if type(i) == list or type(i) == set or type(i) == tuple:
            for j in i:
                if type(j) == str:
                    for n in j:
                        a.append(n)
                else:
                    a.append(j)
        else:
            a.append(i)
    return a


print(get_flat(sl))
