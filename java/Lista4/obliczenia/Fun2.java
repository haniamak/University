package obliczenia;

public abstract class Fun2 extends Fun1 {
  protected Wyrazenie wartosc2;

  public Fun2(Wyrazenie wartosc, Wyrazenie wartosc2) {
    super(wartosc);
    this.wartosc2 = wartosc2;
  }

}
