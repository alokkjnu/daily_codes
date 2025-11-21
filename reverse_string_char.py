""" Write a program to reverse string char by char"""


def revere_str(s):

    res = ""
    for i in s:
        res = i +res

    return res


s = "Alok"
print(revere_str(s))