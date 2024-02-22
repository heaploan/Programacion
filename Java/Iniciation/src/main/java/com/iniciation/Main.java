package com.iniciation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/*
ENTEROS:
-------------------------------
byte, 1 byte, [-128, 127]
short, 2 bytes, [-32K, 32K]
int, 4 bytes, [-2B, 2B]
long, 8 bytes
-------------------------------
DECIMALES:
-------------------------------
float, 4 bytes
double, 8 bytes
-------------------------------
char, 2 bytes, 'A, B, C'
boolean, 1 byte, true / false
*/

public class Main {
    public static void main(String[] args) throws IOException {
        /*
        String name = "";
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Escribe tu nombre: ");
        name = input.readLine();
        System.out.println("Hello " + name + "!");
        Scanner input = new Scanner (System.in); / este suele dar error y por eso no se usa mucho.
        int entire = 0;
        short small = 2;
        long big = 12345;
        double bigFloat = 5.6;
        float decimal = 5.6f;
        System.out.println("Introduce un numero entero:");
        entire = Integer.parseInt(input.readLine());
        System.out.println("Numero introducido: " + entire);
        */
        int a, b, c;
        a = 1;
        b = 4;
        c = a + b;
        System.out.println(c);
        /*
        Creas variables diciendo el tipo que son, se les asigna un valor a 'a' y 'b' y se hace la suma en c.
        Al final se imprime 'c'
        */
        System.out.println(args[0]);
        System.out.println(args[1]);
    }
}