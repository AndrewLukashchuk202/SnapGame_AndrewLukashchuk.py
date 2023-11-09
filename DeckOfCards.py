import random


class DeckOfCards:

    def __init__(self, deck):
        self.deck = deck

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def deal(self, players):
        hand_size = 52 // players
        hands = []
        for i in range(players):
            hand = random.sample(self.deck, k=hand_size)
            hands.append(hand)
            self.deck = [card for card in self.deck if card not in hand]
        self.deck.clear()
        return hands

    def display_deck(self):
        return self.deck
