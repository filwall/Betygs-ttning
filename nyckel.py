import långsam
def hittade_nycklar(nycklar,hinder):
    if nycklar == 1:
        långsam.txt(f'Han såg något blänkande strax efter han paserat {hinder} De verkar vara en nyckel. Den kommer nog till användning.\n')
    elif nycklar == 2:
        långsam.txt(f'En bit bortanför {hinder} hittar han en till nyckel. Han tar med den också.\n')
    elif nycklar == 3:
        långsam.txt(f'Sedär en till nyckel. Undra vad dessa nycklar kan vara bra för.\n')
    elif nycklar == 4:
        långsam.txt(f'Någon är riktigt bra på att tappa nyckar. Om inte någon placerat dem där.\n')
    elif nycklar == 5:
        långsam.txt(f'Detta börjar bli förmycket, enligt spelskaparen ska du inte kuna hitta såhär många nycklar.\n')