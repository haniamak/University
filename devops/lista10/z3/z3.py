class Wyrazenie:
    def oblicz(self, zmienne):
        raise NotImplementedError(
            "Metoda oblicz() nie została zaimplementowana w podklasach."
        )

    def __str__(self):
        raise NotImplementedError(
            "Metoda __str__() nie została zaimplementowana w podklasach."
        )

    def pochodna(self, zmienna):
        raise NotImplementedError(
            "Metoda pochodna() nie została zaimplementowana w podklasach."
        )

    def __add__(self, w2):
        return Dodaj(self, w2)

    def __mul__(self, w2):
        return Razy(self, w2)


class VariableNotFoundException(Exception):
    pass


class DivisionByZeroException(Exception):
    pass


class TypeException(Exception):
    pass


class Zmienna(Wyrazenie):
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def oblicz(self, zmienne):
        if self.nazwa not in zmienne:
            raise VariableNotFoundException(
                f"Zmienna {self.nazwa} nie została znaleziona w słowniku"
            )
        return zmienne[self.nazwa]

    def __str__(self):
        return str(self.nazwa)

    def pochodna(self, zmienna):
        if self.nazwa == zmienna:
            return Stala(1)
        else:
            return Stala(0)


class Stala(Wyrazenie):
    def __init__(self, wartosc):
        self.wartosc = wartosc

    def oblicz(self, zmienne):
        return self.wartosc

    def __str__(self):
        return str(self.wartosc)

    def pochodna(self, zmienna):
        return Stala(0)


class Dodaj(Wyrazenie):
    def __init__(self, w1, w2):
        if not isinstance(w1, Wyrazenie) or not isinstance(w2, Wyrazenie):
            raise TypeException("Wprowadzona zmienna jest złego typu.")
        self.w1 = w1
        self.w2 = w2

    def oblicz(self, zmienne):
        return self.w1.oblicz(zmienne) + self.w2.oblicz(zmienne)

    def __str__(self):
        return f"({self.w1} + {self.w2})"

    def pochodna(self, zmienna):
        return self.w1.pochodna(zmienna) + self.w2.pochodna(zmienna)


class Odejmij(Wyrazenie):
    def __init__(self, w1, w2):
        if not isinstance(w1, Wyrazenie) or not isinstance(w2, Wyrazenie):
            raise TypeException("Wprowadzona zmienna jest złego typu.")
        self.w1 = w1
        self.w2 = w2

    def oblicz(self, zmienne):
        return self.w1.oblicz(zmienne) - self.w2.oblicz(zmienne)

    def __str__(self):
        return f"({self.w1} - {self.w2})"

    def pochodna(self, zmienna):
        return self.w1.pochodna(zmienna) - self.w2.pochodna(zmienna)


class Razy(Wyrazenie):
    def __init__(self, w1, w2):
        if not isinstance(w1, Wyrazenie) or not isinstance(w2, Wyrazenie):
            raise TypeException("Wprowadzona zmienna jest złego typu.")
        self.w1 = w1
        self.w2 = w2

    def oblicz(self, zmienne):
        return self.w1.oblicz(zmienne) * self.w2.oblicz(zmienne)

    def __str__(self):
        return f"({self.w1} * {self.w2})"

    def pochodna(self, zmienna):
        # return self.w1.pochodna(zmienna) * self.w2 + self.w1 * self.w2.pochodna(zmienna)
        return Dodaj(
            Razy(self.w1.pochodna(zmienna), self.w2),
            Razy(self.w1, self.w2.pochodna(zmienna)),
        )


class Podziel(Wyrazenie):
    def __init__(self, w1, w2):
        if not isinstance(w1, Wyrazenie) or not isinstance(w2, Wyrazenie):
            raise TypeException("Wprowadzona zmienna jest złego typu.")
        self.w1 = w1
        self.w2 = w2

    def oblicz(self, zmienne):
        mianownik = self.w2.oblicz(zmienne)
        if mianownik == 0:
            raise DivisionByZeroException("Błąd: Próba dzielenia przez zero.")
        return self.w1.oblicz(zmienne) / mianownik

    def __str__(self):
        return f"({self.w1} / {self.w2})"

    def pochodna(self, zmienna):
        # return (self.w1.pochodna(zmienna) * self.w2 - self.w1 * self.w2.pochodna(zmienna)) / Razy(self.w2, self.w2)
        licznik = Odejmij(
            Razy(self.w1.pochodna(zmienna), self.w2),
            Razy(self.w1, self.w2.pochodna(zmienna)),
        )
        mianownik = Razy(self.w2, self.w2)
        return Podziel(licznik, mianownik)


wyrazenie = Razy(Dodaj(Zmienna("x"), Stala(2)), Zmienna("y"))
print(wyrazenie)

# wyrazenie = Razy(Dodaj(3), Stala(2)), Zmienna("y"))
# zwroci type exception

zmienne = {"x": 3, "y": 4}
wynik = wyrazenie.oblicz(zmienne)
print(wynik)

pochodna_x = wyrazenie.pochodna("x")
print(f"f'(x) = {pochodna_x}")


wyrazenie2 = Podziel(Zmienna("a"), Zmienna("b"))
print(wyrazenie2)
zmienne2 = {"a": 10, "b": 0}
# wynik2 = wyrazenie2.oblicz(zmienne2)
# print(wynik2)
