i = int(input())

for i in range(i):
    w = input()
    print(w if len(w)<=10 else (w[0]+str(len(w[1:-1])) + w[-1]))
