from player import *

# test case
player1 = Player("Prime", 500, 3, 10)
player2 = Player("Secundus", 500, 3, 10)
turn = 1

# game loop:
while player1.hp > 0 and player2.hp > 0:
    print(f'Round: {turn}')
    print("{}'s turn".format(player1.name))
    attack_rolls = player1.attack()
    damage = player2.defend(attack_rolls)
    print(f"{player2.name} takes {damage} damage. {player2.hp} hp left\n")

    print("{}'s turn".format(player2.name))
    attack_rolls = player2.attack()
    damage = player1.defend(attack_rolls)
    print(f"{player1.name} takes {damage} damage. {player1.hp} hp left\n")

    turn += 1


print("Game over.")
if player1.hp <= 0:
    print(f'{player2.name} wins!!')
else:
    print(f'{player1.name} wins!!')