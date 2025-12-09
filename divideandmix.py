# Given the word:
# HelloWorld
# Divide it into two equal halves:
# Hello
# World
# Then mix both halves in such a way that the final output becomes:
# odlllreoHW

# Write a Python program to do this.


def divideandmix(inp):
    inp_len = len(inp)
    mid = inp_len//2
    first_str = inp[:mid]
    last_str = inp[mid:]
    first_str = reverse_str(first_str)
    last_str = reverse_str(last_str)
    res= ""
    for i in range(len(first_str)):
        res = res+first_str[i]
        res = res+last_str[i]

    return res
def reverse_str(inp):
    res = ""
    for i in inp:
        res = i+res
    return res


print(divideandmix("HelloWorld"))