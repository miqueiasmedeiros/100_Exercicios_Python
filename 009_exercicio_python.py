"""
Faça um programa que leia a altura e a largura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pinta-la
sabendo que cada litro de tinta pinta uma área de 2m².
"""
altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))
area = altura*largura
tinta = area/2
print('Será necessário para pintar uma área de {:.3f}m², {:.2f} litros de tinta.' .format(area, tinta))