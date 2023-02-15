import random

# deck
deck = ['6', '7', '8', '9', '10', '6', '7', '8', '9', '10', '6', '7', '8', '9', '10', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace', 'jack', 'queen', 'king', 'ace', 'jack', 'queen', 'king', 'ace', 'jack', 'queen', 'king', 'ace']
random.shuffle(deck)

playerhand = []
dealerhand = []

# who wins
def winwin(count1, count2):  # need to pass count1 and count2 as arguments
    if count1 > 21:
        return "You busted! Dealer wins"
    elif count2 > 21:
        return "Dealer busted! You win"
    elif count1 > count2:  # remove "<21" here
        return f"You win! Your score is {count1} against {count2}"
    elif count2 > count1:  # remove "<21" here
        return f"You lose! Your score is {count1} against {count2}"
    else:
        return "It's a tie!"  # need to handle tie case

# total cards count
def countcard(hand):
    count = 0
    for card in hand:
        if card in ['jack', 'queen', 'king']:
            count += 10
        elif card == 'ace':
            if count + 11 > 21:
                count += 1
            else:
                count += 11
        else:
            count += int(card)
    return count

# dealing cards
def dealcard():
    card1 = random.choice(deck)
    card2 = random.choice(deck)
    playerhand.extend([card1, card2])  # use extend instead of append
    dealerhand.append(card2)
    deck.remove(card1)
    deck.remove(card2)
    print(f'Your current deck: {playerhand}')

# getting new cards
def newcards():
    while len(playerhand) < 5:
        x = input('Want a new card (y/n)? ')
        if x == 'y':
            dealcard()
            count1 = countcard(playerhand)
            count2 = countcard(dealerhand)
            print(f"Your score: {count1}, Dealer's score: {count2}")
            if count1 > 21 or count2 >= 21:  # check for win condition after each new card
                result = winwin(count1, count2)
                save_to_file(playerhand, dealerhand, result)
                print(result)
                break
        elif x == 'n':
            result = winwin(countcard(playerhand), countcard(dealerhand))  # need to pass final counts to winwin()
            save_to_file(playerhand, dealerhand, result)
            print(result)
            break

# save each deck result to a file
def save_to_file(playerhand, dealerhand, result):
    with open('results.txt', 'a') as f:
        f.write(f'Player hand: {playerhand}\n')
        f.write(f'Dealer hand: {dealerhand}\n')
        f.write(f'{result}\n\n')
# intro
print("Welcome to the game of twenty-one! Your goal is to score as many points as you can without exceeding 21. The first player to get more than 21 points loses. Have a nice game! Wish you luck!")
answer = input("Are you ready to play? (Yes/No) ")
if answer.lower() == "yes":
    print("Let's start!")
    dealcard()
    newcards()
elif answer.lower() == "no":
    print("Goodbye.")
else:
    print("Invalid input. Goodbye.")







