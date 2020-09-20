from collections import defaultdict

grades=input("enter the name of the file: ")
with open(grades,"r") as grade_file:
    list_of_name=[]
    list_of_point=[]
    for line in grade_file.readlines():
        lines=line.split()
        list_of_name+=(lines[0]+" "+lines[1]).split(",")
        list_of_point+=(lines[2]).split(",")
    list_of_point=[int(i) for i in list_of_point] #convert numbers to int type

#now we have filled two lists one with names another with points

    myDict=defaultdict(list)
    for name,pt in zip(list_of_name,list_of_point):
        myDict[name].append(pt)
    myDict=dict(myDict)

    res={}
    for i in myDict:
        res[i]=sum(myDict[i])

    #method:1 for sorting the dict
    #------------------------------
    # for key in sorted(res.keys()):
    #     new_dict=("%s: %s"%(key,res[key]))
    #     print(new_dict)
    
    #method:2 to sort the dict
    #--------------------------
    final_res=dict(sorted(res.items()))

    for keys,values in final_res.items():
        s1=len(max(final_res.keys(), key=len))
        s2=len(keys)
        space_size=" "*(s1-s2)+" "
        print(keys,space_size,values)
