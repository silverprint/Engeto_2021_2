from pprint import pprint as pp
KOSIK = {}
ODDELOVAC = "=" * 40
POTRAVINY = {
    "mleko": 30,
    "maso": 100,
    "banan": 30,
    "jogurt": 10,
    "chleb": 20,
    "jablko": 10
}


while (vyber_n := input("VYBERTE ZBOZI: ")) != 'exit':
    if vyber_n not in POTRAVINY:
        print("NENI SKLADEM!")
        continue
    else:
        KOSIK[vyber_n] = POTRAVINY.get(vyber_n, "NENI SKLADEM")

else:
    print(ODDELOVAC)
    CELKEM = sum(KOSIK.values())
    print(KOSIK)
    print(ODDELOVAC)
    print(f"CENA CELKEM: {CELKEM} CZK")