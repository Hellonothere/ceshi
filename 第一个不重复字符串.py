strx=input()
if strx == "":
    print("None")
else:
    listx=list(strx)
    listy=[]
    for i in listx:
        if listx.count(i) == 1:
            listy.append(i)
    print("{}".format(listy[0]))