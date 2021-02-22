NUMBERS = [12, 123, 234, 90, 1289, 1289, 89, 62, 78, 89, 50]

# IDENTIFICAR NUMEROS PARES E IMPARES

pairs = []
for n in NUMBERS:
    if n % 2 == 0:
        pairs.append(n)

print(pairs)

def pair_number(number):
    if number % 2 == 0:
        return True


pairs = filter(pair_number, NUMBERS)  # DEVUELVE UN TIPO DE DATO OBJETO DE TIPO FILTER
print(pairs)

pairs = list(filter(pair_number, NUMBERS))
print(pairs)

pairs.sort()
print(pairs)