def calculate_color_score(hand_count, numbers=[]):
    if hand_count == 0 and len(numbers) == 0: return 0
    multiplier = hand_count + 1
    score = -20 + sum(numbers)
    score *= multiplier
    if hand_count + len(numbers) >= 8:
        score += 20
    return score

def get_numbers_from_string(text):
    numbers = []
    tens = 0
    if text.find('10') >= 0:  
        tens = 10
        text = text.replace('10', '')
    numbers = list(text)
    numbers = list(map(int, numbers))
    if tens > 0:
        numbers.append(10)
    return numbers

def get_hand_input(color):
    hands = -1
    while hands < 0 or hands > 3:
        hands = int(input("How many {0} hands do you have?".format(color)))
    return hands

def get_number_input():
    cards = input("Enter which card you have without spaces or commas. Hit enter for none:")
    return get_numbers_from_string(cards)

def get_input():
    colors = ['red', 'green', 'white', 'yellow', 'blue']
    score = {}
    for color in colors:
        hands = get_hand_input(color)
        cards = get_number_input()
        score[color] = {'hands': hands, 'cards': cards}
    return score

