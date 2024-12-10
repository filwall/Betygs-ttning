import tärning
import långsam
import karaktärer
import kista
import hinder
import random
import nyckel
import final
import resemonolog
import jaellernej
import hjälpamonolog

import os
import time

#ryggsäck = []

#poäng_du_behöver = random.randint(0,4)
#nycklar = 0 #avklarad_nivå
#totalt_spelade_nivåer = 0

#kistmonologlista = [1,2,3,4,5,6]

#hjälpmonologlista = [0,1,2,3,4,5,6]
#hjälpta = []

# Här skriver vi in vilka atributer som karaktärerna ska ha
august = "August Tonkonstnären en tonkonstnär som älskar att underhålla folk med sin gräsliga musiksmak!"
jerome = "Jerome Krigaren en riktig krigare som inte bara är stor och stark men är även i ett förhållande med sin yxa Ylva!"
kristos = "Kristos Präst en man som tror han är jesus eller gud han själv. Han tror väldigt gott om sig själv... kan bli problem i kniviga sitvationer!"
spartasus = "Spartasus Trollgubben det säger sig själv vad spartasus är. Tolka det hur du vill!"


#print(end="\r")
# Här väljer spelaren vilket karaktär som spelet ska använda och där äventyret börjar

def huvudspel():
    os.system("cls")
    ryggsäck = []

    poäng_du_behöver = random.randint(0,4)
    nycklar = 0 #avklarad_nivå
    totalt_spelade_nivåer = 0

    kistmonologlista = [1,2,3,4,5,6]

    hjälpmonologlista = [0,1,2,3,4,5,6]
    hjälpta = []

    print("Välj din spelare genom att skriva in motsvande siffra sedan tryck ENTER")
    långsam.txt("1. August tonkonstnär, 2.Jerome Krigare, 3. Kristos Präst, 4.Spartasus Trollgubbe" "\n")

    while True:
        karaktär = int(input(""))
        if 1 <= karaktär <= 4:
            break
        else:
            print("Du har inte valt en giltlig karakär försökt igen")




    if karaktär == 1:
        spelare1klass = august
        spelare1 = "August Tonkonstnären"

    elif karaktär == 2:
        spelare1klass = jerome
        spelare1 = "Jerome Krigaren"
            
    elif karaktär == 3:
        spelare1klass = kristos
        spelare1 = "Kristos Präst"
            
    elif karaktär == 4:
        spelare1klass = spartasus
        spelare1 = "Spartasus Trollgubben"
            


    #Visar bilden
    if spelare1klass == august:
        karaktärer.print_august()

    elif spelare1klass == jerome:
        karaktärer.print_jerome()

    elif spelare1klass == kristos:
        karaktärer.print_kristos()

    elif spelare1klass == spartasus:
        karaktärer.print_spartasus()
    else:
        print("ERROR 404")

    #Skriver ut vem man valde och lite backstory ett tecken i taget
    långsam.txt(f'Du har valt {spelare1klass}')


    print("\n Tryck på ENTER för att starta ditt äventyr")
    input()
    print(end= '\r')

    ########## KONTROLLERA totalt_spelade_nivåer HÄR
    långsam.txt(f'{spelare1} traskar genom skogen, mest för att han inte har något bättre för sig. Det är tyst, förutom dina egna steg och... magen som kurrar.\n')
    while totalt_spelade_nivåer <= 3:
        # Skapar en lista, säger en sak sedan tar bort den från listan
        
        if totalt_spelade_nivåer == 0:
            resemonolog.kistorna(0)
        else:
            slumptal = random.choice(kistmonologlista)
            resemonolog.kistorna(slumptal)
            kistmonologlista.remove(slumptal)


        print()
        långsam.txt('Väljer han att öppna kistan?\n')


        # Kista och om man vill ha den i väskan
        svar = jaellernej.svar()

        if svar == "nej":
            långsam.txt("Du gick vidare och struntade helt i kistan")
        else:
            ryggsäckens_senaste = kista.slump()
            ryggsäck.append(ryggsäckens_senaste)
            långsam.txt(f'Du hittade {ryggsäckens_senaste} i kistan. Den kan vara bra att ha\n')
            långsam.txt(f'Nu har du {len(ryggsäck)} föremål i väskan\n')
            print(f'Föremålen: {ryggsäck}')
            print()

        print(end="\r")

        # Slumpmässig event melan kistor och hinder
        slumphjälp = random.choice(hjälpmonologlista)
        hjälp_resultat = hjälpamonolog.hjälpa(slumphjälp)
        hjälpmonologlista.remove(slumphjälp)

        if hjälp_resultat != "inget":
            hjälpta.append(hjälp_resultat)


        # Berätta om ditt första hinder
        fiende_hinder = hinder.hinder()
        att_slå = hinder.berätta_hinder(fiende_hinder)[1]

        # Kolla om du har rätt föremål i väskan och annars kasta tärningen
        kast = hinder.fiende_vapen(fiende_hinder, ryggsäck)
        

        if hinder.besegra_hinder(kast,att_slå):
            hinder.berätta_resultat(fiende_hinder,spelare1)
            nycklar += 1
            nyckel.hittade_nycklar(nycklar,fiende_hinder)
            print()
        else:
            långsam.txt(f'Det gick inte att ta sig förbi {fiende_hinder}. Det måste finnas en annan väg\n')  ## Skriv in fler meddelanden och sätt på random
            print()

        totalt_spelade_nivåer += 1
        
    final.slut(nycklar,poäng_du_behöver,karaktär,hjälpta)

# Här startas spelet

huvudspel()
print()
långsam.txt("Tack för att du spelade\n")
långsam.txt("Vill du spela igen\n")
spela_igen = jaellernej.svar()

if spela_igen == "ja":
    huvudspel()
else:
    print()
