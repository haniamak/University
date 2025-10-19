package obliczenia;

public class Stala extends Wyrazenie {
	protected final double wartosc;
	private final String nazwa;

	public Stala(double wartosc, String nazwa) {
		this.wartosc = wartosc;
		this.nazwa = nazwa;
	}

	@Override
	public double oblicz() {
		return wartosc;
	}

	@Override
	public String toString() {
		return nazwa;
	}

	public boolean equals(Object o) {
		if (o == this) {
			return true;
		}
		if (o == null || !(o instanceof Stala)) {
			return false;
		}
		Stala s = (Stala) o;
		return nazwa.equals(s.nazwa);
	}
}
