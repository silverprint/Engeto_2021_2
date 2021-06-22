#hlavni_hangman.py
from hangman_2.hangman_funkce import *


def main():
    hadana_slova = ["jablko", "pomeranc", "mandarinka"]
    hrac = pridej_hrace()
    hadane_slovo = vyber_hadane_slovo(hadana_slova)
    postup, zbyvajici_tahy = schovej_slovo(hadane_slovo)

    while zbyvajici_tahy:
        vypis_stav_hry(hrac, postup, zbyvajici_tahy)
        zbyvajici_tahy = hraci_kolo(hadane_slovo, postup, zbyvajici_tahy)
        konecna_kontrola = posouzeni_stavu(postup, hrac, zbyvajici_tahy, hadane_slovo)
        if konecna_kontrola is not None:  # overuji moznost.
            break


if __name__ == "__main__":
    main()