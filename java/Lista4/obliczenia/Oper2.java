package obliczenia;

public abstract class Oper2 extends Oper1 {
  protected Wyrazenie wartosc2;

  public Oper2(Wyrazenie wartosc, Wyrazenie wartosc2) {
    super(wartosc);
    this.wartosc2 = wartosc2;
  }

}
