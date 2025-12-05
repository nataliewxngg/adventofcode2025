# Dec 5 2025
# Day 5: Cafeteria

# Import the puzzle
import os

here = os.path.dirname(__file__)

with open(os.path.join(here, 'day5Input.txt')) as puzzleFile:
    ranges = []
    
    for line in puzzleFile:
        if (line.strip('\n') == ''):
            break
        ranges.append((int(line.strip('\n')[:line.find('-')]), int(line.strip('\n')[line.find('-')+1:])))

puzzleFile.close()

# Sort the ranges by increasing order of lower bound
ranges.sort(key=lambda x: x[0])

coveredRange = [ranges[0][0], ranges[0][1]]
numOfFresh = ranges[0][1] - ranges[0][0] + 1
print('starting #: ' + str(numOfFresh))

# Add the new numbers of fresh ingredients by iterating through each range
for rangeIndex in range(1, len(ranges)):
    print('current covered range: ' + str(coveredRange))

    if ranges[rangeIndex][0] >= coveredRange[0] and ranges[rangeIndex][0] <= coveredRange[1] and ranges[rangeIndex][1] > coveredRange[1]: # Current range starts overlapped, but later values are not overlapped
        numOfFresh += ranges[rangeIndex][1] - coveredRange[1]
        print('adding ' + str(ranges[rangeIndex][1] - coveredRange[1]))
        coveredRange[1] = ranges[rangeIndex][1]
    
    elif ranges[rangeIndex][0] > coveredRange[1]: # No overlap at all
        numOfFresh += ranges[rangeIndex][1] - ranges[rangeIndex][0] + 1
        print('adding ' + str(ranges[rangeIndex][1] - ranges[rangeIndex][0] + 1))
        coveredRange[1] = ranges[rangeIndex][1] 

    # Otherwise, do nothing if the current range is contained within the covered range completely

print(numOfFresh)
