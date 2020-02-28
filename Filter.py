def fun(variable):
    letters=['a','e','i','o','u']
    if (variable in letters):
        return variable
# sequence
sequence=['w','a','r','e','i','k','o',]
# using filter function
filtered=filter(fun,sequence)
print("the filter items are")
for i in filtered:
    print (i)