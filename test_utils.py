import unittest
from unittest.mock import patch
from utils import * 

class TestUtils(unittest.TestCase):
    def test_no_cards(self):
        score = calculate_color_score(0, [])
        self.assertEqual(score, 0)

    def test_three_hands_negative(self):
        score = calculate_color_score(3, [2,3])
        self.assertEqual(score, -60)

    def test_three_hands_positive(self):
        score = calculate_color_score(3, [3,8,9,10])
        self.assertEqual(score, 40)

    def test_three_hands_eight_cards(self):
        score = calculate_color_score(3, [1,2,3,8,9])
        self.assertEqual(score, 32)

    def test_get_numbers_from_string_empty(self):
        numbers = get_numbers_from_string('')
        self.assertListEqual(numbers, [])

    def test_get_numbers_from_string_without_10(self):
        numbers = get_numbers_from_string('1234')
        self.assertListEqual(numbers, [1,2,3,4])

    def test_get_numbers_from_string_with_10(self):
        numbers = get_numbers_from_string('12310')
        self.assertListEqual(numbers, [1,2,3,10])

    def test_get_numbers_from_string_out_of_order(self):
        numbers = get_numbers_from_string('110345')
        self.assertListEqual(numbers, [1,3,4,5,10])
        
    def test_get_hand_input_0(self):
        with patch('builtins.input', return_value='2'):
            hands = get_hand_input('blue')
            self.assertEqual(hands, 2)

    def test_get_number_input(self):
        with patch('builtins.input', return_value='12310'):
            cards = get_number_input()
            self.assertListEqual(cards, [1, 2, 3, 10])
 
    def test_get_number_input_empty(self):
        with patch('builtins.input', return_value=''):
            self.assertListEqual(get_number_input(), [])

    def test_get_input(self):
        with patch('utils.get_number_input', return_value=[1,2]):
            with patch('utils.get_hand_input', return_value=2):
                expects = {
                    'red': {'hands': 2, 'cards': [1,2]},
                    'green': {'hands': 2, 'cards': [1,2]},
                    'white': {'hands': 2, 'cards': [1,2]},
                    'yellow': {'hands': 2, 'cards': [1,2]},
                    'blue': {'hands': 2, 'cards': [1,2]},
                }
                self.assertDictEqual(get_input(), expects)
