import re
cipher = 'KMFXLZMKDZVOXLZPXKYIPBKRRZFSVYDSVVFKMFXLZXLIYFAKYXVOXLZSKXZYPQZBKDZSVYDSVVFKMFDKMCDZMFIZFVOXLZSKXZYPQZBKNPZXLZCSZYZDKFZQIXXZY'
dictionary = {}

def FindFrequencyOfLetters(text, dictionary):
  for sign in text:
    if sign not in dictionary:
      dictionary[sign] = 1
    else:
      dictionary[sign] += 1
  sorteddictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
  return sorteddictionary

print("KROK 1: Czestotliwosc wystapien liter")
print(FindFrequencyOfLetters(cipher, dictionary), '\n')
# Trzy najczestsze wystapienia liter to: 'Z': 20, 'K': 13, 'X': 13
# Tak sie sklada, ze w angielskim alfabecie trzy najczesciej wystepujace litery to: E, T, A => W_ATE_RS
# Zakladam, ze Z = E, teraz sprawdzimy w szyfrogramie wystepowania XKZ i KXZ by dowiedziec sie jak zaszyfrowane sa A i T

print("KROK 2: Sprawdzenie wystapien XKZ, KXZ w szyfrze i podanie indeksu pierwszego wystapienia")
print('XKZ: ', cipher.find('XKZ'))
print('KXZ: ', cipher.find('KXZ'), '\n')

print("KROK 3: Podanie indeksow wszystkich wystapien KXZ: ")
print([(m.start(0), m.end(0)) for m in re.finditer('KXZ', cipher)], '\n')

# teraz wiemy, ze K = A, X = T and Z = E

# Zatem wyraz "WATERS" najprawdopodobniej wystepuje dwa razy w tym zdaniu
# teraz zakladam, ze S = W, Y = R, P = S, bo SKXZYPQ wystepuje dokladnie dwa razy w takiej kolejnosci

foundletters = {}
foundletters['S'] = 'w'
foundletters['K'] = 'a'
foundletters['X'] = 't'
foundletters['Z'] = 'e'
foundletters['Y'] = 'r'
foundletters['P'] = 's'

print("KROK 4: Odkycie odpowiedników w szyfrze liter składających się na słowo WATERS")
print(foundletters, '\n')

print("KROK 5: podstawienie wszystkich wystapien tych liter w szyfrze: ")
def LetterSubstition(cipher, dictionary):
  newcipher = ''

  for sign in cipher:
    if sign in dictionary:
      newcipher += dictionary[sign]
    else:
      newcipher += sign
  return newcipher

print(LetterSubstition(cipher, foundletters), '\n')
 
# na podstawie kolejnych najczesciej wystepujacych liter:
# ( 'F': 10, 'V': 9, 'L': 7, 'D': 7, 'S': 7, 'M': 6) 'I': 4, 'O': 3, 'B': 3, 'Q': 3, 'R': 2 )
# zakladam kolejne podstawienia

# foundletters['F'] = 'O'
# foundletters['V'] = 'I'
# foundletters['L'] = 'N'
# foundletters['D'] = 'H'
# foundletters['M'] = 'D'
# foundletters['I'] = 'L' 
# foundletters['O'] = 'C'
# foundletters['B'] = 'U' 
# foundletters['Q'] = 'M' 
# foundletters['R'] = 'F'

# ten krok tak naprawde okazal sie byc niepotrzebny, bo nijak nie poprawil kryptoanalizy, ale zostawilam go...

# na podstawie czesciowego odszyfrowania zauwazam, ze "tNe" pojawia sie dosyc czesto szczegolnie przed rzeczownikami:
# tLe star, tLe waters, lub czasami przed jeszcze nie odszyfrowanymi czesciami: 
# co sugeruje mi ze N = h,
# mamy wowczas 'the', ktore jest dosyc czesto pojawiajacym sie trzyliterowym wyrazem w jezyku angielskim

foundletters['L'] = 'h'

print("KROK 6: Podstawienie 'h' ")
print(LetterSubstition(cipher, foundletters), '\n')

# teraz zauwazam thewatersQeBaNsethe 
# mysle, ze QeBaNse to bedzie jeden wyraz, bo thewatersQeBaNsethe w tym momencie od razu po nim pojawia sie the
# moje przypuszczenie: QeBaNse = BECAUSE

foundletters['Q'] = 'b' 
foundletters['B'] = 'c' 
foundletters['N'] = 'u'

print("KROK 7: Podstawienie 'b', 'c', 'u' ")
print(LetterSubstition(cipher, foundletters), '\n')

# teraz zauwazam: thewatersbecausetheCwere C => y; thewatersbecaHe H => m
foundletters['C'] = 'y' 
foundletters['D'] = 'm' 

print("KROK 8: Podstawienie 'y', 'm'")
print(LetterSubstition(cipher, foundletters), '\n')

# teraz mamy: the waters because they were maFe bItter => F = d, I = i
# oraz: the Mame VO the star => M = n, V = o, O = f

foundletters['F'] = 'd' 
foundletters['I'] = 'i'
foundletters['M'] = 'n'
foundletters['V'] = 'o'
foundletters['O'] = 'f' 

print("KROK 9: Podstawienie 'd', 'i', 'n', 'o', 'f'")
print(LetterSubstition(cipher, foundletters), '\n') 

# teraz: andthenameofthestariscaRRedwormwood => R = l
# oraz: andthethirdAartofthewaters => A = p

foundletters['R'] = 'l' 
foundletters['A'] = 'p' 

print("KROK 10: Podstawienie 'l', 'p'")
print(LetterSubstition(cipher, foundletters), '\n') 
