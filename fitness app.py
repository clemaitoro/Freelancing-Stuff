import webbrowser
from time import sleep

print("Aceasta  este o aplicatie care te va ajuta sa slabesti sau sa cresti in greutate")
nume = input("Pentru inceput te rog sa imi spui cum te numesti: ")
ani = input("Cati ani aveti?: ")
kg = input("Imi poti spune ce greutate ai?: ")
inaltime= input("Imi spui te rog si inaltimea in centimetri(cm): ")
Sex = input("Si in final imi poti spune sexul tau? (masculin, feminim) \n"
            "daca nu ai dori sa raspunzi la aceasta intrebare scrie '.' ")
sleep(0.3)

print("Acum iti vom calcula consumul zilnic de energie: ")
print("calculam................................................................")
sleep(1)

if Sex.lower() == "masculin":
    Bmr = (66.47 +( 13.75 * int(kg) + (5.003 * int(inaltime) - (6.755 * int(ani)))))
    print(f"Daca vei consuma acest numar de calorii zilnic nici nu vei slabii dar nici nu te vei "
          f"ingrasa {Bmr}")
elif Sex.lower() == "feminim":
    bmr = 655.1 + (9.563 * int(kg)) + (1.85 * int(inaltime)) - (4.676 * int(ani))
    print(f"Daca vei consuma acest numar de calorii zilnic nici nu vei slabii dar nici nu te vei "
          f"ingrasa {bmr}")
else:
    Bmr = (66.47 + (13.75 * int(kg) + (5.003 * int(inaltime) - (6.755 * int(ani)))))
    print(Bmr)
    print(f"Daca vei consuma acest numar de calorii zilnic nici nu vei slabii dar nici nu te vei "
          f"ingrasa {Bmr}")

dorinta = input("Doriti sa scadeti in greutate?: ")

if dorinta.lower() == "da":
   alegere = input("ati dori sa va recomand site-uri si aplicatii pentru a va ajuta?")
   if alegere.lower() == "da":
        print("Iti voi deschide in broswer un site pentru o dieta, unul cu o aplicate ce te poate ajuta"
              "sa ti curent de calorii si inca unul cu o aplicatie ce are exerctii care te vor ajuta ")
        sleep(1)
        webbrowser.open("https://www.myfitnesspal.com/")
        sleep(1)
        webbrowser.open("https://cureslabit.ro/slabire/plan-de-slabit-in-7-zile/")
        sleep(1)
        webbrowser.open("https://www.youtube.com/watch?v=9nTxjn7Y4vc&ab_channel=ElenaGologan")
   else:
       print(f"Foarte bine {nume} iti urez mult succes")
else:
    alegere = input("ati dori sa va recomand site-uri si aplicatii pentru a va ajuta?")
    if alegere.lower() == "da":
        print(print("Iti voi deschide in broswer un site pentru o dieta, unul cu o aplicate ce te poate ajuta"
                    "sa ti curent de calorii si inca unul cu o aplicatie ce are exerctii care te vor ajuta "))
        sleep(1)
        webbrowser.open("https://www.myfitnesspal.com/")
        sleep(1)
        webbrowser.open("https://doc.ro/controlul-greutatii/dieta-pentru-crestere-in-greutate-si-marirea-masei-musculare")
        sleep(1)
        webbrowser.open("https://www.youtube.com/watch?v=zIz_6Nc2zrE")
    else:
        print(f"Foarte bine {nume} iti urez mult succes")


