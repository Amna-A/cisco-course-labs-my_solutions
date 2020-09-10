c0=int(input("enter a number: "))
steps=0
if c0 > 1:
    while c0!=1:
        if c0%2==0:
            c0/=2
        else:
            c0=3*c0+1

        steps+=1      
        print(int(c0))
    print("steps=",steps)
else:
    print("wrong c0 value")  