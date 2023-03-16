l=input()     
t=l.split()
t[0]=int(t[0])
t[1]=int(t[1])
t[2]=int(t[2])
bombs=['.' for x in range(t[1]) for y in range(t[0])]
arr1=[[0 for x in range(t[1])] for y in range(t[0])]
arr2=[[0 for x in range(t[1])] for y in range(t[0])]
for i in range(0,t[0]):
    bombs[i]=input() 
    for j in range(0,t[1]):
        if(bombs[i][j]=='O'):
            arr1[i][j]=3
            arr2[i][j]=1
        else:
            arr1[i][j]=0
            arr2[i][j]=3


arr3=[[-1 for x in range(t[1])] for y in range(t[0])]
arr4=[[-1 for x in range(t[1])] for y in range(t[0])]
arr5=[[-1 for x in range(t[1])] for y in range(t[0])]
arr6=[[-1 for x in range(t[1])] for y in range(t[0])]

r=t[0]
c=t[1]

for i in range(r):
    for j in range(c):
        temp=arr2[i][j]
        if(temp==1):
            arr3[i][j]=0
            arr4[i][j]=3
            if(i-1>=0):
                arr3[i-1][j]=0
                arr4[i-1][j]=3
            if(j-1>=0):
                arr3[i][j-1]=0
                arr4[i][j-1]=3
            if(i+1<r):
                arr3[i+1][j]=0
                arr4[i+1][j]=3
            if(j+1<c):
                arr3[i][j+1]=0
                arr4[i][j+1]=3
        elif(temp==3):
            if(arr3[i][j]!=0):
                arr3[i][j]=2
                arr4[i][j]=1

for i in range(r):
    for j in range(c):
        temp=arr4[i][j]
        if(temp==1):
            arr5[i][j]=0
            arr6[i][j]=3
            if(i-1>=0):
                arr5[i-1][j]=0
                arr6[i-1][j]=3
            if(j-1>=0):
                arr5[i][j-1]=0
                arr6[i][j-1]=3
            if(i+1<r):
                arr5[i+1][j]=0
                arr6[i+1][j]=3
            if(j+1<c):
                arr5[i][j+1]=0
                arr6[i][j+1]=3
        elif(temp==3):
            if(arr5[i][j]!=0):
                arr5[i][j]=2
                arr6[i][j]=1
n=t[2]
if(n==1):
    res=arr1
elif(n==2):
    res=arr2
else:
    n-=2
    n=n%4
    if(n==1):
        res=arr3
    elif(n==2):
        res=arr4
    elif(n==3):
        res=arr5
    elif(n==0):
        res=arr6

for i in range(r):
    res_str=""
    for j in range(c):
        if(res[i][j]==0):
            res_str+='.'
        else:
            res_str+='O'
    print(res_str)