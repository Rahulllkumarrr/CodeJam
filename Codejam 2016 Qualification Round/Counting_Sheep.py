fr=open("large.txt","r")
fw=open("OutputL.txt","w")
pre=set([0,1,2,3,4,5,6,7,8,9])
test=int(fr.readline())
for i in range(1,test+1):
    print("CASE ",i)
    new=set()
    num=int(fr.readline())
    for z in range(1,20000):
        digits=num*z
        print(digits)
        for k in str(digits):
            new.add(int(k))
        sorted(new)
        length=len(new)
        if new==pre:
            fw.write("Case #{}: {}\n".format(i,digits))
            break
    if new!=pre:
        fw.write("Case #{}: INSOMNIA\n".format(i))

