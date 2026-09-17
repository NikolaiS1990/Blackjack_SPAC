import unittest
from blackjack.components.pool import Pool

class TestPool(unittest.TestCase):

    def setUp(self):
        self.pool = Pool()

    def test_amount_manager_loose(self):
        """Test that amount decreases when win=False."""

        initial_amount = self.pool.get_amount()

        self.pool.amount_manager(20, False)

        new_ammount = self.pool.get_amount()

        self.assertNotEqual(initial_amount, new_ammount)
        self.assertEqual(new_ammount, 180)

    def test_amount_manager_win(self):
        """Test that amount decreases when win=False."""

        initial_amount = self.pool.get_amount()

        self.pool.amount_manager(20, True)

        new_ammount = self.pool.get_amount()

        self.assertNotEqual(initial_amount, new_ammount)
        self.assertEqual(new_ammount, 220)

    def test_get_amount(self):

        self.assertEqual(self.pool.get_amount(), 200)







