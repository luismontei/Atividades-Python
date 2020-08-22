#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo

preco=float(input('Quanto ganha por hora? '))
horas=float(input('Quantas horas que você trabalhou ao mês? '))
salariobruto = preco*horas
inss = salariobruto*0.08
ir = salariobruto*0.11
sindicato = salariobruto* 0.05
descontos = salariobruto*0.25
salarioliquido = salariobruto - descontos
print(' Salário bruto :{}\n IR :{}\n INSS :{}\n Sindicato :{}\n Salário liquido :{}\n Descontos :{}'.format(salariobruto,ir,inss,sindicato,salarioliquido,descontos))












