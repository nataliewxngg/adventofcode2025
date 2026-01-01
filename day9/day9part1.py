# Dec 9 2025
# Day 9: Movie Theater

# Import the puzzle
import os

here = os.path.dirname(__file__)

with open(os.path.join(here, 'day9Input.txt')) as puzzleFile:
    puzzle = []
    
    for line in puzzleFile:
        puzzle.append((int(line[:line.find(',')]), int(line.strip('\n')[line.find(',')+1:])))

puzzleFile.close()

def getArea(pt1, pt2):
    return (pt1[0]-pt2[0]+1) * (pt1[1]-pt2[1]+1)

greatestArea = 0
for indexOfPt1 in range(len(puzzle)):
    for indexOfPt2 in range(indexOfPt1+1, len(puzzle)):
        if getArea(puzzle[indexOfPt1], puzzle[indexOfPt2]) > greatestArea:
            greatestArea = getArea(puzzle[indexOfPt1], puzzle[indexOfPt2])

print(greatestArea)