"""
Write a Python program to check,
 wheather a bracket is closed or not:

Input : "{([])}{}{()"
output : True/False 
"""

def bracket_check(inp):

    while True:
        res = inp.replace("()","").replace("{}","").replace("[]","")
        if inp == res:
            break
        inp = res

    return (inp=="")

ip = "{([])}{}{()"
print(bracket_check(ip))