public class Tema8 {

    public static void main(String[] args) {
        Persona Persona = new Persona();
        Persona.setNombre("Carlos");
        Persona.setEdad(25);
        Persona.setTelefono(123456789);
        System.out.println("Nombre: " + Persona.getNombre());
        System.out.println("Edad: " + Persona.getEdad());
        System.out.println("Telefono: " + Persona.getTelefono());


    }
    static class Persona {
        private String nombre;
        private int edad;
        private int telefono;

        public void setNombre (String nombre){
            this.nombre = nombre;
        }
        public void setEdad (int edad){
            this.edad = edad;
        }
        public void setTelefono (int telefono){
            this.telefono = telefono;
        }
        public String getNombre(){
            return this.nombre;
        }
        public int getEdad(){
            return this.edad;
        }
        public int getTelefono(){
            return this.telefono;
        }

    }

}