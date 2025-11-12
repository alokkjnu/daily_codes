s = "Alok Kumar Maurya"

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

print(reverse_string(s))

