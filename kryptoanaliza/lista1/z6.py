cipher = """LPMUQEMQMGKLWDPMCYRHMHQXMLBMQSKLRMQBHMPDVMCRYCJEMUVKVMEPKLJLBWMPDLKPVVBMULBEPYBM
EILPDMDLEMCDLBMBAZZRVHMLBPYMDLEMGKVQEPMLBMQBMVOOYKPMPYMVECQSVMPDVM*LRVMULBHMERLS
SVHMTALCJRXMPDKYAWDMPDVMWRQEEMHYYKEMYOM*LCPYKXMIQBELYBEMPDYAWDMBYPMTALCJRXMVBYAW
DMPYMSKV*VBPMQMEULKRMYOMWKLPPXMHAEPMOKYIMVBPVKLBWMQRYBWMULPDMDLIMPDVMDQRRUQXMEIV
RPMYOMGYLRVHMCQGGQWVMQBHMYRHMKQWMIQPEMQPMYBVMVBHMYOMLPMQMCYRYAKVHMSYEPVKMPYYMRQK
WVMOYKMLBHYYKMHLESRQXMDQHMGVVBMPQCJVHMPYMPDVMUQRRMLPMHVSLCPVHMELISRXMQBMVBYKIYAE
MOQCVMIYKVMPDQBMQMIVPKVMULHVMPDVMOQCVMYOMQMIQBMYOMQGYAPMOYKPXMOL*VMULPDMQMDVQ*XM
GRQCJMIYAEPQCDVMQBHMKAWWVHRXMDQBHEYIVMOVQPAKVEMULBEPYBMIQHVMOYKMPDVMEPQLKEMLPMUQ
EMBYMAEVMPKXLBWMPDVMRLOPMV*VBMQPMPDVMGVEPMYOMPLIVEMLPMUQEMEVRHYIMUYKJLBWMQBHMQPM
SKVEVBPMPDVMVRVCPKLCMCAKKVBPMUQEMCAPMYOOMHAKLBWMHQXRLWDPMDYAKEMLPMUQEMSQKPMYOMPD
VMVCYBYIXMHKL*VMLBMSKVSQKQPLYBMOYKMDQPVMUVVJMPDVMORQPMUQEMEV*VBMORLWDPEMASMQBHMU
LBEPYBMUDYMUQEMPDLKPXMBLBVMQBHMDQHMQM*QKLCYEVMARCVKMQGY*VMDLEMKLWDPMQBJRVMUVBPME
RYURXMKVEPLBWMEV*VKQRMPLIVEMYBMPDVMUQXMYBMVQCDMRQBHLBWMYSSYELPVMPDVMRLOPMEDQOPMP
DVMSYEPVKMULPDMPDVMVBYKIYAEMOQCVMWQZVHMOKYIMPDVMUQRRMLPMUQEMYBVMYOMPDYEVMSLCPAKV
EMUDLCDMQKVMEYMCYBPKL*VHMPDQPMPDVMVXVEMOYRRYUMXYAMQGYAPMUDVBMXYAMIY*VMGLWMGKYPDV
KMLEMUQPCDLBWMXYAMPDVMCQSPLYBMGVBVQPDMLPMKQBM"""

alphabet = '*ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dictionary = {}

def FindFrequencyOfLetters(text, dictionary):
  for sign in text:
    if sign not in dictionary:
      dictionary[sign] = 1
    else:
      dictionary[sign] += 1
  sorteddictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
  return sorteddictionary

print("KROK 1: Znalezienie czestosc wystepowania liter: ")
print(FindFrequencyOfLetters(cipher, dictionary), '\n')

# 'M': 234, 'V': 110, 'P': 103, 'Y': 82, 'Q': 81

foundletters = {}
foundletters['M'] = ' '
foundletters['V'] = 'e'
foundletters['P'] = 't'
foundletters['Y'] = 'a'

def LetterSubstition(cipher, dictionary):
  newcipher = ''

  for sign in cipher:
    if sign in dictionary:
      newcipher += dictionary[sign]
    else:
      newcipher += sign
  return newcipher

print("KROK 2: podstawienie najczęsciej wystepujacych znakow: ' ', e, t, a")
print(LetterSubstition(cipher, foundletters), '\n')

# zauwazylam czeste wystepowanie tDe => D = h oraz Lt => L = i
# strzal z a okazal sie chyba bledy, bo pojawia sie slowo 'ta', ktore nie wystepuje w jezyku angielskim, 
# zamiast tego podstawmy Y = o

foundletters['Y'] = 'o'
foundletters['D'] = 'h'
foundletters['L'] = 'i'

print("KROK3: podstawienie o h oraz i")
print(LetterSubstition(cipher, foundletters), '\n')

cipher2 = LetterSubstition(cipher, foundletters)

def CountWords(cipher, dictionary):
  words = cipher.split(' ')
  for word in words:
    if word not in dictionary:
      dictionary[word] = 1
    else:
      dictionary[word] += 1
  sorteddictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
  return sorteddictionary

occurence = {}

print("KROK4: zliczenie czesciowo odszyfrowanych slow")
print(CountWords(cipher2, occurence))

# po czestosci wystapien: 'oO': 9, 'Q': 7 => O = f, Q = a

foundletters['O'] = 'f'
foundletters['Q'] = 'a'

print("KROK 5: podstawienie f, a")
print(LetterSubstition(cipher, foundletters), '\n')

#  Analiza tekstu: 
# effoKt => K = r 
# iBto, iB, aB, Bot => B = n

foundletters['K'] = 'r'
foundletters['B'] = 'n'

print("KROK 6: podstawienie r, n")
print(LetterSubstition(cipher, foundletters), '\n')

cipher3 = LetterSubstition(cipher, foundletters)
occurence2 = {}

print("KROK7: zliczenie czesciowo odszyfrowanych slow")
print(CountWords(cipher3, occurence2))

# Analiza wyrazow: 
# 'anH': 6, => H = d
# 'Uith': 3, => U = w
# 'froI': 2 => I = m

foundletters['H'] = 'd'
foundletters['U'] = 'w'
foundletters['I'] = 'm'

print("KROK 8: podstawienie d, w, m")
print(LetterSubstition(cipher, foundletters), '\n')

# Analiza tekstu:
# waE => E = s
# riWht => W = g
# eReCtriC => R = l C = c

foundletters['E'] = 's'
foundletters['W'] = 'g'
foundletters['R'] = 'l'
foundletters['C'] = 'c'

print("KROK 9: podstawienie s, g, l, c")
print(LetterSubstition(cipher, foundletters), '\n')

# Analiza tekstu:
# Gright => G = b
# daX => X = y
# escaSe => S = p
# throAgh => A = u
# worJing => J = k

foundletters['G'] = 'b'
foundletters['X'] = 'y'
foundletters['S'] = 'p'
foundletters['A'] = 'u'
foundletters['J'] = 'k'

print("KROK 10: podstawienie b, y, p, u, k")
print(LetterSubstition(cipher, foundletters), '\n')

# Analiza tekstu:
# e*en, se*en => * = v
# nuZZled => Z = z
# Tuickly => T = q

foundletters['*'] = 'v'
foundletters['Z'] = 'z'
foundletters['T'] = 'q'

print("KROK 11: podstawienie v, z, q")
print(LetterSubstition(cipher, foundletters), '\n')
