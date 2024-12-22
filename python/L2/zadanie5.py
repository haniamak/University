import urllib.request

tekst = urllib.request.urlopen("https://wolnelektury.pl/media/book/txt/balladyna.txt").read().decode()
tekst = tekst[5895:6239]

def kompresja(tekst):
  wynik = []
  counter = 1
  for i in range(1, len(tekst)):
    if tekst[i] == tekst[i - 1]:
      counter+= 1
    else:
      wynik.append((counter, tekst[i - 1]))
      counter = 1
  return wynik

def dekompresja(tekst_skompresowany):
  tekst = ""
  for (count, char) in tekst_skompresowany:
    tekst += count * char
  return tekst

print(kompresja(tekst))
print(dekompresja(kompresja(tekst)))
