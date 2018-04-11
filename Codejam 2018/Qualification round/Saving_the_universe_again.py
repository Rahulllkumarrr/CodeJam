def score(k):
    adder = 1
    total = 0
    for i in k:
        if i=="S":
            total+=adder
        else:
            adder=adder*2

    #print("Total=",total)
    return total


def equal(u):
    while u[len(u) - 1] == "C":
        u.pop()
    #print("Equal list=",u)
    return u


def minpos(z):
    #print("Count of S =",z.count("S"))
    return z.count("S")


def calculator(arr, max):
    if minpos(arr) > max:
        return "IMPOSSIBLE"
    else:
        count = 0
        while score(arr) > max:
            arr = equal(arr)
            i = len(arr) - 1
            while i >= 0:
                if arr[i] == "C":
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    count += 1
                    break
                i-=1
        return count


tests = int(input())
for test in range(1, tests + 1):
    line = input().split()
    max = int(line[0])
    #print(max)
    arr = [str(k) for k in line[1]]
    #print(arr)
    result = calculator(arr,max)
    print("Case #{}: {}".format(test, result))
