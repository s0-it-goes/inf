duration    :int = int(input())
hour        :int = int(input())
exchange   = 1.0 
if hour >= 22 or hour < 6:
    exchange = 1.2

if duration < 30:
    cost = 0
elif duration >= 30 or duration < 120:
    cost = 100 * exchange
elif duration >= 120 or duration < 300:
    cost = 250 * exchange
else:
    cost = 500 * exchange

print(cost)