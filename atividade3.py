print('\t Tabuada')
numero = int(input("Informa o número para ver a tabuada:"))

print('\n Tabuada de', numero, ':')
for i in range(1,11):
    print(numero, 'x', i, '=', (numero * i))