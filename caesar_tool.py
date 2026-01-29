print("--- CAESAR CIPHER TOOL (0xRedvector) ---")

print("Wybierz tryb: ")
print("1. Szyfrowanie (Encrypt)")
print("2. Odszyfrowanie (Decrypt)")
tryb = input("Twój wybór (1 lub 2): ")

tekst = input("\nPodaj tekst: ")
klucz = int(input("Podaj klucz (np. 3):"))

if tryb == "2":
    klucz = -klucz

wynik = ""

for znak in tekst:

    if 32 <= ord(znak) <= 126:
        kod = ord(znak)
        nowy_kod = kod + klucz
        wynik += chr(nowy_kod)
    else:

        wynik += znak

print("-" * 30)
print(f"WYNIK: {wynik}")
print("-" * 30)