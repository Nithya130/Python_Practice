#finding the bigger element in the list
n=int(input("Enter size:"))
l=[]
for i in range(n):
    element=input("enter something:")
    l.append(element)
print ("*"*20)
#print ("The list is:",l)
big=l[0]
#print (big)
for i in range(1,len(l)):

    if big<l[i]:
       big=l[i]
print ("biggest element is:",big)