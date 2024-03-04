package com.iniciation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Locale;

public class FirstClass {
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException{
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Introduce tu edad:");
            int edad = Integer.parseInt(br.readLine());
            if (edad >= 50) {
                System.out.println("Estás en la mejor edad");
            } else if (edad >= 30) {
                if (edad >= 40) {
                    System.out.println("Edad de oro");
                }
                System.out.println("Ni chicha ni limoná");
            } else {
                System.out.println("Disfruta de la vida");
            }
            System.out.println("De qué instrumento quieres partituras?");
            String instrumento = br.readLine();
            switch(instrumento.toLowerCase()){
                case "piano":
                    System.out.println("Tenemos 8888 partituras");
                    break;
                case "guitarra":
                    System.out.println("Tenemos 324 partituras");
                    break;
                case "sexofon":
                    System.out.println("Tenemos 56 partituras");
                    break;
                default:
                    System.out.println("De ese instrumento no tenemos partituras");
            }
        // Bucle for
        for(int i=0; i<=10; i+=1){
            System.out.println(i);
            //i += 1;
            //i = i+1;
        }
        // Bucle while (while-do)
        int contador = 0;
        while(contador <= 10){
            System.out.println(contador);
            contador++;
        }
        // Bucle do while
        // normalmente se usa para menús
        int n = 0;
        do{
            System.out.println("n");
            n++;
        } while (n<=100);
    }
}
