def run_moves(whmap, moves):
    robot = [k for k, v in whmap.items() if v == '@'][0]
    for rm, cm in moves:
        update, to_upt = [robot], []

        while update:
            r, c = update.pop(0)
            if (r, c) in to_upt: continue
            if (r + rm, c + cm) not in whmap:
                to_upt.append((r, c))
                continue
            match whmap[(r + rm, c + cm)]:
                case 'O':
                    update.append((r + rm, c + cm))
                    to_upt.append((r, c))
                case '[':
                    update.append((r + rm, c + cm))
                    update.append((r + rm, c + 1))
                    to_upt.append((r, c))
                case ']':
                    update.append((r + rm, c + cm))
                    update.append((r + rm, c - 1))
                    to_upt.append((r, c))
                case '#':
                    to_upt = []
                    break
                        
        for ru, cu in to_upt[::-1]:
            whmap[(ru + rm, cu + cm)] = whmap[(ru, cu)]
            del whmap[(ru, cu)]
        if to_upt:
            robot = to_upt[0][0] + rm, to_upt[0][1] + cm


whmap, moves = open('2024/input/15.txt').read().split('\n\n')

moves = [{'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}[m] for m in moves.replace('\n', '')]
nwhmap = whmap = {(r, c): t for t, r, c in sorted((t, r, c) for r, row in enumerate(whmap.splitlines()) for c, t in enumerate(row.strip()) if t != '.')}
nwhmap = {(r, 2 * c): '[' if t == 'O' else t for (r, c), t in nwhmap.items()}
nwhmap |= {(r, c + 1): '#' if t == '#' else ']' for (r, c), t in nwhmap.items() if t in '#['}

run_moves(whmap, moves)
run_moves(nwhmap, moves)

part_1 = sum(100 * r + c for (r, c), t in whmap.items() if t == 'O')    
part_2 = sum(100 * r + min(c, abs((max(p[1] for p in whmap) * 2 + 1) * 2 - c)) for (r, c), t in nwhmap.items() if t == '[')    

print(f'{part_1=}')
print(f'{part_2=}')
