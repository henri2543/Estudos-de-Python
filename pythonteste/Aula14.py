''' for c in range(1, 10):
    print(c)
print('Fim') '''

'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('fim')'''

c = 0
par = impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    c += 1
    if n != 0:
        if n % 2:
            par += 1
        else:
            impar += 1

print('Você digitou {} números dos quais {} são pares e {} são ímpares!'.format(c, par, impar))