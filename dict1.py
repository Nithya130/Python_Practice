monthsDictionary = { 1: "January",2: "February",3: "March", 4: "April",5: "May",6: "June",7: "July", 8: "August",9:
     "September",10: "October", 11: "November",12: "December"}
print ("The dictionary items are:")
print (monthsDictionary.items() )
print ( "\nThedictionary keys are:")
print ( monthsDictionary.keys() )
print ("\nThedictionary values are:")
print (monthsDictionary.values() )
print ("\nUsinga for loop to get dictionary items:")
for key in monthsDictionary.keys():
    print ("monthsDictionary[", key, "] =", monthsDictionary[key])
