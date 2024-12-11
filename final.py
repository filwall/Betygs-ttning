import långsam

def slut(nyckel,nycklar_du_behöver,karaktär,hjälpta):
    hjälptext = []
    långsam.txt("Efter mycket slit och möda befan sig en stor port lite vid sidan av stigen\n")
    långsam.txt(f'Det fanns {nycklar_du_behöver} nyckelhål längst med dörrkarmen\n')
    print()
    if nyckel < nycklar_du_behöver:
        print(f'Du har tyvärr bara {nyckel} få nyckar. Vad som finns bakom förblir ett mysterium!\n')
    else:
        långsam.txt("Efter du vridit om alla nyckar börjar portarna öppna sig och du ser en by bakom springan mellan de gigantiska portarna\n")
        långsam.txt("När du väl kommit in ser du\n")
        if "blomma" in hjälpta:
            långsam.txt("Blomman som du vattnade förut stod frisk i en kruka på en fönsterkarm\n")
            hjälptext.append("b")

        if "skottkärra" in hjälpta:
            långsam.txt("den äldre damen med skottkärran du hjälpte förut. Hon kastade ett äpple till dig\n")
            hjälptext.append("s")

        if "fotboll" in hjälpta:
            långsam.txt("barnen du träffade förut spela fotboll på torget\n")
            hjälptext.append("f")

        if "hunden" in hjälpta:
            långsam.txt("hunden som nu låg på en altan med pinnen du kastat i munnen\n")
            hjälptext.append("h")
        
        if "kohage" not in hjälpta:
            långsam.txt("Några kor som gick runt på torget\n")
        
        if "tonåring" in hjälpta:
            långsam.txt("tonåringen var i en carport och skruvade på mopeden\n")
            hjälptext.append("t")

        if "musikant" in hjälpta:
            långsam.txt("musikanten som stod och spelade på en träpall med en liten publik\n")
            hjälptext.append("m")

        if len(hjälptext) == 0:
            långsam.txt("Du hjälpte inte någon så torget är nästan helt öde\n")




        





#print("Du vann")
#if karaktär == 1:
#print("1")
#elif karaktär == 2:
#print("2")
#elif karaktär == 3:
#print("3")
#elif karaktär == 4:
#print("4")
#1
#"August Tonkonstnären"

#2
#"Jerome Krigaren"
        
#3
#"Kristos Präst"
        
#4
#"Spartasus Trollgubben"
