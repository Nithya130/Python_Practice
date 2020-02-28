from functools import reduce

my_list=[1,2,3,4,5,6,8,10,14]
new_list=list(filter(lambda x:(x%2==0),my_list))
new_list1=list(map(lambda x: (x*2),my_list))
product=reduce(lambda x,y: (x*y),my_list)
print (new_list)
print (new_list1)
print (product)