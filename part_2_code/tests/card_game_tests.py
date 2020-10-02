import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_game = CardGame()
        self.card = Card("hearts", 1)
        self.card_1 = Card("spades", 10)

    def test_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card))

    def test_highest_card(self):
        self.assertEqual(self.card_1, self.card_game.highest_card(self.card, self.card_1))

    def test_cards_total(self):
        cards = [self.card, self.card_1]
        self.assertEqual("You have a total of11", self.card_game.cards_total(cards))