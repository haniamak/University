package figury;

public class Trojkat {
  public Punkt x;
  public Punkt y;
  public Punkt z;

  public Trojkat(Punkt x, Punkt y, Punkt z) {
    if(!Punkt.czyRozne(y, z) || !Punkt.czyRozne(x, z) || !Punkt.czyRozne(x, y)) {
      throw new IllegalArgumentException("Wybrales dwa razy ten sam punkt. Nie mozna utworzyc trojkata");
    }
    if(Punkt.czyWspoliniowe(x, y, z)) {
      throw new IllegalArgumentException("Wybrales punkty ktore sa wspolliniowe. Nie mozna utworzyc trojkata");
    }
    this.x = x;
    this.y = y;
    this.z = z;
  }

  public Trojkat przesun(Wektor v) {
    Punkt newx = x.przesun(v);
    Punkt newy = y.przesun(v);
    Punkt newz = z.przesun(v);
    return new Trojkat(newx, newy, newz);
  }

  public Trojkat obroc(Punkt p, double kat) {
    Punkt newx = x.obroc(p, kat);
    Punkt newy = y.obroc(p, kat);
    Punkt newz = z.obroc(p, kat);
    return new Trojkat(newx, newy, newz);
  }

  public Trojkat odbij(Prosta p) {
    Punkt newx = x.odbij(p);
    Punkt newy = y.odbij(p);
    Punkt newz = z.odbij(p);
    return new Trojkat(newx, newy, newz);
  }
}
