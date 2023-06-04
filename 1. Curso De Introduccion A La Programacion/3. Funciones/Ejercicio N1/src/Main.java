public class Main {

    public static void main(String[] args) {
        Suma(1,2,3);

        Coche Mi_Coche = new Coche();
        Mi_Coche.Incrementar_Puertas();
        System.out.println("La Cantidad De Puertas Que Tiene El Coche Es: "+Mi_Coche.Puertas);
    }
    public static int Suma(int a, int b, int c) {
        int Resultado;
        Resultado = a + b + c;
        System.out.println("El Resultado De La Suma Es: "+Resultado);
        return Resultado;
    }
}

class Coche {
    public int Puertas = 1;
    public void Incrementar_Puertas() {
        this.Puertas++;
    }
}