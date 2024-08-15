import functools
'''
total = []
for s1 in l1:
    tmp =[]
    total.append(s1 + l2[0])
    for e1 in s1:
        tmp.append(e1+l2[0][0])
    total.append(tmp)
print(total)
'''
'''
def teste(lista, elemento):
    if(len(lista) == 1): return lista
    total = []
    for s1 in lista:
        tmp =[]
        total.append(s1 +[elemento])
        total.append(s1[:-1]+[s1[-1]+elemento])
    return total
'''
def get_inputs():
    return map(int, input().split(" "))


def gerar_combinacoes(lista):
    if(len(lista) == 1): return lista
    if(len(lista) == 2) : return [lista[0],lista[1]], [lista[0]+lista[1]]
    elemento = lista[-1]
    total = []
    for s1 in gerar_combinacoes(lista[:-1]):
        total.append(s1 +[elemento])
        total.append(s1[:-1]+[s1[-1]+elemento])
    return total


def validar_combinacao(combinacao,start, end):
    pieces_conf = range(start+1,end+1)

    validar_combinacao = True
    for pedaco in combinacao:
        validar_unico = True
        validar_pedacao = False
        for it in pieces_conf:
            if (str(it) not in pedaco):
                validar_unico = False
            else:  
                validar_pedacao = True
        if(validar_unico):
            return True;
        if(not validar_pedacao):
            validar_combinacao = False
    return validar_combinacao

num_pieces, num_conf = get_inputs()
lista = list(map(str,range(1,num_pieces+1)))
conf_list = []

for i in range(num_conf):
    start, end = get_inputs()
    conf_list.append((start,end))

print("Lista = ", lista)
combinacoes = gerar_combinacoes(lista)
print (combinacoes )

# Começar das maiores e parar qd for para uma menor
max = 0
for combinacao in combinacoes:
    valida = True
    for conf in conf_list:
        if(not validar_combinacao(combinacao,conf[0], conf[1])):
           valida = False
           break
    if valida :
        print(combinacao)
        max = max if len(combinacao) < max else len(combinacao)

print("Resultado = ",max)