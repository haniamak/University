from decimal import * 

def vat_faktura(lista):
  suma = 0.0
  suma = sum(lista)
  return sum(lista) * 0.23

def vat_paragon(lista):
  suma = 0.0
  suma = sum([x * 0.23 for x in lista])
  return suma

print((vat_paragon([5, 10])) == vat_faktura([5, 10]))

zakupy1 = [99.90, 0.10]

print(vat_faktura(zakupy1))
print(vat_paragon(zakupy1))
print(vat_faktura(zakupy1) == vat_paragon(zakupy1))


def vat_faktura_dec(lista):
    suma = 0.0
    suma = sum(lista)
    return suma * Decimal('0.23')

def vat_paragon_dec(lista):
    suma = 0.0
    suma = sum([x * Decimal('0.23') for x in lista])
    return suma

zakupy = [Decimal('0.1'), Decimal('2.5'), Decimal('3.8')]
print(vat_faktura_dec(zakupy) == vat_paragon_dec(zakupy))