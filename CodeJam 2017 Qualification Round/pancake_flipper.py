inputFile = open("test.in", "r")
outputFile = open("output2.txt", "w")

testCases = int(inputFile.readline())

for testCase in range(1, testCases + 1):

    inp = inputFile.readline()
    inp = inp.split()

    panCakes = inp[0]
    flipSize = int(inp[1])

    convertor=list(panCakes)
    ans=0
    for i in range(len(panCakes) - flipSize+ 1):
        if convertor[0]=='+':
            convertor.pop(0)
        elif convertor[0]=='-':
            ans=ans+1
            for y in range(flipSize):
                if convertor[y]=='+':
                    convertor[y]="-"
                else:
                    convertor[y]="+"
            convertor.pop(0)
        else:
            break
    for z in range(flipSize-1):
        if convertor[z]=='-':
            ans='IMPOSSIBLE'
            break
        else:
            ans=ans
    print("Case #", testCase, ": ", ans, sep="", file=outputFile)

inputFile.close()
outputFile.close()
