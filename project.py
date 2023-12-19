import random
from colorama import Fore, Style


class Player:
    """
    Class representing the player character in the game.

    This took me awhile to complete.
    The most rewarding lesson was actually which part of the game should go to which class (player, monster or external functions).
    Some of these are explained in each segment of the game itself.

    Attributes:
    level (int): Represents the level of the player. Starts from 1.
    gold (int): Represents the gold owned by the player. Initially 0.
    weapon_level (int): Represents the weapon level. Initially 1.
    armor_level (int): Represents the armor level. Initially 1.
    shield_level (int): Represents the shield level. Initially 1.
    battle_count (int): Represents the number of battles fought. Initially 0.
    """

    def __init__(self):
        """Player attributes."""
        self.level = 1
        self.gold = 0
        self.weapon_level = 1
        self.armor_level = 1
        self.shield_level = 1
        self.battle_count = 0

    def level_up(self):
        """
        Level up the player and reset the battle count.
        While its not shown here, every 3 battles will increase player level by 1.
        I made a choice to put that logic in monster because its a direct effect from battling while leveling is just an outcome.

        """
        self.level += 1
        color(f"Congratulations! You leveled up to level {self.level}!", Fore.GREEN)
        self.battle_count = 0

    def upgrade_equipment(self, equipment_choice):
        """
        Upgrade the player's equipment based on their choice and available gold.
        Equipment are split into 3 categories - weapon, armor and shield.
        Each equipment upgrade will get more expensive over time (20 to 60).
        Maximum level for equipment is level 5 for all equipment types.
        I know its boring and i could add more things like weapon names but its already killing me at this point.

        Args:
        equipment_choice (str): The choice of equipment to upgrade.
        """
        upgrade_costs = {
            "weapon": [20, 30, 40, 50, 60],
            "armor": [20, 30, 40, 50, 60],
            "shield": [20, 30, 40, 50, 60],
        }
        equipment_type = ["weapon", "armor", "shield"][int(equipment_choice) - 1]
        current_level = getattr(self, f"{equipment_type}_level")

        """
        A little complicated here but this just iterate the loops based on equipment level, cost of upgrade and player's current gold.
        Also why i was just not keen to do more to the equipment section.
        """
        if current_level < 5:
            upgrade_cost = upgrade_costs[equipment_type][current_level]
            if self.gold >= upgrade_cost:
                self.gold -= upgrade_cost
                upgraded_level = current_level + 1
                setattr(self, f"{equipment_type}_level", upgraded_level)
                next_upgrade_cost = upgrade_costs[equipment_type][upgraded_level]
                color(
                    f"Your {equipment_type} (Level {current_level}) has been upgraded! Gold spent: {upgrade_cost}, Remaining gold: {self.gold}",
                    Fore.GREEN,
                )
                color(
                    f"Next upgrade cost for {equipment_type}: {next_upgrade_cost} gold",
                    Fore.YELLOW,
                )
            else:
                color("Insufficient gold to upgrade equipment!", Fore.RED)
        else:
            color(f"You have reached the maximum level for {equipment_type}!", Fore.RED)

    def display_stats(self):
        """Display the player's current statistics."""
        print("\n==== Player Stats ====")
        print(f"Level: {self.level}")
        print(f"Gold: {self.gold}")
        print(f"Weapon Level: {self.weapon_level}")
        print(f"Armor Level: {self.armor_level}")
        print(f"Shield Level: {self.shield_level}")

    def increment_battle_count(self):
        """
        Increment the battle count and level up the player if necessary.
        I actually failed to make leveling work for quite awhile, until i just give up and let players assume it works randomly.
        But one day, it just corrected itself, through something i did which i was not really aware of.
        Well, a battle won nonetheless even with luck itself.
        """
        self.battle_count += 1
        if self.battle_count % 3 == 0:
            self.level_up()


class Monster:
    """
    Class representing a monster in the game.
    I initially did a class for Quest because that was the first thing i wanted to do.
    But that started a internal debate and make me realise how to organise different parts of the games.
    Like the name class suggests, it makes more sense to put class for things with attributes, like monsters.
    Honestly its really quite nice to wrap around using gaming analogies.

    Attributes:
    name (str): Name of the monster.
    level (int): Level of the monster.
    gold_reward (int): Gold rewarded to the player upon defeating the monster.
    battle_count (int): Represents the number of battles this monster has fought. Initially 0.
    """

    def __init__(self, name, level, gold_reward):
        """Initialize monster attributes."""
        self.name = name
        self.level = level
        self.gold_reward = gold_reward
        self.battle_count = 0

    def battle(self, player):
        """
        Handle the battle against a monster.
        All the self, player and monster really melted my brain.
        Its not really shown here but i kept writing the wrong term multiple times and having to correct it by trial and error throughout.
        On hindsight, i should have add player(object) and monster (object) etc early on to help myself during the revision.

        Args:
        player (Player): The player object battling the monster.
        """
        self.battle_count += 1
        if self.battle_count % 3 == 0:
            player.level_up()
        player.gold += self.gold_reward
        color(
            f"You defeated a {self.name} (Level {self.level}) and gained {self.gold_reward} gold!",
            Fore.GREEN,
        )


