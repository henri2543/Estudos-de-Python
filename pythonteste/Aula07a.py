n1 = int(input('Digite um valor!'))
n2 = int(input('Digite um valor!'))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2

print('A soma é {}, a subtração é {}, o produto é {}, a divisão é {} '.format(s, sub, m, d), end=' ')
print('A divisão inteira é {} \n e a potência é {}'.format(di, p))
