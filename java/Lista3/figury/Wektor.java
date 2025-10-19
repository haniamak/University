package figury;

public final class Wektor {

  public final double dx;
  public final double dy;

  public Wektor(double dx, double dy) {
    this.dx = dx;
    this.dy = dy;
  }

  public static Wektor skladajWektory(Wektor w1, Wektor w2) {
    double newx = w1.dx + w2.dx;
    double newy = w1.dy + w2.dy;
    return new Wektor(newx, newy);
  }

}
