import time
t=time.time()
fread=open("B-large-practice.in","r")
fwrite=open("Tidy_number_output.txt","w")


def IsTidy(n):
    list_n=list(str(n))
    for i in range(len(list_n)-1,0,-1):
        if int(list_n[i])<int(list_n[i-1]):
            number_to_delete=int("".join(list_n[i:]))+1
            return IsTidy(n-number_to_delete)
    return n



test=int(fread.readline())
for i in range(1,test+1):
    number=int(fread.readline())
    tidy=IsTidy(number)
    print(tidy)
    fwrite.write("Case #{}: {}\n".format(i,tidy))
    print(time.time()-t)
    print("Case {} completed\n".format(i))

fread.close()
fwrite.close()
