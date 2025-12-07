# Dec 6 2025
# Day 6: Trash Compactor

# Import the puzzle
import os
here = os.path.dirname(__file__)

with open(os.path.join(here, 'day6Input.txt')) as puzzleFile:
    nums = []
    
    for line in puzzleFile:
        nums.append(line.strip('\n') + ' ')

puzzleFile.close()

# Add the answer of each question into a finalSum and output it
finalSum = 0

while nums[0].strip() != '':
    indexOfCommonSpace = len(nums[-1])
    operation = nums[-1][:nums[-1].find(' ')] 
    nums[-1] = nums[-1][nums[-1].find(' '):].lstrip()
    indexOfCommonSpace -= len(nums[-1])
    
    # Split the problem by identifying the common ' '
    currentProb = []
    for numIndex in range(len(nums)-1):
        currentProb.append(nums[numIndex][:indexOfCommonSpace-1]) 
        nums[numIndex] = nums[numIndex][indexOfCommonSpace:]

    if operation == '*':
        currentAns = 1
    else:
        currentAns = 0

    while True:
        currentNum = ''
        for numIndex in range(len(currentProb)):
            if currentProb[numIndex].strip() != '':
                currentNum += currentProb[numIndex][-1]
                currentProb[numIndex] = currentProb[numIndex][:-1]

        if currentNum == '':
            break
            
        if operation == '*':
            currentAns *= int(currentNum)
        else:
            currentAns += int(currentNum)
        
    finalSum += currentAns

print(finalSum)