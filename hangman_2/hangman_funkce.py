#funkce_hamgman.py
#=====================================================
#V tomto skriptu jsou funkce pro hru hangman:
#=====================================================
import random


def pridej_hrace() -> None:
    """Tato funce vraci jmeno hrace z inputu"""
    return input("Zadej jmeno hrace: ")

def vyber_hadane_slovo(hadana_slova) -> str:
    """Tato funkce nahodne vraci jedno slovo pro hadani"""
    return random.choice(hadana_slova)

def schovej_slovo(slovo: str) -> (list,int):
    """"""
    return ["_"] * len(slovo), round(1.3 * len(slovo), 0)

def vypis_stav_hry(hr: str, post: str, zbyvajici_tahy: int) -> None:
    zprava = f"HRAC: {hr} | STAV: {' '.join(post)} | ZBYVA: {zbyvajici_tahy} |"
    oddelovac = len(zprava) * "-"
    print(oddelovac, zprava, oddelovac, sep="\n")

def hrac_hada() -> str:
    return input("HADEJ PISMENO: ")

def posouzeni_hadani(pism:str, slovo:str, prog:list):
    for index, letter in enumerate(slovo):
        if letter in pism:
            prog[index] = pism
            print(prog[index])



def hraci_kolo(hadane_slovo:str, postup:list, zbyvajici_tahy:int) -> int:
    hadane_pismeno = hrac_hada()
    posouzeni_hadani(hadane_pismeno, hadane_slovo, postup)
    zbyvajici_tahy -= 1
    return zbyvajici_tahy

def posouzeni_stavu(postup:list, hrac:str, zbyvajici_tahy:int, slovo:str) -> bool:
    if "_" not in postup:

        vypis_stav_hry(hrac, postup, zbyvajici_tahy)
        print(f"VYBORNE, {hrac}! UHADL JSI!")
        return False #udelal jsem zmenu a funguje to lepe
        # exit()

    elif "_" in postup and zbyvajici_tahy == 0:
        print(f"PROHRALS, {hrac}, BOHUZEL!")
        print(f'Hadane slovo bylo: {slovo}.')
        exit()
