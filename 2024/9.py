with open('2024/input/9.txt', 'r') as f:
    disk_map = f.readline().strip()

fid = 0
disk_b = []

for i, k in enumerate(disk_map):
    disk_b.append([fid if i % 2 == 0 else None for _ in range(int(k))])
    fid += 1 if i % 2 == 0 else 0 

disk = [x for b in disk_b for x in b]
cks = []
b = -1

while disk :
    if disk[0] is not None:
        fid = disk.pop(0)
        cks.append(fid)

    elif disk[0] is None:
        while disk and disk[-1] is None:
            disk.pop()
        if not disk:
            break
        disk.pop(0)
        b = disk.pop()
        cks.append(b)

part_1 = sum(i * b for i, b in enumerate(cks))

disk = disk_b

for i in range(len(disk) - 1, -1, -2):
    b = disk[i]
    for j in range(1, i, 2):
        if sum([x == None for x in disk[j]]) >= len(b):
            lb = len(b)
            k = 0
            while k < len(disk[j]) and lb > 0:
                if disk[j][k] is None:
                    lb -= 1
                    disk[j][k] = b[0]
                k += 1
            disk[i][:] = [None] * len(disk[i])
            break

part_2 = sum(i * b for i, b in enumerate([x if x is not None else 0 for b in disk for x in b]))

print(f'{part_1=}')
print(f'{part_2=}')
