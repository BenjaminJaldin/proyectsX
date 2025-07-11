public class CanalTwitch extends Observable {
    private String nombreCanal;

    public CanalTwitch(String nombreCanal) {
        this.nombreCanal = nombreCanal;
    }

    public String getNombreCanal() {
        return nombreCanal;
    }

    public void Stream(String tituloStream) {
        String message = nombreCanal + " ha iniciado una transmisión: " + tituloStream;
        notifyObservers(message);
    }
}
