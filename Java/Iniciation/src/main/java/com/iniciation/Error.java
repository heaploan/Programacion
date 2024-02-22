package com.iniciation;
public class Error {
    public static void main(String[] name){
        float x = 3.2F; // camabiamos int por float
        float y = Float.parseFloat(name[0]); // creamos variable 'y' con valor del argumento introducido
        float result = x + y; // creamos variable result del x+y
        System.out.printf("%.2f",result); // imprimimos con formato de %.2f y result.
    }
}
