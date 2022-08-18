class Character:
    max_speed = 45
    dead_health = 0

    def __init__(self, race, health, damage, armor ):
        self.race = race
        self.health = health
        self.damage = damage
        self.armor = armor

character = Character('Terran', health=100, damage=20, armor=18)
print(Character.max_speed)
print(Character.dead_health)
print(character.race)
print(character.health)
print(character.damage)
print(character.armor)

