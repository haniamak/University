package figury;

public class Punkt {

  private double x;
  private double y;

  public Punkt(double x, double y) {
    this.x = x;
    this.y = y;
  }

  public double getX() {
    return this.x;
  }

  public double getY() {
    return this.y;
  }

  public Punkt przesun(Wektor v) {
    double newx = this.x + v.dx;
    double newy = this.y + v.dy;
    return new Punkt(newx, newy);
  }

  public Punkt obroc(Punkt p, double kat) {
    double katWRadianach = kat * Math.PI / 180.0;
    double newx = p.x + (this.x - p.x) * Math.cos(katWRadianach) - (this.y - p.y) * Math.sin(katWRadianach);
    double newy = p.y + (this.x - p.x) * Math.sin(katWRadianach) + (this.y - p.y) * Math.cos(katWRadianach);
    return new Punkt(newx, newy);
  }

  public Punkt odbij(Prosta p) {
    Prosta pprostopadla = new Prosta(-p.b, p.a, (p.b * this.x - p.a * this.y));
    Punkt srodek = new Punkt(((p.b * pprostopadla.c - pprostopadla.b * p.c) / (p.a * pprostopadla.b - pprostopadla.a * p.b)), ((p.c * pprostopadla.a - pprostopadla.c * p.a) / (p.a * pprostopadla.b - pprostopadla.a * p.b)));
    double newx = 2 * srodek.x - this.x;
    double newy = 2 * srodek.y - this.y;
    return new Punkt(newx, newy);
  }

  public static boolean czyRozne(Punkt a, Punkt b) {
    if ((a.getX() == b.getX()) && (a.getX() == b.getY())) {
      return false;
    } else
      return true;
  }

  public static boolean czyWspoliniowe(Punkt a, Punkt b, Punkt c) {
    double wk1 = (a.y - b.y) / (a.x - b.x);
    double wk2 = (a.y - c.y) / (a.x - c.x);
    if (wk1 == wk2) {
      return true;
    } else {
      return false;
    }
  }
}