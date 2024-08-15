d, v = map(int, input().split(" "))

th = d // v
r = d % v

m = (r * 60)//v

h = (th + 19) % 24


print(f"{h:02d}:{m:02d}")