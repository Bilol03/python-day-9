from os import system
from art import logo
print(logo)
end_game = False
players_list = []
res = 0

while not end_game:
  name = input("What is your name? ")
  bid_price = int(input("What is your bid? $"))
  players_bid = {}
  players_bid["name"] = name
  players_bid["bid_price"] = bid_price
  players_list.append(players_bid)

  for bid in players_list:
    if res < bid["bid_price"]:
      res = bid_price
  end_game_ask = input("Are there any bidders? Type 'yes' or 'no' ")
  if end_game_ask == 'yes':
    system("clear")
  else:
    end_game = True
    for winner in players_list:
      if winner['bid_price'] == res:
        print(f'Winner is {winner["name"] } with a bid of {winner["bid_price"]}$')
  

#HINT: You can call clear() to clear the output in the console.