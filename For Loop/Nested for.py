n=int(input("enter n:"))
m=int(input("enter m:"))
for i in range(n,m+1):
    flag=True
    for j in range(2,i):
        if i%2==0:
            flag=False
    if flag:
        print ("prime num in between given range is:",i)