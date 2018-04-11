tests=int(input().strip())

def getindex(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return i

def ok(n):
    if sorted(n)==n:
        return True
    else:
        return False



def troublesort(list0):
    for passes in range(len(list0)-2):
        for i in range(len(list0)-2):
            if list0[i]>list0[i+1]:
                list0[i],list0[i+1],list0[i+2]=list0[i+2],list0[i+1],list0[i]
    #print(list0)
    if ok(list0):
        return "OK"
    else:
        return getindex(list0)

for test in range(1,tests+1):
    num=int(input().strip())
    arr=[int(k) for k in input().split(" ")]
    result=troublesort(arr)
    print("Case #{}: {}".format(test,result))


