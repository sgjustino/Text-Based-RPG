import pytest
import random
from project import Player, Monster, gamble, color
from colorama import Fore, Style

"""
i realised it was quite hard to test my file.
All i did was checking if printing works in developing the project.
However, it does help to reiterate the logics and check through the file.
1 error that pops up is that gambling can bring you to negative gold.
While i considered making the player restart the game, i thought that this should be lenient enough to make players go in 'debt'.
I supposed its a loophole that is well intended for a friendly game that doesnt force quit a new player who is a serious gambling fanatic.
"""


def test_color(capsys):
    test_text = "This is a test text"
    test_color = Fore.GREEN
    test_style = Style.BRIGHT
    color(test_text, test_color, test_style)
    captured = capsys.readouterr()
    assert captured.out == f"{test_style}{test_color}{test_text}{Style.RESET_ALL}\n" #check color is correct


def test_questing():
    monster = Monster(name="Goblin", level=1, gold_reward=2)
    assert monster.name == "Goblin"
    assert monster.level == 1
    assert monster.gold_reward == 2
    assert monster.battle_count == 0


def test_upgrade_equipment():
    player = Player()
    player.gold = 100

    initial_weapon_level = player.weapon_level
    player.upgrade_equipment("1")  # Upgrade weapon
    assert player.weapon_level == initial_weapon_level + 1
    assert player.gold == 70  # Check if gold is deducted

random.seed(0)

def test_gamble():
    player = Player()
    initial_gold = player.gold

    # Call the gamble function
    gamble(player)

    # Assert that the gold has been correctly updated
    assert player.gold != initial_gold, "Gold should be updated after gambling."