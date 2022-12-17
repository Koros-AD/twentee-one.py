import random

#deck
deck =[6,7,8,9,10,6,7,8,9,10,6,7,8,9,10,6,7,8,9,10,
'jack','queen','king','ace','jack','queen','king','ace','jack','queen','king','ace','jack','queen','king','ace']
random.shuffle(deck)
playerhand=[]
dealerhand=[]


# dealing cards
def dealcard():
     card1 = random.choice(deck)
     card2 = random.choice(deck)
     playerhand.append(card1)
     dealerhand.append(card2)
     deck.remove(card1)
     deck.remove(card2)
     print(f'your current deck is {playerhand}')
     nc = (input('You want a new card?(y/n)'))
     while len(playerhand)!=5:
         if nc=='y':
             dealcard()
         elif nc=='n':
             winwin(countcard1(),countcard2())


#total cards count
def countcard1():
    count1=0
    if int in playerhand in range (2,6):
            count1+=i
    elif str in playerhand=='jack':
            count1+=2
    elif str in playerhand=='queen':
            count1+=3
    elif str in playerhand=='king':
            count1+=4
    elif str in playerhand=='ace':
            count1+=11
    return count1


def countcard2():
    count2=0
    if int in dealerhand in range (2,6):
            count2+=i
    elif str in dealerhand=='jack':
            count2+=2
    elif str in dealerhand=='queen':
            count2+=3
    elif str in dealerhand=='king':
            count2+=4
    elif str in dealerhand=='ace':
            count2+=11
    return count2

c1=countcard1()
c2=countcard2()
#who wins
def winwin(c1,c2):
   if c1()>21:
      print("You busted!Dealer wins")
   elif c2()>21:
      print("Dealer busted!You win")
   elif c1()>c2()<21:
       print(f"You win!Your score is {countcard1} against {countcard2}")
   elif c2()>c2()<21:
      print(f"You lose!Your score is {countcard1} against {countcard2}")


#intro
print("""Welcome to the game of twenty-one! Your goal is to score as many points as you can without exceeding 21. 
The first player to get more than 21 points loses. Have a nice game! Wish you luck!""")
answer= input(("Are you Ready to play? (Yes/No)" ))
if answer=="Yes"or answer=="yes" or answer=="YES" or answer=="yES" or answer=="yEs" or answer=="yeS" or answer=="y":
     print("Let's start")
     dealcard()
elif answer=="No" or answer=="no" or answer=="NO" or answer=="n":
     print("Goodbye.")







