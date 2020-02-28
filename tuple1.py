#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
aTuple=(1,"apple",2,5,"banana","cherry")
print("tuple:",aTuple)
#print the 4th item in the tuple
print (aTuple[5])
#negative index
print(aTuple[-2])
#Return the third, fourth, and fifth item:
print(aTuple[2:5])
print(aTuple[-4:-1])
for i in aTuple:
    print (i)
print (len(aTuple))