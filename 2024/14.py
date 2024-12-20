from collections import Counter
from functools import reduce
from operator import mul

import re
import curses


bots = [list(map(int, re.findall(r'-?\d+', line))) for line in open('2024/input/14.txt').readlines()]

seconds = 100

W = 101
H = 103

def update(bots, seconds=1):
    return [(lambda x, y, vx, vy: ((x + vx * seconds) % W, (y + vy * seconds) % H))(*bot) for bot in bots]

final_bots = update(bots, seconds)
  

part_1 = reduce(mul, (v for k, v in Counter([(lambda x, y: 
                      0 if x < W // 2 and y < H // 2 else 
                      1 if x < W // 2 and y > H // 2 else 
                      2 if x > W // 2 and y < H // 2 else
                      3 if x > W // 2 and y > H // 2 else 
                      None#  if x > 51 and y > 52
                      )(*bot[:2]) for bot in final_bots]).items() if k is not None))

def display(bots):
    board = [[0] * W for _ in range(H)]
    for bot in bots:
        board[bot[1]][bot[0]] += 1
    s = ''
    for row in board:
        s += ''.join(map(str, row)).replace('0', '.') + '\n'
    return s
  


# Very cool solution with variance (from Reddit, not mine!)
# Basically, when there will be the Christmas Tree,
# the robots will be highly clustered
# see that the variance on X axis does not depend on
# variance on Y axis
# We can reach similar result checking for those cases
# were we have e.g. at least K (say > 10) bot arranged
# in the same row adjacently, but this should be more expensive,
from statistics import variance


bx, bxvar, by, byvar = 0, 10*100, 0, 10*1000

for t in range(max(W,H)):
    xs, ys = zip(*update(bots, t))
    if (xvar := variance(xs)) < bxvar: bx, bxvar = t, xvar
    if (yvar := variance(ys)) < byvar: by, byvar = t, yvar

part_2 = bx + ((pow(W, -1, H) * (by - bx)) % H) * W


final_bots = update(bots, 7916)
print(display(final_bots))

print(f'{part_1=}')
print(f'{part_2=}')
