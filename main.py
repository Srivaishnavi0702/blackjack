from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_score = 0


#checking winner

def check_winner(score_1, score_2, card_1, card_2):

    """Checks the final scores of the player and
    dealer and decides win, lose, or draw."""
    if score_1 > score_2:
        print(f"Your Final Hand:{card_1}, final score: {score_1}")
        print(f"Computer's Final Hand:{card_2}, final score: {score_2}")
        print("You Win🥳")
    elif score_2 == score_1:
        print(f"Your Final Hand:{card_1}, final score: {score_1}")
        print(f"Computer's Final Hand:{card_2}, final score: {score_2}")
        print("Draw🙃")
    else:
        print(f"Your Final Hand:{card_1}, final score: {score_1}")
        print(f"Computer's Final Hand:{card_2}, final score: {score_2}")
        print("You Lose😤")

# Dealer round

def dealer_turn(dealer_first_card, total_cards, opponent_score):


    """Processes the dealer's turn according
     to standard Blackjack rules."""
    dealer_card = [dealer_first_card]
    while True:

        card_reveal = random.choice(total_cards)
        dealer_card.append(card_reveal)
        opponent_score += sum(dealer_card)
        if opponent_score != 21 and user_score == 21:
            print(f"Computer's Final Hand:{dealer_card}, final score: {opponent_score}")
            print("Win with a Blackjack!!😎")
            break
        if opponent_score == 21:
            if opponent_score == user_first_score:
                print("Both are getting BlackJack!!😎")
                print("Draw🙃")
                break
            print()
            print("😨🤯 Your Opponent getting BlackJack!!")
            print("You Lose😤")
            break
        elif opponent_score > 17 or opponent_score == 17:
            check_winner(score_1=user_score, score_2= opponent_score, card_1=user_card, card_2=dealer_card)
            break
        while True:
            card_reveal = random.choice(total_cards)
            dealer_card.append(card_reveal)
            opponent_score = sum(dealer_card)
            if opponent_score > 21:
                print(f"Your Final Hand:{user_card}, final score: {user_score}")
                print(f"Computer's Final Hand:{dealer_card}, final score: {opponent_score}")
                print("You Win😁")
                break
            elif opponent_score > 17 or opponent_score == 17:
                check_winner(score_1 = user_score, score_2 = opponent_score, card_1 = user_card, card_2 = dealer_card)
                break
            elif opponent_score < 17:
                continue
            else:
                check_winner(score_1 = user_score, score_2 = opponent_score, card_1 = user_card, card_2 = dealer_card)
                break
        break


while True:
    user_card = random.sample(cards, k=2)
    user_first_score = user_card[0] + user_card[1]
    user_score = user_first_score
    dealer = random.choice(cards)
    dealer_score = dealer
    should_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if should_play == "y":
        print("\n" * 100)
        print(logo)
        print(f"Your's Cards:{user_card}, current score:", user_first_score)
        print(f"Computer's first card: {dealer}")
        if user_first_score == 21:
            print(f"Your Final Hand:{user_card}, final score: {user_first_score}")
            user_score = user_first_score
            dealer_score = 0
            dealer_turn(dealer_first_card = dealer, total_cards = cards, opponent_score = dealer_score)
            continue
        while True:
            ask_hint_or_stand = input("Type 'y' to get another card, type 'n' to pass:").lower()
            new_card = random.choice(cards)
            if ask_hint_or_stand == "y":
                user_card.append(new_card)
                user_score += new_card
                print(f"Your's Cards:{user_card}, current score:{user_score}")
                if user_score > 21:
                    print(f"Your Final Hand:{user_card}, final score: {user_score}")
                    print(f"Computer's Final Hand:{[dealer]}, final score:{dealer_score}")
                    print("You went over. You Lose😭")
                    break
                elif user_score < 21:
                    continue
                elif user_score == 21:
                    dealer_score = 0
                    dealer_turn(dealer_first_card = dealer, total_cards = cards, opponent_score = dealer_score)
                    break
            elif ask_hint_or_stand == "n":
                dealer_score = 0
                dealer_turn(dealer_first_card = dealer, total_cards = cards, opponent_score = dealer_score)
                break
        continue
    else:
        break



