"""What is a value repeated maximum number of times?"""
l = [9,4,2,1,9,7,8,3,5,9,1,9,6]

def max_repeated_num(l):
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    res = max(d)
    return res
    
print(max_repeated_num(l))