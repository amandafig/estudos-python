n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor'))

soma = n1 + n2
sub = n1 - n2
mult= n1 * n2
div = n1 / n2
poten = n1 ** n2
divint = n1 // n2
resto = n1 % n2

print('O valor da soma {} da subtração {}, da multiplicação {}, da divisão {}, da potenciação {}, da divisão inteira {}, o resto da divisão {}'.format(soma, sub, mult, div, poten, divint, resto))