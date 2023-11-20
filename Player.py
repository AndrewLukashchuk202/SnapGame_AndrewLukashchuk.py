from DeckOfCards import DeckOfCards


class Player(DeckOfCards):
    """A class representing a player in a card game.

        Attributes:
            name (str): The name of the player.
            hand (list): A list containing the cards in the player's hand.

        Methods:
            __init__(name, hand, deck): Initializes a Player object.
            snap(players_card, top_card): Checks if the player can snap based on the top card.
            collect_cards(deck): Collects cards from the deck and adds them to the player's hand.
            has_cards(): Checks if the player has any cards in their hand.
    """
    def __init__(self, name, hand, deck):
        """Initialize a Player object.

            Args:
                name (str): The name of the player.
                hand (list): A list of cards representing the player's hand.
                deck (list): A list of cards representing the initial deck of the game.
        """
        super().__init__(deck)
        self.name = name
        self.hand = hand

    def snap(self, players_card, top_card):
        """Check if the player can snap based on the top card. Cards are represented in the following format ->
            (2_spade, 3_heart, 4_club, ace_diamond). For that reason, cards are split by _ underscore sign to
            get separately the number and the suit

            Args:
                players_card (str): The card the player wants to play.
                top_card (str): The current top card on the table.

            Returns:
                bool: True if the player can snap, False otherwise.
        """
        list_of_players_card = players_card.split("_")
        list_of_top_card = top_card.split("_")
        if list_of_players_card[0] == list_of_top_card[0]:
            return True
        else:
            return False

    def collect_cards(self, deck):
        """Collect cards from the deck and add them to the player's hand.

            Args:
                deck (list): A list of cards to be collected by the player.
        """
        for i in deck:
            self.hand.append(i)

    def has_cards(self):
        """Check if the player has any cards in their hand.

           Returns:
               bool: True if the player has cards, False otherwise.
        """
        if len(self.hand) == 0:
            return False
        else:
            return True
    
         
