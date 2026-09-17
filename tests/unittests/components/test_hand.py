import unittest
from blackjack.components.hand import Hand

class TestHand(unittest.TestCase):

    def setUp(self):
        self.hand = Hand()

    def test_set_max_total_value(self):

        initial_max_total_value = self.hand.get_max_total_value()

        self.hand.set_max_total_value(17)

        new_max_total_value = self.hand.get_max_total_value()

        self.assertNotEqual(initial_max_total_value, new_max_total_value)

        self.assertEqual(new_max_total_value, 17)

    def test_set_max_total_value_throw_errer_when_not_integer(self):

        with self.assertRaises(ValueError) as context:
            self.hand.set_max_total_value("not an integer")

        self.assertEqual(str(context.exception), "Error: max_total_value has to be an integer.")

    def test_add_card(self):

        self.hand.set_max_total_value(17)

        initial_hand = self.hand.get_cards_on_hand()

        self.hand.add_card(['♣', 2])

        new_hand = self.hand.get_cards_on_hand()

        self.assertNotEqual(initial_hand, new_hand)

        self.assertEqual(new_hand, ('♣', 2))

        self.hand.add_card(['♠', 7])

        updated_hand_with_two_cards = self.hand.get_cards_on_hand()

        self.assertEqual(updated_hand_with_two_cards, (['♣', 2], ['♠', 7]))



