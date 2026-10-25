depth = [1, 3, 2, 5, 4, 6, 1]

treasure_index = []

for i in range(1, len(depth) - 1):
    if depth[i] > depth[i - 1] and depth[i] > depth[i+1]:
        treasure_index.append(i)

max = depth[0]

for i in treasure_index:
    max = depth[i] if depth[i] > max else max

depth.remove(max)

print(depth)