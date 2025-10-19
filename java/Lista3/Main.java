// kompilacja java -jar ./figury.jar

import figury.Wektor;
import figury.Odcinek;
import figury.Prosta;
import figury.Punkt;
import figury.Trojkat;

public class Main {
  public static void main (String[] args) {

    // TESTY KLASY WEKTOR: 
    Wektor w1 = new Wektor(0,3);
    Wektor w2 = new Wektor(1, 5);
    Wektor w3 = Wektor.skladajWektory(w1, w2);
    System.out.println("wspolrzedne wektora w3 to: (" + w3.dx + ", " + w3.dy + ")");
    //oczekiwany wynik: w3 = (1, 8)


    //TESTY KLASY PUNKT:
    Punkt p1 = new Punkt(-7, 0);
    System.out.println("wspolrzedne punktu p1 to: (" + p1.getX() + ", " + p1.getY() + ")");
    Wektor wp = new Wektor(4, -1);
    Punkt nowyPunkt = p1.przesun(wp);
    System.out.println("wspolrzedne nowego punktu to: (" + nowyPunkt.getX() + ", " + nowyPunkt.getY() + ")");
    // oczekiwany wynik p1 = (-3, -1);
 
    Punkt p2 = new Punkt(-3, 4);
    Punkt p3 = new Punkt(1, 8);
    Punkt p4 = new Punkt(1, 8);
    boolean wynik1 = Punkt.czyWspoliniowe(p1, p2, p3);
    System.out.println("Czy punkty p1, p2, p3 sa wspolliniowe?: " + wynik1);
    // oczekiwana odpowiedz: true;
    boolean wynik2 = Punkt.czyRozne(p2, p3);
    System.out.println("Czy punkty p2, p3 sa rozne?: " + wynik2);
    //oczekiwana odpowiedz: true;
    boolean wynik3 = Punkt.czyRozne(p3, p4);
    System.out.println("Czy punkty p3 i p4 sa rozne?: " + wynik3);
    // oczekiwana odpowiedz: nie;

    Punkt p6 = new Punkt(1, 1);
    Punkt p5 = p2.obroc(p6, 90);
    System.out.println("wspolrzedne nowego punktu to: (" + p5.getX() + ", " + p5.getY() + ")");
    //oczekiwany wynik to p5 = (-2, -3);

    Prosta k1 = new Prosta(1, 1, 1);
    Punkt p7 = p1.odbij(k1);
    System.out.println("wspolrzedne nowego punktu to: (" + p7.getX() + ", " + p7.getY() + ")");
    //oczekiwany wynik: p7 = (-1, 6)


    //TESTY KLASY PROSTA:
    Prosta k2 = Prosta.przesunOWektor(k1, w1);
    System.out.println("wspolrzedne nowej prostej to: " + k2.a  +  k2.b  + k2.c);
    Prosta k3 = new Prosta(1, 1, 6);
    boolean wynik4 = Prosta.czyProstopadle(k1, k3);
    System.out.println("Czy proste k1, k3 sa prostopadle? : " + wynik4);
    // oczekiwany wynik false
    boolean wynik5 = Prosta.czyRownolegle(k1, k3);
    System.out.println("Czy proste k1, k3 sa rownolegle? : " + wynik5);
    // oczekiwany wynik true
    //Punkt p8 = Prosta.punktPrzeciecia(k2, k3);
    //System.out.println(p8.getX());
    //oczekiwany wynik: wyrzucenie wyjątku
    Prosta k4 = new Prosta(2, 1, 1);
    Punkt p9 = Prosta.punktPrzeciecia(k3, k4);
    System.out.println("wspolrzedne punktu przeciecia to: (" + p9.getX() + ", " + p9.getY() + ")");

    //TESTY KLASY ODCINEK
    Odcinek o1 = new Odcinek(p1, p2);
    Odcinek o2 = o1.przesun(w1);
    System.out.println("wspolrzedne nowego odcinka to: (" + o2.a.getX() + ", " + o2.a.getY() + ")" + " i: (" + o2.b.getX() + ", " + o2.b.getY() + ")");
    Punkt p10 = new Punkt(0,0);
    Punkt p11 = new Punkt(0, 4);
    Odcinek o3 = new Odcinek(p10, p11);
    Odcinek o4 = o3.obroc(p1, 90);
    System.out.println("wspolrzedne nowego odcinka to: (" + o4.a.getX() + ", " + o4.a.getY() + ")" + " i: (" + o4.b.getX() + ", " + o4.b.getY() + ")");
    Punkt o12 = new Punkt(2, 1);
    Punkt o13 = new Punkt(5, 1);
    Odcinek o5 = new Odcinek(o12, o13);
    Odcinek o6 = o5.odbij(k3);
    System.out.println("wspolrzedne nowego odcinka to: (" + o6.a.getX() + ", " + o6.a.getY() + ")" + " i: (" + o6.b.getX() + ", " + o6.b.getY() + ")");
    
    //TESTY KLASY TROJKAT
    //Trojkat t1 = new Trojkat(p1, p2, p3);
    //System.out.println(t1.x.getX());
    // ?? cos nie tak z czyrozne
    //przesun
    //obroc
    //odbij
    Punkt p12 = new Punkt(4, 7);
    Punkt p14 = new Punkt(3, 1);
    Trojkat t3 = new Trojkat(p6, p14, p12);
    Trojkat t4 = t3.przesun(w1);
    System.out.println("wspolrzedne nowego trojkata to: (" + t4.x.getX() + ", " + t4.x.getY() + ")" + " i: (" + t4.y.getX() + ", " + t4.y.getY() + ")" + " i: (" + t4.z.getX() + ", " + t4.z.getY() + ")");
    Trojkat t5 = t3.odbij(k1);
    System.out.println("wspolrzedne nowego trojkata to: (" + t5.x.getX() + ", " + t5.x.getY() + ")" + " i: (" + t5.y.getX() + ", " + t5.y.getY() + ")" + " i: (" + t5.z.getX() + ", " + t5.z.getY() + ")");
  }
}
