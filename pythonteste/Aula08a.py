# para importar todas as funções de uma library usa se 'import "nome da library"
from math import sqrt  # quando se busca somente uma função de uma library
num = int(input('Digite um número'))

r = sqrt(num)  # função raiz quadrada na importação especifíca (ao importar todas as
# funções de library precisa chamar a função através do "library name.function"

print('A raiz de {} é igual a {}'.format(num, r))
