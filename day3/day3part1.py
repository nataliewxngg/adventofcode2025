# Dec 3 2025
# Day 3: Lobby

# Import the puzzle
import os
here = os.path.dirname(__file__)

with open(os.path.join(here, 'day3Input.txt')) as puzzleFile:
    puzzle = puzzleFile.read().splitlines()
print(puzzle)

puzzleFile.close()

# Find the max joltage in each bank
maxJoltages = []

for i in puzzle:
    maxJoltage = 0

    for digit1Index in range(len(i)-1): # Digit 1 starts at 0, and cannot be last char in string
        for digit2Index in range(digit1Index+1, len(i)): # Digit 2 starts behind digit 1
            currentJoltage = i[digit1Index] + i[digit2Index]
            if int(currentJoltage) > maxJoltage:
                maxJoltage = int(currentJoltage)
    
    maxJoltages.append(maxJoltage)

print(sum(maxJoltages))