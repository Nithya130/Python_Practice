line=input("Enter Line:")
List_line=line.split()
wc,dc,sc=0,0,0
for i in (List_line):
    if i.isdigit():
        dc=dc+1
    elif i.isalnum():
        wc=wc+1
    else:
        sc=sc+1
print ("words:",wc)
print ("Digits:",dc)
print("Special Word:",sc)
