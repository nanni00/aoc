with open('2024/input/2.txt') as fr:
    f = fr.readlines()


def check(r):
    return abs(sum([-1 if -3 <= r[i] - r[i+1] <= -1 else 0 for i in range(len(r) - 1)])) == len(r) - 1


def rec(r):
    for i in range(0, len(r)):
        if check(r[:i] + r[i+1:]):
            return True
    return False


part_1 = sum(
    map(
        check,
        map(lambda r: r if r[0] <= r[-1] else r[::-1], [list(map(int, line.split())) for line in f])
    )
)
        
part_2 = sum(
    map(
        rec,
        map(lambda r: r if r[0] <= r[-1] else r[::-1], [list(map(int, line.split())) for line in f])
    )
)

print(f"{part_1=}")
print(f"{part_2=}")
