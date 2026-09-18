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

    def test_set_max_total_value_throw_errer_when_not_integer(self):

        with self.assertRaises(ValueError) as context:
            self.hand.set_max_total_value(16)

        self.assertEqual(str(context.exception), "Error: the max_total_value has to be either 17 or 21.")
     
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

    def test_add_card_raise_error_not_card(self):

        self.hand.set_max_total_value(17)

        with self.assertRaises(ValueError) as context:
            self.hand.add_card("´Klø'r 10")

        self.assertEqual(str(context.exception), "Error: cards has to be a list of lists with an integer and a string.")

    def test_add_card_raise_error_no_max_value_set(self):

        with self.assertRaises(ValueError) as context:
            self.hand.add_card(['♣', 2])

        self.assertEqual(str(context.exception), "Error: You must set a max total value first. Use `set_max_total_value`.")

    def test_add_card_increase_value(self):

        self.hand.set_max_total_value(17)

        initial_value = self.hand.get_hand_value()

        self.hand.add_card(['♠', 7])

        new_value = self.hand.get_hand_value()

        self.assertNotEqual(initial_value, new_value)

        self.assertEqual(new_value, 7)

    def test_clear_hand(self):

        self.hand.set_max_total_value(17)

        self.hand.add_card(['♠', 7])

        self.assertEqual(self.hand.get_hand_value(), 7)

        self.hand.clear_hand()

        self.assertEqual(self.hand.get_hand_value(), 0)

    def test_clear_max_value(self):

        self.hand.set_max_total_value(17)

        self.assertEqual(self.hand.get_max_total_value(), 17)

        self.hand.clear_max_total_value()

        self.assertEqual(self.hand.get_max_total_value(), 0)

    def test_get_hand_value(self):

        self.assertIsInstance(self.hand.get_hand_value(), int)

        self.assertEqual(self.hand.get_hand_value(), 0)

    def test_get_max_total_value(self):

        self.assertIsInstance(self.hand.get_max_total_value(), int)

        self.assertEqual(self.hand.get_max_total_value(), 0)

    def test_get_cards_on_hand(self):

        self.hand.set_max_total_value(17)

        self.hand.add_card(['♠', 7])

        self.assertIsInstance(self.hand.get_cards_on_hand(), tuple)

    def test_get_cards_on_hand_when_none(self):

        self.assertEqual(self.hand.get_cards_on_hand(), None)

