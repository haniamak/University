package obliczenia;

public class Liczba extends Wyrazenie {
	private double wartosc;

	public Liczba(double wartosc) {
		this.wartosc = wartosc;
	}

	@Override
	public double oblicz() {
		return wartosc;
	}

	@Override
	public String toString() {
		return Double.toString(wartosc);
	}

	@Override
	public boolean equals(Object o) {
		if (this == o) {
			return true;
		}
		if (o == null || !(o instanceof Liczba)) {
			return false;
		}
		Liczba other = (Liczba) o;
		return wartosc == other.wartosc;
	}

	@Override
	public Object clone() throws CloneNotSupportedException {
		return super.clone();
	}
}
