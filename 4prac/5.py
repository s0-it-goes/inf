distance :float = float(input())
speed    :int   = int(input())

if distance <= 0.1 and speed <= 100:
    print("WIFI")
elif distance <= 10 and speed <= 150:
    print("LTE")
elif distance <= 2 and speed <= 1000:
    print("5G")
elif distance <= 1000 and speed <= 200:
    print("SATELITE")
else:
    print("NO SIGNAL")