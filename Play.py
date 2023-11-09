from Player import Player
from DeckOfCards import DeckOfCards
import random


class Play:

    deck = ['2_spades', '3_spades', '4_spades', '5_spades', '6_spades', '7_spades', '8_spades', '9_spades', '10_spades',
            'jack_spades', 'queen_spades', 'king_spades', 'ace_spades', '2_hearts', '3_hearts', '4_hearts', '5_hearts',
            '6_hearts', '7_hearts', '8_hearts', '9_hearts', '10_hearts', 'jack_hearts', 'queen_hearts', 'king_hearts',
            'ace_hearts', '2_diamonds', '3_diamonds', '4_diamonds', '5_diamonds', '6_diamonds', '7_diamonds',
            '8_diamonds', '9_diamonds', '10_diamonds', 'jack_diamonds', 'queen_diamonds', 'king_diamonds',
            'ace_diamonds', '2_clubs', '3_clubs', '4_clubs', '5_clubs', '6_clubs', '7_clubs', '8_clubs',
            '9_clubs', '10_clubs', 'jack_clubs', 'queen_clubs', 'king_clubs', 'ace_clubs']

    def __init__(self, name):
        self.name = name

    def set_deck(self):
        gaming_deck = DeckOfCards(self.deck)
        return gaming_deck

    def get_players_amount(self):
        players_amount = int(input("How many players are playing? "))
        return players_amount

    def get_players(self):
        players = []
        players_amount = self.get_players_amount()
        for i in range(players_amount):
            name = input("Provide player's name please! ")
            player = Player(name, None, self.deck)
            players.append(player)
        return players

    def play(self):
        # creating deck
        gaming_deck = self.set_deck()
        # making players
        list_of_players = self.get_players()

        rounds = 1

        # shuffling cards
        gaming_deck.shuffle()

        # getting number of players and giving them cards
        hands = gaming_deck.deal(len(list_of_players))
        card_index = 0
        for i in list_of_players:
            i.hand = hands[card_index]
            card_index += 1

        # game starts
        print("Snap game starts!")

        # bool variable to see if we play or not in case if user has run out of cards
        do_we_play = True

        while do_we_play:
            print(f"\tStart of the round number  {rounds}:")
            for player in list_of_players:
                print(f"Player - {player.name} has {player.hand}")

            print(f"Cards on the table - {gaming_deck.display_deck()}")

            # checking if it is not the first round because on the first round table is empty
            if rounds != 1:
                for player in list_of_players:
                    players_card = random.choice(player.hand)
                    if len(gaming_deck.deck) != 0:
                        if not player.snap(players_card, gaming_deck.display_deck()[-1]):
                            gaming_deck.deck.append(players_card)
                            player.hand.remove(players_card)
                            print(f"Player {player.name} puts card {players_card} on the table")
                        else:
                            print(f"Player {player.name} puts card {players_card}, says - snap! and takes all the cards")
                            player.collect_cards(gaming_deck.deck)
                            gaming_deck.deck.clear()
                    else:
                        gaming_deck.deck.append(players_card)
                        player.hand.remove(players_card)
                        print(f"Player {player.name} puts card {players_card} on the table")

                print(f"\tEnd of the round number {rounds}:")
                for player in list_of_players:
                    print(f"Player - {player.name} has {player.hand}")
                print(f"Cards on desk - {gaming_deck.deck}")
                rounds += 1

                for player in list_of_players:
                    if not player.has_cards() and len(list_of_players) != 1:
                        list_of_players.remove(player)

                    if len(list_of_players) == 1:
                        do_we_play = False
            else:
                # checking if table still empty or someone already put a card
                for player in list_of_players:
                    players_card = random.choice(player.hand)
                    if len(gaming_deck.deck) != 0:
                        if not player.snap(players_card, gaming_deck.display_deck()[-1]):
                            gaming_deck.deck.append(players_card)
                            player.hand.remove(players_card)
                            print(f"Player {player.name} puts card {players_card} on the table")
                        else:
                            print(f"Player {player.name} puts {players_card}, says - snap! And takes all the cards")
                            player.collect_cards(gaming_deck.deck)
                            gaming_deck.deck.clear()
                    else:
                        gaming_deck.deck.append(players_card)
                        player.hand.remove(players_card)
                        print(f"Player {player.name} puts card {players_card} on the table")

                print(f"\tEnd of the round number {rounds}:")
                for player in list_of_players:
                    print(f"Player - {player.name} has {player.hand}")
                print(f"Cards on desk - {gaming_deck.deck}")
                rounds += 1

                for player in list_of_players:
                    if not player.has_cards() and len(list_of_players) != 1:
                        list_of_players.remove(player)

                    if len(list_of_players) == 1:
                        do_we_play = False

        for player in list_of_players:
            if player.has_cards():
               print(f"Player {player.name} has won!")

game1 = Play("Room 101")
game1.play()

