import time



lista_hasel = ["admin", "12345", "qwerty", "PolskaGola", "cyber245", "aksze43", "samsung", "toor", "root", "haslo123", "admin", "12345", "123456", "password", "12345678", "qwerty", "123456789",
    "1234", "111111", "1234567", "dragon", "polska", "kochamcie", "iloveyou",
    "master", "123123", "mysz", "kot", "samsung", "apple", "root", "toor",
    "admin1", "haslo", "internet", "warszawa", "krakow", "start", "logowanie",
    "zaloguj", "test", "test1", "student", "szkola", "wiosna2024", "lato2024",
    "superman", "batman", "joker", "minecraft", "roblox", "fortnite", "cyberpunk",
    "tajne", "sekret", "god", "zamek", "brama", "klucz", "0xRedVector", "windows", "microsoft", "google", "facebook", "twitter", "instagram",
    "tiktok", "youtube", "amazon", "netflix", "spotify", "twitch", "discord",
    "steam", "epic", "origin", "uplay", "battle", "league", "legends", "csgo",
    "valorant", "gta", "gta5", "fifa", "sims", "pokemon", "mario", "zelda",
    "sonic", "lego", "starwars", "harrypotter", "lordoftherings", "avengers",
    "spiderman", "ironman", "thor", "hulk", "captainamerica", "blackwidow",
    "hawkeye", "thanos", "loki", "venom", "deadpool", "wolverine", "xmen",
    "matrix", "neo", "trinity", "morpheus", "terminator", "skynet", "cyberdyne",
    "alien", "predator", "godzilla", "kong", "jurassic", "park", "world",
    "marcin", "tomek", "kasia", "ania", "piotr", "pawel", "michal", "agnieszka",
    "magda", "monika", "mama", "tata", "babcia", "dziadek", "dom", "praca",
    "biuro", "firma", "szef", "kierownik", "prezes", "sekretarka", "ksiegowa",
    "faktura", "dokument", "projekt", "raport", "analiza", "budzet", "plan",
    "strategia", "rozwoj", "sukces", "pieniadze", "kasa", "wygrana", "loteria",
    "szczescie", "milosc", "rodzina", "przyjaciele", "wakacje", "podroz",
    "wycieczka", "hotel", "plaza", "slonce", "morze", "gory", "las", "jezioro",
    "rower", "narty", "pilka", "mecz", "stadion", "bramka", "gol", "wygrana",
    "mistrz", "puchar"]

print("--- SYMULATOR ATAKU SŁOWNIKOWEGO ---")


cel = input("Podaj hasło, które chcesz przetestować (musi być na liście!): ")

print(f"\n[+] Rozpoczynam atak na hasło: {cel}")
print("-" * 30)

znaleziono = False


for proba in lista_hasel:


    time.sleep(0.2)


    if proba == cel:
        print(f"\n[!!!] SUKCES! Hasło złamane: {proba}")
        print("[i] Uzyskano dostęp do systemu.")
        znaleziono = True
        break
    
    else:
        print(f"[-] Sprawdzam: {proba} ... BŁĄD")


if znaleziono == False:
    print("\n[-] NIEUDANE. Hasła nie ma w naszej bazie.")