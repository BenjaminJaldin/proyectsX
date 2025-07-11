import java.util.ArrayList;
import java.util.List;

class Subscripcion implements Observer 
{
    
    private String nombre;
    private boolean subscrito;
    private boolean activarNotificaciones;
    private List<CanalTwitch> canalesSuscritos;

    public Subscripcion(String nombre) 
    {
        this.nombre = nombre;
        this.subscrito = true;
        this.activarNotificaciones = true;
        this.canalesSuscritos = new ArrayList<>();
    }

    public void update(String mensaje) 
    {
        if (activarNotificaciones) {
            System.out.println(nombre + " ha recibido una notificación: " + mensaje);
        }
    }

    public void desuscritoDeCanal(CanalTwitch canal) 
    {
        canal.detach(this);
        canalesSuscritos.remove(canal);
        System.out.println(nombre + " se ha desuscrito de " + canal.getNombreCanal());
    }

    public void subscribirACanal(CanalTwitch canal)
    {
        canal.attach(this);
        canalesSuscritos.add(canal);
        System.out.println(nombre + " se ha suscrito al canal de " + canal.getNombreCanal());
    }

    public void activarNotificaciones() 
    {
        activarNotificaciones = true;
        System.out.println(nombre + " ha activado las notificaciones");
    }

    public void desactivarNotificaciones() 
    {
        activarNotificaciones = false;
        System.out.println(nombre+ " ha desactivado las notificaciones.");    
    }

    public boolean estaSuscrito() 
    {
        return subscrito;
    }

    public String getNombre() 
    {
        return nombre;
    }

    public List<CanalTwitch> getCanalesSuscritos() 
    {
        return canalesSuscritos;
    }
}