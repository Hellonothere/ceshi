with open("in.txt","r") as f:
    f=f.readlines()
print(f)
list1=[]
dict1={}
for i in f:
    i=i.split(" ")
    for x in i:
        if x in list1:
            dict1[x]=dict1[x]+1
        else:
            list1.append(x)
            dict1[x]=1
list2=[]
for i in dict1.items():
    list2.append(i)
list2.sort(key=lambda x: (-x[1],x[0]))
with open("out.txt","w") as f:
    for x in list2:
        f.write("{} {}\n".format(x[0],x[1]))
print("hello")