start1  = int(input())
end1    = int(input())
start2  = int(input())
end2    = int(input())

left    = max(start1, start2)
right   = min(end1, end2)

if left < right:
    print("YES")
else:
    print("NO")