
numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]
def media():
  return sum(numeros) / len(numeros)
def maior():
  return max(numeros)
def menor():
  return min(numeros)
def pares():
  numerospares = list(filter(lambda x: x % 2 == 0, numeros))
  return len(numerospares)
