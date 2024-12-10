import långsam
import jaellernej

def hjälpa(tal):
    resultat = "inget"
    if tal == 0:
        långsam.txt("Han ser en halvvissen blomma på gräsbiten mellan traktorspåren\n")
        långsam.txt("Kommer han vattna den?\n")
        if jaellernej.svar() == "ja":
            resultat = "blomma"
            långsam.txt("Han valde att offra lite av sitt dricksvatten, hoppas de hjälper\n")
        else:
            långsam.txt("Han struntade i blomman, den borde klara sig ändå.\n")

    elif tal == 1:
        långsam.txt("Han såg en äldre dam som hade vält med sin skottkärra full med äpplen\n")
        långsam.txt("Kommer han hjälpa till att resa skottkärran?\n")
        if jaellernej.svar() == "ja":
            resultat = "skottkärra"
            långsam.txt("Han valde att resa skottkärran före han fortsatte gå\n")
        else:
            långsam.txt("Han gick bara förbi, hon löser det någ ändå\n")

    elif tal == 2:
        långsam.txt("Han såg några barn som tittade upp i ett träd och det visade sig att deras fotboll har fastnat där uppe\n")
        långsam.txt("Kommer han klättra upp för att hämta fotbollen?\n")
        if jaellernej.svar() == "ja":
            resultat = "fotboll"
            långsam.txt("Han valde att klättra upp då barn inte alltid har koll på vart dem sätter fötterna\n")
        else:
            långsam.txt("Han gick förbi barnen. Om dem får upp den måste dem få ner den\n")

    elif tal == 3:
        långsam.txt("Han såg en glad hund som ville leka\n")
        långsam.txt("Kommer han kasta en pinne som hunden kan hämta?\n")
        if jaellernej.svar() == "ja":
            resultat = "pinne"
            långsam.txt("Han kastade pinnen några gånger tills hunden la sig och vilade med pinnen i munnen\n")
        else:
            långsam.txt("Han struntade i hunden då man aldrig vet hur djur man inte känner beter sig\n")


    elif tal == 4:
        långsam.txt("Han såg en grind som var öppen till en kohage\n")
        långsam.txt("Kommer han stänga grinden?\n")
        if jaellernej.svar() == "ja":
            resultat = "kohage"
            långsam.txt("Han stängde grinden då det är bättre att vara på den säkra sidan\n")
        else:
            långsam.txt("Bonden är säkert i närheten tänkte han\n")

    elif tal == 5:
        långsam.txt("En tonåring stog och försökte få igång sin moped\n")
        långsam.txt("Ska han hjälpa till genom att försöka skjuva igång den?\n")
        if jaellernej.svar() == "ja":
            resultat = "moped"
            långsam.txt("Det fungerade mopeden gick igång, tonåringen tackade för hjälpen och åkte iväg\n")
        else:
            långsam.txt("Han kan ju inget om mopeder, vad kunde man gjort?\n")


    elif tal == 6:    
        långsam.txt("Han mötte en musikant\n")
        långsam.txt("Vill han stanna en stund för att lyssna på lite musik?\n")
        if jaellernej.svar() == "ja":
            resultat = "musikant"
            långsam.txt("Han lyssnade en stund och han känner sig mycket piggare och gladare\n")
        else:
            långsam.txt("Du gick förbi då musikanten inte såg ut att matcha din musiksmak\n")
    print()
    return resultat
