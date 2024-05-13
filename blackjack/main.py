import os
import random
from art import logo

# The deck is unlimited in size.
# The Jack/Queen/King all count as 10.
# The Ace can count as 1 or 11.
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def new_card():
    """Returns a random card from the deck."""

    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Returns the score calculated from the cards."""
    
    score = 0

    for card in cards:
        if card == 'A':
            score += 11
        elif card in ['J', 'Q', 'K']:
            score += 10
        else:
            score += int(card)

        if score > 21:
            if card == 'A':
                score -= 10

    if score == 21:
        if len(cards) == 2:
            score = 0 # blackjack

    return score

def compare_score(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Computer has Blackjack. You lose. 😱"
    elif user_score == 0:
        return "You have a Blackjack. You win. 😎"
    elif user_score > 21:
        return "You went over. You lose. 😭"
    elif computer_score > 21:
        return "Computer went over. You win. 😬"
    elif user_score > computer_score:
        return "You win. 🙂"
    else:
        return "You lose. 😤"

def play_game():
    print(logo)

    user_cards = []
    computer_cards = []

    user_cards.append(new_card())
    user_cards.append(new_card())

    computer_cards.append(new_card())
    computer_cards.append(new_card())

    computer_cards_2 = computer_cards.copy()
    computer_cards_2[0] = '?'

    print(f"Computer cards: {computer_cards_2}")
    print(f"Your cards: {user_cards}, your score: {calculate_score(user_cards)}")
      
    # user turn
    is_game_over = False
    while not is_game_over:
        more_cards = input("Do you want another card? Type 'y' or 'n' to pass: ")

        if more_cards == 'y':
            user_cards.append(new_card())
        else:
            is_game_over = True
        
        user_score = calculate_score(user_cards)

        print(f"Your cards: {user_cards}, your score: {user_score}")

        if user_score > 21:
            is_game_over = True

    # computer turn
    is_game_over = False
    while not is_game_over:
        computer_score = calculate_score(computer_cards)

        if computer_score == 0:
            is_game_over = True
        if computer_score < 17:
            computer_cards.append(new_card())
        else:
            is_game_over = True

    print(f"Computer cards: {computer_cards}, computer score: {computer_score}")

    print(compare_score(user_score, computer_score) + "\n")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()