package obliczenia;

public class Log extends Fun2 {
  public Log(Wyrazenie wartosc, Wyrazenie wartosc2) {
    super(wartosc, wartosc2);
  }

  @Override
  public double oblicz() {
    return Math.log(wartosc2.oblicz()) / Math.log(wartosc.oblicz());
  }

  @Override
  public String toString() {
    return "log(" + wartosc.toString() + "," + wartosc2.toString() + ")";
  }

  @Override
  public boolean equals(Object o) {
    if (o == this) {
      return true;
    }
    if (o == null || !(o instanceof Log)) {
      return false;
    }
    Log other = (Log) o;
    return wartosc.equals(other.wartosc) && wartosc2.equals(other.wartosc2);
  }
}
