import random

# Kortsymboler och kortnamn
farger = ["♠", "♥", "♦", "♣"]
kort_namn = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


# Skapa kortleken samt blanda dom
def skapa_kortlek():

    kortlek = []

    for farg in farger:
        for namn in kort_namn:
            kortlek.append((namn, farg))

    random.shuffle(kortlek)

    return kortlek



# poäng räkning
def rakna_poang(hand):

    poang = 0
    antal_ess = 0

    for kort in hand:

        namn = kort[0]

        if namn in ["J", "Q", "K"]:
            poang += 10

        elif namn == "A":
            poang += 11
            antal_ess += 1

        else:
            poang += int(namn)

    # Gör om ess från 11 till 1 vid behov
    while poang > 21 and antal_ess > 0:
        poang -= 10
        antal_ess -= 1

    return poang


# Visa hand
def visa_hand(hand, dold_forsta=False):

    kort_text = ""

    for i, kort in enumerate(hand):

        if i == 0 and dold_forsta:
            kort_text += "[??] "

        else:
            namn = kort[0]
            farg = kort[1]
            kort_text += f"[{namn}{farg}] "

    return kort_text



# själva spelet börjar
def blackjack():

    print("=== BLACKJACK ===")

    kortlek = skapa_kortlek()

    spelarens_hand = []
    dealerns_hand = []

    # Dela ut startkort
    spelarens_hand.append(kortlek.pop())
    spelarens_hand.append(kortlek.pop())

    dealerns_hand.append(kortlek.pop())
    dealerns_hand.append(kortlek.pop())

    # Spelarens tur
    while True:

        print("\nDealer:")
        print(visa_hand(dealerns_hand, dold_forsta=True))

        print("\nDu:")
        print(visa_hand(spelarens_hand))

        spelar_poang = rakna_poang(spelarens_hand)

        print("Poäng:", spelar_poang)

        # Bust
        if spelar_poang > 21:
            print("\nDu blev bust! Dealer vann.")
            return

        val = input("\nHit eller Stand? (h/s): ").lower()

        if val == "h":
            spelarens_hand.append(kortlek.pop())

        elif val == "s":
            break

        else:
            print("Skriv antingen h eller s!")

    # Dealerns tur
    while rakna_poang(dealerns_hand) < 17:
        dealerns_hand.append(kortlek.pop())

    # Slutresultat
    spelar_poang = rakna_poang(spelarens_hand)
    dealer_poang = rakna_poang(dealerns_hand)

    print("\n=== RESULTAT ===")

    print("\nDealer:")
    print(visa_hand(dealerns_hand))
    print("Poäng:", dealer_poang)

    print("\nDu:")
    print(visa_hand(spelarens_hand))
    print("Poäng:", spelar_poang)

    # Avgör vinnare
    if dealer_poang > 21:
        print("\nDealer blev bust! Du vann!")

    elif spelar_poang > dealer_poang:
        print("\nDu vann!")

    elif dealer_poang > spelar_poang:
        print("\nDealer vann!")

    else:
        print("\nOavgjort!")



# Starta spelet
blackjack()

