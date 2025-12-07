# Dec 6 2025
# Day 6: Trash Compactor

# Import the puzzle
import os
here = os.path.dirname(__file__)

readingRanges = True
with open(os.path.join(here, 'day6Input.txt')) as puzzleFile:
    nums = []
    
    for line in puzzleFile:
        nums.append(line.strip('\n').strip() + ' ')

puzzleFile.close()

# Add the answer of each question into a finalSum and output it
finalSum = 0

while nums[0].strip() != '':
    operation = nums[-1][:nums[-1].find(' ')] 
    nums[-1] = nums[-1][nums[-1].find(' '):].lstrip()
    
    if operation == '*':
        currentAns = 1
    else:
        currentAns = 0

    for numIndex in range(len(nums)-1):
        if operation == '*':
            currentAns *= int(nums[numIndex][:nums[numIndex].find(' ')])
        else:
            currentAns += int(nums[numIndex][:nums[numIndex].find(' ')])
        
        nums[numIndex] = nums[numIndex][nums[numIndex].find(' '):].lstrip()

    finalSum += currentAns

print(finalSum)