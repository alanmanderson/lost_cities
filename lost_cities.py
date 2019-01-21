from utils import *

score = get_input()
total = 0
for color in score:
    score[color]['score'] = calculate_color_score(score[color]['hands'], score[color]['cards'])
    total += score[color]['score']
print(score)
print("Total Score: " + str(total))
