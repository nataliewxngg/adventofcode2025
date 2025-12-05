# Dec 5 2025
# Day 5: Cafeteria

# Import the puzzle
import os
here = os.path.dirname(__file__)

readingRanges = True
with open(os.path.join(here, 'day5Input.txt')) as puzzleFile:
    freshRanges = []
    ingredients = []
    
    for line in puzzleFile:
        if (line.strip('\n') == ''):
            readingRanges = False
        elif (readingRanges):
            freshRanges.append(line.strip('\n'))
        else: 
            ingredients.append(int(line.strip('\n')))

puzzleFile.close()

# Check if an ingredient is available in each inputted range and increment the number of fresh ingredients if so
numOfFreshIngredients = 0
processedIngredients = []

for freshRange in freshRanges:
    lowerBound = int(freshRange[:freshRange.find('-')])
    upperBound = int(freshRange[freshRange.find('-')+1:])

    for ingredient in ingredients:
        if ingredient >= lowerBound and ingredient <= upperBound and ingredient not in processedIngredients:
            numOfFreshIngredients += 1
            processedIngredients.append(ingredient)

print(numOfFreshIngredients)