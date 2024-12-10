import random
import tärning
import långsam

# lista på saker man kan få
fiender = ["bro","orm","jättespindel","datorvirus","zombie"]

def hinder():
    tal = random.randrange(len(fiender)) #Väljer ett slumpmässigt hinder från listan
    fiende = fiender[tal] # sak blir det man får
    return fiende


def berätta_hinder(nuvarande): #Lägg in tärningens tal för att skippa om man har föremål
    if nuvarande == "bro":
        långsam.txt("Du har nått en bro slå en 2 eller högre för att komma över bron.\n")
        print()
        tal = 2

    elif nuvarande == "orm":
        långsam.txt("Framför dig ser du ett ormbo slå en 3 eller högre för att ta dig över stengärdsgård utan att väcka ormarna.\n")
        tal = 3

    elif nuvarande == "jättespindel":
        långsam.txt("Du ser en jättespindel slå 4 eller högre för smyga runt den utan att något av dess 8 ögon ser dig.\n")
        tal = 4

    elif nuvarande == "datorvirus":
        långsam.txt("Du håller på att bli hackad slå en 5 eller högre för att klara dig undan datorviruset Wabbit.\n")
        tal = 5

    elif nuvarande == "zombie":
        långsam.txt("Du ser en zombie slå en 6 för lyckas slå ut zombien i solljuset så den brinner upp.\n")
        tal = 6

    else:
        print("Error")
    return nuvarande, tal

#hinder1 = hinder.hinder()
#tal = hinder.berätta_hinder(hinder1)[1]
#print(tal)
    
def fiende_vapen(hinder, ryggsäck):
    kast = 7
    if hinder == "bro" and 'plankor' in ryggsäck:
        ryggsäck.remove('plankor')
        långsam.txt("När du kom fram till bron insåg du att du har plankor med dig och kan laga bron så du kunde pasera säkert utan att använda tärningen\n")

    elif hinder == "orm" and 'stor leksaksorm' in ryggsäck:
        ryggsäck.remove('stor leksaksorm')
        långsam.txt("När du började närma dig ormboet insåg du att du har en jätte leksaksorm i väskan vilket skrämmer de riktiga ormarna och strunta i tärningen\n")

    elif hinder == "jättespindel" and 'tysta kängor' in ryggsäck:
        ryggsäck.remove('tysta kängor')
        långsam.txt("För att undankomma den stora spindeln tar du på dig dina tysta kängor och struntar i tärningen för att smyga run jättespindeln\n")

    elif hinder == "datorvirus" and 'nordvpn' in ryggsäck:
        ryggsäck.remove('nordvpn')
        långsam.txt("Din mobil började överhetta och få massa felmeddelanden som tur är har du NordVPN som räddar dig helt utan tärningen\n")

    elif hinder == "zombie" and 'guldäpple' in ryggsäck:
        ryggsäck.remove('guldäpple')
        långsam.txt("Istället för att ta hjälp av tärningen använder du ditt guldäpple för att befria zombien genom att göra den till en bybo\n")
    else:
        print("\n Tryck på ENTER för att kasta din tärning")
        input()
        print(end= '\r')
        tärning.snurra(6)
        kast = tärning.siffra()
        tärning.tärning(kast)
    return kast

## Fungerande exempel
#vapen = "plankor"
#stop = "bro"
#ryggsäck = ["plankor"]
#kast = hinder.fiende_vapen(stop, vapen, ryggsäck)


##############Ska besegra_hinder och berätta_resultat vara samma funtkion # Troligtvis JA
def besegra_hinder(kast, att_slå):
    if kast >=  att_slå:
        besegrad = True
    else:
        besegrad = False
    if 1 >= kast >= 6: 
        långsam.txt(f'Du slog en {kast}\n')
    print()
    return besegrad

# lägg in om man lyckas eller inte 
def berätta_resultat(fiende, karaktär):
    print()
    if fiende == "bro":
        långsam.txt(f'{karaktär} lyckades ta sig över bron utan att falla ner i den långa avgrunden\n')
    elif fiende == "orm":
        långsam.txt(f'{karaktär} tog sig över stengärdsgård utan att väcka ormarna\n')
    elif fiende == "jättespindel":
        långsam.txt(f'{karaktär} smöga runt jättespindeln utan att något av dess 8 ögon såg honom\n')
    elif fiende == "datorvirus":
        långsam.txt(f'{karaktär} klara sig undan datorviruset Wabbit\n')
    elif fiende == "zombie":
        långsam.txt(f'{karaktär} lyckas slå ut zombien i solljuset och låter elden göra resten\n')
  

##############################
#Fungerande Exempel#
#import hinder
#
#
#if hinder.besegra_hinder(4):
#    print("Grattis")
#else:
#    print("Du dog")

