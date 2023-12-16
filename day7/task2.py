from puzzle_input import example_input, puzzle_input

CONFIG = 1 # 0 = example input, 1 = puzzle input
INPUT = example_input if CONFIG == 0 else puzzle_input

su = 0
cards_list, bid_list = [], []

# Parse input
for line_idx, line in enumerate(INPUT.splitlines()):
    if len(line) == 0:
        continue
    cur_cards, cur_bid = line.split(" ")
    cards_list.append(cur_cards)
    bid_list.append(int(cur_bid))

# Rank the cards
def card_height(card) -> int:
    card_values = {'A': 99, 'K': 98, 'Q': 97, 'T': 95, '9': 94, '8': 93, '7': 92, '6': 91, '5': 90, '4': 89, '3': 88, '2': 87, 'J': 86}
    combination_score = 1 # High card
    height_score = ""
    # Find combination: five of a kind, four of a kind, full house, three of a kind, two pair, one pair, high card
    # Create a dict of each card and its count
    card_count = {}
    num_of_jokers = 0
    card_without_jokers = ""
    for c in card:
        if c != "J":
            card_without_jokers += c
        else:
            num_of_jokers += 1
    for c in card_without_jokers:
        if c in card_count:
            card_count[c] += 1
        else:
            card_count[c] = 1
    card_count = sorted(card_count.values(), reverse=True)
    if not card_count:
        card_count = [0]
    # Find the combination
    if card_count[0] + num_of_jokers == 5:
        combination_score = 7
    elif card_count[0] + num_of_jokers == 4:
        combination_score = 6
    elif card_count[0] + num_of_jokers == 3 and card_count[1] == 2:
        combination_score = 5
    elif card_count[0] + num_of_jokers == 3:
        combination_score = 4
    elif card_count[0] == 2 and (num_of_jokers == 1 or card_count[1] == 2):
        combination_score = 3
    elif card_count[0] == 2 or num_of_jokers == 1:
        combination_score = 2

    # Find the height
    for c in card:
        height_score += str(card_values[c])
    height_score = int(height_score)
    return int(str(combination_score) + str(height_score))

cards_list_sorted = sorted(cards_list, key=card_height)

# Use same ordering for bid_list
bid_list_sorted = []
for idx, cards in enumerate(cards_list_sorted):
    bid_list_sorted.append(bid_list[cards_list.index(cards)])
    
# Calculate sum
for i in range(len(bid_list_sorted)):
    su += bid_list_sorted[i] * (i+1)

for idx, cards in enumerate(cards_list_sorted):
    print(cards, card_height(cards), bid_list_sorted[idx])
print("su:", su)
