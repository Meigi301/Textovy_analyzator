'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Monika Plzakova
email: moni.plzakova@gmail.com
discord: Meigi#7675
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

import getpass

registrovani_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }
oddelovac = "----------------------------------------"

zadane_jmeno = input(f"username: ")
zadane_heslo = getpass.getpass(f"password: ")

pocet_jednotlivych_slov = {}
pocet_slov = 0
pocet_slov_velkymi = 0
zacina_velkymi = 0
zacina_malymi = 0
cisla = 0
soucet_cisel = 0
pocet_vyskytu_delek_slov = {}

if zadane_jmeno in registrovani_uzivatele and zadane_heslo in registrovani_uzivatele.get(zadane_jmeno):
    pass
else:
    print("unregistered user, terminating the program...")
    quit()

print(oddelovac)
print(f"Welcome to the app, {zadane_jmeno} We have 3 texts to be analyzed")
print(oddelovac)

zadane_cislo = input("Enter a number btw. 1 and 3 to select: ")
if zadane_cislo.isnumeric():
     zadane_cislo = int(zadane_cislo)
     print(oddelovac)
else:
    print("the entered input is not a number, terminating program...")
    quit()

if zadane_cislo > 0 and zadane_cislo < 4:
    vybrany_text = TEXTS[zadane_cislo - 1].split()
    for slovo in vybrany_text:
        slovo = slovo.strip('.,?!')
        pocet_slov += 1

        if slovo.isalpha() and slovo.isupper():
            pocet_slov_velkymi += 1
        
        if slovo.isalpha() and slovo[0].isupper():
            zacina_velkymi += 1
      
        if slovo.isalpha() and slovo[0].islower():
            zacina_malymi += 1
        
        if slovo.isnumeric():
            cisla += 1
            soucet_cisel = soucet_cisel + int(slovo)

        if len(slovo) not in pocet_vyskytu_delek_slov:
            pocet_vyskytu_delek_slov.update({len(slovo):1})
        else:
            pocet_vyskytu_delek_slov[len(slovo)] = pocet_vyskytu_delek_slov[len(slovo)] + 1
        
    serazeny_list_vyskytu_delek = sorted(pocet_vyskytu_delek_slov.items())
    pocet_vyskytu_delek_slov = dict(serazeny_list_vyskytu_delek)
        
else:
    print("the entered number of a text does not exist, terminating program...")
    quit()

print(f"There are {pocet_slov} word in the selected text.")
print(f"There are {pocet_slov_velkymi} uppercase words.")
print(f"There are {zacina_velkymi} titlecase words.")
print(f"There are {zacina_malymi} lowercase words.")
print(f"There are {cisla} numeric strings.")
print(f"The sum of all the numbers: {soucet_cisel}")
print(oddelovac)
print(f"LEN|   OCCURENCES         |NR.")
print(oddelovac)

for key, value in pocet_vyskytu_delek_slov.items():
    print(f"{key:3}| {'*' * value:20} |{value}")