def main():
    """
    Main function that shows the action dashboard, and link to each of the individual functions like questing.
    Most of the non-main worthy stuff here are added towards the tail-end of the project and thus seems weird.
    Initializes the game world, monsters, player, and handles game progression.
    """
    player = Player()
    monsters = [
        Monster("Goblin", 1, 2),
        Monster("Skeleton", 1, 3),
        Monster("Zombie", 1, 4),
        Monster("Orc", 2, 5),
        Monster("Troll", 2, 5),
        Monster("Giant Spider", 3, 6),
        Monster("Werewolf", 3, 6),
        Monster("Vampire", 3, 7),
        Monster("Golem", 4, 8),
        Monster("Dragon", 5, 10),
    ]

    day_count = 1

    while True:
        print("\n" + "=" * 50)
        color(f"Day {day_count}: World of Exodium", Fore.BLUE)
        print("=" * 50)

        player.display_stats()

        print("\nChoose your action:")
        color("1. Quest", Fore.RED)
        color("2. Upgrade equipment", Fore.YELLOW)
        color("3. Gamble", Fore.GREEN)
        color("4. Exit game", Fore.CYAN)

        action_choice = input("Enter the number of the action you would like to take: ")

        if action_choice == "1":
            questing(monsters, player)
            day_count += 1
        elif action_choice == "2":
            upgrade_equipment(player)
            day_count += 1
        elif action_choice == "3":
            gamble(player)
            day_count += 1
        elif action_choice == "4":
            color("Thank you for playing!", Fore.CYAN)
            break
        else:
            color("Invalid input! Please enter a valid number.", Fore.RED)

            
def color(text, color=Fore.WHITE, style=Style.NORMAL):
    """
    Display text with the specified color and style.
    Wonderful library. I tried to not use library but honestly, this doesnt count since its just display purpose, right?

    Args:
    text (str): The text to be printed.
    color (str): The colorama.Fore color to be applied to the text.
    style (str): The colorama.Style to be applied to the text.
    """
    print(style + color + text + Style.RESET_ALL)


def questing(monsters, player):
    """
    Embark on a quest and battle a random monster.
    Again, this was the part that was originally a class and then taken out.
    This prompted me to draw out a mindmap (used in my video) to really lay the right organisation.
    Which then helped to really structure the game better.
    I think we should start with drawing a mindmap or table before doing projects in general.

    Args:
    monsters (list): A list of available Monster objects.
    player (Player): The player object embarking on a quest.
    """
    print("\n" + "=" * 50)
    color("Questing...", Fore.RED)
    print("=" * 50)

    monster = random.choice(sorted(monsters, key=lambda x: x.level))
    print(f"Oh no! You encountered a {monster.name} (Level {monster.level})!")
    monster.battle(player)
    player.increment_battle_count()
    player.display_stats()


def upgrade_equipment(player):
    """
    Upgrade the player's equipment if they have enough gold.
    Like David mentioned, Class really helped when you are building out bigger stuff.
    Once you sort out the classes, the external functions and main really become very easy to define.

    Args:
    player (Player): The player object upgrading equipment.
    """
    print("\n" + "=" * 50)
    color("Equipment Upgrade", Fore.YELLOW)
    print("=" * 50)

    equipment_choice = input(
        "Enter the number of the equipment (1. Weapon, 2. Armor, 3. Shield): "
    )
    player.upgrade_equipment(equipment_choice)


def gamble(player):
    """
    Simulate gambling and update the player's gold.
    I know the game is unfair because its 60% chance of losing.
    But its gambling, and its not good for us right.

    Args:
    player (Player): The player object gambling.
    """
    print("\n" + "=" * 50)
    color("Gambling", Fore.GREEN)
    print("=" * 50)

    # 60% chance of losing
    if random.random() < 0.6:
        lose_amount = random.randint(1, 10)
        player.gold -= lose_amount
        color(
            f"Oh no! You lost {lose_amount} gold in gambling! Remaining gold: {player.gold}",
            Fore.RED,
        )
    else:
        win_amount = random.randint(1, 30)
        player.gold += win_amount
        color(
            f"Congratulations! You won {win_amount} gold in gambling! Total gold: {player.gold}",
            Fore.GREEN,
        )

    player.display_stats()


if __name__ == "__main__":
    main()
