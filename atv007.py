##Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
fah = float(input('Indique a sua temperatura: '))
c = (fah-32)/1.8
print('A temperatura de fahrenheit é {} a conversão para celsius deu {}'.format(fah,c))
