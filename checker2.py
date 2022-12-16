import random
#deck
deck =[6,7,8,9,10,6,7,8,9,10,6,7,8,9,10,6,7,8,9,10,'jack','queen','king','ace','jack','queen','king','ace','jack','queen','king','ace','jack','queen','king','ace']
random.shuffle(deck)
playerhand=[]
dealerhand=[]
count1=0
count2=0


#who wins
def winwin():
   if count1>21:
      print("You busted!Dealer wins")
   elif count2>21:
      print("Dealer busted!You win")
   elif count1>count2<21:
       print(f"You win!Your score is {count1} against {count2}")
   elif count2>count2<21:
      print(f"You lose!Your score is {count1} against {count2}")


# dealing cards
def dealcard():
     card1 = random.choice(deck)
     card2 = random.choice(deck)
     playerhand.append(card1)
     dealerhand.append(card2)
     deck.remove(card1)
     deck.remove(card2)
     return (card1,card2)
def newcard():
     dealcard()
     if len(playerhand)<=5:
       print(f'Your current deck {playerhand}')
       nc=(input('You want new card?(y?/n)'))
       countcard1(card1)
       countcard2(card2)
       if nc=='y':
        dealcard()
       elif nc=='n':
        winwin()

#total cards count
def countcard1():
      if card1 in range(6,10):
            count1+=card1
      elif card1=='jack':
            count1+=2
      elif card1=='queen':
            count1+=3
      elif card1=='king':
            count1+=4
      elif card1=='ace':
            count1+=11
      return count1
countcard1()

def countcard2():
      if card2 in range(6,10):
            count2+=card2
      elif card2=='jack':
            count2+=2
      elif card2=='queen':
            count2+=3
      elif card2=='king':
            count2+=4
      elif card2=='ace':
            count2+=11
      return count2
countcard2()

#intro
print("""Welcome to the game of twenty-one! Your goal is to score as many points as you can without exceeding 21. 
The first player to get more than 21 points loses. Have a nice game! Wish you luck!""")
answer= input(("Are you Ready to play? (Yes/No)" ))
if answer=="Yes"or answer=="yes" or answer=="YES" or answer=="yES" or answer=="yEs" or answer=="yeS" or answer=="y":
     print("Let's start")
     newcard()
elif answer=="No" or answer=="no" or answer=="NO" or answer=="n":
     print("Goodbye.")

def writein():
    plr1=(input("Player 1 name:"))
    plr2=(input("Player 2 name: "))