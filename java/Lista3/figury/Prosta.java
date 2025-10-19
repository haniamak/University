package figury;

public final class Prosta {

  public final double a;
  public final double b;
  public final double c;

  public Prosta(double a, double b, double c) {
    this.a = a;
    this.b = b;
    this.c = c;
  }

  public static Prosta przesunOWektor(Prosta k, Wektor w) {
    double newa = k.a;
    double newb = k.b;
    double newc = k.c - (k.a * w.dx) - w.dy;
    return new Prosta(newa, newb, newc);
  }

  public static boolean czyRownolegle(Prosta k, Prosta l) {
    if (k.a == l.a) {
      return true;
    } else {
      return false;
    }
  }

  public static boolean czyProstopadle(Prosta k, Prosta l) {
    if (k.a * l.a == -1) {
      return true;
    } else {
      return false;
    }
  }

  public static Punkt punktPrzeciecia(Prosta k, Prosta l) {
    if (czyRownolegle(k, l) == true) {
      throw new IllegalArgumentException("Proste sa rownolegle");
    }
    double px = ((k.c * l.b) - (k.b * l.c)) / ((k.b * l.a) - (k.a * l.b));
    double py = ((k.a * l.c) - (k.c * l.a)) / ((k.b * l.a) - (k.a * l.b));
    return new Punkt(px, py);
  }

}
