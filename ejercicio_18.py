 
numeros = [10, 20, 30, 40, 50]
cambio = numeros[0]
numeros[0] = numeros[-1]
numeros[-1] = cambio
print(numeros)