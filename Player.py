from DeckOfCards import DeckOfCards
import random


class Player(DeckOfCards):

    def __init__(self, name, hand, deck):
        super().__init__(deck)
        self.name = name
        self.hand = hand

    def snap(self, players_card, top_card):
        list_of_players_card = players_card.split("_")
        list_of_top_card = top_card.split("_")
        if list_of_players_card[0] == list_of_top_card[0]:
            return True
        else:
            return False

    def collect_cards(self, deck):
        for i in deck:
            self.hand.append(i)

    def has_cards(self):
        if len(self.hand) == 0:
            return False
        else:
            return True

    
         
