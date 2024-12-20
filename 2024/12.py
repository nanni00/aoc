from collections import Counter
from itertools import groupby


G = [row.strip() for row in open('2024/input/12.txt')]

points, visited = [(0, 0)], set()
part_1 = part_2 = 0

def is_in(r, c):
    return 0 <= r < len(G) and 0 <= c < len(G[0])

while points:
    r, c = points.pop()
    if (r, c) in visited:
        continue

    region_q = [(r, c)]
    adj = set()
    region = set()

    # explore this region
    while region_q:
        rq, cq = region_q.pop()
        if (rq, cq) in visited:
            continue
        # check each adjacent point
        for mr, mc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            mrq = rq + mr
            mcq = cq + mc
            # if it's of the same type, add a new adjacent pair and a new element to the queue
            if 0 <= mrq < len(G) and 0 <= mcq < len(G[0]):
                if G[mrq][mcq] == G[rq][cq]:
                    adj.add(((rq, cq), (mrq, mcq)))
                    region_q.append((mrq, mcq))
                else:
                    points.append((mrq, mcq))

        region.add((rq, cq))
        visited.add((rq, cq))

    sides = sum(1 for _, f in Counter([(rg + rr, cg + cc) for rg, cg in region for rr, cc in [[0, 0], [0, 1], [1, 0], [1, 1]]]).items() if f % 2 != 0)

    sides += sum(2 
                 for _, gg 
                 in groupby(sorted([((rg, cg), (rg + rr, cg + cc)) for rg, cg in region for rr, cc in [[0, 0], [0, 1], [1, 0], [1, 1]]], key=lambda x: x[1]), key=lambda x: x[1])
                 if (lambda gg: len(gg) == 2 and abs(gg[0][0] - gg[1][0]) + abs(gg[0][1] - gg[1][1]) == 2)([x[0] for x in gg])
                 )

    part_1 += len(region) * (4 * len(region) - len(adj))
    part_2 += len(region) * sides

print(f'{part_1=}')
print(f'{part_2=}')
