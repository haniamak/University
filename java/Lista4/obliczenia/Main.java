package obliczenia;

import struktury.*;

public class Main {
  public static void main(String[] args) {

    Wyrazenie w1 = new Odejm(
        new Doda(
            new Liczba(7),
            new Mnoz(
                new Liczba(5),
                new Liczba(3))),
        new Liczba(1));
    System.out.println(w1.toString());
    System.out.println(w1.oblicz());
    System.out.println();

    Zmienna.zapiszZmienna("x", 1.618);
    Wyrazenie w2 = new Mnoz(
        new Przec(new Odejm(new Liczba(2), new Zmienna("x"))),
        new E());
    System.out.println(w2.toString());
    System.out.println(w2.oblicz());
    System.out.println();

    Wyrazenie w3 = new Dziel(
        new Odejm(
            new Mnoz(new Liczba(3), new Pi()),
            new Liczba(1)),
        new Doda(new Zmienna("x"), new Liczba(5)));
    System.out.println(w3.toString());
    System.out.println(w3.oblicz());
    System.out.println();

    Wyrazenie w4 = new Sin(
        new Dziel(
            new Doda(new Zmienna("x"), new Liczba(13)),
            new Odejm(new Liczba(1), new Zmienna("x"))));
    System.out.println(w4.toString());
    System.out.println(w4.oblicz());
    System.out.println();

    Wyrazenie w5 = new Doda(
        new Exp(new Liczba(5)),
        new Mnoz(new Zmienna("x"), new Log(new E(), new Zmienna("x"))));
    System.out.println(w5.toString());
    System.out.println(w5.oblicz());
    System.out.println();

    Para p = new Para("d", 0);
    try {
      Para p1 = (Para) p.clone();
      System.out.println(p1.toString());
    } catch (CloneNotSupportedException e) {
      e.printStackTrace();
    }

    Zmienna a1 = new Zmienna("y");
    Zmienna a2 = new Zmienna("y");
    System.out.println(a1.equals(a2));

    ZbiorTablicowy z = new ZbiorTablicowy(10);
    try {
      ZbiorTablicowy z2 = z.clone();
      System.out.println(z);
      System.out.println(z2);
    } catch (CloneNotSupportedException e) {
      e.printStackTrace();
    }

    System.out.println(Wyrazenie.sumuj(w1, w2, w3, w4));
    System.out.println(Wyrazenie.pomnoz(w1, w2, w3, w4));
  }
}