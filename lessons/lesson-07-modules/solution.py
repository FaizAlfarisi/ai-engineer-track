# Lesson 7 — Modules
# Write all exercise solutions here first, then paste each into its notebook cell.
# Do not delete or reorder these solutions — the notebook cells must stay in sync.

# E1
import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(25))

import math as m 
print(m.floor(2.7))

# E2
def main():
    print("running as script")

if __name__ == "__main__":
    main()
    
print(__name__)

# E3
import random

random.seed(42)
print(random.randint(1,10), end=" ")
print(random.randint(1,10), end=" ")
print(random.randint(1,10))

# E4
import random
deck = list(range(1,11))
random.seed(0)
print(f"sample: {random.sample(deck, 3)}")

deck = list(range(1,11))
random.seed(0)
random.shuffle(deck)
print(f"shuffled: {deck}")

# E5
import os

p = os.path.join("data", "raw", "labels.csv")
print(os.path.basename(p))
print(os.path.splitext(p)[1])

# M1
import random

random.seed(1)
a = [random.randint(1,100) for _ in range(5)]

random.seed(1)
b = [random.randint(1,100) for _ in range(5)]

print(a == b)
print(a)

# M2
import random

random.seed(42)
counts = {}

for _ in range(100):
    f = random.choice(["H", "T"])
    counts[f] = counts.get(f, 0) + 1
    
print(dict(sorted(counts.items())))

# M3
import random

deck = ["A", "K", "Q", "J", "10", "9", "8", "7", "6"]
random.seed(3)
random.shuffle(deck)
print(f"hand1: {deck[:3]}")
print(f"hand2: {deck[3:6]}")

# H1
import random
random.seed(1)                # keep this line — determinism
# from random import *          # bug A — star import, delete this line     # assume i've delete it by commented it
print(random.randint(1, 6))

number = 5                    # bug B — shadows the module
print(random.randint(1, 6))

import math as m
print(m.sqrt(16))               # bug C — the name is not in your box

random.seed(1)
for _ in range(3):
    # random.seed(1)            # bug D — resets every iteration
    print(random.randint(1, 100))

def main():
    print("running as script")


if __name__ == "__main__":
    main()                        # bug E — runs on import

# H2
import random

seen = set()
rolls = 0
random.seed(5)

while len(seen) < 6:
    seen.add(random.choice([1,2,3,4,5,6]))
    rolls += 1
        
print(f"{rolls} rolls to collect all 6 faces")
print(f"seen: {sorted(seen)}")

# CHALLENGE
import random 
import sys

def parse_args(argv):
    count = 0
    names = []
    seed = None
    
    if "--seed" == argv[0]:
        seed = int(argv[1])
        count = int(argv[2])
        names = argv[3:]
    else:
        count = int(argv[0])
        names = argv[1:]
        
    return names, count, seed

def pick(names, count, seed=None):
    if seed is not None:
        random.seed(seed)
        
    return random.sample(names, count)

def print_winners(winners):
    print("=== winners ===")
    print('\n'.join(f"{i+1}. {winner}" for i, winner in enumerate(winners)))

def main():
    argv = sys.argv
    
    if len(argv) < 3:
        print("usage: python solution.py <count> <name> [name ...]")
        return 
    
    try:
        names, count, seed = parse_args(argv[1:])
    except (ValueError, IndexError):
        print("invalid count")
        return
    
    if count < 1 or count > len(names):
        print(f"invalid count: {count}")
        return
    
    winners = pick(names, count, seed)
    print_winners(winners)

if __name__ == "__main__":
    main()
