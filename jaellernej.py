def svar():
    while True:
        svar = input("Ange ditt svar (Ja eller Nej): \n").strip() 

        if svar.lower() == "ja" or svar.lower() == "nej":
            svar = svar.lower()
            break 
    return svar