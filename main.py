from text_representation import Texts
from money_coins import Coins, AniCoin
from decider import Decider
from reseter import Clear
from time import sleep


clear = Clear()
ani_c = AniCoin().coin_animate()
decider = Decider()
text = Texts()
coins = Coins()

# start of app

ani_c
sleep(1)
print(text.title())
print(coins.many_coins())

clear.cls()

cycle = True
while cycle:
    
    decision = decider.heads_or_tails()
    if decision == 1:
        print("\n \n")
        print(text.head())

    else: 
        print("\n")
        print(text.tails())

    sleep(1)

    for i in range(3):
        print(" ")

    choice = input("\nDo you want to flip a coin again?\t_ ").lower()

    if choice == "yes" or choice == "y" or choice == "yeah" or choice == "sure":
        pass
    else:
        print("The coin flipper is about to close..")
        sleep(2)
        cycle = False

