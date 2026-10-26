n :int = int(input())

coords :list = [0, 0]

moves :list = []

for i in range(n):
    moves.append(input())
    
for i in moves:
    match i:
        case 'U':
            coords[0] += 1
        case 'D':
            coords[0] -= 1
        case 'L':
            coords[1] -= 1
        case 'R':
            coords[1] += 1

print(f'x: {coords[0]}, y: {coords[1]}, r: {abs(coords[0] + abs(coords[1]))}')