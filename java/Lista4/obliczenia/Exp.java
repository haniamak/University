package obliczenia;

public class Exp extends Fun1 {
  public Exp(Wyrazenie wartosc) {
    super(wartosc);
  }

  @Override
  public double oblicz() {
    return Math.exp(wartosc.oblicz());
  }

  @Override
  public String toString() {
    return "exp(" + wartosc.toString() + ")";
  }

  @Override
  public boolean equals(Object o) {
    if (o == this) {
      return true;
    }
    if (o == null || !(o instanceof Exp)) {
      return false;
    }
    Exp other = (Exp) o;
    return (this.oblicz() == other.oblicz());
  }
}
