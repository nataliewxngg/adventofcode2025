# Dec 8 2025
# Day 8: Playground

import math

# Import the puzzle
import os

here = os.path.dirname(__file__)

with open(os.path.join(here, 'day8Input.txt')) as puzzleFile:
    puzzle = []
    
    for line in puzzleFile:
        puzzle.append(line.strip('\n'))

puzzleFile.close()

# Create a function to calculate the distance between two junctions
def calcDistance(pt1, pt2):
    pt1Arr = pt1.split(',')
    pt2Arr = pt2.split(',')

    return math.sqrt((int(pt2Arr[0])-int(pt1Arr[0]))**2 + 
                     (int(pt2Arr[1])-int(pt1Arr[1]))**2 + 
                     (int(pt2Arr[2])-int(pt1Arr[2]))**2)

def getAns(circuits):
    circuitSizes = [1, 1, 1]

    for circuit in circuits:
        if len(circuit) > circuitSizes[2]:
            if len(circuit) > circuitSizes[1]:
                if len(circuit) > circuitSizes[0]:
                    circuitSizes[2] = circuitSizes[1]
                    circuitSizes[1] = circuitSizes[0]
                    circuitSizes[0] = len(circuit)
                else:
                    circuitSizes[2] = circuitSizes[1]
                    circuitSizes[1] = len(circuit)
            else:
                circuitSizes[2] = len(circuit)

    return circuitSizes[0]*circuitSizes[1]*circuitSizes[2]

# allDistances is a dictionary containing the distance between ALL junctions as the key, 
# and a tuple of the indexes of the two respective junctions as the value
# Dictionary items are sorted from shortest to greatest distances
allDistances = {}

for indexOfJunction1 in range(len(puzzle)):
    for indexOfJunction2 in range(indexOfJunction1+1, len(puzzle)):
        allDistances[calcDistance(puzzle[indexOfJunction1], 
                                  puzzle[indexOfJunction2])] = (indexOfJunction1, indexOfJunction2)
        
allDistances = dict(sorted(allDistances.items()))

# An array of arrays that represent circuits
circuits = []
# An array of already added junctions
addedJunctions = []

# Go through all junctions distance by distance and add them to circuits
for key, value in allDistances.items():
    indexOfJunction1 = value[0]
    indexOfJunction2 = value[1]

    if indexOfJunction1 in addedJunctions and indexOfJunction2 in addedJunctions: # both junctions are in circuits already
        # check if they're in the same circuit, if not, merge the two circuits
        for indexOfCircuit in range(len(circuits)):
            if indexOfJunction1 in circuits[indexOfCircuit] and indexOfJunction2 not in circuits[indexOfCircuit]:
                # find the index of the circuit junction2 is in
                for indexOfCircuit2 in range(len(circuits)):
                    if indexOfJunction2 in circuits[indexOfCircuit2]:
                        circuits[indexOfCircuit] = circuits[indexOfCircuit] + circuits[indexOfCircuit2]
                        del circuits[indexOfCircuit2]
                        break 
                break

    elif indexOfJunction1 in addedJunctions and indexOfJunction2 not in addedJunctions: # only junction 1 is in a circuit already
        # find the index of the circuit junction1 is in, then add junction2 into that same circuit
        for indexOfCircuit in range(len(circuits)):
            if indexOfJunction1 in circuits[indexOfCircuit]:
                circuits[indexOfCircuit].append(indexOfJunction2)
                addedJunctions.append(indexOfJunction2)
                break
    
    elif indexOfJunction1 not in addedJunctions and indexOfJunction2 in addedJunctions: # only junction 2 is in a circuit already
        # find the index of the circuit junction2 is in, then add junction1 into that same circuit
        for indexOfCircuit in range(len(circuits)):
            if indexOfJunction2 in circuits[indexOfCircuit]:
                circuits[indexOfCircuit].append(indexOfJunction1)
                addedJunctions.append(indexOfJunction1)
                break

    else:
        circuits.append([indexOfJunction1, indexOfJunction2])
        addedJunctions.append(indexOfJunction1)
        addedJunctions.append(indexOfJunction2)

    if len(circuits) == 1 and len(addedJunctions) == len(puzzle):
        print(int(puzzle[indexOfJunction1][:puzzle[indexOfJunction1].find(',')])*int(puzzle[indexOfJunction2][:puzzle[indexOfJunction2].find(',')]))
        break
