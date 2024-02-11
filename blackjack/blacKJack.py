from art import logo 
import random
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_on=True
while game_on:
  validation=input("Sould we start the game of blackjack press'y' to start 'n'to no")
  if validation=="y":
    game_on=True
  elif validation=="n":
    game_on=False
  else:
    print("enter the valid input") 
  user_cards=random.choices(cards,k=2)
  another=True
  while another:
    sum_user_cards=sum(user_cards)
    print(f"your cards:{user_cards} and there sum is {sum_user_cards}")
    
    comp_cards=random.choices(cards,k=2)
    print(f"one computer card is {comp_cards[1]}")
    sum_comp_cards=sum(comp_cards)
    if sum_user_cards==21:
      print("you have blackjack you won")
    elif sum_comp_cards==21:
      print(f"computer final card is {comp_cards} sum={sum_comp_cards}, you lose")
      game_on=False
    if sum_user_cards>21:
      for card in user_cards:
        if card ==11:       
          card=1
        
          if sum(user_cards)>21:
            print("you lose")
            game_on=False
        else:
          print("you lose")
          game_on=False
    another_card=input("do you want to get another card write 'y' or 'n'")
    
    if another_card=="y":
      user_cards.append(random.choice(cards))
    elif another_card=="n":
      another=False
  if sum_comp_cards<17:
    comp_cards.append(random.choice(cards))
    sum_comp_cards=sum(comp_cards)
  if sum_comp_cards>21:
    print("you won")
    game_on=False
    
  if sum_comp_cards<sum_user_cards:
    print("you lose")
    game_on=False
     
  elif sum_comp_cards==sum_user_cards:
    print("draw")
    game_on=False
  else:
    print("you lose")
    game_on=False