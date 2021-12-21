#Faça um programa que leia um número e imprima na tela sua tabuada
n = int(input('Digite um número: '))
for i in range(1,11):
    r = n*i
    print('{} x {} = {}'.format(n,i,r))