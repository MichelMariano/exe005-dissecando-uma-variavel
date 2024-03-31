# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')

print('O tipo primitivo desse é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É um alfabético? ', a.isalpha())
print('Está em Maiúculas? ', a.isupper())
print('Está em minusculas? ', a.islower())
print('Está Capitalizada? ', a.istitle())

#esse (a) chamamos de objeto, e todo objeto tem caracteriscas e realiza funcionalidades,
#eles tem ATRIBUTOS e METODOS, no caso do exercicios acima, como tem parenteses em cada
#um deles, então estamos trabalhando Metodos. Todo objeto strings tem metodos (is. ... isspace
#isspace, isalpha...)
