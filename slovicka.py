import random
import sys
import os 

def napoveda(): # definovani funkce 
  return ("Priklad pouziti: slovicka.py slovicka.csv")

if ((len(sys.argv) < 2) or (len(sys.argv) > 2)) :
  print(napoveda()) # kontrola kolik argumentu je zadano v prikazovem radku (zda je zadan nazev souboru + nazev .csv souboru), nutno zadat 2 
  exit()

soubor_cesta = str(sys.argv[1])

if not os.path.isfile(soubor_cesta): # kontrola zda soubor existuje 
  print("Soubor neexistuje")
  exit()
slova = open(soubor_cesta, encoding = 'utf-8')
radky = [radek.strip().split(";") for radek in slova]
slova.close()

i = 0
spravne = 0 # promenna pro pocitadlo spravnych odpovedi
spatne = 0 # promenna pro pocitadlo nespravnych odpovedi 

pocet_opakovani = int(input(f"Zadej pocet slovicek, ktere chces prekladat: "))

while i < pocet_opakovani: # while cyklus - zajisti nabizeni slovicek bez nutnosti spousteni skriptu, uživatel zadá počet opakování 

  nahodny_radek = random.sample(radky,1)
  anglicke_slovo = ' '.join([str(slovo[0]) for slovo in nahodny_radek])
  ceske_slovo = ",".join([slovo[1] for slovo in nahodny_radek]).split(',')
  vyzva = input(f"Zadej cesky preklad anglickeho slova:{anglicke_slovo} ")
  mezery = [mezera.split('(')[0].strip() for mezera in ceske_slovo]
  if vyzva in mezery:
    print("Spravne!")
    spravne += 1 # pocitadlo spravne uvedenych odpovedi
  else:
    x = ','.join(mezery)
    print(f"Spatne, zkus to znovu, spravny  preklad: {x}")
    spatne += 1  # pocitadlo nespravne uvedenych odpovedi 

  i += 1
print(f"Pocet spravnych odpovedi: {spravne}, Pocet spatnych odpovedi: {spatne}")











