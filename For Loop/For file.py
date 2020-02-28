#finding given num is prime oe not
n=int(input("Enter value of n:"))
flag=True
for i in range(2,n):
    if n%i==0:
        flag=False
if flag:
    print("prime num:",n)
else:
    print(n,"is not a prime")