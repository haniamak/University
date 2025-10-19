package struktury;

import java.util.Arrays;

public class ZbiorTablicowy implements Zbior, Cloneable {
  private final Para[] zbior;
  private int zapelnienie;

  public ZbiorTablicowy(int rozmiar) {
    zbior = new Para[rozmiar];
    zapelnienie = 0;
  }

  public @Override Para szukaj(String k) {
    for (int i = 0; i < zapelnienie; i++) {
      if (zbior[i].klucz.equals(k)) {
        return zbior[i];
      }
    }
    return null;
  }

  public @Override void wstaw(Para p) {
    if (zapelnienie == zbior.length) {
      throw new IllegalStateException("Nie mozna wstawic elementu do zbioru. Tablica jest zapelniona.");
    }
    if (szukaj(p.klucz) == null) {
      zbior[zapelnienie++] = p;
    } else {
      for (int i = 0; i < zapelnienie; i++) {
        if (zbior[i].klucz.equals(p.klucz)) {
          zbior[i] = p;
          break;
        }
      }
    }
  }

  
  @Override
    public void usun(String k) {
        for (int i = 0; i < zapelnienie; i++) {
            if (zbior[i].klucz.equals(k)) {
                zbior[i] = zbior[zapelnienie - 1];
                zbior[zapelnienie - 1] = null;
                zapelnienie--;
                break;
            }
        }
    }

  public @Override void czysc() {
    zapelnienie = 0;
    Arrays.fill(zbior, null);

  }

  public @Override int ile() {
    return zapelnienie;
  }

  @Override
  public ZbiorTablicowy clone() throws CloneNotSupportedException {
    ZbiorTablicowy z = new ZbiorTablicowy(zapelnienie);
    for (int i = 0; i < zapelnienie; i++) {
      Para p = (Para) zbior[i].clone(); 
      z.zbior[i] = p;
    }
    return z;
  }
}
