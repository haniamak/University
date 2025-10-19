package obliczenia;

public class Odwr extends Oper1 {

  public Odwr(Wyrazenie wartosc) {
    super(wartosc);
  }

  @Override
  public double oblicz() {
    return (1 / wartosc.oblicz());
  }

  @Override
  public String toString() {
    return "1 / (" + wartosc.toString() + ")";
  }

  @Override
  public boolean equals(Object o) {
    if (o == this) {
      return true;
    }
    if (o == null || !(o instanceof Odwr)) {
      return false;
    }
    Odwr other = (Odwr) o;
    return (this.oblicz() == other.oblicz());
  }
}

