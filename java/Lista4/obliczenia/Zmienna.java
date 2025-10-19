package obliczenia;

import struktury.*;

public class Zmienna extends Wyrazenie {

	private static final ZbiorTablicowy zbiorZmiennych = new ZbiorTablicowy(10);
	public final String identyfikator;

	public Zmienna(String identyfikator) {
		this.identyfikator = identyfikator;
	}

	public static void zapiszZmienna(String identyfikator, double wartosc) {
		Para p = zbiorZmiennych.szukaj(identyfikator);
		if (p == null) {
			Para newPara = new Para(identyfikator, wartosc);
			zbiorZmiennych.wstaw(newPara);
		}
		else {
			p.setWartosc(wartosc);
		}
	}

	public static double odczytajZmienna(String identyfikator) {
		Para p = zbiorZmiennych.szukaj(identyfikator);
		if (p == null) {
			throw new IllegalArgumentException("Nie ma takiej zmiennej.");
		}
		else {
			return p.getWartosc();
		}
	}

	@Override
	public double oblicz() {
		return odczytajZmienna(identyfikator);
	}

	@Override
	public String toString() {
		return identyfikator;
	}

	@Override
	public boolean equals(Object o) {
		if (this == o) {
			return true;
		}
		if(o == null || !(o instanceof Zmienna)) {
			return false;
		}
		Zmienna zmienna = (Zmienna) o;
		return identyfikator.equals(zmienna.identyfikator);
	}

	@Override
  public Object clone() throws CloneNotSupportedException {
    return super.clone();
  }
}