"""
Faça um programa que leia um preço de um produto e
mostre seu novo preço com 5% de desconto.
"""
preco = float(input('Digite o preço do produto: '))
novopreco = preco-(preco*0.05)
print('O preço do seu produto com 5% de desconto ficará em R${:.2f}.'.format(novopreco))