




def updateGusano(gusano,bloque):
	count  = len(gusano)-1
	lstNuevoGusano = range(len(gusano))
	#Recorre el gusano antiguo y lo pone en el nuevo pero descartando
	#la ultima posicion
	while count > 0 :
		lstNuevoGusano[count] = gusano[count-1]
		count = count - 1
	lstNuevoGusano[0] = bloque

	return lstNuevoGusano

def addGusano(gusano,bloque):
	count  = len(gusano)-1
	lstNuevoGusanoNew = range(len(gusano)+1)
	#Recorre el gusano antiguo y lo pone en el nuevo pero descartando
	#la ultima posicion
	while count > 0 :
		lstNuevoGusanoNew[count] = gusano[count-1]
		count = count - 1
	lstNuevoGusanoNew[0] = bloque

	return lstNuevoGusanoNew
