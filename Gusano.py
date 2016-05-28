


def actualizaGusano(gusano,bloque):
	count  = len(gusano)-1
	lstNuevoGusano = newArray
	#Recorre el gusano antiguo y lo pone en el nuevo pero descartando
	#la ultima posicion
	while count > 0 :
		lstNuevoGusano[count] = gusano[count-1]
	lstNuevoGusano[0] = bloque
