package obliczenia;

public class Sin extends Fun1{
  
  public Sin(Wyrazenie wartosc) {
    super(wartosc);
  }

  @Override
  public double oblicz() {
    return Math.sin(wartosc.oblicz());
  }

  @Override
    public String toString() {
        return "sin(" + wartosc.toString() + ")";
    }

  @Override
  public boolean equals(Object o) {
    if (o == this) {
      return true;
    }
    if (o == null || !(o instanceof Sin)) {
      return false;
    }
    Sin other = (Sin) o;
    return (this.oblicz() == other.oblicz());
  }

}
