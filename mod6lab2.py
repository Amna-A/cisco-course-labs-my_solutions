'''the output histogram will be sorted based on the characters' 
frequency (the bigger counter should be presented first)
the histogram should be sent to a file with the same name as the input one, 
but with the suffix '.hist' (it should be concatenated to the original name)'''

from os import strerror
import errno

user_file=input("enter file name:")

try:
    counter=0
    alpha=[]
    my_dict={}

    fi=open(user_file, "r")
    content=fi.read()
    

    for ch in content:
        counter+=1
        if ch.isalpha():
            alpha.append(ch.lower())
            alpha=sorted(alpha)
    #x=alpha.count()
    
    for i in alpha:
        my_dict[i]=alpha.count(i)
    #print(my_dict)
            
   
        
except IOError as e:
    print("oh no !...I/O error occured", strerror(e.errno))
    exit(e.errno)
finally:
    fi.close()
#----------------hist file-------------------------------------------
new_dict=sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
new_dict=dict(new_dict)
list_of_strings=[f'{key}:{new_dict[key]}' for key in new_dict]

try:
    with open("kimchi.hist","w") as new_file:
        [new_file.write(f'{s}\n') for s in list_of_strings]
except IOError:
    print("cannot creat new file")


