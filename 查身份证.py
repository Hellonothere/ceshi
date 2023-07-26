identity=input()
dict1={0:7,1:9,2:10,3:5,4:8,5:4,6:2,7:1,8:6,9:3,10:7,11:9,12:10,13:5,14:8,15:4,16:2}
dict2={0:"1",1:"0",2:"X",3:"9",4:"8",5:"7",6:"6",7:"5",8:"4",9:"3",10:"2"}
if len(identity)!=18:
    print("Error")
else:
    listi=list(identity)
    listx=[]
    for i in range(17):
        x=int(listi[i])*dict1[i]
        listx.append(x)
    yz=sum(listx)%11
    if dict2[yz]==listi[17]:
        print("Correct")
    else:
        print("Wrong")