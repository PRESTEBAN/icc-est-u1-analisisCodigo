import java.util.Random;

public class Benchmarking {
    
    private MetodosOrdenamiento metodosOrdenamiento;
    
    public Benchmarking(){
        long inicioMillis = System.currentTimeMillis();//tiempo epoch
        long inicioNano = System.nanoTime();// desde que se ejecuta el  programa
        
        //System.out.println(inicioMillis); //tiempo epoch
        //System.out.println(inicioNano); // desde que se ejecuta el  programa

        metodosOrdenamiento = new MetodosOrdenamiento();
        int[] arreglo = generarAleatorio(1000000);
        Runnable tarea = () -> metodosOrdenamiento.burbujaTradicional(arreglo);
         // manda la fncion de metodosOrdenamiento en una variable tipo runnable
        double tiempoNano = medirconNanoTime(tarea);
        double tiempoMillis = medirConCurrentTime(tarea);

        System.out.println("Tiempo con nanoTime: " + tiempoNano + " segundos");
        System.out.println("Tiempo con currentTimeMillis: " + tiempoMillis + " segundos");
    }

     public double medirconNanoTime(Runnable tarea) {
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1000000000.0;  
    }

    public double medirConCurrentTime(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();

        return (fin-inicio) / 1000.0;
    }

    public int[] generarAleatorio(int tamano){
        int[] arreglo = new int[tamano];
         Random rand = new Random();
         for (int i = 0; i < tamano; i++) {
            arreglo[i] = rand.nextInt(10000);  // Genera números aleatorios entre 0 y 9999
        }

        return arreglo;
    }
}
