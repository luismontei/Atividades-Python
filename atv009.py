##Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
##Para homens: (72.7*h) - 58
##Para mulheres: (62.1*h) - 44.7
h = float(input('Informe a sua altura: '))
sexo = input('Informe o seu sexo com m ou f: ')
if (sexo == 'f') :
    f = (62.1 * h) - 44.7
    print('O seu peso ideal é {} '.format(f))
else:
    m = (72.7*h) - 58
    print('O seu peso ideal é {}'.format(m))

