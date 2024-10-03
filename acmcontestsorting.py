takenInput = input()
totalTime=0
totalCorrect=0
wrongDict={}
while takenInput != "-1":
    m,n,word = takenInput.split()
    m = int(m)
    if word == "wrong":
        if n in wrongDict:
            wrongDict[n]+=1
        else:
            wrongDict[n]=1
    else:
        totalCorrect+=1
        if n in wrongDict:
            totalTime+=m
            totalTime+=(wrongDict[n]*20)
        else:
            totalTime+=m
    takenInput = input()
print(totalCorrect, totalTime)
