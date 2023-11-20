import random


class DeckOfCards:
    """A class representing a deck of playing cards. The number of cards must be 52 otherwise certain methods will not
        work, 12 cards of each suit not including jokers.

        Attributes:
            deck (list): A list containing the cards in the deck.

        Methods:
            shuffle(): Shuffles the cards in the deck.
            deal(players): Deals cards to the players.
            display_deck(): Returns the current state of the deck.
    """
    def __init__(self, deck):
        """Initialize the DeckOfCards object with a provided deck.

            Args:
                deck (list): A list of strings representing the initial deck of cards.
        """
        self.deck = deck

    def shuffle(self):
        """Shuffle the cards in the deck.

            Returns:
                list: The shuffled deck.
        """
        random.shuffle(self.deck)
        return self.deck

    def deal(self, players):
        """Deal cards to the players.

            Args:
                players (int): The number of players.

            Returns:
                list: A list of lists, where each sublist represents the hand of a player.
        """
        hand_size = 52 // players
        hands = []
        for i in range(players):
            hand = random.sample(self.deck, k=hand_size)
            hands.append(hand)
            self.deck = [card for card in self.deck if card not in hand]
        self.deck.clear()
        return hands

    def display_deck(self):
        """Return the current state of the deck.

            Returns:
                list: The current deck of cards.
        """
        return self.deck
