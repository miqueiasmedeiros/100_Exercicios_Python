"""
Faça um algoritmo que leia o salário de um funcionário e mostre
seu novo salário com 15% de aumento.
"""
salario = float(input('Digite seu salário: '))
novosalario = salario+(salario*0.15)
print('O seu novo salário com aumento de 15% será R${:.2f}.'.format(novosalario))