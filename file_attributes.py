'''
File attributes
'''
print ("File operation")
fd=open('Test.py','w')
fd.write("#python file")
print ("Name of file:",fd.name)
print ("Mode of File:",fd.mode)
print ("Before :",fd.closed)
if fd.closed is False :
     fd.close()
print ("file is closed or not:",fd.closed)