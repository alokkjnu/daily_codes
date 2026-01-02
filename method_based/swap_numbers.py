
a = 5
b = 7
def swap_number1(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b

print(swap_number1(a,b))

def swap_number2(a,b):
    a,b = b,a
    return a,b

print(swap_number2(a,b))


def swap_number3(a,b):
    c = a
    a = b
    b = c

    return a,b

print(swap_number3(a,b))