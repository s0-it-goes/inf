a :int = int(input())
b :int = int(input())
c :int = int(input())
d :int = int(input())

if (a > 255 or a < 0) or (b > 255 or b < 0) \
or (c > 255 or b < 0) or (d > 255 or d < 0):
    print("INVALID")
elif a == 127 and b == 0 and c == 0 and d == 1:
    print("LOOPBACK")
elif a == 0 and b == 0 and c == 0 and d == 0:
    print("UNSPECIFIED")
elif (a >= 224 and a <= 239):
    print("MULTICAST")
elif (a == 10) or (a == 172 and (b >= 16 and b <= 31)) \
or (a == 192 and b == 168):
    print("PRIVATE")
else:
    print("PUBLIC")