n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m >= 5.75:
    print('O aluno foi aprovado com média de {:.2f}'.format(m))
else:
    print('O aluno foi reprovado com a média {:.2f}'.format(m))
