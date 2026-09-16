import unittest
from src.blackjack.components.cards import Cards

class TestCards(unittest.TestCase):

    def setUp(self):
        self.cards = Cards()

    def test_set_deck_creates_52_cards(self):
        """Test that set_deck initializes the deck with 52 cards.
        
        It uses get_deck() to check if the attribute was updated.
        """

        self.cards.set_deck()

        # print(self.cards._Cards__deck.pop(1))

        self.assertEqual(len(self.cards.get_deck()), 52)

    # def test_shuffle_cards_randomizes_deck(self):
    #     """Test that the shuffle_cards randomizes the card deck"""


    #     intial_order = self.cards.get_deck()

    #     self.shuffle_cards()

    #     new_order = self.cards.get_deck()

    #     self.assertIsNot = 

