
#input: Alok Kumar Maurya

#output: "Maurya Kumar Alok"



def reverse_string(sr):
    res = ""
    st = ""
    for i in s:
        if i == " ":
            res = st+" "+res
            st = ""

        else:
            st += i
    res = st+ " " +res
    
    return res

    
s = "Alok Kumar Maurya"

print(reverse_string(s))



def reverse_string1(sr):
    sr = sr.split(" ")
    res =""
    for i in sr:
        res  = i +" "+res
    return res

s = "Alok Kumar Maurya"

print(reverse_string1(s))