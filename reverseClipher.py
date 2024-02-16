# Szzyfr odwrotny

massage = input('Podaj tekst do zaszyfrowania: ')
translated = ''

i = len(massage) - 1
while i >= 0:
    translated = translated + massage[i]
    i = i - 1
    print(translated)

print(translated)
