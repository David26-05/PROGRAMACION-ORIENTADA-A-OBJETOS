//EJEMPLO POO
import java.util.Scanner;
public class TemperaturaPOO {

    public static void main(String[] args) {
        SemanaClimatica semana = new SemanaClimatica();
        semana.ingresarTemperaturas();
        semana.mostrarResumenSemanal();
    }
}

class DiaClimatico {
    private String nombreDia;
    private double temperatura;

    public DiaClimatico(String nombreDia) {
        this.nombreDia = nombreDia;
    }

    // Getters y Setters (encapsulamiento)
    public String getNombreDia() {
        return nombreDia;
    }

    public double getTemperatura() {
        return temperatura;
    }

    public void setTemperatura(double temperatura) {
        this.temperatura = temperatura;
    }
}

class SemanaClimatica {
    private DiaClimatico[] dias;
    private static final String[] NOMBRES_DIAS = {"Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"};

    public SemanaClimatica() {
        dias = new DiaClimatico[7];
        for (int i = 0; i < 7; i++) {
            dias[i] = new DiaClimatico(NOMBRES_DIAS[i]);
        }
    }

    // Método para ingresar temperaturas
    public void ingresarTemperaturas() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese las temperaturas de la semana:");

        for (DiaClimatico dia : dias) {
            System.out.print("Temperatura para " + dia.getNombreDia() + ": ");
            double temp = scanner.nextDouble();
            dia.setTemperatura(temp);
        }
        scanner.close();
    }

    // Método para calcular promedio semanal
    public double calcularPromedioSemanal() {
        double suma = 0;
        for (DiaClimatico dia : dias) {
            suma += dia.getTemperatura();
        }
        return suma / dias.length;
    }

    // Método para mostrar resumen
    public void mostrarResumenSemanal() {
        System.out.println("\nResumen de temperaturas:");
        for (DiaClimatico dia : dias) {
            System.out.printf("%-10s: %.1f°C%n", dia.getNombreDia(), dia.getTemperatura());
        }
        System.out.printf("\nEl promedio semanal es: %.1f°C%n", calcularPromedioSemanal());
    }
}
