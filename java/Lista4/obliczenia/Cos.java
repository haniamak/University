package obliczenia;

public class Cos extends Fun1 {
  public Cos(Wyrazenie wartosc) {
    super(wartosc);
  }

  @Override
  public double oblicz() {
    return Math.cos(wartosc.oblicz());
  }

  @Override
  public String toString() {
    return "cos(" + wartosc.toString() + ")";
  }

  @Override
  public boolean equals(Object o) {
    if (o == this) {
      return true;
    }
    if (o == null || !(o instanceof Cos)) {
      return false;
    }
    Cos other = (Cos) o;
    return (this.oblicz() == other.oblicz());
  }
}
