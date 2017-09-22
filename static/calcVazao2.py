arraySize_1 = 100000000
searchTime_1 = [2.041, 2.114, 2.276, 2.157, 2.802, 3.723, 4.618, 5.014, 5.204, 5.240, 6.340, 5.489, 5.609, 5.592, 5.800]

arraySize_2 = [100000000, 110000000, 120000000, 130000000, 140000000, 150000000, 160000000, 170000000, 180000000, 190000000, 200000000 ] 
searchTime_2 = [1.562, 1.716, 1.880, 2.302, 2.177, 2.365, 2.729, 2.641, 2.849, 2.957, 3.129]

lista = []
for i in range(len(arraySize_2)):
	#Vazão questão 01
	#calc = arraySize_1 / i
	#print("%.2f" %calc)

	#tempo de serviço questão 01
	#s = i / arraySize_1
	#print("%.10f"%s)

	#vazão questão 02
	#calc = arraySize_2[i] / searchTime_2[i]
	#calc = "%.2f" %calc
	#lista.append(float(calc))

	#tempo de serviço
	calc = searchTime_2[i] / arraySize_2[i]
	calc = "%.12f" %calc
	lista.append(calc)

print(lista)

