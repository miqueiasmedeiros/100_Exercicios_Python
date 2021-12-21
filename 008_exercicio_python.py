# Crie um programa que leia quanto uma pessoa tem na carteira e quantos dólares ela pode comprar.

din = float(input('Quanto você tem na carteira? '))
dollar = 5.74
cotacao = din/dollar
print('Com R${} reais você pode comprar ${:.2f} dólares. Cotação dólar hoje é de R${}'.format(din, cotacao, dollar))