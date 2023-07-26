a  =  input()
b  =  input()
la  =  len(a)
lb  =  len(b)
res  =  [[0 for i in range(lb+1)] for i in range(la+1)]
print(res)
lc  =  []
mmax  =  0
for  i  in  range(1,  la+1):
    for  j  in  range(1,  lb+1):
        if  a[i-1]  ==  b[j-1]:
            res[i][j]  =  res[i-1][j-1]  +  1
            if(res[i][j]>mmax):
                mmax  =  res[i][j]
                        
print(mmax)