# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
medida = float(input('Digite uma distância em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {}m em decímetro é {}dm.' .format(medida, dm))
print('A medida de {}m em centímetro é {}cm.' .format(medida, cm))
print('A medida de {}m em milímetro é {}mm.' .format(medida, mm))
print('A medida de {}m em decâmetro é {}dam.' .format(medida, dam))
print('A medida de {}m em hectômetro é {}hm.' .format(medida, hm))
print('A medida de {}m em quilômetro é {}km.' .format(medida, km))
