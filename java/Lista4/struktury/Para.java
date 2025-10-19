package struktury;

public class Para implements Cloneable, Comparable<Para> {
  public final String klucz;
  private double wartosc;

  public Para(String klucz, double wartosc) {
    if (klucz == null) {
      throw new IllegalArgumentException("Klucz nie moze byc pusty");
    }
    if (!klucz.matches("[a-z]+")) {
      throw new IllegalArgumentException("Klucz powinien skladac sie tylko z malych liter alfabetu angielskiego");
    }
    this.klucz = klucz;
    this.wartosc = wartosc;
  }

  public double getWartosc() {
    return this.wartosc;
  }

  public void setWartosc(double wartosc) {
    this.wartosc = wartosc;
  }

  @Override
  public String toString() {
    return "Para ma nastepujacy klucz i wartosc: (" + this.klucz + ", " + this.wartosc + ")";
  }

  
  public int compareTo(Para p) {
    return klucz.compareTo(p.klucz);

  }

  @Override
  public boolean equals(Object o)
    {
        if(o==this)
        {
            return true;
        }
        if(o == null || !(o instanceof Para))
        {
            return false;
        }
        Para z = (Para) o;
        return klucz.equals(z.klucz);
    }
    
  @Override
  public Object clone() throws CloneNotSupportedException {
    return super.clone();
  }
}