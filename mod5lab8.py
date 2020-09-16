'''Your task is to write a program which answers the following question: 
are the characters comprising the first string hidden inside the second string?
ex: string 1: "dog", string 2: "vcxzxduybfdsobywuefgas", output: yes
there are the letters d,o and g inside the second string'''

def finding_word(txt,n):
    
    for ch in n:
        if ch in txt: return "yes"
    return "no"


word = input("Enter the word you wish to find: ").upper()
text = input("Enter the string you wish to search through: ").upper()
print(finding_word(text,word))

