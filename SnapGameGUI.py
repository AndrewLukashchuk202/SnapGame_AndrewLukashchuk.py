from tkinter import *
import random
from PIL import Image, ImageTk
from DeckOfCards import DeckOfCards
from Player import Player
from time import sleep
import os


class SnapGameGUI:
    """
    SnapGameGUI - A simple Snap card game GUI using Tkinter.

    This class represents the graphical user interface (GUI) for a Snap card game.
    It allows two players to play the Snap card game against each other. The game
    involves players trying to "snap" and collect cards when they spot two consecutive
    cards of the same rank on the playing table.

    Attributes:
        deck (list): A list of strings representing the cards in the deck.
        master (Tk): The main Tkinter window for the Snap game GUI.
        player1_image: An image object representing the current card of Player 1.
        player2_image: An image object representing the current card of Player 2.
        desk_image: An image object representing the card on the playing table.
        players (list): A list containing instances of Player representing the players.
        gaming_deck (DeckOfCards): An instance of DeckOfCards representing the game deck.
        round (int): An integer representing the current round of the game.
        player1_frame (LabelFrame): A Tkinter LabelFrame for displaying Player 1's information.
        player2_frame (LabelFrame): A Tkinter LabelFrame for displaying Player 2's information.
        desk_frame (LabelFrame): A Tkinter LabelFrame for displaying information about the playing table.
        desk_label (Label): A Tkinter Label for displaying the current card on the playing table.
        player1_label (Label): A Tkinter Label for displaying Player 1's current card.
        player2_label (Label): A Tkinter Label for displaying Player 2's current card.
        card_button (Button): A Tkinter Button for advancing to the next round of the game.
    """

    deck = ['2_spades', '3_spades', '4_spades', '5_spades', '6_spades', '7_spades', '8_spades', '9_spades', '10_spades',
            'jack_spades', 'queen_spades', 'king_spades', 'ace_spades', '2_hearts', '3_hearts', '4_hearts', '5_hearts',
            '6_hearts', '7_hearts', '8_hearts', '9_hearts', '10_hearts', 'jack_hearts', 'queen_hearts', 'king_hearts',
            'ace_hearts', '2_diamonds', '3_diamonds', '4_diamonds', '5_diamonds', '6_diamonds', '7_diamonds',
            '8_diamonds', '9_diamonds', '10_diamonds', 'jack_diamonds', 'queen_diamonds', 'king_diamonds',
            'ace_diamonds', '2_clubs', '3_clubs', '4_clubs', '5_clubs', '6_clubs', '7_clubs', '8_clubs',
            '9_clubs', '10_clubs', 'jack_clubs', 'queen_clubs', 'king_clubs', 'ace_clubs']

    def __init__(self):
        self.master = Tk()
        self.master.title("Snap Game")
        self.master.geometry("520x500")
        self.master.configure(background="green")

        # Initialize images
        self.player1_image = None
        self.player2_image = None
        self.desk_image = None

        # Get players
        self.players = self.get_players()

        # Initialize the deck
        self.gaming_deck = DeckOfCards(self.deck)

        # Initialize round
        self.round = 1

        # Create Frames for Cards
        self.player1_frame = LabelFrame(self.master, text=self.players[0].name, bd=0)
        self.player1_frame.grid(row=0, column=0, padx=20, ipadx=20)

        self.player2_frame = LabelFrame(self.master, text=self.players[1].name, bd=0)
        self.player2_frame.grid(row=0, column=1, ipadx=20)

        # Create Frame for Top Card on desk
        self.desk_frame = LabelFrame(self.master, text='', bd=0)
        self.desk_frame.grid(row=0, column=3, ipadx=20, padx=20)

        # Create Label for the Desk
        self.desk_label = Label(self.desk_frame, text='')
        self.desk_label.pack(pady=20)

        # Create labels for displaying cards
        self.player1_label = Label(self.player1_frame, text='')
        self.player1_label.pack(pady=20)

        self.player2_label = Label(self.player2_frame, text='')
        self.player2_label.pack(pady=20)

        # Create a button
        self.card_button = Button(self.master, text="Next Round", font=("Helvetica", 14), command=self.play_round)
        self.card_button.grid(row=1, column=1, pady=20)

        # Shuffle deck before the game starts
        self.gaming_deck.shuffle()

        # Deal card with the players
        self.deal_cards()

        self.update_game_status()

    def play_round(self):
        """
        Plays a round of the Snap game, updating the GUI accordingly.
        """

        self.master.geometry("750x500")
        self.update_game_status()

        if len(self.players[0].hand) > 0 and len(self.players[1].hand) > 0:

            for player in self.players:
                players_card = random.choice(player.hand)
                if len(self.gaming_deck.deck) != 0:
                    if not player.snap(players_card, self.gaming_deck.display_deck()[-1]):

                        self.display_players_card(player, players_card)

                        self.gaming_deck.deck.append(players_card)
                        player.hand.remove(players_card)

                    else:
                        self.display_players_card(player, players_card)

                        self.master.title(f"Player - {player.name} says snap and collects all cards")

                        player.collect_cards(self.gaming_deck.deck)
                        self.gaming_deck.deck.clear()
                else:
                    self.display_players_card(player, players_card)

                    self.gaming_deck.deck.append(players_card)
                    player.hand.remove(players_card)

            self.round += 1

        elif len(self.players[0].hand) == 0 and len(self.players[1].hand) == 0:
            self.master.title("No one won as no one shouted - Snap")
        else:
            for player in self.players:
                if player.has_cards():
                    self.master.title(f"Player {player.name} wins because he is the only one left with cards!")
                    # using sleep to read the messages
                    sleep(0.7)

    def display_players_card(self, player, players_card):
        """
        Displays the current card of a player on the GUI.

        Parameters:
            player (Player): The player whose card is being displayed.
            players_card (str): The card to be displayed.
        """

        # Check what card has player put recently
        if player.name == self.players[0].name:
            # displaying current card on the table and player's hand
            self.desk_image = self.player1_image = self.resize_cards(players_card)

            self.player1_label.config(image=self.player1_image)
            self.desk_label.config(image=self.desk_image)
        else:

            self.desk_image = self.player2_image = self.resize_cards(players_card)

            self.player2_label.config(image=self.player2_image)
            self.desk_label.config(image=self.desk_image)

    def get_players(self):
        """
        Returns a list of Player instances representing the players.

        Returns:
            list: A list containing instances of Player representing the players.
        """

        players_list = []

        player1 = Player("Andrew", None, self.deck)
        player2 = Player("Jai", None, self.deck)

        players_list.append(player1)
        players_list.append(player2)

        return players_list

    def update_game_status(self):
        """
            Updates the GUI with information about the current game state.
        """
        self.player1_frame.config(text=f'{self.players[0].name} - has {len(self.players[0].hand)} cards', bd=0)
        self.player2_frame.config(text=f'{self.players[1].name} - has {len(self.players[1].hand)} cards', bd=0)

        self.desk_frame.config(text=f'Cards on the table - {len(self.gaming_deck.display_deck())}')
        self.master.title(f"Round number - {self.round}")

    def resize_cards(self, card):
        """
        Resizes the card image for display on the GUI.

        Parameters:
            card (str): The card for which the image needs to be resized.

        Returns:
            ImageTk.PhotoImage: The resized image object.
        """
        image_path = os.path.join('PlayingCards', f'{card}.png')

        # Open the image
        our_card_img = Image.open(image_path)

        # Resize The Image
        our_card_resize_img = our_card_img.resize((180, 250))

        # Output the card
        image = ImageTk.PhotoImage(our_card_resize_img)

        return image

    def deal_cards(self):
        """
        Deals cards to the players at the start of the game.
        """
        hands = self.gaming_deck.deal(len(self.players))
        card_index = 0
        for player in self.players:
            player.hand = hands[card_index]
            card_index += 1

    def run_game(self):
        """
        Runs the Snap game GUI, entering the Tkinter main event loop.
        """
        self.master.mainloop()


gui = SnapGameGUI()
gui.run_game()
