'''checks whether, the entered texts are anagrams and prints the result.
assume that two empty strings are not anagrams;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check - treat them as non-existent'''

t1=input("enter first text:")
t2=input("enter second text:")

t1.replace(" ","")
t2.replace(" ","")

t1=list(t1.upper())
t2=list(t2.upper())

t1.sort()
t2.sort()

if t1==t2:
    print("the two texts are anagrams")
else:
    print("the two texts are NOT anagrams")
