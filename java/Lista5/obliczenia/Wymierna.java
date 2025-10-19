package obliczenia;

public class Wymierna implements Comparable<Wymierna>{
  private int licznik, mianownik;

  public Wymierna() {
    this.licznik = 0;
    this.mianownik = 1;
  }


  public Wymierna(int n) {
    this(n, 1);
  }

  private int NWD(int pierwsza, int druga) {
    if (druga == 0) {
      return pierwsza;
    } else {
      return NWD(druga, pierwsza % druga);
    }
  }

  public Wymierna(int k, int m) {
    if (m == 0) {
      throw new IllegalArgumentException("Mianownik nie moze byc rowny 0.");
    }

    if (m < 0) {
      k = -k;
      m = -m;
    }

    this.licznik = k;
    this.mianownik = m;

    int nwd = NWD(Math.abs(this.licznik), this.mianownik);
    this.licznik /= nwd;
    this.mianownik /= nwd;
  }

  public int getLicznik() {
    return licznik;
  }

  public int getMianownik() {
    return mianownik;
  }

  @Override
  public String toString() {
    return licznik + "/" + mianownik;
  }

  @Override
	public boolean equals(Object o) {
		if (this == o) {
			return true;
		}
		if (o == null || !(o instanceof Wymierna)) {
			return false;
		}
		Wymierna wymierna = (Wymierna) o;
		return licznik == wymierna.licznik && mianownik == wymierna.mianownik;
	}

  // czemu tu musi byc Integer zamiast int?
  @Override
  public int compareTo(Wymierna o) {
    Integer newLicznikLiczby1 = this.licznik * o.mianownik;
    Integer newLicznikLiczby2 = o.licznik * this.mianownik;
    return newLicznikLiczby1.compareTo(newLicznikLiczby2);
  }

  public static Wymierna dodawanie(Wymierna a, Wymierna b) {
    int newLicznik = a.licznik * b.mianownik + b.licznik * a.mianownik;
    int newMianownik = a.mianownik * b.mianownik;

    return new Wymierna(newLicznik, newMianownik);
}

public static Wymierna odejmowanie(Wymierna a, Wymierna b) {
    int newLicznik = a.licznik * b.mianownik - b.licznik * a.mianownik;
    int newMianownik = a.mianownik * b.mianownik;

    return new Wymierna(newLicznik, newMianownik);
}

public static Wymierna mnozenie(Wymierna a, Wymierna b) {
    int newLicznik = a.licznik * b.licznik;
    int newMianownik = a.mianownik * b.mianownik;

    return new Wymierna(newLicznik, newMianownik);
}

public static Wymierna dzielenie(Wymierna a, Wymierna b) {
    if(b.licznik == 0) {
      throw new ArithmeticException("Nie mozna dzielic przez 0");
    }

    int newLicznik = a.licznik * b.mianownik;
    int newMianownik = a.mianownik * b.licznik;

    return new Wymierna(newLicznik, newMianownik);
}
}