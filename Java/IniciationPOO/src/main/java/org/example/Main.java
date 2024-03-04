package org.example;

public class Main {
    public static void main(String[] args) {
        Planeta planeta1 = new Planeta(4000, 3000, 32020, 300000, 1, "Vobunus");
        Planeta planeta2 = new Planeta(5000, 4000, 4589, 400000, 2, "Indora");
        System.out.print("ID: " + planeta1.getIdNumber() + "\nPlaneta: " + planeta1.getName()+"\nDensidad: " + planeta1.getDensity() );
        System.out.print("Distancia al Sol: " + planeta1.getDistanceToSun() +"\nDiametro: " + planeta1.getDiameter());
        System.out.print("\nID: " + planeta2.getIdNumber() + "\nPlaneta: " + planeta2.getName()+"\nDensidad: " + planeta2.getDensity() );
        System.out.print("Distancia al Sol: " + planeta2.getDistanceToSun() +"\nDiametro: " + planeta2.getDiameter());

    }
}

