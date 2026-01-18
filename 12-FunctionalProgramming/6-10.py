#jakieś dziwne zadanie


pomiary = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# 1. Użycie map() do przygotowania danych (zgodnie ze wskazówką)
miasta = list(map(lambda k: k, pomiary.keys()))
temperatury = list(map(lambda v: v, pomiary.values()))

print("Wykres temperatur (tekstowy):")
print("-" * 30)

# 2. Logika rysowania wykresu
# Szukamy najniższej temperatury, żeby wiedzieć, gdzie zacząć rysowanie (offset)
min_temp = min(temperatury)
offset = abs(min_temp) if min_temp < 0 else 0

for i in range(len(miasta)):
    m = miasta[i]
    t = temperatury[i]
    
    # Tworzenie paska
    if t >= 0:
        # Dla dodatnich: puste miejsce (offset) + kreska pionowa + kwadraciki
        pasek = " " * offset + "|" + "■" * t
    else:
        # Dla ujemnych: puste miejsce (offset - długość paska) + kwadraciki + kreska
        pasek = " " * (offset - abs(t)) + "■" * abs(t) + "|"
    
    # Wyświetlanie: nazwa miasta wyrównana do prawej (10 znaków) + pasek + wartość
    print(f"{m:>10} {pasek} {t}°C")

print("-" * 30)
print(f"{' ' * (10 + offset)}| (0°C)")