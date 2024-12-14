import re
from collections import Counter, defaultdict


def rules(s):
    if s == 0: return [1]
    elif len(str(s)) % 2 != 0: return [s * 2024]
    # math bleah, int->str->int is better
    return [int(str(s)[:len(str(s)) // 2]), int(str(s)[len(str(s)) // 2:])]
    

def blink(n, stones):
    for _ in range(n):
        next_stones = defaultdict(int)
        for s, freq in stones.items():
            for ss in rules(s):
                next_stones[ss] += freq
        stones = next_stones
    return sum(stones.values())

stones = Counter(map(int, open('2024/input/11.txt').readline().split()))

print(f'part_1={blink(25, stones)}')
print(f'part_2={blink(75, stones)}')



# Nice solution with recursion and caching
# From reddit, not mine
from functools import cache
from math import floor, log10

@cache
def count(x, d=75):
    if d == 0: return 1
    if x == 0: return count(1, d-1)

    l = floor(log10(x))+1
    if l % 2: return count(x*2024, d-1)

    return (count(x // 10**(l//2), d-1)+
            count(x %  10**(l//2), d-1))

data = map(int, open('2024/input/11.txt').readline().split())
print(sum(map(count, data)))

