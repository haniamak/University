package obliczenia;

public class Przec extends Oper1 {

  public Przec(Wyrazenie wartosc) {
    super(wartosc);
  }

  @Override
  public double oblicz() {
    return (wartosc.oblicz() * (-1));
  }

  @Override
  public String toString() {
    return "~(" + wartosc.toString() + ")";
  }

  @Override
  public boolean equals(Object o) {
    if (o == this) {
      return true;
    }
    if (o == null || !(o instanceof Przec)) {
      return false;
    }
    Przec other = (Przec) o;
    return (this.oblicz() == other.oblicz());
  }
}
