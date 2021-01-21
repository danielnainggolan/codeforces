n,d = map(int,input().split())
ds = 0
for i in range(int(n)):
    ops, val = input().split()
    val = int(val)
    if ops == '+':
        d += val
    else:
        if d < val:
            ds += 1
        else: 
            d -= val
print(d,ds)