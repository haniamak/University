def is_palindrom(text):

  is_palindrom = True
  newText = text.lower()

  bad_chars = [' ', '.', ',', ':', ';', '-', '\"', '?', '!', '\'']
  for i in bad_chars:
     newText = newText.replace(i, '')

  tab = list(newText)
  #print(tab)
  length = len(tab) / 2

  for i in range (int(length)):
     if tab[i] == tab[-i-1]:
        continue
     else:
        is_palindrom = False
        break
  return is_palindrom

        

is_palindrom("Eine güldne, gute Tugend: Lüge nie!")
is_palindrom("Míč omočím.")
is_palindrom("Kobyła ma mały bok.")
is_palindrom("hAnia")