package obliczenia;

public class Ln extends Fun1 {
  public Ln(Wyrazenie wartosc) {
    super(wartosc);
  }

  @Override
  public double oblicz() {
    return Math.log(wartosc.oblicz());
  }

  @Override
  public String toString() {
    return "log(" + wartosc.toString() + ")";
  }

  @Override
  public boolean equals(Object o) {
    if (o == this) {
      return true;
    }
    if (o == null || !(o instanceof Ln)) {
      return false;
    }
    Ln other = (Ln) o;
    return (this.oblicz() == other.oblicz());
  }
}
