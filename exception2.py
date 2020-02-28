try:
	fd=open('C:/Users/nvemula/PycharmProjects/Python_Practice/Files/abc.txt','r')
except IOError:
    print ("Error: cont find the file")
else:
	l=fd.readlines()
	for i in l:
		print (i)
finally:
	try:
		if not fd.closed:
			fd.close()
		print ("Read done")
	except NameError as e1:
		print ("I am name error",e1)
		pass