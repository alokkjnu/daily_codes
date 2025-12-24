import copy
a = [1,2,34,4,5,6,23]
b = copy.copy(a)

b[0] = 10
print(a)
print(b)



a = [1,2,34,4,5,6,00]
b = copy.deepcopy(a)

b[0] = 55
print(a)
print(b)


