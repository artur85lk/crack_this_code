# Szyfr Cezara:

import pyperclip

message = 'XCBSw88S18A1S 2SB41SE .8zSEwAS50D5A5x81V'

key = 22

# Określenie trybu pracy:
mode = 'decript'

# Znaki które można zaszyfrować:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Zmienna przechowująca zaszyfrowaną lub odszyfrowaną postaC wiadomości:
translated = ''


for symbol in message:
    # UWAGA: Tylko symbole zdefiniowane w ciągu SYMBOLS mogą być szyfrowane i deszyfrowane
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Przeprowadzenie szyfrowania i deszyfrowania:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decript':
            translatedIndex = symbolIndex - key

        # Obsługa zawinięcia jeśli zachodzi potrzeba:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        translated = translated + SYMBOLS[translatedIndex]

    else:
        # Dołączenie znaku bez jego wcześniejszego szyfrowania i deszyfrowania
        translated = translated + symbol

# Wyświetlenie skonwertowanego ciągu tekstowego:
print(translated)
pyperclip.copy(translated)
