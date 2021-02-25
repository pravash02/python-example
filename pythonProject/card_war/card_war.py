import random


class Deck:
    def __init__(self, suite, ranks):
        print('Creating new ordered Deck!')
        self.my_cards = [(s, r) for s in suite for r in ranks]

    def shuffle_deck(self):
        print('Shuffling Cards!')
        random.shuffle(self.my_cards)

    def split_in_half(self):
        print('Splitting Cards!')
        return self.my_cards[:26], self.my_cards[:26]


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return f"Contains {len(self.cards)} cards"

    def add_cards(self, my_cards):
        return self.cards.extend(my_cards)

    def remove_cards(self):
        return self.cards.pop()


class Players:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand    # Hand class object

    def play_cards(self):
        drawn_cards = self.hand.remove_cards()
        print(f"{self.name} placed card {self.hand}")
        return drawn_cards

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_cards())
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 0


if __name__ == '__main__':
    SUITE = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    print("Welcome to war and begin")
    d = Deck(SUITE, RANKS)
    d.shuffle_deck()
    card1, card2 = d.split_in_half()

    comp1 = Players('computer', Hand(card1))
    comp2 = Players('computer2', Hand(card2))
    print(comp1.name + ' has cards - ' + str(len(comp1.hand.cards)))
    print(comp2.name + ' has cards - ' + str(len(comp2.hand.cards)))

    total_rounds = 0
    war_counts = 0

    while comp1.still_has_cards() and comp2.still_has_cards():
        total_rounds += 1
        print('Time for new round!')
        print('Here are the standings')
        print(comp1.name + ' has cards - ' + str(len(comp1.hand.cards)))
        print(comp2.name + ' has cards - ' + str(len(comp2.hand.cards)))

        table_cards = []

        print('play a card!')
        c1_card = comp1.play_cards()
        c2_card = comp2.play_cards()

        table_cards.append(c1_card)
        table_cards.append(c2_card)
        if c1_card[1] == c2_card[1]:
            war_counts += 1
            print('war!')
            table_cards.extend(comp1.remove_war_cards())
            table_cards.extend(comp2.remove_war_cards())

            if RANKS.index(c1_card[1]) < RANKS.index(c2_card[1]):
                comp1.hand.add_cards(table_cards)
            else:
                comp2.hand.add_cards(table_cards)
        else:
            if RANKS.index(c1_card[1]) < RANKS.index(c2_card[1]):
                comp1.hand.add_cards(table_cards)
            else:
                comp2.hand.add_cards(table_cards)

    print('GAME OVER')
    print('number of rounds', total_rounds)
    print('A war happened ' + str(war_counts) + ' times')
    print('Does first player has cards?')
    print(comp1.still_has_cards())
    print('Does second player has cards?')
    print(comp2.still_has_cards())
