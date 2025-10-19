package rozgrywka;

import java.util.InputMismatchException;
import java.util.Scanner;

import obliczenia.Wymierna;

public class Gra {
  private int zakres;
  private Wymierna liczba;
  private int maksIloscProb;
  private int licznikProb;
  private StanGry stanGry;

  public Gra() {
    stanGry = StanGry.NIEAKTYWNA;
  }

  private int pobierzLiczbeZKonsoli(Scanner reader, String komunikat) {
    System.out.println(komunikat);
    int liczba;
      try {
        liczba = reader.nextInt();
      } catch (InputMismatchException exception) {
        liczba = 0;
      }
    return liczba;
  }

  private void rozgrywkaWKonsoli() {
    Scanner reader = new Scanner(System.in);
    while (this.stanGry == StanGry.AKTYWNA) {
      int licznik, mianownik;
      licznik = pobierzLiczbeZKonsoli(reader, "Podaj licznik: (0 zeby zrezygnowac z gry)");
      if (licznik == 0) {
          this.stanGry = StanGry.REZYGNACJA;
          break;
      }
      mianownik = pobierzLiczbeZKonsoli(reader, "Podaj mianownik: (0 zeby zrezygnowac z gry)");
      if (mianownik == 0) {
          this.stanGry = StanGry.REZYGNACJA;
          break;
      }
      Wymierna proba = new Wymierna(licznik, mianownik);
      StanGry stan = this.sprawdzProbe(proba);
      System.out.println(stan.toString());
    }
    reader.close();
    System.out.println(this.stanGry.toString());
  }

  public int porownaj(Wymierna proba) {
    if (proba.equals(liczba)) {
      return 0;
    }
    return proba.compareTo(liczba);
  }

  public StanGry sprawdzProbe(Wymierna proba) {
      if (proba.compareTo(new Wymierna()) > 0 && proba.compareTo(new Wymierna(1)) < 0) {
        if (proba.compareTo(this.liczba) > 0) {
          // System.out.println("Za duzo");
          this.licznikProb++;
        } else if (proba.compareTo(this.liczba) < 0) {
          // System.out.println("Za malo");
          this.licznikProb++;
        } else {
          this.stanGry = StanGry.ZWYCIESTWO;
        }
      } else {
        // System.out.println("Liczba spoza zakresu");
        this.licznikProb++;
      }

      if (this.licznikProb > this.maksIloscProb) {
        // System.out.println("Przekroczono ilosc prob");
        this.stanGry = StanGry.PORAZKA;
      }
      return this.odczytajStanGry();
  }

  public int start(int z) { // czy moze int? zeby zwracac zakres
    if (z < 5 || z > 20) {
      throw new IllegalArgumentException("Zakres losowanych wartosci to 5-20");
    }
    this.zakres = z;
    int licz;
    int mian;
    do {
      licz = (int) (Math.random() * zakres) + 1;
      mian = (int) (Math.random() * zakres) + 1;
    } while (licz >= mian);
    this.liczba = new Wymierna(licz, mian);
    // assert this.liczba.compareTo(new Wymierna()) > 0 && this.liczba.compareTo(new Wymierna(1)) < 0;
    this.maksIloscProb = (int) Math.ceil(3 * (Math.log(zakres) / Math.log(2)));
    this.licznikProb = 0;
    this.stanGry = StanGry.AKTYWNA;
    return this.maksIloscProb;
    // this.rozgrywkaWKonsoli();
  }

  public void rezygnuj() {
    this.stanGry = StanGry.REZYGNACJA;
  }

  public int zakres() {
    return zakres;
  }

  public int ileProb() {
    return maksIloscProb;
  }

  public int ileProbZuzyto() {
    return licznikProb;
  }

  public int ileProbZostalo() {
    return maksIloscProb - licznikProb;
  }

  public StanGry odczytajStanGry() {
    return stanGry;
  }

  public String podpowiedz() {
    return liczba.toString();
  }

}

