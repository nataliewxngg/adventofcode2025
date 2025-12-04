# Dec 3 2025
# Day 3: Lobby

# Import the puzzle
import os
here = os.path.dirname(__file__)

with open(os.path.join(here, 'day3Input.txt')) as puzzleFile:
    puzzle = puzzleFile.read().splitlines()

puzzleFile.close()

# Find the max joltage in each bank
maxJoltages = []

# Return the lexicographically largest subsequence of length k (preserving order).
# Uses a monotonic-stack approach in O(n) time.
def max_k_subsequence(s: str, k: int) -> str:
    stack = []
    to_remove = len(s) - k
    
    for ch in s:
        # ensure digits remain chars; compare lexicographically which matches numeric order for single digits
        while stack and to_remove > 0 and stack[-1] < ch:
            stack.pop()
            to_remove -= 1
        stack.append(ch)

    # take first k characters
    return ''.join(stack[:k])

for line in puzzle:
    s = line.strip()

    if len(s) < 12:
        maxJoltage = 0
    else:
        best = max_k_subsequence(s, 12) # a string of digits
        maxJoltage = int(best)

    maxJoltages.append(maxJoltage)

print(sum(maxJoltages))