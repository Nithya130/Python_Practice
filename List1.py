# add values to list
aList=[]
for number in range(1,11):
    aList.append(number)
print("The value of aListis:", aList)
# access list values by iteration
print("\nAccessing values by iteration:")

for item in aList:
    print(item, end=" ")
    print()

# access list values by index
print("\nAccessing values by index:")
print("Subscript   Value")
for i in range( len( aList) ):
    print("%9d %7d"% ( i, aList[ i] ))

# modify list
print("\nModifyinga list value...")
print("Value of aListbefore modification:", aList)
aList[0] = -100
aList[ -3] =19
print("Value of aListafter modification:", aList)
