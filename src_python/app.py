import benchmarking as Ben
from metodos_Ordenamiento import MetodosOrdanamiento
import benchmarking as bM

if __name__ == "__main__":
    print("Funciona")
    metodos = MetodosOrdanamiento()
    tam = 10000
    benchmark = bM.Benchmarking()
    arreglo_base = benchmark.build_arreglo(tam)
    
    metodos = {
        "burbuja": MetodosOrdanamiento().sortByBubble, #Referencia a la funcion, no es el ejecutable de la función
        "seleccion": MetodosOrdanamiento().sort_seleccion
    }
    
    resultados = []
    
    for nombre,metodo in metodos.items():
        tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
        tuplaResultado = (tam,nombre,tiempo)
        resultados.append(tuplaResultado)
        
    for resultado in resultados:
        tam,nombre,tiempo = resultado
        print(f"Tamaño: {tam}, Metodo: {nombre}, Tiempo: {tiempo:.6f} segundos") #el .6f dice que tenga solo 6 decimales