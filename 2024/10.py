tmap = [list(map(int, row.strip())) for row in open('2024/input/10.txt')]
R, C = len(tmap), len(tmap[0])

trailheads = [[r, c] for r in range(R) for c in range(C) if tmap[r][c] == 0]
moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# depth-first strategy
def trail(r, c, visited, part):
    if tmap[r][c] == 9 and ((part == 1 and (r, c) not in visited) or part == 2):
        if part == 1:
            visited.add((r, c))
        return 1

    trails = 0
    for m in moves:
        nr, nc = r + m[0], c + m[1]
        if 0 <= nr < R and 0 <= nc < C and tmap[r][c] + 1 == tmap[nr][nc]:
            trails += trail(nr, nc, visited, part)
    return trails

part_1 = sum(trail(*trailhead, set(), 1) for trailhead in trailheads)
part_2 = sum(trail(*trailhead, set(), 2) for trailhead in trailheads)

print(f'{part_1=}')
print(f'{part_2=}')
