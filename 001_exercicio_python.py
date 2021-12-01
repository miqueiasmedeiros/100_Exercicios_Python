# Crie um script python que leia o nome de alguém e mostre uma mensagem de boas vindas.
nome = input('Digite seu nome: ')
print("É um prazer em te conhecer {}!" .format(nome))

# Crie um script em python que leia a data de nascimento e mostra uma mensagem com a data formatada
print('Digite sua data de nascimento: ')
dia = input('Dia = ')
mes = input('Mes = ')
ano = input('Ano = ')
print('Você nasceu no dia {} de {} de {}. Correto?'.format(dia, mes, ano))

# Crie um script python que leia dois numeros e mostre a soma entre eles.
a1 = int(input('Digite o primeiro número: '))
b2 = int(input('Digite o segundo número: '))
s = a1+b2
print('A soma entre {} e {} vale {}'.format(a1, b2, s))
