"""Faça um programa que leia um número e mostre na tela seu antecessor e sucessor
exemplos 1 e 2"""
#exemplo número 1
n = int(input('Digite um número: '))
a = n-1
s = n+1
print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}.'.format(n, a, s))

#exemplo 2
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}.'.format(n, (n-1), n+1))