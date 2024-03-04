package actividad2;

public class Banc {
    private String NumeroCuenta;
    private double Saldo;
    private String Titular;

    public Banc(String numeroCuenta, double saldo, String titular) {
        NumeroCuenta = numeroCuenta;
        Saldo = saldo;
        Titular = titular;
    }

    public String getNumeroCuenta() {
        return NumeroCuenta;
    }

    public double getSaldo() {
        return Saldo;
    }

    public String getTitular() {
        return Titular;
    }

    public void ingreso(double cantidad) {
        this.Saldo += cantidad;
    }

    public void retirada(double cantidad){
        this.Saldo -= cantidad;
    }
}
