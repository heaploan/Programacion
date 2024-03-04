package actividad2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        Banc[] cuentas = new Banc[2];
        cuentas[0] = new Banc("E341234556", 130, "Jeremy");
        cuentas[1] = new Banc("E567812334", 300, "Naria");
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int option;
        int cuentaCliente;
        double ingreso;
        double retirada;
        do {
            System.out.println("¿De qué cuenta quieres consultar el saldo?");
            System.out.println("1: " + cuentas[0].getNumeroCuenta());
            System.out.println("2: " + cuentas[1].getNumeroCuenta() + "\n");
            cuentaCliente = Integer.parseInt(input.readLine()) - 1;
        } while (cuentaCliente +1 > cuentas.length);

        do {
            System.out.println("1. Consultar saldo.");
            System.out.println("2. Ingresar dinero.");
            System.out.println("3. Sacar dinero.");
            System.out.println("4. Realizar transferencia (sacar dinero de una cuenta para ponerlos en otra).");
            System.out.println("5. Salir.");
            option = Integer.parseInt(input.readLine());
            if (option == 1) {
                System.out.println("Tu saldo es: " + cuentas[cuentaCliente].getSaldo());
            } else if (option == 2) {
                ingreso = Double.parseDouble(input.readLine());
                cuentas[cuentaCliente].ingreso(ingreso);
                System.out.println("Ingreso realizado correctamente.");
            } else if (option == 3) {
                retirada = Double.parseDouble(input.readLine());
                cuentas[cuentaCliente].retirada(retirada);
                System.out.println("Retiro realizado con éxito.");
            } else if (option == 4) {
                System.out.println("Opción 4");
            }
        } while (option != 5);
    }
}

