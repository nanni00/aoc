from itertools import groupby


with open('2024/input/5.txt') as fr:
    lines = fr.readlines()
    rules, updates = lines[:lines.index('\n')], lines[lines.index('\n')+1:]

rules = [list(map(int, rule.split('|'))) for rule in rules]
rules = {k: [y[0] for y in g] for k, g in groupby(sorted(rules, key=lambda x: x[1]), key=lambda x: x[1])}
updates = [list(map(int, update.split(','))) for update in updates]


def is_correct(update):
    return all(x not in update[i:] for i, y in enumerate(update) if y in rules for x in rules[y])


def rebuild(update:list):
    l = []
    while len(l) < len(update):
        l.insert(0, update[len(l)])
        i = 0
        while not is_correct(l):
            l[i], l[i+1] = l[i+1], l[i]
            i += 1
    return l


part_1, part_2 = map(sum, 
                     zip(*[
                         [update[len(update) // 2], 0] if is_correct(update) else [0, rebuild(update)[len(update) // 2]]
                         for update in updates
                         ]
                        )
                    )


print(f'{part_1=}')
print(f'{part_2=}')
