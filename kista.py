
def slump():
    import random
    saker = ["plankor","stor leksaksorm","tysta kängor","nordvpn","guldäpple"]
    tal = random.randrange(len(saker)) #Väljer en slumpmässig sak från listan saker
    sak = saker[tal] # sak blir det man får
    return sak

# Vi får skriva in vilka saker som ska finnas och vad dem ska göra
#print(slump())