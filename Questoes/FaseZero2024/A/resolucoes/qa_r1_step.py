entradas = list(map(int,input().split(" ")))

# solution 1
cancoes = [0,0,0,0]
for e in entradas:
    cancoes[e] = 1

print(cancoes.index(0))


# solution 2
for i in range(1,4):
    if not(i in entradas):
        print(i)
        break





