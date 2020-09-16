'''program find if a word is a palindrome, and prints result.
- assume that an empty string isn't a palindrome;
- treat upper- and lower-case letters as equal;
- spaces are not taken into account during the check - treat them as non-existent'''

word=input("please enter a word:")
#not_palindrome = ''
word.replace(" ","")
if len(word)>1 and word.upper()==word[::-1].upper(): #check if string = reverse string
    print("the word is palindrome")
else:
    print("the word is NOT palindrome")
