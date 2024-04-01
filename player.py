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
        self.alive = True
        self.grievous_wounds = False

    def attack(self):
        return *dice_roll(self.attack_dice), 0

    def defend(self, incoming_attack_rolls, attack_type):
        defence_rolls = dice_roll(self.defence_dice)
        offence_successes = success_count(incoming_attack_rolls)
        defence_successes = success_count(defence_rolls)
        damage = 0
        if offence_successes > (defence_successes + self.armour):  # successful attack, failed defence
            self.bleeding = True
            print(f'damage before deductions: {sum(incoming_attack_rolls)}')
            damage = max(0, sum(incoming_attack_rolls) - (self.armour))

        if attack_type == 2:
            self.grievous_wounds = True

        if self.bleeding:
            damage += 25

        if self.grievous_wounds:
            damage += 50

        self.hp -= damage

        return damage

    def healing_potion(self):
        healing_array = dice_roll(7)
        health = sum(healing_array)
        self.hp += health
        return health

    def heavy_weapon_super(self):
        return dice_roll(int(self.attack_dice * 1.5)), 1

    def light_weapon_super(self):
        return dice_roll(self.attack_dice), 2
