import random

import urllib.request

tekst2 = urllib.request.urlopen("https://wolnelektury.pl/media/book/txt/balladyna.txt").read().decode()
tekst2 = tekst2[5895:6239]


def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
  out = ""
  for zdanie in tekst.split("\r\n"):
    wynik = []
    for slowo in zdanie.split():
      if len(slowo) <= dl_slowa:
        wynik.append(slowo)
  
    if len(wynik) > liczba_slow:
      for i in range(len(wynik) - liczba_slow):
        wynik.pop(random.randrange(0, len(wynik)))

    output = " ".join(wynik)
    out = out + output  + ('\n')
  return out

print(uprosc_zdanie(tekst2, 8, 3))

tekst1 = "Podział peryklinalny inicjałów wrzecionowatych \
kambium charakteryzuje się ścianą podziałową inicjowaną \
w płaszczyźnie maksymalnej."
wynik = uprosc_zdanie(tekst1, 10, 5)
print(wynik)