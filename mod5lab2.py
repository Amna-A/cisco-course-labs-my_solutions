''' a function that behaves like the split() method'''

def mysplit(strng):
    new_list=[]
    temp=""

    if strng.isspace():
        return new_list
    
    for ch in strng: 
        if ch!=" ":
            temp+=ch
        else:
            new_list.append(temp)
            temp=""
    no_space_final_list = [item for item in new_list if not item == ""] 
    return no_space_final_list

print(mysplit("To be or not to be, this is a question"))
print(mysplit("To be or not to be,this is a question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

