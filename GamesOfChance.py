import random

num = random.randint(1, 10)
money = 100

def flippingCoin(bet, choice):
  coin = random.randint(1,2)
  if coin == choice:
    return bet
  return -bet

def choHan(bet, choice):
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  #Even or odd
  if dice1 + dice2 % 2 == 0:
    final = 'Even'
  else:
    final = 'Odd'

  if choice == final:
    return bet
  else:
    return -bet
    
def pickCard(bet1, bet2):
  deck = [n for n in range(1, 13) for i in range(4)]
  
  player1 = random.choice(deck)

  deck.remove(player1)

  player2 = random.choice(deck.remove(player1))
  
  if player1 > player2:
    return(f'Player 1 wins {(money+bet1)} and Player 2 looses. Total player 2 ({money+bet2})')
  
  if player2 > player1:
    return(f'Player 2 wins {(money+bet1)})and Player 1 looses. Total player 1 ({money+bet2})')
  
  if player1 == player2:
    return('There is a tie.')
  
  
def roulette(bet, choice):
    number = random.randint(0,36)

    #Even or odd
    if number % 2 == 0:
        final = 'Even'
    else:
        final = 'Odd'

    if choice == int and choice == number:
        return bet*35
    elif choice == int and choice != number:
        return -bet
    elif choice == str and  final == choice:
        return bet
    elif choice == str and final != choice:
        return -bet



#Checking

money += flippingCoin(10, "Heads")
print(money)

money += choHan(40, 'Odd')
print(money)