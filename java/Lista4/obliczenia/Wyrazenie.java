package obliczenia;

abstract class Wyrazenie implements Obliczalny {

  public static double sumuj(Wyrazenie... wyrazenie) {
    double suma = 0;
    for (Wyrazenie w : wyrazenie) {
      suma += w.oblicz();
    }
    return suma;
  }

  public static double pomnoz(Wyrazenie... wyrazenie) {
    double iloczyn = 1;
    for (Wyrazenie w : wyrazenie) {
      iloczyn *= w.oblicz();
    }
    return iloczyn;
  }

}
