package obliczenia;

public class Doda extends Oper2 {

  public Doda(Wyrazenie wartosc, Wyrazenie wartosc2) {
    super(wartosc, wartosc2);
  }

  @Override
  public double oblicz() {
    return (wartosc.oblicz() + wartosc2.oblicz());
  }

  @Override
  public String toString() {
    return "(" + wartosc.toString() + " + " + wartosc2.toString() + ")";
  }

  @Override
  public boolean equals(Object o) {
    if (o == this) {
      return true;
    }
    if (o == null || !(o instanceof Doda)) {
      return false;
    }
    Doda other = (Doda) o;
    return wartosc.equals(other.wartosc) && wartosc2.equals(other.wartosc2);
  }
}
