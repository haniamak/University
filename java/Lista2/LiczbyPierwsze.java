public final class LiczbyPierwsze {

  private final static int POTEGA2 = 21;
  private final static int[] SITO = new int[1 << POTEGA2];

  // potrzebny jest statyczny blok inicjalizacyjny dla sita
  // [0, 1, 2, 3, 2, 5, 2, 7, 2, 3, 2, 11, … ]

  static {
    SITO[1] = 1;
    for (int i = 2; i < (1 << POTEGA2); i += 2) {
      SITO[i] = 2;
    }
    for (int i = 3; i < (1 << POTEGA2); i++) {
      if (SITO[i] == 0) {
        for (int j = i; j < (1 << POTEGA2); j += i) {
          if (SITO[j] == 0) {
            SITO[j] = i;
          }
        }
      }
    }
  }

  public static boolean czyPierwsza(long x) {
    if (x == -9223372036854775808L) {

      return false;
    }
    if (x < 2) {
      return false;
    }
    if (x < SITO.length) {
      if (SITO[(int) x] == x) {
        return true;
      }
      return false;
    }
    if (x >= SITO.length) {
      long sqrtX = (long)Math.sqrt(x)+1;
      for (long i = 2; i != sqrtX; i++) {
        if (x % i == 0) {
          return false;
        }
      }
      return true;
    } else {
      return false;
    }
  }

  public static long[] naCzynnikiPierwsze(long x) {

    int power = 0;
    if (x < 0) {
      while (x <= (-1 * Math.pow(2, power))) {
        power++;
      }
      power++;
    } else {
      while (x >= Math.pow(2, power)) {
        power++;
      }
    }

    int counter = 0;
    long[] dividers = new long[power];

    if (x == -9223372036854775808L) {
      dividers[counter] = -1;
      counter++;
      dividers[counter] = 2;
      x /= 2;
      x = Math.abs(x);
      counter++;
    }
    if (x == 1 || x == 0 || x == -1) {
      dividers[counter] = x;
      return dividers;
    }

    if (x < 0) {
      dividers[counter] = -1;
      x = Math.abs(x);
      counter++;
    }
    if (x < (1 << POTEGA2)) {
      while (x > 1) {
        dividers[counter] = SITO[(int) x];
        x /= SITO[(int) x];
        counter++;
      }
      return dividers;
    }

    if (x > (1 << POTEGA2)) {
      long y = x;
      for (long i = 2; i * i <= x; i++) {
        while ((y % i) == 0) {
          dividers[counter] = i;
          y /= i;
          counter++;
        }
        if (y == 1) {
          break;
        }
      }
      return dividers;
    }
    return dividers;
  }

  public static void printonscreen(long[] dividers) {
    for (int i = 0; dividers[i] != 0; i++) {
      if (dividers[i + 1] == 0) {
        System.out.println(dividers[i]);
      } else {
        System.out.print(dividers[i] + " * ");
      }
    }
  }

  public static void main(String[] args) {
    if(args.length==0)
        {
            System.err.println("Podaj liczby calkowite typu long: ");
            return;
        }
    for (String x : args) {
      long variable = Long.parseLong(x);
      if (LiczbyPierwsze.czyPierwsza(variable)) {
        System.out.println("Liczba " + variable + " jest pierwsza.");
      } else {
        System.out.print(variable + " = ");
        printonscreen(LiczbyPierwsze.naCzynnikiPierwsze(variable));
      }
    }
  }

}