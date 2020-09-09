with open('nombre.txt') as myFile:
	for num, nombre in enumerate(myFile,1000):
		with open('corte.txt') as myFile2:
			for num2, corte in enumerate(myFile2,1000):
				if num == num2:
					print('dato1:'+nombre.replace('\n', '')+' corte:'+nombre.replace('\n', ''))