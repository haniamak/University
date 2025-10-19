package obliczenia;

public class Pot extends Fun2 {

  public Pot(Wyrazenie wartosc, Wyrazenie wartosc2) {
    super(wartosc, wartosc2);
  }

  @Override
  public double oblicz() {
    return Math.pow(wartosc.oblicz(), wartosc2.oblicz());
  }

  @Override
  public String toString() {
    return "pow(" + wartosc.toString() + "," + wartosc2.toString() + ")";
  }

  @Override
  public boolean equals(Object o) {
    if (o == this) {
      return true;
    }
    if (o == null || !(o instanceof Pot)) {
      return false;
    }
    Pot other = (Pot) o;
    return wartosc.equals(other.wartosc) && wartosc2.equals(other.wartosc2);
  }
}
