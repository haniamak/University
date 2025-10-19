package prezentacja;

import java.awt.*;
import java.awt.event.*;
import java.io.IOException;
import java.util.logging.*;

import obliczenia.Wymierna;
import rozgrywka.Gra;
import rozgrywka.StanGry;

public class Okno extends Frame {
  private TextField licznikTextField, mianownikTextField, komunikatField;
  private Button probaButton, nowaGraButton, zakonczButton, rezygnacjaButton;
  private Scrollbar probyScrollbar, zakresScrollbar;
  private Label licznikLabel, mianownikLabel, komunikatLabel, zakresLabel, probyLabel, gornyZakresLabel, dolnyZakresLabel;
  private Wymierna gornyZakres, dolnyZakres;

  private String zakresLabelTxt = "Przedzial - wartosci (5-20):";
  private String probyLabelTxt = "Liczba prob:";

  private Gra gra;
  private static Logger logger = Logger.getLogger("LoggerGry");

  public static void main(String[] args) {
    Okno okno = new Okno();
    okno.setVisible(true);
    inicjalizujLog();
  }

  private static void inicjalizujLog() {
    FileHandler fileHandler;
    try {
      Logger.getGlobal().setLevel(Level.ALL);
      System.out.println(logger.getHandlers().length);
      Handler h = new ConsoleHandler();
      h.setLevel(Level.ALL);
      logger.addHandler(h);
      fileHandler = new FileHandler("rozgrywka.log", true);
      logger.addHandler(fileHandler);
      SimpleFormatter formatter = new SimpleFormatter();
      fileHandler.setFormatter(formatter);
      logger.setLevel(Level.ALL);
      
      logger.info("Inicjalizacja logu.");
    } catch (SecurityException e) {
      e.printStackTrace();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  private void inicjalizujOkno() {
    addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent we) {
        logger.log(Level.INFO, "Zamknieto aplikacje.");
        System.exit(0);
      }
    });

