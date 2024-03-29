from random import randint


def dice_roll(pool):
    return [randint(1, 10) for i in range(pool)]


def success_count(roll_array):
    return len([roll for roll in roll_array if roll >= 5])


class Player:
    def __init__(self, name, hp, armour, attack_dice):
        self.name = name
        self.hp = hp
        self.armour = armour
        self.attack_dice = attack_dice
        self.defence_dice = armour * 2
        self.bleeding = False

    def attack(self):
        return dice_roll(self.attack_dice)

    def defend(self, incoming_attack_rolls):
        defence_rolls = dice_roll(self.defence_dice)
        offence_successes = success_count(incoming_attack_rolls)
        defence_successes = success_count(defence_rolls)
        damage = 0
        if offence_successes > (defence_successes + self.armour):  # successful attack, failed defence
            self.bleeding = True
            print(f'damage before deductions: {sum(incoming_attack_rolls)}')
            damage = sum(incoming_attack_rolls) - (20 * self.armour)

        if self.bleeding:
            damage += 0.15 * self.hp

        self.hp -= damage

        return damage

'''
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
'''
