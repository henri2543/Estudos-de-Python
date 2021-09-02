nome = str(input('Digite o seu nome: '))
if nome == 'Henrique':
    print('Meu lindão Tchuco Tchuco!')
elif nome == 'Nair' or nome == 'Mylena':
    print('Você conhece meu Tchuco Tchuco!')
elif nome in 'Jhonny Fabiano Diego Cristiano':
    print('Você é um desafeto do Henrique!')
else:
    print('c é um merdão hein!')
print('Tenha um bom dia {}!'. format(nome))