    setTitle("Gra");
    setSize(700, 350);
    setLayout(null);
  }

  private void inicjalizujGUI() {
    
    int x_kontrolekLewejSekcji = 50;
    licznikLabel = new Label("Licznik:");
    licznikLabel.setBounds(x_kontrolekLewejSekcji, 80, 70, 20);
    add(licznikLabel);
    licznikTextField = new TextField("", 10);
    licznikTextField.setBounds(x_kontrolekLewejSekcji + licznikLabel.getWidth() + 10, licznikLabel.getY(), 50, 20);
    add(licznikTextField);

    mianownikLabel = new Label("Mianownik:");
    mianownikLabel.setBounds(x_kontrolekLewejSekcji, 100, 70, 20);
    add(mianownikLabel);
    mianownikTextField = new TextField("", 10);
    mianownikTextField.setBounds(x_kontrolekLewejSekcji + mianownikLabel.getWidth() + 10, mianownikLabel.getY(), 50, 20);
    add(mianownikTextField);

    probaButton = new Button("Zgadnij");
    probaButton.setBounds(x_kontrolekLewejSekcji, 140, 160, 40);
    add(probaButton);
    probaButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent ae) {
        sprawdz();
      }
    });
    probaButton.addMouseListener(new java.awt.event.MouseAdapter() {
      public void mouseEntered(java.awt.event.MouseEvent evt) {
        try {
          int licznik = Integer.parseInt(licznikTextField.getText());
          int mianownik = Integer.parseInt(mianownikTextField.getText());
          Wymierna proba = new Wymierna(licznik, mianownik);
          komunikatField.setText("Twoja liczba to: " + proba.toString() + ". Potwierdz swoj wybor.");
          komunikatField.setBackground(Color.YELLOW);
        } catch (NumberFormatException e) {
          komunikatField.setText("Niepoprawny format aktualnie wpisanej liczby!");
          komunikatField.setBackground(Color.RED);
        } catch (IllegalArgumentException e) {
          logger.log(Level.SEVERE, "Mianownik rowny 0.");
          komunikatField.setText("Niepoprawny format aktualnie wpisanej liczby!");
          komunikatField.setBackground(Color.RED);
        }
      }
    });

    gornyZakresLabel = new Label("Gorny zakres");
    gornyZakresLabel.setBounds(x_kontrolekLewejSekcji, 200, 200, 20);
    add(gornyZakresLabel);
    dolnyZakresLabel = new Label("Dolny zakres");
    dolnyZakresLabel.setBounds(x_kontrolekLewejSekcji, 220, 200, 20);
    add(dolnyZakresLabel);

    int x_kontrolekPrawejSekcji = 270;
    zakresLabel = new Label(zakresLabelTxt);
    zakresLabel.setBounds(x_kontrolekPrawejSekcji, 80, 400, 20);
    add(zakresLabel);
    zakresScrollbar = new Scrollbar(Scrollbar.HORIZONTAL, 12, 1, 5, 20);
    zakresScrollbar.setBounds(x_kontrolekPrawejSekcji, 100, 400, 20);
    zakresScrollbar.setBackground(Color.BLACK);
    zakresScrollbar.setForeground(Color.WHITE);
    add(zakresScrollbar);

    probyLabel = new Label(probyLabelTxt);
    probyLabel.setBounds(x_kontrolekPrawejSekcji, 130, 400, 20);
    add(probyLabel);
    probyScrollbar = new Scrollbar(Scrollbar.HORIZONTAL, 0, 1, 0, 20);
    probyScrollbar.setBounds(x_kontrolekPrawejSekcji, 150, 400, 20);
    probyScrollbar.setBackground(Color.BLACK);
    probyScrollbar.setForeground(Color.WHITE);
    add(probyScrollbar);

    komunikatLabel = new Label("Stan gry:");
    komunikatLabel.setBounds(x_kontrolekPrawejSekcji, 180, 70, 20);
    add(komunikatLabel);
    komunikatField = new TextField("Wybierz zakres i rozpocznij gre", 10);
    komunikatField.setBounds(x_kontrolekPrawejSekcji, 200, 400, 40);
    add(komunikatField);
    komunikatField.setEditable(false);
    komunikatField.setBackground(Color.GREEN);

    int y_buttonow = 270;
    nowaGraButton = new Button("Rozpocznij gre");
    nowaGraButton.setBounds(x_kontrolekPrawejSekcji, y_buttonow, 100, 30);
    add(nowaGraButton);
    nowaGraButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent ae) {
        rozpocznijNowaGre();
      }
    });

    rezygnacjaButton = new Button("Poddaj sie");
    rezygnacjaButton.setBounds(nowaGraButton.getX() + nowaGraButton.getWidth() + 30, y_buttonow, 100, 30);
    add(rezygnacjaButton);
    rezygnacjaButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent ae) {
        gra.rezygnuj();
        ustawWygladGUI();
        komunikatField.setText("Poddano sie.");
        komunikatField.setBackground(Color.RED);
        logger.log(Level.INFO, "Poddano sie.");
      }
    });

    zakonczButton = new Button("Zakoncz gre");
    zakonczButton.setBounds(rezygnacjaButton.getX() + rezygnacjaButton.getWidth() + 30, y_buttonow, 100, 30);
    add(zakonczButton);
    zakonczButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent ae) {
        logger.log(Level.INFO, "Zakonczono gre.");
        System.exit(0);
      }
    });
  }

  public Okno() {
    inicjalizujOkno();
    inicjalizujGUI();
    gra = new Gra();
    ustawWygladGUI();
    logger.log(Level.INFO, "Aplikacja zostala zainicjalizowana.");
  }

  private void ustawWygladGUI() {
    StanGry stan = gra.odczytajStanGry();
    switch (stan) {
      case NIEAKTYWNA, REZYGNACJA, ZWYCIESTWO, PORAZKA:
        licznikLabel.setEnabled(false);
        licznikTextField.setEnabled(false);
        rezygnacjaButton.setEnabled(false);
        mianownikLabel.setEnabled(false);
        mianownikTextField.setEnabled(false);
        probyLabel.setEnabled(false);
        probaButton.setEnabled(false);
        nowaGraButton.setEnabled(true);
        zakresLabel.setFocusable(true);
        zakresScrollbar.setFocusable(true);
        probyScrollbar.setFocusable(true);
        gornyZakresLabel.setEnabled(false);
        dolnyZakresLabel.setEnabled(false);
        break;
      case AKTYWNA:
        licznikLabel.setEnabled(true);
        licznikTextField.setEnabled(true);
        mianownikLabel.setEnabled(true);
        mianownikTextField.setEnabled(true);
        probyLabel.setEnabled(true);
        probaButton.setEnabled(true);
        nowaGraButton.setEnabled(false);
        rezygnacjaButton.setEnabled(true);
        zakresScrollbar.setFocusable(false);
        probyScrollbar.setFocusable(false);
        dolnyZakresLabel.setEnabled(true);
        gornyZakresLabel.setEnabled(true);
        komunikatField.setText("Gra jest aktywna. Liczba prob to: " + gra.ileProb());
        komunikatField.setBackground(Color.GREEN);
        probyScrollbar.setValue(gra.ileProb());
        zakresLabel.setText(zakresLabelTxt + ' ' + ((Integer)gra.zakres()).toString());
        probyLabel.setText(probyLabelTxt + ' ' + ((Integer)gra.ileProb()).toString());

        break;
      default:
        logger.log(Level.WARNING, "Niepoprawny status gry. Funkcja ustawWyglad otrzymala argument " + stan.toString());
        throw new IllegalArgumentException("Niepoprawny status gry. Funkcja ustawWyglad otrzymala argument " + stan.toString());
    }
  }

  private void rozpocznijNowaGre() {
    int zakres = zakresScrollbar.getValue();
    int iloscProb = gra.start(zakres);
    logger.log(Level.INFO, "Rozpoczeto nowa gre. Zakres to: " + zakres + ". Liczba prob to: " + iloscProb);
    logger.log(Level.FINEST, "Podpowiedz: " + gra.podpowiedz());
    ustawWygladGUI();
  }

  private void porownaj(Wymierna proba) {
    int porownanie = gra.porownaj(proba);
    if (porownanie < 0) {
      komunikatField.setText("Podana liczba " + proba.toString() + " jest za mala");
      if (dolnyZakres == null || dolnyZakres.compareTo(proba) < 0) {
        dolnyZakres = proba;
        dolnyZakresLabel.setText("Dolny zakres to: " + dolnyZakres.toString());
      }
    } else {
      komunikatField.setText("Podana liczba " + proba.toString() + " jest za duza!");
      if (gornyZakres == null || gornyZakres.compareTo(proba) > 0) {
        gornyZakres = proba;
        gornyZakresLabel.setText("Gorny zakres to: " + gornyZakres.toString());
      }
    }
  }

  private void sprawdz() {
    if (gra.odczytajStanGry() == StanGry.AKTYWNA) {
      try {
        int licznik = Integer.parseInt(licznikTextField.getText());
        int mianownik = Integer.parseInt(mianownikTextField.getText());
        if (licznik >= mianownik) {
          logger.log(Level.FINER, "Licznik musi być mniejszy od mianownika!");
          komunikatField.setText("Licznik musi być mniejszy od mianownika!");
          komunikatField.setBackground(Color.RED);
        }
        Wymierna proba = new Wymierna(licznik, mianownik);
        StanGry wynik = gra.sprawdzProbe(proba);
        if (wynik == StanGry.ZWYCIESTWO) {
          komunikatField.setBackground(Color.GREEN);
          komunikatField.setText("Zwyciestwo! Rozpocznij nową gre!");
          logger.log(Level.INFO, "Zwyciestwo!");
          ustawWygladGUI();
        } else if (wynik == StanGry.PORAZKA) {
          komunikatField.setBackground(Color.RED);
          komunikatField.setText("Porazka! Rozpocznij nową gre!");
          logger.log(Level.INFO, "Porazka!");
          ustawWygladGUI();
        } else {
          komunikatField.setBackground(Color.YELLOW);
          porownaj(proba);
          licznikTextField.setText("");
          mianownikTextField.setText("");
          probyScrollbar.setValue(gra.ileProbZuzyto());
        }
      } catch (NumberFormatException e) {
        logger.log(Level.SEVERE, "Niepoprawny format liczby.");
        komunikatField.setText("Niepoprawny format liczby!");
        komunikatField.setBackground(Color.RED);
      } catch (IllegalArgumentException e) {
        logger.log(Level.SEVERE, "Mianownik rowny 0.");
        komunikatField.setText("Niepoprawny format liczby!");
        komunikatField.setBackground(Color.RED);
      }
    } else {
      logger.log(Level.FINER, "Gra nie jest aktywna.");
    }
  }
}
