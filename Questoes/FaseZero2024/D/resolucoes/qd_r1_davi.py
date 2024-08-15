entrada = list(map(int,input().split(" ")))

horasInicial = entrada[0]//entrada[1]

horasFinal = (horasInicial+19)%24

restoMin = entrada[0]%entrada[1]

minutosFinal = int(60*restoMin/entrada[1])

print(f"{horasFinal}:{minutosFinal}")