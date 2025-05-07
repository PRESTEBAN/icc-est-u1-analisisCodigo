from matplotlib import pyplot as plt
import benchmarking as Ben
from metodos_Ordenamiento import MetodosOrdanamiento
import benchmarking as bM
from datetime import datetime

if __name__ == "__main__":
    print("Funciona")
    metodos = MetodosOrdanamiento()
    benchmark = bM.Benchmarking()
    
    tamanios = [500,1000,2000]
    resultados = []
    
    for tam in tamanios:
        arreglo_base = benchmark.build_arreglo(tam)
    
        metodos = {
            "burbuja": MetodosOrdanamiento().sortByBubble, #Referencia a la funcion, no es el ejecutable de la función
            "seleccion": MetodosOrdanamiento().sort_seleccion
        }
    
        for nombre,metodo in metodos.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
            tuplaResultado = (tam,nombre,tiempo)
            resultados.append(tuplaResultado)
        
        for resultado in resultados:
            tam,nombre,tiempo = resultado
            print(f"Tamaño: {tam}, Metodo: {nombre}, Tiempo: {tiempo:.6f} segundos") #el .6f dice que tenga solo 6 decimales
        
    
    tiempos_by_metodo={
        "burbuja" : [],
        "seleccion" : []
    }
    
    #clasificar los tiempos segun el metodo
    for tam,nombre,tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)
    
        
    fecha_hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    #crear una gráfica
    fig = plt.figure(figsize=(10,6))
    fig.canvas.manager.set_window_title(f"Esteban Pesantez - {fecha_hora_actual}") 
    #graficar una lina de tiempo para cada metodo
    # el x sean el tamanio del arreglo
    # el y sea los tiempos obtenidos
    
    for nombre,tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label=nombre, marker='o')
        
    
  
    #Agregar los parametros
    
    plt.title(f"Esteban Pesantez - {fecha_hora_actual}")
    plt.xlabel("Tiempos obtenidos")
    plt.ylabel("Tamanios arreglo")
    plt.legend()
    plt.grid()
    plt.show()