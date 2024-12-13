import math
from itertools import groupby
from itertools import combinations


amap = open('2024/input/8.txt').readlines()
antennas = [(k, r, c) for r, line in enumerate(amap) for c, k in enumerate(line.strip()) if k != '.']
antennas = [{aa[1:] for aa in a[1]} for a in groupby(sorted(antennas), key=lambda a: a[0])]

R = len(amap)
C = len(amap[0]) - 1


def is_in(p):
    return 0 <= p[0] < R and 0 <= p[1] < C


def antinodes(a, b, part=1):
    rd, cd = abs(a[0] - b[0]), abs(a[1] - b[1])
    if part != 1:
        rd //= math.gcd(rd, cd)
        cd //= math.gcd(rd, cd)
        
    p1, p2 = a, b
    p1_points = []
    p2_points = []

    while (p1 := (p1[0] + (rd if a[0] > b[0] else -rd), p1[1] + (cd if a[1] > b[1] else -cd))) and is_in(p1):
        p1_points.append(p1)

    while (p2 := (p2[0] + (rd if a[0] < b[0] else -rd), p2[1] + (cd if a[1] < b[1] else -cd))) and is_in(p2):
        p2_points.append(p2)
    
    return [*p1_points[:1], *p2_points[:1]] if part == 1 else p1_points + p2_points + [a, b]


def solve(part):
    return len({
        p
        for aa in antennas
        for (a, b) in combinations(aa, r=2)
        for p in antinodes(a, b, part)
        if is_in(p)
    })


print(f'part 1={solve(1)}')
print(f'part 2={solve(2)}')
