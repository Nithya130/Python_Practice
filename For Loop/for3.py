#reversing the given string
st=input("Enter the string:")
temp=""
for i in range(len(st)-1,-1,-1):#range(5,-1,-1)
#st[5]="a",st[4]="y".....
    temp=temp+st[i]
print (temp)