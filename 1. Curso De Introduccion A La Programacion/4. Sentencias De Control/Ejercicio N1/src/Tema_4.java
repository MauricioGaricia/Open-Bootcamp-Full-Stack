public class Tema_4 {

    public static void main(String[] args) {
        int Numero_If = -8;
        int Numero_While = 0;
        int Numero_Do_While = 3;
        int Numero_For = 2;
        String Estacion = "OTOÑO";

        System.out.println("SOLUCION EJERCICIO 1 - IF");
        if (Numero_If>0){
            System.out.println("El Valor Es POSITIVO");
        } else if (Numero_If<0){
            System.out.println("El Valor Es NEGATIVO");
        } else{
            System.out.println("El Valor Es 0 ");
        }

        System.out.println("SOLUCION EJERCICIO 2 - WHILE");
        if (Numero_While>=3){
            System.out.println("Ha ingresado un numero mayor o igual a 3 por lo tanto no ha entrado al Bucle");
        }else {
            while (Numero_While < 3) {
                Numero_While = Numero_While + 1;
                System.out.println("La variable While ahora es: " + Numero_While);
            }
        }

        System.out.println("SOLUCION EJERCICIO 3 - DO WHILE");
        do{
            Numero_Do_While = Numero_Do_While + 1;
            System.out.println("La Variable Do While ahora es: " + Numero_Do_While);
        }while(Numero_Do_While<3);

        System.out.println("SOLUCION EJERCICIO 4 - FOR");

        if (Numero_For<= 3){ //Me parecio conveniente poner un if anterior para que muestre un mensaje si no entra al bucle

            for (;Numero_For<= 3; Numero_For++) {
                System.out.println("La variable For ahora es: " + Numero_For);
            }

        } else{
            System.out.println("Ha ingresado un numero mayor a 3 por lo tanto no ha entrado al Bucle");
        }

        switch(Estacion) {

            case "VERANO":
                System.out.println("SOLUCION EJERCICIO 5 - SWITCH");
                System.out.println("Es VERANO");
                break;

            case "INVIERNO":
                System.out.println("SOLUCION EJERCICIO 5 - SWITCH");
                System.out.println("Es INVIERNO");
                break;

            case "PRIMAVERA":
                System.out.println("SOLUCION EJERCICIO 5 - SWITCH");
                System.out.println("Es PRIMAVERA");
                break;

            case "OTOÑO":
                System.out.println("SOLUCION EJERCICIO 5 - SWITCH");
                System.out.println("Es OTOÑO");
                break;

            default:
                System.out.println("SOLUCION EJERCICIO 5 - SWITCH");
                System.out.println("NO HA INGRESADO UNA ESTACION O INGRESO EN MINUSCULAS");

        }

    }

}