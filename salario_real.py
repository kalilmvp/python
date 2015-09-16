# coding: utf-8

salario = int(input("Salario?"))
imposto = input("Imposto em % (Ex: 27.5%)?")

if not imposto:
	imposto = 27.5
else:
	imposto = float(imposto)

if imposto < 10:
	print('Baixo')
elif imposto >= 10 and imposto <= 27:
	print('Médio')
elif imposto >= 27 and imposto <= 100:
	print('Alto')
else:
	print('Inválido')

print("O valor real e: {0}".format(salario - (salario * (imposto * 0.01))))