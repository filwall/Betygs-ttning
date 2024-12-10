import random

def siffra():
    kast = random.randrange(1,7)
    return kast

def tärning(tal):

    tärningar = {
        1: [
            "+-------+",
            "|       |",
            "|   O   |",
            "|       |",
            "+-------+"
        ],
        2: [
            "+-------+",
            "| O     |",
            "|       |",
            "|     O |",
            "+-------+"
        ],
        3: [
            "+-------+",
            "| O     |",
            "|   O   |",
            "|     O |",
            "+-------+"
        ],
        4: [
            "+-------+",
            "| O   O |",
            "|       |",
            "| O   O |",
            "+-------+"
        ],
        5: [
            "+-------+",
            "| O   O |",
            "|   O   |",
            "| O   O |",
            "+-------+"
        ],
        6: [
            "+-------+",
            "| O   O |",
            "| O   O |",
            "| O   O |",
            "+-------+"
        ]
    }
    

    if tal in tärningar:
        for rad in tärningar[tal]:
            print(rad)
    else:
        print("Välj mellan 1 och 6.")

def snurra(gånger):
    import time
    for i in range(gånger):
        print("\033c", end="")
        tärning(siffra())
        time.sleep(0.4)
        print("\033c", end="")

#snurra_tärning(10)
#tärning(siffra())