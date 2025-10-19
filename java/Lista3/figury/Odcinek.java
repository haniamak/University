package figury;

public class Odcinek {
  public Punkt a;
  public Punkt b;

  public Odcinek(Punkt a, Punkt b) {
    if (!Punkt.czyRozne(a, b)) {
      throw new IllegalArgumentException("Wybrales dwa razy ten sam punkt. Nie mozna utworzyc odcinka");
    }
    this.a = a;
    this.b = b;
  }

  public Odcinek przesun(Wektor v) {
    Punkt newa = a.przesun(v);
    Punkt newb = b.przesun(v);
    return new Odcinek(newa, newb);
  }

  public Odcinek obroc(Punkt p, double kat) {
    Punkt newa = a.obroc(p, kat);
    Punkt newb = b.obroc(p, kat);
    return new Odcinek(newa, newb);
  }

  public Odcinek odbij(Prosta p) {
    Punkt newa = a.odbij(p);
    Punkt newb = b.odbij(p);
    return new Odcinek(newa, newb);
  }
}
