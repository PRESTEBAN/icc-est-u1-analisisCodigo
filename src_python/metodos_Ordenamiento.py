class MetodosOrdanamiento:
    def sortByBubble(self, arreglo): #obligatorio poner el self en cada metodo
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i+1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i],arreglo[j] = arreglo[j],arreglo[i]
        return arreglo
    
    def sort_seleccion(self,array):
        array = array.copy()
        n = len(array)
        for i in range(n):
            indice_minimo = i
            for j in range(i+1, n):
                if array[j] < array[indice_minimo]:
                    indice_minimo = j
            array[i], array[indice_minimo] = array[indice_minimo], array[i]
        return array