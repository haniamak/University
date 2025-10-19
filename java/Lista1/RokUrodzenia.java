// rozwiązanie działa w Command Prompt
// uruchomienie: java -Dfile.encoding=utf-8 RokUrodzenia.java

import java.util.Scanner;

public class RokUrodzenia {
  public static void main(String[] args)

  {
    try (Scanner scanner = new Scanner(System.in, "cp852")) {
      System.out.print("Podaj swoje imię: ");
      String imie = scanner.nextLine();

      System.out.print("Podaj rok urodzenia: ");
      int rokUrodzenia = scanner.nextInt();

      System.out.println("Cześć " + imie + "!");

      System.out.println("Rok urodzenia w zapisie rzymskim: " + rzymska(rokUrodzenia));

      System.out.println("Patron dla tego roku w kalendarzu chińskim: " + znajdzPatronChinski(rokUrodzenia));
      // gdyby importujemy javautilscanner to dostajemy tez closeable zatem nie musimy robic catcha
    }

  }

  private static final String[] RZYMSKIE = {
      "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
  };

  private static final int[] ARABSKIE = {
      1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
  };

  public static String rzymska(int n) {
    if (n <= 0 || n >= 4000) {
      throw new IllegalArgumentException("liczba " + n + " spoza zakresu 1-3999");
    }

    StringBuilder rokrzymski = new StringBuilder();
    for(int i = 0; n > 0;) {
      if (n - ARABSKIE[i] >= 0) {
        rokrzymski.append(RZYMSKIE[i]);
        n = n - ARABSKIE[i];
      } else {
        i++;
      }
    }
    return rokrzymski.toString();
  }
    static final String[] patronChinski = {
        "małpa", "kurczak", "pies", "świnia", "szczur", "bawół", "tygrys", "królik", "smok", "wąż", "koń", "owca"
    };

  public static String znajdzPatronChinski(int rok) {
    int number = rok % 12;
    String patron = switch (number) {
      case 0 -> patronChinski[number];
      case 1 -> patronChinski[number];
      case 2 -> patronChinski[number];
      case 3 -> patronChinski[number];
      case 4 -> patronChinski[number];
      case 5 -> patronChinski[number];
      case 6 -> patronChinski[number];
      case 7 -> patronChinski[number];
      case 8 -> patronChinski[number];
      case 9 -> patronChinski[number];
      case 10 -> patronChinski[number];
      case 11 -> patronChinski[number];
      default -> throw new IllegalArgumentException("Unexpected value: " + number);
    };
    return patron;

  }
}
