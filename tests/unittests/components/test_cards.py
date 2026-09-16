import unittest
from blackjack.components.cards import Cards

class TestCards(unittest.TestCase):

    def setUp(self):
        self.cards = Cards()

    def test_set_deck_creates_52_cards(self):
        """Test that set_deck initializes the deck with 52 cards.
        
        It uses get_deck() to check if the attribute was updated.
        """

        self.cards.set_deck()

        self.assertEqual(len(self.cards.get_deck()), 52)

    def test_shuffle_cards_randomizes_deck(self):
        """Test that the shuffle_cards randomizes the card deck"""

        self.cards.set_deck()

        intial_order = self.cards.get_deck()

        self.cards.shuffle_cards()

        new_order = self.cards.get_deck()

        self.assertNotEqual(intial_order, new_order)

    def test_pick_card_returns_none(self):

        self.assertFalse(self.cards.pick_card())

    def test_pick_card_removes_card_from_deck(self):

        self.cards.set_deck()

        self.cards.shuffle_cards()

        self.cards.pick_card()

        self.assertNotEqual(len(self.cards.get_deck()), 52)

    def test_pick_card_returns_card(self):

        self.cards.set_deck()

        self.cards.shuffle_cards()

        self.assertIsInstance(self.cards.pick_card(), list)

    def test_get_deck_returns_none(self):

        self.assertFalse(self.cards.get_deck())

    def test_get_deck_returns_tuple(self):

        self.cards.set_deck()

        self.cards.shuffle_cards()

        self.assertIsInstance(self.cards.get_deck(), tuple)
