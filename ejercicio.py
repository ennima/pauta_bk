import os

ejercicios_circuito = 5
max_repeticiones = 4


ejercicio_acumulado = 0
circuito_acumulado = 0
for i in range(0,max_repeticiones):
	print("Repeticiones: ",i + 1)
	ejercicio_acumulado += i + 1
	print("Acumulado: ",ejercicio_acumulado)
	circuito_acumulado = ejercicio_acumulado * ejercicios_circuito
	print("Circuito Acumulado:",circuito_acumulado)