# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('A media entre {:.1f} e {:.1f} é igual a {:.1f}' .format(n1, n2, m))