Ejemplo de Programacion Tradicional
import java.util.Scanner;
public class TemperaturaPT {

// Constante para los días de la semana
    private static final String[] DIAS_SEMANA = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"};
    
    public static void main(String[] args) {
        double[] temperaturas = new double[7]; // Array para almacenar las temperaturas de la semana
        
        // Llamada a la función para ingresar datos
        ingresarTemperaturas(temperaturas);
        
        // Llamada a la función para calcular y mostrar el promedio
        mostrarPromedioSemanal(temperaturas);
    }
    
    /**
     * Función para ingresar las temperaturas de cada día de la semana
     * @param temps Array donde se almacenarán las temperaturas
     */
    public static void ingresarTemperaturas(double[] temps) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Ingrese las temperaturas de la semana:");
        
        for (int i = 0; i < DIAS_SEMANA.length; i++) {
            System.out.print("Temperatura para " + DIAS_SEMANA[i] + ": ");
            temps[i] = scanner.nextDouble();
        }
        
        scanner.close();
    }
    
    /**
     * Función que calcula el promedio de temperaturas de la semana
     * @param temps Array con las temperaturas de la semana
     * @return El promedio de temperaturas
     */
    public static double calcularPromedioSemanal(double[] temps) {
        double suma = 0;
        
        for (double temp : temps) {
            suma += temp;
        }
        
        return suma / temps.length;
    }
    
    /**
     * Función que muestra las temperaturas y el promedio semanal
     * @param temps Array con las temperaturas de la semana
     */
    public static void mostrarPromedioSemanal(double[] temps) {
        System.out.println("\nResumen de temperaturas:");
        
        // Mostrar temperaturas por día
        for (int i = 0; i < DIAS_SEMANA.length; i++) {
            System.out.printf("%-10s: %.1f°C%n", DIAS_SEMANA[i], temps[i]);
        }
        
        // Mostrar promedio
        double promedio = calcularPromedioSemanal(temps);
        System.out.printf("\nEl promedio semanal es: %.1f°C%n", promedio);
    }
}

