public class Tema9 {

    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        cliente.nombre = "Carlos";
        cliente.edad = 45;
        cliente.telefono = 98765442;
        cliente.credito = 50000;
        System.out.println("Nombre de Cliente: " + cliente.nombre);
        System.out.println("Edad del cliente: " + cliente.edad);
        System.out.println("Telefono del cliente: " + cliente.telefono);
        System.out.println("Credito disponible del cliente: " + cliente.credito);

        System.out.println("                ");

        Trabajador trabajador = new Trabajador();
        trabajador.nombre = "Pedro";
        trabajador.edad = 25;
        trabajador.telefono = 345678999;
        trabajador.salario = 10000;
        System.out.println("Nombre del Trabajador: " + trabajador.nombre);
        System.out.println("Edad del Trabajador: " + trabajador.edad);
        System.out.println("Telefono del Trabajador: " + trabajador.telefono);
        System.out.println("Salario del Trabajador: " + trabajador.salario);
    }
    static class Persona {
        String nombre;
        int edad;
        int telefono;
    }
    static class Cliente extends Persona{
        double credito;
    }

    static class Trabajador extends Persona {
        double salario;
    }


}