class MetodosOrdanamiento:
    def sortByBubble(self, arreglo): #obligatorio poner el self en cada metodo
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i+1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i],arreglo[j] = arreglo[j],arreglo[i]
        return arreglo
    
    
                     
            
        
        