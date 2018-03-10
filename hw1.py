

userInput = input("Enter the numbers:")
oldList=list(map(int, userInput.split()))

newList = []
for i in range(int(len(oldList)/2)):
    newList.append((oldList[2*i]+oldList[2*i+1])/2)

for j in range(len(newList)):
    print(newList[j])
    
    
