"""Crie um algoritmo que leia um número e mostre seu Dobro, Triplo
e Raiz Quadrada"""
# exemplo 1
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1 / 2)
print('O dobro de {} vale {}'.format(n, d))
print('O triplo de {} vale {}'.format(n, t))
print('A raiz quadrada de {} é igual a {:.1f}'.format(n, r))

# exemplo 2
n = int(input('Digite um número: '))
print('O Dobro de {} vale {}'.format(n, (n * 2)))
print('O triplo de {} vale {}'.format(n, (n * 3)))
print('A raiz quadrada de {} é igual a {:.2f}'.format(n, pow(n, (1 / 2))))

# exemplo 3
n = int(input('Digite um número: '))
print('O dobro de {} vale {}'.format(n, (n * 2)))
print('O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.3f}'.format(n, (n * 3), n, (n ** (1 / 2))))
