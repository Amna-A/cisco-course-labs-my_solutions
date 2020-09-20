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
            alpha.append(ch.upper())
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
    


for keys,values in my_dict.items():
    print(keys,"->", values)