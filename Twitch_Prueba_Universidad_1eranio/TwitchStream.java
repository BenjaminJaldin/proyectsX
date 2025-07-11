import java.util.Scanner;

public class TwitchStream {
    public static void main(String[] args) {
        CanalTwitch canalTwitch1 = new CanalTwitch("AuronPlay");
        CanalTwitch canalTwitch2 = new CanalTwitch("LuzuVlogs");

        Subscripcion subscriptor1 = new Subscripcion("Usuario1");

        subscriptor1.subscribirACanal(canalTwitch1);
        subscriptor1.subscribirACanal(canalTwitch2);
        canalTwitch1.Stream("Partida de Fortnite");
        canalTwitch2.Stream("Partida de Minecraft");

        Scanner scanner = new Scanner(System.in);
        int option;

        do {
            System.out.println("=== MENU ===");
            System.out.println("1. Ver stream de " + canalTwitch1.getNombreCanal());
            System.out.println("2. Ver stream de " + canalTwitch2.getNombreCanal());
            System.out.println("3. Suscribirse a un canal");
            System.out.println("4. Desuscribirse de un canal");
            System.out.println("5. Activar notificaciones");
            System.out.println("6. Desactivar notificaciones");
            System.out.println("7. Ver suscripciones");
            System.out.println("0. Salir");
            System.out.print("Seleccione una opción: ");
            option = scanner.nextInt();

            switch (option) {
                case 1:
                    System.out.println("Viendo el stream de " + canalTwitch1.getNombreCanal());
                    break;
                case 2:
                    System.out.println("Viendo el stream de " + canalTwitch2.getNombreCanal());
                    break;
                case 3:
                    scanner.nextLine();
                    System.out.println("=== CANALES ===");
                    System.out.println("1. " + canalTwitch1.getNombreCanal());
                    System.out.println("2. " + canalTwitch2.getNombreCanal());
                    System.out.print("Seleccione un canal para suscribirse: ");
                    int canalOption = scanner.nextInt();
                    scanner.nextLine();
                    if (canalOption == 1) {
                        subscriptor1.subscribirACanal(canalTwitch1);
                    } else if (canalOption == 2) {
                        subscriptor1.subscribirACanal(canalTwitch2);
                    } else {
                        System.out.println("Opción inválida. Intente nuevamente.");
                    }
                    break;
                case 4:
                    scanner.nextLine();
                    System.out.println("=== CANALES ===");
                    System.out.println("1. " + canalTwitch1.getNombreCanal());
                    System.out.println("2. " + canalTwitch2.getNombreCanal());
                    System.out.print("Seleccione un canal para desuscribirse: ");
                    int desuscribirOption = scanner.nextInt();
                    scanner.nextLine();
                    if (desuscribirOption == 1) {
                        subscriptor1.desuscritoDeCanal(canalTwitch1);
                    } else if (desuscribirOption == 2) {
                        subscriptor1.desuscritoDeCanal(canalTwitch2);
                    } else {
                        System.out.println("Opción inválida. Intente nuevamente.");
                    }
                    break;
                case 5:
                    subscriptor1.activarNotificaciones();
                    scanner.nextLine();
                    System.out.println("=== CANALES ===");
                    System.out.println("1. " + canalTwitch1.getNombreCanal());
                    System.out.println("2. " + canalTwitch2.getNombreCanal());
                    System.out.print("Seleccione un canal para desuscribirse: ");
                    int activarnoti = scanner.nextInt();
                    scanner.nextLine();
                    if (activarnoti == 1) {
                        canalTwitch1.Stream("Partida de Fortnite");
                    } else if (activarnoti == 2) {
                         canalTwitch2.Stream("Partida de Minecraft");
                    } else {
                        System.out.println("Opción inválida. Intente nuevamente.");
                    }
                    break;
                case 6:
                    subscriptor1.desactivarNotificaciones();
                    break;
                case 7:
                    System.out.println("=== SUSCRIPCIONES ===");
                    System.out.println(subscriptor1.getNombre() + " está suscrito a los siguientes canales:");
                    if (subscriptor1.estaSuscrito()) {
                        for (CanalTwitch canal : subscriptor1.getCanalesSuscritos()) {
                            System.out.println("- " + canal.getNombreCanal());
                        }
                    } else {
                        System.out.println("Ningún canal");
                    }
                    break;
                case 0:
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    System.out.println("Opción inválida. Intente nuevamente.");
                    break;
            }

            System.out.println();
        } while (option != 0);

        scanner.close();
    }
}
