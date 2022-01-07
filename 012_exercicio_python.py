'''
Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
'''
c = float(input('Digite a temeratura em ºC: '))
f = (c * 9/5) + 32
print('{:.1f}ºC corresponde à {:.1f}ºF' .format(c,f))