def czywpole(s, row, col, num):
  return (not czywkolumnie(s, col, num)
    and not czywwierszu(s, row, num)
    and not czywkwadracie(s, row - (row % 3), col - (col % 3), num))

def czywkolumnie(s, col, num):
  for i in range(9):
    if s[i][col] == num:
      return True
  return False

def czywwierszu(s, row, num):
  for i in range(9):
    if s[row][i] == num:
      return True
  return False

def czywkwadracie(s, row, col, num):
  for i in range(3):
    for j in range(3):
      if s[row + i][col + j] == num:
        return True
  return False

def znajdzpustepole(s):
  for row in range(9):
    for col in range(9):
      if s[row][col] == 0:
        return (row, col)
  return None
    


sudoku = [
    [0, 3, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 3],
    [0, 0, 0, 8, 0, 3, 0, 0, 1],
    [0, 0, 0, 0, 2, 0, 0, 0, 6],
    [9, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [3, 0, 0, 0, 8, 0, 0, 7, 9]
]



#print(czywpole(sudoku, 0, 2, 1))
#print(znajdzpustepole(sudoku))

def rozwiaz_sudoku_wszystkie(s):
    pustepole = znajdzpustepole(s)
    
    if not pustepole:
        # Dodaj kopię rozwiązania do listy rozwiązań
        yield [row[:] for row in s]
    
    row, col = pustepole
    
    for num in range(1, 10):
        if czywpole(s, row, col, num):
            s[row][col] = num
            
            # Rekurencyjne szukanie wszystkich rozwiązań
            yield from rozwiaz_sudoku_wszystkie(s)
            
            # backtracking
            s[row][col] = 0


for rozwiazanie in rozwiaz_sudoku_wszystkie(sudoku):
    for row in rozwiazanie:
        print(row)
    print()



