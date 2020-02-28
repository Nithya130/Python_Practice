str1="nithya is going"
l=str1.split()
out_st=""
for i in l:
    erev=""
    for j in range(len(i)-1,-1,-1):
        erev=erev+i[j]
    out_st=out_st+" "+erev
print (out_st)