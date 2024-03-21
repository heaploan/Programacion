package actividad1;

public class Planeta {
    private int mass;
    private int density;
    private int diameter;
    private int distanceToSun;
    private int idNumber;
    private String name;

    public Planeta(int mass, int density, int diameter, int distanceToSun, int idNumber, String name) {
        this.mass = mass;
        this.density = density;
        this.diameter = diameter;
        this.distanceToSun = distanceToSun;
        this.idNumber = idNumber;
        this.name = name;
    }

    public int getMass() {return mass;}
    public int getDensity() {return density;}
    public int getDiameter() {return diameter;}
    public int getDistanceToSun() {return distanceToSun;}
    public int getIdNumber() {return idNumber;}
    public String getName() {return name;}

}
