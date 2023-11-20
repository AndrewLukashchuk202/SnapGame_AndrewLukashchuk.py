from Player import Player
from DeckOfCards import DeckOfCards
import random


class Play:
    """A class representing a card game.

        Attributes:
            deck (list): A list containing the initial deck of cards.
            name (str): The name of the game.

        Methods:
            __init__(name): Initializes a Play object with the given name.
            set_deck(): Creates and returns a new deck of cards.
            get_players(): Prompts the user for the number of players and their names.
            play(): Manages the gameplay, dealing cards, and determining the winner.
        """

    deck = ['2_spades', '3_spades', '4_spades', '5_spades', '6_spades', '7_spades', '8_spades', '9_spades', '10_spades',
            'jack_spades', 'queen_spades', 'king_spades', 'ace_spades', '2_hearts', '3_hearts', '4_hearts', '5_hearts',
            '6_hearts', '7_hearts', '8_hearts', '9_hearts', '10_hearts', 'jack_hearts', 'queen_hearts', 'king_hearts',
            'ace_hearts', '2_diamonds', '3_diamonds', '4_diamonds', '5_diamonds', '6_diamonds', '7_diamonds',
            '8_diamonds', '9_diamonds', '10_diamonds', 'jack_diamonds', 'queen_diamonds', 'king_diamonds',
            'ace_diamonds', '2_clubs', '3_clubs', '4_clubs', '5_clubs', '6_clubs', '7_clubs', '8_clubs',
            '9_clubs', '10_clubs', 'jack_clubs', 'queen_clubs', 'king_clubs', 'ace_clubs']

    def __init__(self, name):
        """Initialize a Play object with the given name.

        Args:
            name (str): The name of the game.
        """
        self.name = name

    def set_deck(self):
        """Create and return a new deck of cards.

        Returns:
            DeckOfCards: A DeckOfCards object representing the deck.
        """
        gaming_deck = DeckOfCards(self.deck)
        return gaming_deck

    def get_players(self):
        """Prompt the user for the number of players and their names.

        Returns:
            list: A list of Player objects representing the players.
        """
        players_list = []

        while True:
            try:
                number_of_players = int(input("How many players are playing? "))
                if 2 <= number_of_players <= 52:
                    break
                else:
                    print("Inappropriate number of players, please resubmit your number again")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        for i in range(number_of_players):
            name = input("Provide player's name please! ")
            player = Player(name, None, self.deck)
            players_list.append(player)

        return players_list

    def play(self):
        """Manage the gameplay, dealing cards, and determining the winner.

            The game consists of the following steps:
            1. Create a new deck of cards.
            2. Prompt the user for the number of players and their names.
            3. Shuffle the deck and deal cards to the players.
            4. Conduct rounds of the game until only one player has cards.
            5. Display the status of each round and the winner.

            The gameplay involves players taking turns putting cards on the table.
            If a player's card matches the top card on the table, they shout "snap!"
            and collect all the cards on the table. The game continues until only
            one player has cards remaining.

            This method does not return any value but prints the game status and
            the winner at the end.
            """

        gaming_deck = self.set_deck()

        list_of_players = self.get_players()

        rounds = 1

        gaming_deck.shuffle()

        hands = gaming_deck.deal(len(list_of_players))
        card_index = 0
        for player in list_of_players:
            player.hand = hands[card_index]
            card_index += 1

        print("Snap game starts!")

        while len(list_of_players) > 1:
            print("---------------------------------------")
            print(f"\tStart of the round number  {rounds}:")
            for player in list_of_players:
                print(f"Player - {player.name} has {player.hand}")

            print(f"Cards on the table - {gaming_deck.display_deck()}")

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

            print(f"\tEnd of the round number {rounds}")
            print("---------------------------------------")

            rounds += 1

            for player in list_of_players:
                if not player.has_cards():
                    list_of_players.remove(player)

        for player in list_of_players:
            if player.has_cards():
                print(f"Player {player.name} has won, since he/she is the only player with cards")


game1 = Play("Room 101")
game1.play()
