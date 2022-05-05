from ast import Break
from dataclasses import dataclass
from os import remove
from pickle import TRUE
import random
import time
from tkinter.messagebox import RETRY
from copy import *
from unittest.mock import NonCallableMagicMock

@dataclass
class Card:
    super_type: str
    card_name: str
    attribute: str
    monster_type: str
    sub_type: str
    level: int
    attack: int
    defense: int
    has_effect: bool
    card_text: str

@dataclass
class Deck:
    player_deck: list

@dataclass
class Hand: 
    player_hand: list

@dataclass
class SetCard:
    label: str
    card: Card


## Global Variables
# Cards
tri_horned_dragon = Card("Monster", "Tri-Horned Dragon", "Dark", "Dragon", "Normal", 8, 2850, 2350, False, "")
blue_eyes_white_dragon = Card("Monster", "Blue-Eyes White Dragon", "Light", "Dragon", "Normal", 8, 3000, 2500, False, "")
hitotsu_me_giant = Card("Monster", "Hitotsu-Me Giant", "Earth", "Beast-Warrior", "Normal", 4, 1200, 1000, False, "")
flame_swordsman = Card("Monster", "Flame Swordsman", "Fire", "Warrior", "Fusion", 5, 1800, 1600, False, "")
skull_servant = Card("Monster", "Skull Servant", "Dark", "Zombie", "Normal", 1, 300, 200, False, "")
dark_magician = Card("Monster", "Dark Magician", "Dark", "Spellcaster", "Normal", 7, 2500, 2100, False, "")
gaia_the_fierce_knight = Card("Monster", "Gaia the Fierce Knight", "Earth", "Warrior", 7, "Normal", 2300, 2100, False, "")
celtic_guardian = Card("Monster", "Celtic Guardian", "Earth", "Warrior", "Normal", 4, 1400, 1200, False, "")
basic_insect = Card("Monster", "Basic Insect", "Earth", "Insect", "Normal", 2, 500, 700, False, "")
mammoth_graveyard = Card("Monster", "Mammoth Graveyard", "Earth", "Dinosaur", "Normal", 3, 1200, 800, False, "")
silver_fang = Card("Monster", "Silver Fang", "Earth", "Beast", "Normal", 3, 1200, 800, False, "")
dark_gray = Card("Monster", "Dark Gray", "Earth", "Beast", "Normal", 3, 800, 900, False, "")
trial_of_nightmare = Card("Monster", "Trial of Nightmare", "Dark", "Fiend", "Normal", 4, 1300, 900, False, "")
nemuriko = Card("Monster", "Nemuriko", "Dark", "Spellcaster", "Normal", 3, 800, 700, False, "")
the_13th_grave = Card("Monster", "The 13th Grave", "Dark", "Zombie", "Normal", 3, 1200, 900, False, "")
charubin_the_fire_knight = Card("Monster", "Charubin the Fire Knight", "Fire", "Pyro", "Fusion", 3, 1100, 800, False, "")
flame_manipulator = Card("Monster", "Flame Manipulator", "Fire", "Spellcaster", "Normal", 3, 900, 1000, False, "")
monster_egg = Card("Monster", "Monster Egg", "Earth", "Warrior", "Normal", 3, 600, 900, False, "")
firegrass = Card("Monster", "Firegrass", "Earth", "Plant", "Normal", 2, 700, 600, False, "")
darkfire_dragon = Card("Monster", "Darkfire Dragon", "Dark", "Dragon", "Fusion", 4, 1500, 1250, False, "")
dark_king_of_the_abyss = Card("Monster", "Dark King of the Abyss", "Dark", "Fiend", "Normal", 3, 1200, 800, False, "")
fiend_reflection_2 = Card("Monster", "Fiend Reflection #2", "Light", "Winged Beast", "Normal", 4, 1100, 1400, False, "")
fusionist = Card("Monster", "Fusionist", "Earth", "Beast", "Fusion", 3, 900, 700, False, "")
turtle_tiger = Card("Monster", "Turtle Tiger", "Water", "Aqua", "Normal", 4, 1000, 1500, False, "")
petit_dragon = Card("Monster", "Petit Dragon", "Wind", "Dragon", "Normal", 2, 600, 700, False, "")
petit_angel = Card("Monster", "Petit Angel", "Light", "Fairy", "Normal", 3, 600, 900, False, "")
hinotama_soul = Card("Monster", "Hinotama Soul", "Fire", "Pyro", "Normal", 2, 600, 500, False, "")
aqua_madoor = Card("Monster", "Aqua Madoor", "Water", "Spellcaster", "Normal", 4, 1200, 2000, False, "")
kagemusha_of_the_blue_flame = Card("Monster", "Kagemusha of the Blue Flame", "Earth", "Warrior", "Normal", 2, 800, 400, False, "")
flame_ghost = Card("Monster", "Flame Ghost", "Dark", "Zombie", "Fusion", 3, 1000, 800, False, "")
two_mouth_darkruler = Card("Monster", "Two-Mouth Darkruler", "Earth", "Dinosaur", "Normal", 3, 900, 700, False, "")
dissolverock = Card("Monster", "Dissolverock", "Earth", "Rock", "Normal", 3, 900, 1000, False, "")
root_water = Card("Monster", "Root Water", "Water", "Fish", "Normal", 3, 900, 800, False, "")
the_furious_sea_king = Card("Monster", "The Furious Sea King", "Water", "Aqua", "Normal", 3, 800, 700, False, "")
green_phantom_king = Card("Monster", "Green Phantom King", "Earth", "Plant", "Normal", 3, 500, 1600, False, "")
ray_and_temperature = Card("Monster", "Ray & Temperature", "Light", "Fairy", "Normal", 3, 1000, 1000, False, "")
king_fog = Card("Monster", "King Fog", "Dark", "Fiend", "Normal", 3, 1000, 900, False, "")
mystical_sheep_2 = Card("Monster", "Mystical Sheep #2", "Earth", "Beast", "Normal", 3, 800, 1000, False, "")
masaki_the_legendary_swordsman = Card("Monster", "Masaki the Legendary Swordsman", "Earth", "Warrior", "Normal", 4, 1100, 1100, False, "")
kurama = Card("Monster", "Kurama", "Wind", "Winged Beast", "Normal", 3, 800, 800, False, "")

legendary_sword = Card("Spell", "Legendary Sword", None, None, "Equip", None, None, None, True, "Equip only to a Warrior monster. It gains 300 ATK/DEF.")
beast_fangs = Card("Spell", "Beast Fangs", None, None, "Equip", None, None, None, True, "A Beast-Type monster equipped with this card increases its ATK and DEF by 300 points.")
violet_crystal = Card("Spell", "Violet Crystal", None, None, "Equip", None, None, None, True, "Equip only to a Zombie monster. It gains 300 ATK/DEF.")
book_of_secret_arts = Card("Spell", "Book of Secret Arts", None, None, "Equip", None, None, None, True, "A Spellcaster-Type monster equipped with this card increases its ATK and DEF by 300 points.")
power_of_kaishin = Card("Spell", "Power of Kaishin", None, None, "Equip", None, None, None, True, "Equip only to an Aqua monster. It gains 300 ATK/DEF.")

dragon_capture_jar = Card("Trap", "Dragon Capture Jar", None, None, "Continuous", None, None, None, True, "Change all face-up Dragon-Type monsters of the field to Defense Position, also they cannot change their battle positions.")

forest = Card("Spell", "Forest", None, None, "Field", None, None, None, True, "All Insect, Beast, Plant, and Beast-Warrior monsters of the field gain 200 ATK/DEF.")
wasteland = Card("Spell", "Wasteland", None, None, "Field", None, None, None, True, "All Dinosaur, Zombie, and Rock monsters on the field gain 200 ATK/DEF.")
mountain = Card("Spell", "Mountain", None, None, "Field", None, None, None, True, "All Dragon, Winged Beast, and Thunder monsters on the field gain 200 ATK/DEF.")
sogen = Card("Spell", "Sogen", None, None, "Field", None, None, None, True, "All Warrior and Beast-Warrior monsters of the field gain 200 ATK/DEF.")
umi = Card("Spell", "Umi", None, None, "Field", None, None, None, True, "All Fish, Sea Serpent, Thunder, and Aqua monsters on the field gain 200 ATK/DEF, also all Machine and Pyro monsters on the field lose 200 ATK/DEF.")
yami = Card("Spell", "Yami", None, None, "Field", None, None, None, True, "All Fiend and Spellcaster monsters on the field gain 200 ATK/DEF, also all Fairy monsters of the field lose 200 ATK/DEF.")

dark_hole = Card("Spell", "Dark Hole", None, None, "Normal", None, None, None, True, "Destroy all monsters on the field.")
raigeki = Card("Spell", "Raigeki", None, None, "Normal", None, None, None, True, "Destroy all monsters your opponent controls.")
red_medicine = Card("Spell", "Red Medicine", None, None, "Normal", None, None, None, True, "Increase your Life Points by 500 points.")
sparks = Card("Spell", "Sparks", None, None, "Normal", None, None, None, True, "Inflict 200 points of damage to your opponent's Life Points.")
hinotama = Card("Spell", "Hinotama", None, None, "Normal", None, None, None, True, "Inflict 500 damage to your opponent.")
fissure = Card("Spell", "Fissure", None, None, "Normal", None, None, None, True, "Destroy the 1 face-up monster your opponent controls that has the lowest ATK (your choice, if tied).")

trap_hole = Card("Trap", "Trap Hole", None, None, "Normal", None, None, None, True, "When your opponent Normal or Flip Summons 1 monster with 1000 or more ATK: Target that monster; destroy that target.")

polymerization = Card("Spell", "Polymerization", None, None, "Normal", None, None, None, True, "Fusion Summon 1 Fusion Monster from your Extra Deck, using monsters from your hand or field as Fusion Material.")
remove_trap = Card("Spell", "Remove Trap", None, None, "Normal", None, None, None, True, "Select 1 face-up Trap Card on the field and destroy it.")

two_pronged_attack = Card("Trap", "Two-Pronged Attack", None, None, "Normal", None, None, None, True, "Select and destroy 2 of your monsters and 1 of your opponent's monsters.")

mystical_elf = Card("Monster", "Mystical Elf", "Light", "Spellcaster", "Normal", 4, 800, 2000, False, "")
tyhone = Card("Monster", "Tyhone", "Wind", "Winged Beast", "Normal", 4, 1200, 1400, False, "")
beaver_warrior = Card("Monster", "Beaver Warrior", "Earth", "Beast-Warrior", "Normal", 4, 1200, 1500, False, "")

gravedigger_ghoul = Card("Spell", "Gravedigger Ghoul", None, None, "Normal", None, None, None, True, "Select up to 2 Monster Card(s) from your opponent's Graveyard. Remove the selected card(s) from play.")

curse_of_dragon = Card("Monster", "Curse of Dragon", "Dark", "Dragon", "Normal", 5, 2000, 1500, False, "")
karbonala_warrior = Card("Monster", "Karbonala Warrior", "Earth", "Warrior", "Fusion", 4, 1500, 1200, False, "")
giant_soldier_of_stone = Card("Monster", "Giant Soldier of Stone", "Earth", "Rock", "Normal", 3, 1300, 2000, False, "")
uraby = Card("Monster", "Uraby", "Earth", "Dinosaur", "Normal", 4, 1500, 800, False, "")
red_eyes_black_dragon = Card("Monster", "Red-Eyes Black Dragon", "Dark", "Dragon", "Normal", 7, 2400, 2000, False, "")
reaper_of_the_cards = Card("Monster", "Reaper of the Cards", "Dark", "Fiend", "Flip", 5, 1380, 1930, True, "FLIP: Select 1 Trap Card on the field and destroy it. If the selected card is Set, pick up and see the card. If it is a Trap Card, it is destroyed. If it is a Spell Card, return it to its original position.")
witty_phantom = Card("Monster", "Witty Phantom", "Dark", "Fiend", "Normal", 4, 1400, 1300, False, "")
larvas = Card("Monster", "Larvas", "Earth", "Beast", "Normal", 3, 800, 1000, False, "")
hard_armor = Card("Monster", "Hard Armor", "Earth", "Warrior", "Normal", 3, 300, 1200, False, "")
man_eater = Card("Monster", "Man Eater", "Earth", "Plant", "Normal", 2, 800, 600, False, "")
m_warrior_1 = Card("Monster", "M-Warrior #1", "Earth", "Warrior", "Normal", 3, 1000, 500, False, "")
m_warrior_2 = Card("Monster", "M-Warrior #2", "Earth", "Warrior", "Normal", 3, 500, 1000, False, "")
spirit_of_the_harp = Card("Monster", "Spirit of the Harp", "Light", "Fairy", "Normal", 4, 800, 2000, False, "")
armaill = Card("Monster", "Armaill", "Earth", "Warrior", "Normal", 3, 700, 1300, False, "")
terra_the_terrible = Card("Monster", "Terra the Terrible", "Dark", "Fiend", "Normal", 4, 1200, 1300, False, "")
frenzied_panda = Card("Monster", "Frenzied Panda", "Earth", "Beast", "Normal", 4, 1200, 1000, False, "")
kumootoko = Card("Monster", "Kumootoko", "Earth", "Insect", "Normal", 3, 700, 1400, False, "")
meda_bat = Card("Monster", "Meda Bat", "Dark", "Fiend", "Normal", 2, 800, 400, False, "")
enchanting_mermaid = Card("Monster", "Enchanting Mermaid", "Water", "Fish", "Normal", 3, 1200, 900, False, "")
fireyarou = Card("Monster", "Fireyarou", "Fire", "Pyro", "Normal", 4, 1300, 1000, False, "")
dragoness_the_wicked_knight = Card("Monster", "Dragoness the Wicked Knight", "Wind", "Warrior", "Fusion", 3, 1200, 900, False, "")
one_eyed_shield_dragon = Card("Monster", "One-Eyed Shield Dragon", "Wind", "Dragon", "Normal", 3, 700, 1300, False, "")

dark_energy = Card("Spell", "Dark Energy", None, None, "Equip", None, None, None, True, "Increase the ATK and DEF of a Fiend-Type monster equipped with this card by 300 points.")
laser_cannon_armor = Card("Spell", "Laser Cannon Armor", None, None, "Equip", None, None, None, True, "Equip only to an Insect monster. It gains 300 ATK/DEF.")
vile_germs = Card("Spell", "Vile Germs", None, None, "Equip", None, None, None, True, "A Plant-Type monster equipped with this card increases its ATK and DEF by 300 points.")
silver_bow_and_arrow = Card("Spell", "Silver Bow and Arrow", None, None, "Equip", None, None, None, True, "A Fairy-Type monster equipped with this card increases its ATK and DEF by 300 points.")
dragon_treasure = Card("Spell", "Dragon Treasure", None, None, "Equip", None, None, None, True, "A Dragon-Type monster equipped with this card increases its ATK and DEF by 300 points.")
electro_whip = Card("Spell", "Electro-Whip", None, None, "Equip", None, None, None, True, "Increase the ATK and DEF of a Thunder-Type monster equipped with this card by 300 points.")
mystical_moon = Card("Spell", "Mystical Moon", None, None, "Equip", None, None, None, True, "Equip only to a Beast-Warrior-Type monster. It gains 300 ATK and DEF.")

stop_defense = Card("Spell", "Stop Defense", None, None, "Normal", None, None, None, True, "Select 1 Defense Position monster on your opponent's side of the field and change it to Attack Position.")

machine_conversion_factory = Card("Spell", "Machine Conversion Factory", None, None, "Equip", None, None, None, True, "Equip only to a Machine monster. It gains 300 ATK/DEF.")
raise_body_heat = Card("Spell", "Raise Body Heat", None, None, "Equip", None, None, None, True, "Equip only to a Dinosaur monster. It gains 300 ATK/DEF.")
follow_wind = Card("Spell", "Follow Wind", None, None, "Equip", None, None, None, True, "Increase the ATK and DEF of a Winged Beast-Type monster equipped with this card by 300 points.")

goblins_secret_remedy = Card("Spell", "Goblin's Secret Remedy", None, None, "Normal", None, None, None, True, "Increase your Life Points by 600 points.")
final_flame = Card("Spell", "Final Flame", None, None, "Normal", None, None, None, True, "Inflict 600 points of damage to your opponent's Life Points.")
swords_of_revealing_light = Card("Spell", "Swords of Revealing Light", None, None, "Normal", None, None, None, True, "After this card's activation, it remains on the field, but you must destroy it during the End Phase of your opponent's 3rd turn. When this card is activated: If your opponent controls a face-down monster, flip all monster they control face-up. While this card is face-up on the field, your opponent's monsters cannot declare an attack.")

metal_dragon = Card("Monster", "Metal Dragon", "Wind", "Machine", "Fusion", 6, 1850, 1700, False, "")
spike_seadra = Card("Monster", "Spike Seadra", "Water", "Sea Serpent", "Normal", 5, 1600, 1300, False, "")
tripwire_beast = Card("Monster", "Tripwire Beast", "Earth", "Thunder", "Normal", 4, 1200, 1300, False, "")
skull_red_bird = Card("Monster", "Skull Red Bird", "Wind", "Winged Beast", "Normal", 4, 1550, 1200, False, "")
armed_ninja = Card("Monster", "Armed Ninja", "Earth", "Warrior", "Flip", 1, 300, 300, True, "FLIP: Target 1 Spell Card on the field; destroy that target. (If the card is Set, reveal it, and destroy it if it is a Spell Card. Otherwise, return it to its original position.")
flower_wolf = Card("Monster", "Flower Wolf", "Earth", "Beast", "Fusion", 5, 1800, 1400, False, "")
man_eater_bug = Card("Monster", "Man-Eater Bug", "Earth", "Insect", "Flip", 2, 450, 600, True, "FLIP: Target 1 monster of the field; destroy it.")
sand_stone = Card("Monster", "Sand Stone", "Earth", "Rock", "Normal", 5, 1300, 1600, False, "")
hane_hane = Card("Monster", "Hane-Hane", "Earth", "Beast", "Flip", 2, 450, 500, True, "FLIP: Select 1 monster on the field and return it to its owner's hand.")
misairuzame = Card("Monster", "Misairuzame", "Water", "Fish", "Normal", 5, 1400, 1600, False, "")
steel_ogre_grotto_1 = Card("Monster", "Steel Ogre Grotto #1", "Earth", "Machine", "Normal", 5, 1400, 1800, False, "")
lesser_dragon = Card("Monster", "Lesser Dragon", "Wind", "Dragon", "Normal", 4, 1200, 1000, False, "")
darkworld_thorns = Card("Monster", "Darkworld Thorns", "Earth", "Plant", "Normal", 3, 1200, 900, False, "")
drooling_lizard = Card("Monster", "Drooling Lizard", "Earth", "Reptile", "Normal", 3, 900, 800, False, "")
armored_starfish = Card("Monster", "Armored Starfish", "Water", "Aqua", "Normal", 4, 850, 1400, False, "")
succubus_knight = Card("Monster", "Succubus Knight", "Dark", "Warrior", "Normal", 5, 1650, 1300, False, "")

monster_reborn = Card("Spell", "Monster Reborn", None, None, "Normal", None, None, None, True, "Target 1 monster in either Graveyard; Special Summon it.")
pot_of_greed = Card("Spell", "Pot of Greed", None, None, "Normal", None, None, None, True, "Draw 2 cards.")

right_leg_exodia = Card("Monster", "Right Leg of the Forbidden One", "Dark", "Spellcaster", "Normal", 1, 200, 300, False, "")
left_leg_exodia = Card("Monster", "Left Leg of the Forbidden One", "Dark", "Spellcaster", "Normal", 1, 200, 300, False, "")
right_arm_exodia = Card("Monster", "Right Arm of the Forbidden One", "Dark", "Spellcaster", "Normal", 1, 200, 300, False, "")
left_arm_exodia = Card("Monster", "Left Arm of the Forbidden One", "Dark", "Spellcaster", "Normal", 1, 200, 300, False, "")
exodia_the_forbidden_one = Card("Monster", "Exodia the Forbidden One", "Dark", "Spellcaster", "Effect", 3, 1000, 1000, True, "If you have 'Right Leg of the Forbidden One', 'Left Leg of the Forbidden One', 'Right Arm of the Forbidden One' and 'Left Arm of the Forbidden One' in addition to this card in your hand, you win the Duel.")

gaia_the_dragon_champion = Card("Monster", "Gaia the Dragon Champion", "Wind", "Dragon", "Fusion", 7, 2600, 2100, False, "")


cards_list = [tri_horned_dragon, blue_eyes_white_dragon, hitotsu_me_giant, flame_swordsman, skull_servant, dark_magician, 
gaia_the_fierce_knight, celtic_guardian, basic_insect, mammoth_graveyard, silver_fang, dark_gray, trial_of_nightmare, nemuriko,
the_13th_grave, charubin_the_fire_knight, flame_manipulator, monster_egg, firegrass, darkfire_dragon, dark_king_of_the_abyss,
fiend_reflection_2, fusionist, turtle_tiger, petit_dragon, petit_angel, hinotama_soul, aqua_madoor, kagemusha_of_the_blue_flame, 
flame_ghost, two_mouth_darkruler, dissolverock, root_water, the_furious_sea_king, green_phantom_king, ray_and_temperature, king_fog,
mystical_sheep_2, masaki_the_legendary_swordsman, kurama, legendary_sword, beast_fangs, violet_crystal, book_of_secret_arts, 
power_of_kaishin, dragon_capture_jar, forest, wasteland, mountain, sogen, umi, yami, dark_hole, raigeki, red_medicine, sparks, 
hinotama, fissure, trap_hole, polymerization, remove_trap, two_pronged_attack, mystical_elf, tyhone, beaver_warrior, 
gravedigger_ghoul, curse_of_dragon, karbonala_warrior, giant_soldier_of_stone, uraby, red_eyes_black_dragon, reaper_of_the_cards, 
witty_phantom, larvas, hard_armor, man_eater, m_warrior_1, m_warrior_2, spirit_of_the_harp, armaill, terra_the_terrible, 
frenzied_panda, kumootoko, meda_bat, enchanting_mermaid, fireyarou, dragoness_the_wicked_knight, one_eyed_shield_dragon, 
dark_energy, laser_cannon_armor, vile_germs, silver_bow_and_arrow, dragon_treasure, electro_whip, mystical_moon, stop_defense, 
machine_conversion_factory, raise_body_heat, follow_wind, goblins_secret_remedy, final_flame, swords_of_revealing_light, 
metal_dragon, spike_seadra, tripwire_beast, skull_red_bird, armed_ninja, flower_wolf, man_eater_bug, sand_stone, hane_hane, 
misairuzame, steel_ogre_grotto_1, lesser_dragon, darkworld_thorns, drooling_lizard, armored_starfish, succubus_knight, 
monster_reborn, pot_of_greed, right_leg_exodia, left_leg_exodia, right_arm_exodia, left_arm_exodia, exodia_the_forbidden_one, 
gaia_the_dragon_champion]

# Player Variables
player1_deck = Deck([forest, hitotsu_me_giant, silver_fang, spike_seadra, tri_horned_dragon, gaia_the_fierce_knight])
player2_deck = Deck([sogen, lesser_dragon, dragon_treasure, tri_horned_dragon, gaia_the_fierce_knight, celtic_guardian])

player1_hand = Hand([])
player2_hand = Hand([])

player1_extra = [flame_swordsman]
player2_extra = [None for _ in range(15)]

player1_grave = []
player2_grave = []

player1_banished = []
player2_banished = []

player1_monster_zones = [None for _ in range(3)]
player1_st_zones = [None for _ in range(3)]

player2_monster_zones = [None for _ in range(3)]
player2_st_zones = [None for _ in range(3)]

p1_field_zone = [None]
p2_field_zone = [None]

p1_field_set = SetCard("Set Card", None)
p2_field_set = SetCard("Set Card", None)

p1_just_activated_field = True
p2_just_activated_field = True

p1_monster1= None
p1_monster2= None
p1_monster3= None

p1_set1 = SetCard("Set Card", None)
p1_set2 = SetCard("Set Card", None)
p1_set3 = SetCard("Set Card", None)

p1_st_set1 = SetCard("Set Card", None)
p1_st_set2 = SetCard("Set Card", None)
p1_st_set3 = SetCard("Set Card", None)

p1_just_set1 = False
p1_just_set2 = False
p1_just_set3 = False

p1_st_just_set1 = False
p1_st_just_set2 = False
p1_st_just_set3 = False

p2_monster1= None
p2_monster2= None
p2_monster3= None

p2_set1 = SetCard("Set Card", None)
p2_set2 = SetCard("Set Card", None)
p2_set3 = SetCard("Set Card", None)

p2_st_set1 = SetCard("Set Card", None)
p2_st_set2 = SetCard("Set Card", None)
p2_st_set3 = SetCard("Set Card", None)

p2_just_set1 = False
p2_just_set2 = False
p2_just_set3 = False

p2_st_just_set1 = False
p2_st_just_set2 = False
p2_st_just_set3 = False

player1_lp = 4000
player2_lp = 4000

player1_deckout = False
player2_deckout = False

has_summoned = False
p1_just_summoned_zone1 = False
p1_just_summoned_zone2 = False
p1_just_summoned_zone3 = False
p2_just_summoned_zone1 = False
p2_just_summoned_zone2 = False
p2_just_summoned_zone3 = False
p1_has_attacked_zone1 = False
p1_has_attacked_zone2 = False
p1_has_attacked_zone3 = False
p2_has_attacked_zone1 = False
p2_has_attacked_zone2 = False
p2_has_attacked_zone3 = False

curr_player = 1
curr_phase = "dp"
turn_counter = 1

p1_swords_counter1 = 0
p1_swords_counter2 = 0
p1_swords_counter3 = 0

p2_swords_counter1 = 0
p2_swords_counter2 = 0
p2_swords_counter3 = 0

p1_pair_monster_equip1 = None
p1_pair_monster_equip2 = None
p1_pair_monster_equip3 = None

p2_pair_monster_equip1 = None
p2_pair_monster_equip2 = None
p2_pair_monster_equip3 = None


## Functions

# Draw top card of deck and add it to the hand
def draw_card(deck, hand):
    global player1_deckout, player2_deckout

    if len(deck.player_deck) >= 1:
        print(deck.player_deck[0].card_name + " has been added to the hand.")
        hand.player_hand.append(deck.player_deck[0])
        deck.player_deck.pop(0)
    else:
        print("Player " + str(curr_player) + " lost by deckout.")
        if curr_player == 1:
            player1_deckout = True
        elif curr_player == 2:
            player2_deckout = True

# View hand of current player
def view_hand(hand):
    curr_hand = []
    if len(hand) == 0:
        print(hand)
    else:
        for card in hand:
            curr_hand.append(card.card_name)
        print("Current Hand: ", curr_hand)

# View current field. The current player's field will show up on the bottom, the opponent on the top.
def view_field(player):
    if player == 1:
        print(player2_st_zones)
        print(player2_monster_zones)
        print(player1_monster_zones)
        print(player1_st_zones)
    elif player == 2:
        print(player1_st_zones)
        print(player1_monster_zones)
        print(player2_monster_zones)
        print(player2_st_zones)

# View graveyard of current player
def view_grave(player):
    if player == 1:
        if len(player1_grave) > 0:
            for i in player1_grave:
                print(i)
        else:
            print(player1_grave)
    elif player == 2:
        if len(player2_grave) > 0:
            for i in player2_grave:
                print(i)
        else:
            print(player2_grave)

# Prints the turn player's Extra Deck.
def view_extra(player):
    extra = []
    if player == 1:
        if len(player1_extra) == 0:
            print(player1_extra)
        else:
            for i in player1_extra:
                extra.append(i.card_name)
            print(extra)

    elif player == 2:
        if len(player2_extra) == 0:
            print(player2_extra)
        else:
            for i in player2_extra:
                extra.append(i.card_name)
            print(extra)
            
# Prints the stats of a given card (Name, Attribute, Type, Level, Attack, Defense, Text)
def card_stats(card):
    for i in cards_list:
        if card == i.card_name:
            print(i)

# Get the Card object associated with a card's name.
def get_card(name):
    for i in cards_list:
        if name == i.card_name:
            return i
    return None

# Prints out a list of possible actions, with a description of what each does.
def list_actions():
    print()
    print("summon: Used to Normal Summon/Set a monster from your hand. Monsters with a Level > 5 require 1 or 2 Tributes.")
    print("set: Used to Set a Spell or Trap card from your hand to the chosen Spell/Trap zone.")
    print("flip: Flip Summons a Set monster Card, changing it from face-down Defense Position to face-up Attack Position.")
    print("switch: Switch the position of a face-up monster. From Attack Position to Defense Position, or vice-versa. Cannot switch the position of a monster the turn it was Summoned.")
    print("activate: Activates a Spell Card from hand if requirements are met, or activates a Trap Card that was previously Set on the field.")
    print("hand: Shows the player their current hand.")
    print("field: Shows the current field.")
    print("grave: Allows current player to view their or their opponent's Graveyard.")
    print("stats: Check the stats of a card by inputting the card name.")
    print("end: Ends the Main Phase for the current player.")
    print("help: Lists all possible actions.")
    print()

# Returns an integer representing the number of monsters a player has in their respective Monster zones.
def how_many_monsters(zones):
    count = 0
    for i in zones:
        if i != None:
            i += 1

    return count

# Check if a monster exists in the argument monster zones.
def has_monster(zones):
    for i in zones:
        if i != None:
            return True
    
    return False

# Check if a face-up monster exists in argument monster zones.
def has_faceup_monster(zones):
    for i in zones:
        if i != None and i != "Set Card":
            return True

    return False

# Check if a monster with a specific type exists in the argument monster zones.
def has_monster_type(zones, type):
    for i in zones:
        if i != None:
            if i[len(i)-3:len(i)] == "(D)":
                if get_card(i[0:len(i)-4]).monster_type == type:
                    return True

            elif get_card(i).monster_type == type:
                return True

    return False

# Checks if there is a Set monster in the argument monster zones.
def has_set_monster(zones):
    for i in zones:
        if i == "Set Card":
            return True
    
    return False

# Checks if there is a Defense Position monster in the argument monster zones.
def has_defense_monster(zones):
    for i in zones:
        if i == None:
            pass
        elif i[len(i)-3:len(i)] == "(D)":
            return True

    return False

# Check if player has a face-up Spell in their spell/trap zones.
def has_spell(zones):
    for i in zones:
        card = get_card(i)

        if card.super_type == "Spell":
            return True
    
    return False

# Check if player has a face-up Trap in their spell/trap zones.
def has_trap(zones):
    for i in zones:
        card = get_card(i)

        if card.super_type == "Trap":
            return True

    return False

# Check if player has a monster card in their hand.
def has_monster_hand(hand):
    for i in hand:
        card = get_card(i)

        if card.super_type == "Monster":
            return True

    return False

# Checks if a monster card exists in a player's graveyard.
def monster_in_grave(grave):
    for i in grave:
        card = get_card(i)

        if card.super_type == "Monster":
            return True

    return False

# Checks if a player has the necessary Fusion material in hand. Used for checking if Polymerization has necessary activation requirements.
def check_fusion_material(hand):
    if flame_manipulator in hand and masaki_the_legendary_swordsman in hand:
        return True

    elif monster_egg in hand and hinotama_soul in hand:
        return True

    elif firegrass in hand and petit_dragon in hand:
        return True

    elif petit_angel in hand and mystical_sheep_2 in hand:
        return True

    elif skull_servant in hand and dissolverock in hand:
        return True

    elif m_warrior_1 in hand and m_warrior_2 in hand:
        return True

    elif armaill in hand and one_eyed_shield_dragon in hand:
        return True

    elif steel_ogre_grotto_1 in hand and lesser_dragon in hand:
        return True

    elif silver_fang in hand and darkworld_thorns in hand:
        return True

    elif gaia_the_fierce_knight in hand and curse_of_dragon in hand:
        return True

    else:
        return False

# Handles flipping a monster face-up and putting into defense position when the 
# opponent would attack a Set monster.
def attacking_set(zone):
    global curr_player
    global p1_monster1, p1_monster2, p1_monster3
    global p2_monster1, p2_monster2, p2_monster3
    global p1_set1, p1_set2, p1_set3
    global p2_set1, p2_set2, p2_set3

    if curr_player == 1:
        if zone - 1 == 0:
            player2_monster_zones.pop(zone-1)
            p2_monster1 = copy(p2_set1.card)
            player2_monster_zones.insert(zone-1, p2_monster1.card_name)
            player2_monster_zones[zone-1] = p2_monster1.card_name + " (D)"
        elif zone - 1 == 1:
            player2_monster_zones.pop(zone-1)
            p2_monster2 = copy(p2_set2.card)
            player2_monster_zones.insert(zone-1, p2_monster2.card_name)
            player2_monster_zones[zone-1] = p2_monster2.card_name + " (D)"
        elif zone - 1 == 2:
            player2_monster_zones.pop(zone-1)
            p2_monster3 = copy(p2_set3.card)
            player2_monster_zones.insert(zone-1, p2_monster3.card_name)
            player2_monster_zones[zone-1] = p2_monster3.card_name + " (D)"
    
    elif curr_player == 2:
        if zone - 1 == 0:
            player1_monster_zones.pop(zone-1)
            p1_monster1 = copy(p1_set1.card)
            player1_monster_zones.insert(zone-1, p1_monster1.card_name)
            player1_monster_zones[zone-1] = p1_monster1.card_name + " (D)"
        elif zone - 1 == 1:
            player1_monster_zones.pop(zone-1)
            p1_monster2 = copy(p1_set2.card)
            player1_monster_zones.insert(zone-1, p1_monster2.card_name)
            player1_monster_zones[zone-1] = p1_monster2.card_name + " (D)"
        elif zone - 1 == 2:
            player1_monster_zones.pop(zone-1)
            p1_monster3 = copy(p1_set3.card)
            player1_monster_zones.insert(zone-1, p1_monster3.card_name)
            player1_monster_zones[zone-1] = p1_monster3.card_name + " (D)"

# Checks if Equip Spells should be removed from the field when a player's monster is destroyed. 
def check_remove_equips(monster_zone, which_player):
    if which_player == 1:
        if monster_zone - 1 == 0:
            if p1_pair_monster_equip1 != None:
                if p1_pair_monster_equip1[0] == p1_monster1:
                    for i in p1_pair_monster_equip1[2]:
                        player1_st_zones[i] = None 

            if p2_pair_monster_equip1 != None:
                if p2_pair_monster_equip1[0] == p1_monster1:
                    for i in p2_pair_monster_equip1[2]:
                        player2_st_zones[i] = None

        elif monster_zone - 1 == 1:
            if p1_pair_monster_equip2 != None:
                if p1_pair_monster_equip2[0] == p1_monster2:
                    for i in p1_pair_monster_equip2[2]:
                        player1_st_zones[i] = None 

            if p2_pair_monster_equip2 != None:
                if p2_pair_monster_equip2[0] == p1_monster2:
                    for i in p2_pair_monster_equip2[2]:
                        player2_st_zones[i] = None

        elif monster_zone - 1 == 2:
            if p1_pair_monster_equip3 != None:
                if p1_pair_monster_equip3[0] == p1_monster3:
                    for i in p1_pair_monster_equip3[2]:
                        player1_st_zones[i] = None 

            if p2_pair_monster_equip3 != None:
                if p2_pair_monster_equip3[0] == p1_monster3:
                    for i in p2_pair_monster_equip3[2]:
                        player2_st_zones[i] = None

    elif which_player == 2:
        if monster_zone - 1 == 0:
            if p1_pair_monster_equip1 != None:
                if p1_pair_monster_equip1[0] == p2_monster1:
                    for i in p1_pair_monster_equip1[2]:
                        player1_st_zones[i] = None 

            if p2_pair_monster_equip1 != None:
                if p2_pair_monster_equip1[0] == p2_monster1:
                    for i in p2_pair_monster_equip1[2]:
                        player2_st_zones[i] = None

        elif monster_zone - 1 == 1:
            if p1_pair_monster_equip2 != None:
                if p1_pair_monster_equip2[0] == p2_monster2:
                    for i in p1_pair_monster_equip2[2]:
                        player1_st_zones[i] = None 

            if p2_pair_monster_equip2 != None:
                if p2_pair_monster_equip2[0] == p2_monster2:
                    for i in p2_pair_monster_equip2[2]:
                        player2_st_zones[i] = None

        elif monster_zone - 1 == 2:
            if p1_pair_monster_equip3 != None:
                if p1_pair_monster_equip3[0] == p2_monster3:
                    for i in p1_pair_monster_equip3[2]:
                        player1_st_zones[i] = None 

            if p2_pair_monster_equip3 != None:
                if p2_pair_monster_equip3[0] == p2_monster3:
                    for i in p2_pair_monster_equip3[2]:
                        player2_st_zones[i] = None

# Handles removing the buff to ATK/DEF for monsters of certain types when a player's Field Spell is destroyed or is replaced.
def remove_field_buff(player_field_zone):
    if player_field_zone == "Forest":
        if p1_monster1 != None:
            if p1_monster1.monster_type == "Insect" or p1_monster1.monster_type == "Beast" or p1_monster1.monster_type == "Plant" or p1_monster1.monster_type == "Beast-Warrior":
                p1_monster1.attack -= 200
                p1_monster1.defense -= 200

        if p1_monster2 != None:
            if p1_monster2.monster_type == "Insect" or p1_monster2.monster_type == "Beast" or p1_monster2.monster_type == "Plant" or p1_monster2.monster_type == "Beast-Warrior":
                p1_monster2.attack -= 200
                p1_monster2.defense -= 200

        if p1_monster3 != None:
            if p1_monster3.monster_type == "Insect" or p1_monster3.monster_type == "Beast" or p1_monster3.monster_type == "Plant" or p1_monster3.monster_type == "Beast-Warrior":
                p1_monster3.attack -= 200
                p1_monster3.defense -= 200 

        if p2_monster1 != None:
            if p2_monster1.monster_type == "Insect" or p2_monster1.monster_type == "Beast" or p2_monster1.monster_type == "Plant" or p2_monster1.monster_type == "Beast-Warrior":
                p2_monster1.attack -= 200
                p2_monster1.defense -= 200

        if p2_monster2 != None:
            if p2_monster2.monster_type == "Insect" or p2_monster2.monster_type == "Beast" or p2_monster2.monster_type == "Plant" or p2_monster2.monster_type == "Beast-Warrior":
                p2_monster2.attack -= 200
                p2_monster2.defense -= 200

        if p1_monster3 != None:
            if p2_monster3.monster_type == "Insect" or p2_monster3.monster_type == "Beast" or p2_monster3.monster_type == "Plant" or p2_monster3.monster_type == "Beast-Warrior":
                p2_monster3.attack -= 200
                p2_monster3.defense -= 200

    elif player_field_zone == "Wasteland":
        if p1_monster1 != None:
            if p1_monster1.monster_type == "Dinosaur" or p1_monster1.monster_type == "Zombie" or p1_monster1.monster_type == "Rock":
                p1_monster1.attack -= 200
                p1_monster1.defense -= 200

        if p1_monster2 != None:
            if p1_monster2.monster_type == "Dinosaur" or p1_monster2.monster_type == "Zombie" or p1_monster2.monster_type == "Rock":
                p1_monster2.attack -= 200
                p1_monster2.defense -= 200

        if p1_monster3 != None:
            if p1_monster3.monster_type == "Dinosaur" or p1_monster3.monster_type == "Zombie" or p1_monster3.monster_type == "Rock":
                p1_monster3.attack -= 200
                p1_monster3.defense -= 200 

        if p2_monster1 != None:
            if p2_monster1.monster_type == "Dinosaur" or p2_monster1.monster_type == "Zombie" or p2_monster1.monster_type == "Rock":
                p2_monster1.attack -= 200
                p2_monster1.defense -= 200

        if p2_monster2 != None:
            if p2_monster2.monster_type == "Dinosaur" or p2_monster2.monster_type == "Zombie" or p2_monster2.monster_type == "Rock":
                p2_monster2.attack -= 200
                p2_monster2.defense -= 200

        if p1_monster3 != None:
            if p2_monster3.monster_type == "Dinosaur" or p2_monster3.monster_type == "Zombie" or p2_monster3.monster_type == "Rock":
                p2_monster3.attack -= 200
                p2_monster3.defense -= 200

    elif player_field_zone == "Mountain":
        if p1_monster1 != None:
            if p1_monster1.monster_type == "Dragon" or p1_monster1.monster_type == "Winged Beast" or p1_monster1.monster_type == "Thunder":
                p1_monster1.attack -= 200
                p1_monster1.defense -= 200

        if p1_monster2 != None:
            if p1_monster2.monster_type == "Dragon" or p1_monster2.monster_type == "Winged Beast" or p1_monster2.monster_type == "Thunder":
                p1_monster2.attack -= 200
                p1_monster2.defense -= 200

        if p1_monster3 != None:
            if p1_monster3.monster_type == "Dragon" or p1_monster3.monster_type == "Winged Beast" or p1_monster3.monster_type == "Thunder":
                p1_monster3.attack -= 200
                p1_monster3.defense -= 200 

        if p2_monster1 != None:
            if p2_monster1.monster_type == "Dragon" or p2_monster1.monster_type == "Winged Beast" or p2_monster1.monster_type == "Thunder":
                p2_monster1.attack -= 200
                p2_monster1.defense -= 200

        if p2_monster2 != None:
            if p2_monster2.monster_type == "Dragon" or p2_monster2.monster_type == "Winged Beast" or p2_monster2.monster_type == "Thunder":
                p2_monster2.attack -= 200
                p2_monster2.defense -= 200

        if p1_monster3 != None:
            if p2_monster3.monster_type == "Dragon" or p2_monster3.monster_type == "Winged Beast" or p2_monster3.monster_type == "Thunder":
                p2_monster3.attack -= 200
                p2_monster3.defense -= 200

    elif player_field_zone == "Sogen":
        if p1_monster1 != None:
            if p1_monster1.monster_type == "Warrior" or p1_monster1.monster_type == "Beast-Warrior":
                p1_monster1.attack -= 200
                p1_monster1.defense -= 200

        if p1_monster2 != None:
            if p1_monster2.monster_type == "Warrior" or p1_monster2.monster_type == "Beast-Warrior":
                p1_monster2.attack -= 200
                p1_monster2.defense -= 200

        if p1_monster3 != None:
            if p1_monster3.monster_type == "Warrior" or p1_monster3.monster_type == "Beast-Warrior":
                p1_monster3.attack -= 200
                p1_monster3.defense -= 200 

        if p2_monster1 != None:
            if p2_monster1.monster_type == "Warrior" or p2_monster1.monster_type == "Beast-Warrior":
                p2_monster1.attack -= 200
                p2_monster1.defense -= 200

        if p2_monster2 != None:
            if p2_monster2.monster_type == "Warrior" or p2_monster2.monster_type == "Beast-Warrior":
                p2_monster2.attack -= 200
                p2_monster2.defense -= 200

        if p1_monster3 != None:
            if p2_monster3.monster_type == "Warrior" or p2_monster3.monster_type == "Beast-Warrior":
                p2_monster3.attack -= 200
                p2_monster3.defense -= 200

    elif player_field_zone == "Umi":
        if p1_monster1 != None:
            if p1_monster1.monster_type == "Fish" or p1_monster1.monster_type == "Sea Serpent" or p1_monster1.monster_type == "Thunder" or p1_monster1.monster_type == "Aqua":
                p1_monster1.attack -= 200
                p1_monster1.defense -= 200

        if p1_monster2 != None:
            if p1_monster2.monster_type == "Fish" or p1_monster2.monster_type == "Sea Serpent" or p1_monster2.monster_type == "Thunder" or p1_monster2.monster_type == "Aqua":
                p1_monster2.attack -= 200
                p1_monster2.defense -= 200

        if p1_monster3 != None:
            if p1_monster3.monster_type == "Fish" or p1_monster3.monster_type == "Sea Serpent" or p1_monster3.monster_type == "Thunder" or p1_monster3.monster_type == "Aqua":
                p1_monster3.attack -= 200
                p1_monster3.defense -= 200 

        if p2_monster1 != None:
            if p2_monster1.monster_type == "Fish" or p2_monster1.monster_type == "Sea Serpent" or p2_monster1.monster_type == "Thunder" or p2_monster1.monster_type == "Aqua":
                p2_monster1.attack -= 200
                p2_monster1.defense -= 200

        if p2_monster2 != None:
            if p2_monster2.monster_type == "Fish" or p2_monster2.monster_type == "Sea Serpent" or p2_monster2.monster_type == "Thunder" or p2_monster2.monster_type == "Aqua":
                p2_monster2.attack -= 200
                p2_monster2.defense -= 200

        if p1_monster3 != None:
            if p2_monster3.monster_type == "Fish" or p2_monster3.monster_type == "Sea Serpent" or p2_monster3.monster_type == "Thunder" or p2_monster3.monster_type == "Aqua":
                p2_monster3.attack -= 200
                p2_monster3.defense -= 200

        if p1_monster1 != None:
            if p1_monster1.monster_type == "Machine" or p1_monster1.monster_type == "Pyro":
                p1_monster1.attack += 200
                p1_monster1.defense += 200

        if p1_monster2 != None:
            if p1_monster2.monster_type == "Machine" or p1_monster2.monster_type == "Pyro":
                p1_monster2.attack += 200
                p1_monster2.defense += 200

        if p1_monster3 != None:
            if p1_monster3.monster_type == "Machine" or p1_monster3.monster_type == "Pyro":
                p1_monster3.attack += 200
                p1_monster3.defense += 200 

        if p2_monster1 != None:
            if p2_monster1.monster_type == "Machine" or p2_monster1.monster_type == "Pyro":
                p2_monster1.attack += 200
                p2_monster1.defense += 200

        if p2_monster2 != None:
            if p2_monster2.monster_type == "Machine" or p2_monster2.monster_type == "Pyro":
                p2_monster2.attack += 200
                p2_monster2.defense += 200

        if p1_monster3 != None:
            if p2_monster3.monster_type == "Machine" or p2_monster3.monster_type == "Pyro":
                p2_monster3.attack += 200
                p2_monster3.defense += 200

    elif player_field_zone == "Yami":
        if p1_monster1 != None:
            if p1_monster1.monster_type == "Fiend" or p1_monster1.monster_type == "Spellcaster":
                p1_monster1.attack -= 200
                p1_monster1.defense -= 200

        if p1_monster2 != None:
            if p1_monster2.monster_type == "Fiend" or p1_monster2.monster_type == "Spellcaster":
                p1_monster2.attack -= 200
                p1_monster2.defense -= 200

        if p1_monster3 != None:
            if p1_monster3.monster_type == "Fiend" or p1_monster3.monster_type == "Spellcaster":
                p1_monster3.attack -= 200
                p1_monster3.defense -= 200 

        if p2_monster1 != None:
            if p2_monster1.monster_type == "Fiend" or p2_monster1.monster_type == "Spellcaster":
                p2_monster1.attack -= 200
                p2_monster1.defense -= 200

        if p2_monster2 != None:
            if p2_monster2.monster_type == "Fiend" or p2_monster2.monster_type == "Spellcaster":
                p2_monster2.attack -= 200
                p2_monster2.defense -= 200

        if p1_monster3 != None:
            if p2_monster3.monster_type == "Fiend" or p2_monster3.monster_type == "Spellcaster":
                p2_monster3.attack -= 200
                p2_monster3.defense -= 200

        if p1_monster1 != None:
            if p1_monster1.monster_type == "Fairy":
                p1_monster1.attack += 200
                p1_monster1.defense += 200

        if p1_monster2 != None:
            if p1_monster2.monster_type == "Fairy":
                p1_monster2.attack += 200
                p1_monster2.defense += 200

        if p1_monster3 != None:
            if p1_monster3.monster_type == "Fairy":
                p1_monster3.attack += 200
                p1_monster3.defense += 200 

        if p2_monster1 != None:
            if p2_monster1.monster_type == "Fairy":
                p2_monster1.attack += 200
                p2_monster1.defense += 200

        if p2_monster2 != None:
            if p2_monster2.monster_type == "Fairy":
                p2_monster2.attack += 200
                p2_monster2.defense += 200

        if p1_monster3 != None:
            if p2_monster3.monster_type == "Fairy":
                p2_monster3.attack += 200
                p2_monster3.defense += 200

# Handles increasing the Attack and Defense of monsters if a Field Spell is on the field in either players Field Zone and the monster being summoned has the correct Type.
def activate_field_on_summon(zone, p1_field, p2_field, player):
    if player == 1:
        if p1_field == None and p2_field == None:
            return

        elif p1_field == "Set Card" and p2_field == "Set Card":
            return
        
        else:
            card = get_card(player1_monster_zones[zone-1])

            if p1_field == "Forest" and p2_field == "Sogen":
                if card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p1_monster1.attack += 400
                        p1_monster1.defense += 400

                    elif zone - 1 == 1:
                        p1_monster2.attack += 400
                        p1_monster2.defense += 400

                    elif zone - 1 == 2:
                        p1_monster3.attack += 400
                        p1_monster3.defense += 400

            elif p1_field == "Sogen" and p2_field == "Forest":
                if card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p1_monster1.attack += 400
                        p1_monster1.defense += 400

                    elif zone - 1 == 1:
                        p1_monster2.attack += 400
                        p1_monster2.defense += 400

                    elif zone - 1 == 2:
                        p1_monster3.attack += 400
                        p1_monster3.defense += 400

            elif p1_field == "Umi" and p2_field == "Mountain":
                if card.monster_type == "Thunder":
                    if zone - 1 == 0:
                        p1_monster1.attack += 400
                        p1_monster1.defense += 400

                    elif zone - 1 == 1:
                        p1_monster2.attack += 400
                        p1_monster2.defense += 400

                    elif zone - 1 == 2:
                        p1_monster3.attack += 400
                        p1_monster3.defense += 400

            elif p1_field == "Mountain" and p2_field == "Umi":
                if card.monster_type == "Thunder":
                    if zone - 1 == 0:
                        p1_monster1.attack += 400
                        p1_monster1.defense += 400

                    elif zone - 1 == 1:
                        p1_monster2.attack += 400
                        p1_monster2.defense += 400

                    elif zone - 1 == 2:
                        p1_monster3.attack += 400
                        p1_monster3.defense += 400

            elif p1_field == "Forest" and not p2_field == "Forest":
                if card.monster_type == "Insect" or card.monster_type == "Beast" or card.monster_type == "Plant" or card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p1_monster1.attack += 200
                        p1_monster1.defense += 200

                    elif zone - 1 == 1:
                        p1_monster2.attack += 200
                        p1_monster2.defense += 200

                    elif zone - 1 == 2:
                        p1_monster3.attack += 200
                        p1_monster3.defense += 200
            
            elif not p1_field == "Forest" and p2_field == "Forest":
                if card.monster_type == "Insect" or card.monster_type == "Beast" or card.monster_type == "Plant" or card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p1_monster1.attack += 200
                        p1_monster1.defense += 200

                    elif zone - 1 == 1:
                        p1_monster2.attack += 200
                        p1_monster2.defense += 200

                    elif zone - 1 == 2:
                        p1_monster3.attack += 200
                        p1_monster3.defense += 200

            elif p1_field == "Forest" and p2_field == "Forest":
                if card.monster_type == "Insect" or card.monster_type == "Beast" or card.monster_type == "Plant" or card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p1_monster1.attack += 400
                        p1_monster1.defense += 400

                    elif zone - 1 == 1:
                        p1_monster2.attack += 400
                        p1_monster2.defense += 400

                    elif zone - 1 == 2:
                        p1_monster3.attack += 400
                        p1_monster3.defense += 400

            elif p1_field == "Wasteland" and not p2_field == "Wasteland":
                if card.monster_type == "Dinosaur" or card.monster_type == "Zombie" or card.monster_type == "Rock":
                    if zone - 1 == 0:
                        p1_monster1.attack += 200
                        p1_monster1.defense += 200

                    elif zone - 1 == 1:
                        p1_monster2.attack += 200
                        p1_monster2.defense += 200

                    elif zone - 1 == 2:
                        p1_monster3.attack += 200
                        p1_monster3.defense += 200
            
            elif not p1_field == "Wasteland" and not p2_field == "Wasteland":
                if card.monster_type == "Dinosaur" or card.monster_type == "Zombie" or card.monster_type == "Rock":
                    if zone - 1 == 0:
                        p1_monster1.attack += 200
                        p1_monster1.defense += 200

                    elif zone - 1 == 1:
                        p1_monster2.attack += 200
                        p1_monster2.defense += 200

                    elif zone - 1 == 2:
                        p1_monster3.attack += 200
                        p1_monster3.defense += 200

            elif p1_field == "Wasteland" and p2_field == "Wasteland":
                if card.monster_type == "Dinosaur" or card.monster_type == "Zombie" or card.monster_type == "Rock":
                    if zone - 1 == 0:
                        p1_monster1.attack += 400
                        p1_monster1.defense += 400

                    elif zone - 1 == 1:
                        p1_monster2.attack += 400
                        p1_monster2.defense += 400

                    elif zone - 1 == 2:
                        p1_monster3.attack += 400
                        p1_monster3.defense += 400

            elif p1_field == "Mountain" and not p2_field == "Mountain":
                if card.monster_type == "Dragon" or card.monster_type == "Winged Beast" or card.monster_type == "Thunder":
                    if zone - 1 == 0:
                        p1_monster1.attack += 200
                        p1_monster1.defense += 200

                    elif zone - 1 == 1:
                        p1_monster2.attack += 200
                        p1_monster2.defense += 200

                    elif zone - 1 == 2:
                        p1_monster3.attack += 200
                        p1_monster3.defense += 200

            elif not p1_field == "Mountain" and p2_field == "Mountain":
                if card.monster_type == "Dragon" or card.monster_type == "Winged Beast" or card.monster_type == "Thunder":
                    if zone - 1 == 0:
                        p1_monster1.attack += 200
                        p1_monster1.defense += 200

                    elif zone - 1 == 1:
                        p1_monster2.attack += 200
                        p1_monster2.defense += 200

                    elif zone - 1 == 2:
                        p1_monster3.attack += 200
                        p1_monster3.defense += 200

            elif p1_field == "Mountain" and p2_field == "Mountain":
                if card.monster_type == "Dragon" or card.monster_type == "Winged Beast" or card.monster_type == "Thunder":
                    if zone - 1 == 0:
                        p1_monster1.attack += 400
                        p1_monster1.defense += 400

                    elif zone - 1 == 1:
                        p1_monster2.attack += 400
                        p1_monster2.defense += 400

                    elif zone - 1 == 2:
                        p1_monster3.attack += 400
                        p1_monster3.defense += 400

            elif p1_field == "Sogen" and not p2_field == "Sogen":
                if card.monster_type == "Warrior" or card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p1_monster1.attack += 200
                        p1_monster1.defense += 200

                    elif zone - 1 == 1:
                        p1_monster2.attack += 200
                        p1_monster2.defense += 200

                    elif zone - 1 == 2:
                        p1_monster3.attack += 200
                        p1_monster3.defense += 200

            elif not p1_field == "Sogen" and p2_field == "Sogen":
                if card.monster_type == "Warrior" or card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p1_monster1.attack += 200
                        p1_monster1.defense += 200

                    elif zone - 1 == 1:
                        p1_monster2.attack += 200
                        p1_monster2.defense += 200

                    elif zone - 1 == 2:
                        p1_monster3.attack += 200
                        p1_monster3.defense += 200

            elif p1_field == "Sogen" and p2_field == "Sogen":
                if card.monster_type == "Warrior" or card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p1_monster1.attack += 400
                        p1_monster1.defense += 400

                    elif zone - 1 == 1:
                        p1_monster2.attack += 400
                        p1_monster2.defense += 400

                    elif zone - 1 == 2:
                        p1_monster3.attack += 400
                        p1_monster3.defense += 400

            elif p1_field == "Umi" and not p2_field == "Umi":
                if card.monster_type == "Fish" or card.monster_type == "Sea Serpent" or card.monster_type == "Thunder" or card.monster_type == "Aqua":
                    if zone - 1 == 0:
                        p1_monster1.attack += 200
                        p1_monster1.defense += 200

                    elif zone - 1 == 1:
                        p1_monster2.attack += 200
                        p1_monster2.defense += 200

                    elif zone - 1 == 2:
                        p1_monster3.attack += 200
                        p1_monster3.defense += 200

                elif card.monster_type == "Machine" or card.monster_type == "Pyro":
                    if zone - 1 == 0:
                        p1_monster1.attack -= 200
                        p1_monster1.defense -= 200

                    elif zone - 1 == 1:
                        p1_monster2.attack -= 200
                        p1_monster2.defense -= 200

                    elif zone - 1 == 2:
                        p1_monster3.attack -= 200
                        p1_monster3.defense -= 200

            elif not p1_field == "Umi" and p2_field == "Umi":
                if card.monster_type == "Fish" or card.monster_type == "Sea Serpent" or card.monster_type == "Thunder" or card.monster_type == "Aqua":
                    if zone - 1 == 0:
                        p1_monster1.attack += 200
                        p1_monster1.defense += 200

                    elif zone - 1 == 1:
                        p1_monster2.attack += 200
                        p1_monster2.defense += 200

                    elif zone - 1 == 2:
                        p1_monster3.attack += 200
                        p1_monster3.defense += 200

                elif card.monster_type == "Machine" or card.monster_type == "Pyro":
                    if zone - 1 == 0:
                        p1_monster1.attack -= 200
                        p1_monster1.defense -= 200

                    elif zone - 1 == 1:
                        p1_monster2.attack -= 200
                        p1_monster2.defense -= 200

                    elif zone - 1 == 2:
                        p1_monster3.attack -= 200
                        p1_monster3.defense -= 200

            elif p1_field == "Umi" and p2_field == "Umi":
                if card.monster_type == "Fish" or card.monster_type == "Sea Serpent" or card.monster_type == "Thunder" or card.monster_type == "Aqua":
                    if zone - 1 == 0:
                        p1_monster1.attack += 400
                        p1_monster1.defense += 400

                    elif zone - 1 == 1:
                        p1_monster2.attack += 400
                        p1_monster2.defense += 400

                    elif zone - 1 == 2:
                        p1_monster3.attack += 400
                        p1_monster3.defense += 400

                elif card.monster_type == "Machine" or card.monster_type == "Pyro":
                    if zone - 1 == 0:
                        p1_monster1.attack -= 400
                        p1_monster1.defense -= 400

                    elif zone - 1 == 1:
                        p1_monster2.attack -= 400
                        p1_monster2.defense -= 400

                    elif zone - 1 == 2:
                        p1_monster3.attack -= 400
                        p1_monster3.defense -= 400

            elif p1_field == "Yami" and not p2_field == "Yami":
                if card.monster_type == "Fiend" or card.monster_type == "Spellcaster":
                    if zone - 1 == 0:
                        p1_monster1.attack += 200
                        p1_monster1.defense += 200

                    elif zone - 1 == 1:
                        p1_monster2.attack += 200
                        p1_monster2.defense += 200

                    elif zone - 1 == 2:
                        p1_monster3.attack += 200
                        p1_monster3.defense += 200

                elif card.monster_type == "Fairy":
                    if zone - 1 == 0:
                        p1_monster1.attack -= 200
                        p1_monster1.defense -= 200

                    elif zone - 1 == 1:
                        p1_monster2.attack -= 200
                        p1_monster2.defense -= 200

                    elif zone - 1 == 2:
                        p1_monster3.attack -= 200
                        p1_monster3.defense -= 200

            elif not p1_field == "Yami" and p2_field == "Yami":
                if card.monster_type == "Fiend" or card.monster_type == "Spellcaster":
                    if zone - 1 == 0:
                        p1_monster1.attack += 200
                        p1_monster1.defense += 200

                    elif zone - 1 == 1:
                        p1_monster2.attack += 200
                        p1_monster2.defense += 200

                    elif zone - 1 == 2:
                        p1_monster3.attack += 200
                        p1_monster3.defense += 200

                elif card.monster_type == "Fairy":
                    if zone - 1 == 0:
                        p1_monster1.attack -= 200
                        p1_monster1.defense -= 200

                    elif zone - 1 == 1:
                        p1_monster2.attack -= 200
                        p1_monster2.defense -= 200

                    elif zone - 1 == 2:
                        p1_monster3.attack -= 200
                        p1_monster3.defense -= 200

            elif p1_field == "Yami" and p2_field == "Yami":
                if card.monster_type == "Fiend" or card.monster_type == "Spellcaster":
                    if zone - 1 == 0:
                        p1_monster1.attack += 400
                        p1_monster1.defense += 400

                    elif zone - 1 == 1:
                        p1_monster2.attack += 400
                        p1_monster2.defense += 400

                    elif zone - 1 == 2:
                        p1_monster3.attack += 400
                        p1_monster3.defense += 400

                elif card.monster_type == "Fairy":
                    if zone - 1 == 0:
                        p1_monster1.attack -= 400
                        p1_monster1.defense -= 400

                    elif zone - 1 == 1:
                        p1_monster2.attack -= 400
                        p1_monster2.defense -= 400

                    elif zone - 1 == 2:
                        p1_monster3.attack -= 400
                        p1_monster3.defense -= 400

    if player == 2:
        if p1_field == None and p2_field == None:
            return

        elif p1_field == "Set Card" and p2_field == "Set Card":
            return
        
        else:
            card = get_card(player2_monster_zones[zone-1])

            if p1_field == "Forest" and p2_field == "Sogen":
                if card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p2_monster1.attack += 400
                        p2_monster1.defense += 400

                    elif zone - 1 == 1:
                        p2_monster2.attack += 400
                        p2_monster2.defense += 400

                    elif zone - 1 == 2:
                        p2_monster3.attack += 400
                        p2_monster3.defense += 400

            elif p1_field == "Sogen" and p2_field == "Forest":
                if card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p2_monster1.attack += 400
                        p2_monster1.defense += 400

                    elif zone - 1 == 1:
                        p2_monster2.attack += 400
                        p2_monster2.defense += 400

                    elif zone - 1 == 2:
                        p2_monster3.attack += 400
                        p2_monster3.defense += 400

            elif p1_field == "Umi" and p2_field == "Mountain":
                if card.monster_type == "Thunder":
                    if zone - 1 == 0:
                        p2_monster1.attack += 400
                        p2_monster1.defense += 400

                    elif zone - 1 == 1:
                        p2_monster2.attack += 400
                        p2_monster2.defense += 400

                    elif zone - 1 == 2:
                        p2_monster3.attack += 400
                        p2_monster3.defense += 400

            elif p1_field == "Mountain" and p2_field == "Umi":
                if card.monster_type == "Thunder":
                    if zone - 1 == 0:
                        p2_monster1.attack += 400
                        p2_monster1.defense += 400

                    elif zone - 1 == 1:
                        p2_monster2.attack += 400
                        p2_monster2.defense += 400

                    elif zone - 1 == 2:
                        p2_monster3.attack += 400
                        p2_monster3.defense += 400

            elif p1_field == "Forest" and not p2_field == "Forest":
                if card.monster_type == "Insect" or card.monster_type == "Beast" or card.monster_type == "Plant" or card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p2_monster1.attack += 200
                        p2_monster1.defense += 200

                    elif zone - 1 == 1:
                        p2_monster2.attack += 200
                        p2_monster2.defense += 200

                    elif zone - 1 == 2:
                        p2_monster3.attack += 200
                        p2_monster3.defense += 200
            
            elif not p1_field == "Forest" and p2_field == "Forest":
                if card.monster_type == "Insect" or card.monster_type == "Beast" or card.monster_type == "Plant" or card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p2_monster1.attack += 200
                        p2_monster1.defense += 200

                    elif zone - 1 == 1:
                        p2_monster2.attack += 200
                        p2_monster2.defense += 200

                    elif zone - 1 == 2:
                        p2_monster3.attack += 200
                        p2_monster3.defense += 200

            elif p1_field == "Forest" and p2_field == "Forest":
                if card.monster_type == "Insect" or card.monster_type == "Beast" or card.monster_type == "Plant" or card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p2_monster1.attack += 400
                        p2_monster1.defense += 400

                    elif zone - 1 == 1:
                        p2_monster2.attack += 400
                        p2_monster2.defense += 400

                    elif zone - 1 == 2:
                        p2_monster3.attack += 400
                        p2_monster3.defense += 400

            elif p1_field == "Wasteland" and not p2_field == "Wasteland":
                if card.monster_type == "Dinosaur" or card.monster_type == "Zombie" or card.monster_type == "Rock":
                    if zone - 1 == 0:
                        p2_monster1.attack += 200
                        p2_monster1.defense += 200

                    elif zone - 1 == 1:
                        p2_monster2.attack += 200
                        p2_monster2.defense += 200

                    elif zone - 1 == 2:
                        p2_monster3.attack += 200
                        p2_monster3.defense += 200
            
            elif not p1_field == "Wasteland" and not p2_field == "Wasteland":
                if card.monster_type == "Dinosaur" or card.monster_type == "Zombie" or card.monster_type == "Rock":
                    if zone - 1 == 0:
                        p2_monster1.attack += 200
                        p2_monster1.defense += 200

                    elif zone - 1 == 1:
                        p2_monster2.attack += 200
                        p2_monster2.defense += 200

                    elif zone - 1 == 2:
                        p2_monster3.attack += 200
                        p2_monster3.defense += 200

            elif p1_field == "Wasteland" and p2_field == "Wasteland":
                if card.monster_type == "Dinosaur" or card.monster_type == "Zombie" or card.monster_type == "Rock":
                    if zone - 1 == 0:
                        p2_monster1.attack += 400
                        p2_monster1.defense += 400

                    elif zone - 1 == 1:
                        p2_monster2.attack += 400
                        p2_monster2.defense += 400

                    elif zone - 1 == 2:
                        p2_monster3.attack += 400
                        p2_monster3.defense += 400

            elif p1_field == "Mountain" and not p2_field == "Mountain":
                if card.monster_type == "Dragon" or card.monster_type == "Winged Beast" or card.monster_type == "Thunder":
                    if zone - 1 == 0:
                        p2_monster1.attack += 200
                        p2_monster1.defense += 200

                    elif zone - 1 == 1:
                        p2_monster2.attack += 200
                        p2_monster2.defense += 200

                    elif zone - 1 == 2:
                        p2_monster3.attack += 200
                        p2_monster3.defense += 200

            elif not p1_field == "Mountain" and p2_field == "Mountain":
                if card.monster_type == "Dragon" or card.monster_type == "Winged Beast" or card.monster_type == "Thunder":
                    if zone - 1 == 0:
                        p2_monster1.attack += 200
                        p2_monster1.defense += 200

                    elif zone - 1 == 1:
                        p2_monster2.attack += 200
                        p2_monster2.defense += 200

                    elif zone - 1 == 2:
                        p2_monster3.attack += 200
                        p2_monster3.defense += 200

            elif p1_field == "Mountain" and p2_field == "Mountain":
                if card.monster_type == "Dragon" or card.monster_type == "Winged Beast" or card.monster_type == "Thunder":
                    if zone - 1 == 0:
                        p2_monster1.attack += 400
                        p2_monster1.defense += 400

                    elif zone - 1 == 1:
                        p2_monster2.attack += 400
                        p2_monster2.defense += 400

                    elif zone - 1 == 2:
                        p2_monster3.attack += 400
                        p2_monster3.defense += 400

            elif p1_field == "Sogen" and not p2_field == "Sogen":
                if card.monster_type == "Warrior" or card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p2_monster1.attack += 200
                        p2_monster1.defense += 200

                    elif zone - 1 == 1:
                        p2_monster2.attack += 200
                        p2_monster2.defense += 200

                    elif zone - 1 == 2:
                        p2_monster3.attack += 200
                        p2_monster3.defense += 200

            elif not p1_field == "Sogen" and p2_field == "Sogen":
                if card.monster_type == "Warrior" or card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p2_monster1.attack += 200
                        p2_monster1.defense += 200

                    elif zone - 1 == 1:
                        p2_monster2.attack += 200
                        p2_monster2.defense += 200

                    elif zone - 1 == 2:
                        p2_monster3.attack += 200
                        p2_monster3.defense += 200

            elif p1_field == "Sogen" and p2_field == "Sogen":
                if card.monster_type == "Warrior" or card.monster_type == "Beast-Warrior":
                    if zone - 1 == 0:
                        p2_monster1.attack += 400
                        p2_monster1.defense += 400

                    elif zone - 1 == 1:
                        p2_monster2.attack += 400
                        p2_monster2.defense += 400

                    elif zone - 1 == 2:
                        p2_monster3.attack += 400
                        p2_monster3.defense += 400

            elif p1_field == "Umi" and not p2_field == "Umi":
                if card.monster_type == "Fish" or card.monster_type == "Sea Serpent" or card.monster_type == "Thunder" or card.monster_type == "Aqua":
                    if zone - 1 == 0:
                        p2_monster1.attack += 200
                        p2_monster1.defense += 200

                    elif zone - 1 == 1:
                        p2_monster2.attack += 200
                        p2_monster2.defense += 200

                    elif zone - 1 == 2:
                        p2_monster3.attack += 200
                        p2_monster3.defense += 200

                elif card.monster_type == "Machine" or card.monster_type == "Pyro":
                    if zone - 1 == 0:
                        p2_monster1.attack -= 200
                        p2_monster1.defense -= 200

                    elif zone - 1 == 1:
                        p2_monster2.attack -= 200
                        p2_monster2.defense -= 200

                    elif zone - 1 == 2:
                        p2_monster3.attack -= 200
                        p2_monster3.defense -= 200

            elif not p1_field == "Umi" and p2_field == "Umi":
                if card.monster_type == "Fish" or card.monster_type == "Sea Serpent" or card.monster_type == "Thunder" or card.monster_type == "Aqua":
                    if zone - 1 == 0:
                        p2_monster1.attack += 200
                        p2_monster1.defense += 200

                    elif zone - 1 == 1:
                        p2_monster2.attack += 200
                        p2_monster2.defense += 200

                    elif zone - 1 == 2:
                        p2_monster3.attack += 200
                        p2_monster3.defense += 200

                elif card.monster_type == "Machine" or card.monster_type == "Pyro":
                    if zone - 1 == 0:
                        p2_monster1.attack -= 200
                        p2_monster1.defense -= 200

                    elif zone - 1 == 1:
                        p2_monster2.attack -= 200
                        p2_monster2.defense -= 200

                    elif zone - 1 == 2:
                        p2_monster3.attack -= 200
                        p2_monster3.defense -= 200

            elif p1_field == "Umi" and p2_field == "Umi":
                if card.monster_type == "Fish" or card.monster_type == "Sea Serpent" or card.monster_type == "Thunder" or player2_monster_zones[zone-1].monster_type == "Aqua":
                    if zone - 1 == 0:
                        p2_monster1.attack += 400
                        p2_monster1.defense += 400

                    elif zone - 1 == 1:
                        p2_monster2.attack += 400
                        p2_monster2.defense += 400

                    elif zone - 1 == 2:
                        p2_monster3.attack += 400
                        p2_monster3.defense += 400

                elif card.monster_type == "Machine" or card.monster_type == "Pyro":
                    if zone - 1 == 0:
                        p2_monster1.attack -= 400
                        p2_monster1.defense -= 400

                    elif zone - 1 == 1:
                        p2_monster2.attack -= 400
                        p2_monster2.defense -= 400

                    elif zone - 1 == 2:
                        p2_monster3.attack -= 400
                        p2_monster3.defense -= 400

            elif p1_field == "Yami" and not p2_field == "Yami":
                if card.monster_type == "Fiend" or card.monster_type == "Spellcaster":
                    if zone - 1 == 0:
                        p2_monster1.attack += 200
                        p2_monster1.defense += 200

                    elif zone - 1 == 1:
                        p2_monster2.attack += 200
                        p2_monster2.defense += 200

                    elif zone - 1 == 2:
                        p2_monster3.attack += 200
                        p2_monster3.defense += 200

                elif card.monster_type == "Fairy":
                    if zone - 1 == 0:
                        p2_monster1.attack -= 200
                        p2_monster1.defense -= 200

                    elif zone - 1 == 1:
                        p2_monster2.attack -= 200
                        p2_monster2.defense -= 200

                    elif zone - 1 == 2:
                        p2_monster3.attack -= 200
                        p2_monster3.defense -= 200

            elif not p1_field == "Yami" and p2_field == "Yami":
                if card.monster_type == "Fiend" or card.monster_type == "Spellcaster":
                    if zone - 1 == 0:
                        p2_monster1.attack += 200
                        p2_monster1.defense += 200

                    elif zone - 1 == 1:
                        p2_monster2.attack += 200
                        p2_monster2.defense += 200

                    elif zone - 1 == 2:
                        p2_monster3.attack += 200
                        p2_monster3.defense += 200

                elif card.monster_type == "Fairy":
                    if zone - 1 == 0:
                        p2_monster1.attack -= 200
                        p2_monster1.defense -= 200

                    elif zone - 1 == 1:
                        p2_monster2.attack -= 200
                        p2_monster2.defense -= 200

                    elif zone - 1 == 2:
                        p2_monster3.attack -= 200
                        p2_monster3.defense -= 200

            elif p1_field == "Yami" and p2_field == "Yami":
                if card.monster_type == "Fiend" or card.monster_type == "Spellcaster":
                    if zone - 1 == 0:
                        p2_monster1.attack += 400
                        p2_monster1.defense += 400

                    elif zone - 1 == 1:
                        p2_monster2.attack += 400
                        p2_monster2.defense += 400

                    elif zone - 1 == 2:
                        p2_monster3.attack += 400
                        p2_monster3.defense += 400

                elif card.monster_type == "Fairy":
                    if zone - 1 == 0:
                        p2_monster1.attack -= 400
                        p2_monster1.defense -= 400

                    elif zone - 1 == 1:
                        p2_monster2.attack -= 400
                        p2_monster2.defense -= 400

                    elif zone - 1 == 2:
                        p2_monster3.attack -= 400
                        p2_monster3.defense -= 400

# Handles switch a Dragon-Type monster to defense position if they are summoned while Dragon Capture Jar is face-up in either player's Spell/Trap zones
def dragon_capture_jar_on_summon(zone):
    global curr_player

    if curr_player == 1:
        if dragon_capture_jar.card_name in player1_st_zones or dragon_capture_jar.card_name in player2_st_zones:
            if zone - 1 == 0:
                if p1_monster1.monster_type == "Dragon":
                    player1_monster_zones[0] == p1_monster1.card_name + " (D)"

            elif zone - 1 == 1:
                if p1_monster2.monster_type == "Dragon":
                    player1_monster_zones[1] == p1_monster2.card_name + " (D)"

            elif zone - 1 == 2:
                if p1_monster3.monster_type == "Dragon":
                    player1_monster_zones[2] == p1_monster3.card_name + " (D)"

    elif curr_player == 2:
        if dragon_capture_jar.card_name in player1_st_zones or dragon_capture_jar.card_name in player2_st_zones:
            if zone - 1 == 0:
                if p2_monster1.monster_type == "Dragon":
                    player2_monster_zones[0] == p2_monster1.card_name + " (D)"

            elif zone - 1 == 1:
                if p2_monster2.monster_type == "Dragon":
                    player2_monster_zones[1] == p2_monster2.card_name + " (D)"

            elif zone - 1 == 2:
                if p2_monster3.monster_type == "Dragon":
                    player2_monster_zones[2] == p2_monster3.card_name + " (D)"


def activate_trap(player):
    if player == 1:
        if p1_st_set1 != None:
            if p1_st_set1.card == trap_hole and has_faceup_monster(player2_monster_zones):
                can_activate = check_activation_requirement(trap_hole)

                if can_activate:
                    while(1):
                        inp = input("P1: Activate Trap Hole (y/n): ")

                        if inp == "y":
                            print("Player 1 activates Trap Hole")
                            player1_st_zones[0] = None
                            activate_effect(trap_hole, 0)
                            player1_grave.append(trap_hole.card_name)
                            p1_st_set1 = None

                            break
                                            
                        else:
                            break

            elif p1_st_set1.card == two_pronged_attack:
                can_activate = check_activation_requirement(two_pronged_attack)

                if can_activate:
                    while(1):
                        inp = input("P1: Activate Two-Pronged Attack (y/n): ")

                        if inp == "y":
                            print("Player 1 activates Two-Pronged Attack")
                            player1_st_zones[0] = None
                            activate_effect(two_pronged_attack, 0)
                            player1_grave.append(two_pronged_attack.card_name)
                            p1_st_set1 = None

                            break
                                            
                        else:
                            break

            elif p1_st_set1.card == dragon_capture_jar:
                while(1):
                    inp = input("P1: Activate Dragon Capture Jar (y/n): ")

                    if inp == "y":
                        print("Player 1 activates Dragon Capture Jar")
                        activate_effect(dragon_capture_jar, 0)
                        p1_st_set1 = None

                        break
                                            
                    else:
                        break

        elif p1_st_set2 != None:
            if p1_st_set2.card == trap_hole and has_faceup_monster(player2_monster_zones):
                can_activate = check_activation_requirement(trap_hole)

                if can_activate:
                    while(1):
                        inp = input("P1: Activate Trap Hole (y/n): ")

                        if inp == "y":
                            print("Player 1 activates Trap Hole")
                            player1_st_zones[1] = None
                            activate_effect(trap_hole, 1)
                            player1_grave.append(trap_hole.card_name)
                            p1_st_set2 = None

                            break
                                            
                        else:
                            break

            elif p1_st_set2.card == two_pronged_attack:
                can_activate = check_activation_requirement(two_pronged_attack)

                if can_activate:
                    while(1):
                        inp = input("P1: Activate Two-Pronged Attack (y/n): ")

                        if inp == "y":
                            print("Player 1 activates Two-Pronged Attack")
                            player1_st_zones[1] = None
                            activate_effect(two_pronged_attack, 1)
                            player1_grave.append(two_pronged_attack.card_name)
                            p1_st_set2 = None

                            break
                                            
                        else:
                            break

            elif p1_st_set2.card == dragon_capture_jar:
                while(1):
                    inp = input("P1: Activate Dragon Capture Jar (y/n): ")

                    if inp == "y":
                        print("Player 1 activates Dragon Capture Jar")
                        activate_effect(dragon_capture_jar, 1)
                        p1_st_set2 = None

                        break
                                            
                    else:
                        break

        elif p1_st_set3 != None:
            if p1_st_set3.card == trap_hole and has_faceup_monster(player2_monster_zones):
                can_activate = check_activation_requirement(trap_hole)

                if can_activate:
                    while(1):
                        inp = input("P1: Activate Trap Hole (y/n): ")

                        if inp == "y":
                            print("Player 1 activates Trap Hole")
                            player1_st_zones[2] = None
                            activate_effect(trap_hole, 2)
                            player1_grave.append(trap_hole.card_name)
                            p1_st_set3 = None

                            break
                                            
                        else:
                            break

            elif p1_st_set3.card == two_pronged_attack:
                can_activate = check_activation_requirement(two_pronged_attack)

                if can_activate:
                    while(1):
                        inp = input("P1: Activate Two-Pronged Attack (y/n): ")

                        if inp == "y":
                            print("Player 1 activates Two-Pronged Attack")
                            player1_st_zones[2] = None
                            activate_effect(two_pronged_attack, 2)
                            player1_grave.append(two_pronged_attack.card_name)
                            p1_st_set3 = None

                            break
                                            
                        else:
                            break

            elif p1_st_set3.card == dragon_capture_jar:
                while(1):
                    inp = input("P1: Activate Dragon Capture Jar (y/n): ")

                    if inp == "y":
                        print("Player 1 activates Dragon Capture Jar")
                        activate_effect(dragon_capture_jar, 2)
                        p1_st_set3 = None

                        break
                                            
                    else:
                        break

    elif player == 2:
        if p2_st_set1 != None:
            if p2_st_set1.card == trap_hole and has_faceup_monster(player1_monster_zones):
                can_activate = check_activation_requirement(trap_hole)

                if can_activate:
                    while(1):
                        inp = input("P2: Activate Trap Hole (y/n): ")

                        if inp == "y":
                            print("Player 2 activates Trap Hole")
                            player2_st_zones[0] = None
                            activate_effect(trap_hole, 0)
                            player2_grave.append(trap_hole.card_name)
                            p2_st_set1 = None

                            break
                                            
                        else:
                            break

            elif p2_st_set1.card == two_pronged_attack:
                can_activate = check_activation_requirement(two_pronged_attack)

                if can_activate:
                    while(1):
                        inp = input("P2: Activate Two-Pronged Attack (y/n): ")

                        if inp == "y":
                            print("Player 2 activates Two-Pronged Attack")
                            player2_st_zones[0] = None
                            activate_effect(two_pronged_attack, 0)
                            player2_grave.append(two_pronged_attack.card_name)
                            p2_st_set1 = None

                            break
                                            
                        else:
                            break

            elif p2_st_set1.card == dragon_capture_jar:
                while(1):
                    inp = input("P2: Activate Dragon Capture Jar (y/n): ")

                    if inp == "y":
                        print("Player 2 activates Dragon Capture Jar")
                        activate_effect(dragon_capture_jar, 0)
                        p2_st_set1 = None

                        break
                                            
                    else:
                        break

        elif p2_st_set2 != None:
            if p2_st_set2.card == trap_hole and has_faceup_monster(player1_monster_zones):
                can_activate = check_activation_requirement(trap_hole)

                if can_activate:
                    while(1):
                        inp = input("P2: Activate Trap Hole (y/n): ")

                        if inp == "y":
                            print("Player 2 activates Trap Hole")
                            player2_st_zones[1] = None
                            activate_effect(trap_hole, 1)
                            player2_grave.append(trap_hole.card_name)
                            p2_st_set2 = None

                            break
                                            
                        else:
                            break

            elif p2_st_set2.card == two_pronged_attack:
                can_activate = check_activation_requirement(two_pronged_attack)

                if can_activate:
                    while(1):
                        inp = input("P2: Activate Two-Pronged Attack (y/n): ")

                        if inp == "y":
                            print("Player 2 activates Two-Pronged Attack")
                            player2_st_zones[1] = None
                            activate_effect(two_pronged_attack, 1)
                            player2_grave.append(two_pronged_attack.card_name)
                            p2_st_set2 = None

                            break
                                            
                        else:
                            break

            elif p2_st_set2.card == dragon_capture_jar:
                while(1):
                    inp = input("P2: Activate Dragon Capture Jar (y/n): ")

                    if inp == "y":
                        print("Player 2 activates Dragon Capture Jar")
                        activate_effect(dragon_capture_jar, 1)
                        p2_st_set2 = None

                        break
                                            
                    else:
                        break

        elif p2_st_set3 != None:
            if p2_st_set3.card == trap_hole and has_faceup_monster(player1_monster_zones):
                can_activate = check_activation_requirement(trap_hole)

                if can_activate:
                    while(1):
                        inp = input("P2: Activate Trap Hole (y/n): ")

                        if inp == "y":
                            print("Player 2 activates Trap Hole")
                            player2_st_zones[2] = None
                            activate_effect(trap_hole, 2)
                            player2_grave.append(trap_hole.card_name)
                            p2_st_set3 = None

                            break
                                            
                        else:
                            break

            elif p2_st_set3.card == two_pronged_attack:
                can_activate = check_activation_requirement(two_pronged_attack)

                if can_activate:
                    while(1):
                        inp = input("P2: Activate Two-Pronged Attack (y/n): ")

                        if inp == "y":
                            print("Player 2 activates Two-Pronged Attack")
                            player2_st_zones[2] = None
                            activate_effect(two_pronged_attack, 2)
                            player2_grave.append(two_pronged_attack.card_name)
                            p2_st_set3 = None

                            break
                                            
                        else:
                            break

            elif p2_st_set3.card == dragon_capture_jar:
                while(1):
                    inp = input("P2: Activate Dragon Capture Jar (y/n): ")

                    if inp == "y":
                        print("Player 2 activates Dragon Capture Jar")
                        activate_effect(dragon_capture_jar, 2)
                        p2_st_set3 = None

                        break
                                            
                    else:
                        break

# Checks if the activation requirement for the effects of Monster/Spell/Trap cards are met. If the activation requirements are not met, the function returns False, which
# will cause the card to not be allowed to activate.
def check_activation_requirement(card):
    global curr_player

    if curr_player == 1:
        if player1_st_zones[0] != None and player1_st_zones[1] != None and player1_st_zones[2] != None:
            print("Cannot be activated since there is not an empty Spell/Trap zone.")
            return False

        elif card.sub_type == "Equip" and not has_monster(player1_monster_zones) and not has_defense_monster(player1_monster_zones) and not has_monster(player2_monster_zones) and not has_defense_monster(player2_monster_zones):
            print("Cannot be activated since there are no monsters.")
            return False

        elif card == dark_hole and not has_monster(player1_monster_zones) and not has_monster(player2_monster_zones):
            print("Cannot be activated since there are no monsters.")
            return False

        elif card == raigeki or card == fissure or card == stop_defense and not has_monster(player2_monster_zones):
            print("Cannot be activated since Player 2 controls no monsters.")
            return False

        elif card == polymerization and player1_extra == []:
            print("Cannot be activated since you have no Fusion monsters.")
            return False

        elif card == polymerization and not has_monster(player1_monster_zones) and not check_fusion_material(player1_hand.player_hand):
            print("Cannot be activated since you control no monsters.")
            return False

        elif card == stop_defense and not has_set_monster(player2_monster_zones) and not has_defense_monster(player2_monster_zones):
            print("Cannot be activated since Player 2 does not control a Defense Position monster.")
            return False

        elif card == gravedigger_ghoul and not monster_in_grave(player2_grave):
            print("Cannot be activated since Player 2 has no monsters in their Graveyard.")
            return False

        elif card == remove_trap and not has_trap(player2_st_zones):
            print("Cannot be activated since Player 2 has no Traps.")
            return False

        elif card == monster_reborn and not monster_in_grave(player1_grave) and not monster_in_grave(player2_grave):
            print("Cannot be activated since neither Graveyard contains a monster.")
            return False

        elif card == legendary_sword and not has_monster_type(player1_monster_zones, "Warrior") and not has_monster_type(player2_monster_zones, "Warrior"):
            print("Cannot be activated since there are no Warrior-Type monsters on the field.")
            return False

        elif card == beast_fangs and not has_monster_type(player1_monster_zones, "Beast") and not has_monster_type(player2_monster_zones, "Beast"):
            print("Cannot be activated since there are no Beast-Type monsters on the field.")
            return False

        elif card == violet_crystal and not has_monster_type(player1_monster_zones, "Zombie") and not has_monster_type(player2_monster_zones, "Zombie"):
            print("Cannot be activated since there are no Zombie-Type monsters on the field.")
            return False

        elif card == book_of_secret_arts and not has_monster_type(player1_monster_zones, "Spellcaster") and not has_monster_type(player2_monster_zones, "Spellcaster"):
            print("Cannot be activated since there are no Spellcaster-Type monsters on the field.")
            return False

        elif card == power_of_kaishin and not has_monster_type(player1_monster_zones, "Aqua") and not has_monster_type(player2_monster_zones, "Aqua"):
            print("Cannot be activated since there are no Aqua-Type monsters on the field.")
            return False

        elif card == dark_energy and not has_monster_type(player1_monster_zones, "Fiend") and not has_monster_type(player2_monster_zones, "Fiend"):
            print("Cannot be activated since there are no Fiend-Type monsters on the field.")
            return False

        elif card == laser_cannon_armor and not has_monster_type(player1_monster_zones, "Insect") and not has_monster_type(player2_monster_zones, "Insect"):
            print("Cannot be activated since there are no Insect-Type monsters on the field.")
            return False

        elif card == vile_germs and not has_monster_type(player1_monster_zones, "Plant") and not has_monster_type(player2_monster_zones, "Plant"):
            print("Cannot be activated since there are no Plant-Type monsters on the field.")
            return False

        elif card == silver_bow_and_arrow and not has_monster_type(player1_monster_zones, "Fairy") and not has_monster_type(player2_monster_zones, "Fairy"):
            print("Cannot be activated since there are no Fairy-Type monsters on the field.")
            return False

        elif card == dragon_treasure and not has_monster_type(player1_monster_zones, "Dragon") and not has_monster_type(player2_monster_zones, "Dragon"):
            print("Cannot be activated since there are no Dragon-Type monsters on the field.")
            return False

        elif card == electro_whip and not has_monster_type(player1_monster_zones, "Thunder") and not has_monster_type(player2_monster_zones, "Thunder"):
            print("Cannot be activated since there are no Thunder-Type monsters on the field.")
            return False

        elif card == mystical_moon and not has_monster_type(player1_monster_zones, "Beast-Warrior") and not has_monster_type(player2_monster_zones, "Beast-Warrior"):
            print("Cannot be activated since there are no Beast-Warrior-Type monsters on the field.")
            return False

        elif card == machine_conversion_factory and not has_monster_type(player1_monster_zones, "Machine") and not has_monster_type(player2_monster_zones, "Machine"):
            print("Cannot be activated since there are no Machine-Type monsters on the field.")
            return False

        elif card == raise_body_heat and not has_monster_type(player1_monster_zones, "Dinosaur") and not has_monster_type(player2_monster_zones, "Dinosaur"):
            print("Cannot be activated since there are no Dinosaur-Type monsters on the field.")
            return False

        elif card == follow_wind and not has_monster_type(player1_monster_zones, "Winged Beast") and not has_monster_type(player2_monster_zones, "Winged Beast"):
            print("Cannot be activated since there are no Winged Beast-Type monsters on the field.")
            return False

        elif card == reaper_of_the_cards and player1_st_zones == [None, None, None] and player2_st_zones == [None, None, None] and p1_field_zone == [] and p2_field_zone == []:
            print("Cannot activate Reaper of the Cards effect since there are no valid targets.")
            return False

        elif card == armed_ninja and player1_st_zones == [None, None, None] and player2_st_zones == [None, None, None] and p1_field_zone == [] and p2_field_zone == []:
            print("Cannot activate Armed Ninja effect since there are no valid targets.")
            return False

        elif card == trap_hole and (p2_just_summoned_zone1 == True and p2_monster1.attack < 1000) or (p2_just_summoned_zone2 == True and p2_monster2.attack < 1000) or (p2_just_summoned_zone3 == True and p2_monster3.attack < 1000):
            print("Cannot activate Trap Hole sinec there is no valid target.")
            return False

        elif card == two_pronged_attack and how_many_monsters(player1_monster_zones) < 2 or how_many_monsters(player2_monster_zones) < 1:
            print("Cannot activate Two-Pronged Attack since there are not enough Monsters.")
            return False

        else:
            return True

    elif curr_player == 2:
        if player2_st_zones[0] != None and player2_st_zones[1] != None and player2_st_zones[2] != None:
            print("Cannot be activated since there is not an empty Spell/Trap zone.")
            return False

        elif card == dark_hole and not has_monster(player1_monster_zones) and not has_monster(player2_monster_zones):
            print("Cannot be activated since there are no monsters.")
            return False

        elif card == raigeki or card == fissure or card == stop_defense and not has_monster(player1_monster_zones):
            print("Cannot be activated since Player 1 controls no monsters.")
            return False

        elif card == polymerization and player2_extra == []:
            print("Cannot be activated since you have no Fusion monsters.")
            return False

        elif card == polymerization and not has_monster(player2_monster_zones) and not check_fusion_material(player2_hand.player_hand):
            print("Cannot be activated since you control no monsters on the field and do not have the material in hand.")
            return False

        elif card == stop_defense and not has_set_monster(player1_monster_zones) and not has_defense_monster(player1_monster_zones):
                print("Cannot be activated since Player 1 does not control a Defense Position monster.")
                return False

        elif card == gravedigger_ghoul and not monster_in_grave(player1_grave):
            print("Cannot be activated since Player 1 has no monsters in their Graveyard.")
            return False

        elif card == remove_trap and not has_trap(player1_st_zones):
            print("Cannot be activated since Player 1 has no Traps.")
            return False

        elif card == monster_reborn and not monster_in_grave(player1_grave) and not monster_in_grave(player2_grave):
            print("Cannot be activated since neither Graveyard contains a monster.")
            return False

        elif card == legendary_sword and not has_monster_type(player1_monster_zones, "Warrior") and not has_monster_type(player2_monster_zones, "Warrior"):
            print("Cannot be activated since there are no Warrior-Type monsters on the field.")
            return False

        elif card == beast_fangs and not has_monster_type(player1_monster_zones, "Beast") and not has_monster_type(player2_monster_zones, "Beast"):
            print("Cannot be activated since there are no Beast-Type monsters on the field.")
            return False

        elif card == violet_crystal and not has_monster_type(player1_monster_zones, "Zombie") and not has_monster_type(player2_monster_zones, "Zombie"):
            print("Cannot be activated since there are no Zombie-Type monsters on the field.")
            return False

        elif card == book_of_secret_arts and not has_monster_type(player1_monster_zones, "Spellcaster") and not has_monster_type(player2_monster_zones, "Spellcaster"):
            print("Cannot be activated since there are no Spellcaster-Type monsters on the field.")
            return False

        elif card == power_of_kaishin and not has_monster_type(player1_monster_zones, "Aqua") and not has_monster_type(player2_monster_zones, "Aqua"):
            print("Cannot be activated since there are no Aqua-Type monsters on the field.")
            return False

        elif card == dark_energy and not has_monster_type(player1_monster_zones, "Fiend") and not has_monster_type(player2_monster_zones, "Fiend"):
            print("Cannot be activated since there are no Fiend-Type monsters on the field.")
            return False

        elif card == laser_cannon_armor and not has_monster_type(player1_monster_zones, "Insect") and not has_monster_type(player2_monster_zones, "Insect"):
            print("Cannot be activated since there are no Insect-Type monsters on the field.")
            return False

        elif card == vile_germs and not has_monster_type(player1_monster_zones, "Plant") and not has_monster_type(player2_monster_zones, "Plant"):
            print("Cannot be activated since there are no Plant-Type monsters on the field.")
            return False

        elif card == silver_bow_and_arrow and not has_monster_type(player1_monster_zones, "Fairy") and not has_monster_type(player2_monster_zones, "Fairy"):
            print("Cannot be activated since there are no Fairy-Type monsters on the field.")
            return False

        elif card == dragon_treasure and not has_monster_type(player1_monster_zones, "Dragon") and not has_monster_type(player2_monster_zones, "Dragon"):
            print("Cannot be activated since there are no Dragon-Type monsters on the field.")
            return False

        elif card == electro_whip and not has_monster_type(player1_monster_zones, "Thunder") and not has_monster_type(player2_monster_zones, "Thunder"):
            print("Cannot be activated since there are no Thunder-Type monsters on the field.")
            return False

        elif card == mystical_moon and not has_monster_type(player1_monster_zones, "Beast-Warrior") and not has_monster_type(player2_monster_zones, "Beast-Warrior"):
            print("Cannot be activated since there are no Beast-Warrior-Type monsters on the field.")
            return False

        elif card == machine_conversion_factory and not has_monster_type(player1_monster_zones, "Machine") and not has_monster_type(player2_monster_zones, "Machine"):
            print("Cannot be activated since there are no Machine-Type monsters on the field.")
            return False

        elif card == raise_body_heat and not has_monster_type(player1_monster_zones, "Dinosaur") and not has_monster_type(player2_monster_zones, "Dinosaur"):
            print("Cannot be activated since there are no Dinosaur-Type monsters on the field.")
            return False

        elif card == follow_wind and not has_monster_type(player1_monster_zones, "Winged Beast") and not has_monster_type(player2_monster_zones, "Winged Beast"):
            print("Cannot be activated since there are no Winged Beast-Type monsters on the field.")
            return False

        elif card == reaper_of_the_cards and player1_st_zones == [None, None, None] and player2_st_zones == [None, None, None] and p1_field_zone == [] and p2_field_zone == []:
            print("Cannot activate Reaper of the Cards effect since there are no valid targets.")
            return False

        elif card == armed_ninja and player1_st_zones == [None, None, None] and player2_st_zones == [None, None, None] and p1_field_zone == [] and p2_field_zone == []:
            print("Cannot activate Armed Ninja effect since there are no valid targets.")
            return False

        elif card == trap_hole and (p1_just_summoned_zone1 == True and p1_monster1.attack < 1000) or (p1_just_summoned_zone2 == True and p1_monster2.attack < 1000) or (p1_just_summoned_zone3 == True and p1_monster3.attack < 1000):
            print("Cannot activate Trap Hole sinec there is no valid target.")
            return False

        elif card == two_pronged_attack and how_many_monsters(player2_monster_zones) < 2 or how_many_monsters(player1_monster_zones) < 1:
            print("Cannot activate Two-Pronged Attack since there are not enough Monsters.")
            return False

        else:
            return True

# Checks if any of the possible win conditions have been met.
def check_win_conditions():
    if player1_lp <= 0 or player2_lp <= 0:
        return True

    if player1_deckout == True:
        return True

    if right_leg_exodia in player1_hand.player_hand and left_leg_exodia in player1_hand.player_hand and right_arm_exodia in player1_hand.player_hand and left_arm_exodia in player1_hand.player_hand and exodia_the_forbidden_one in player1_hand.player_hand:
        return True

    if player2_deckout == True:
        return True

    if right_leg_exodia in player2_hand.player_hand and left_leg_exodia in player2_hand.player_hand and right_arm_exodia in player2_hand.player_hand and left_arm_exodia in player2_hand.player_hand and exodia_the_forbidden_one in player2_hand.player_hand:
        return True

# Handles activating the effect of an Effect Monster, Spell, or Trap card when the player attempts to activate. Only activates if the conditions for activation are 
# correct.
def activate_effect(card, card_zone):
    global curr_player, curr_phase, player1_lp, player2_lp
    global p1_monster1, p1_monster2, p1_monster3
    global p2_monster1, p2_monster2, p2_monster3
    global p1_set1, p1_set2, p1_set3
    global p2_set1, p2_set2, p2_set3
    global p1_pair_monster_equip1, p1_pair_monster_equip2, p1_pair_monster_equip3
    global p2_pair_monster_equip1, p2_pair_monster_equip2, p2_pair_monster_equip3
    global p1_just_activated_field, p2_just_activated_field

    if (card == legendary_sword or card == beast_fangs or card == violet_crystal or card == book_of_secret_arts or card == power_of_kaishin
        or card == dark_energy or card == laser_cannon_armor or card == vile_germs or card == silver_bow_and_arrow or card == dragon_treasure
        or card == electro_whip or card == mystical_moon or card == machine_conversion_factory or card == raise_body_heat or card == follow_wind):
        if curr_player == 1:
            while(1):
                which_player = int(input("Target Your (1) or Opponent (2) Monster: "))

                if which_player == 1:
                    while(1):
                        target = int(input("Choose zone: "))

                        if player1_monster_zones[target-1] == None or player1_monster_zones[target-1] == "Set Card":
                            print("Not a valid target.")

                        else:
                            if target - 1 == 0:
                                p1_monster1.attack += 300
                                p1_monster1.defense += 300

                                if p1_pair_monster_equip1 == None:
                                    p1_pair_monster_equip1 = (p1_monster1, [card], [card_zone-1], which_player)

                                else:
                                    p1_pair_monster_equip1[1].append(card)
                                    p1_pair_monster_equip1[2].append(card_zone-1)

                                break

                            elif target - 1 == 1:
                                p1_monster2.attack += 300
                                p1_monster2.defense += 300
                                
                                if p1_pair_monster_equip2 == None:
                                    p1_pair_monster_equip2 = (p1_monster2, [card], [card_zone-1], which_player)

                                else:
                                    p1_pair_monster_equip2[1].append(card)
                                    p1_pair_monster_equip2[2].append(card_zone-1)

                                break

                            elif target - 1 == 2:
                                p1_monster3.attack += 300
                                p1_monster3.defense += 300
                                
                                if p1_pair_monster_equip3 == None:
                                    p1_pair_monster_equip3 = (p1_monster3, [card], [card_zone-1], which_player)

                                else:
                                    p1_pair_monster_equip3[1].append(card)
                                    p1_pair_monster_equip3[2].append(card_zone-1)

                                break

                    break

                elif which_player == 2:
                    while(1):
                        target = int(input("Choose zone: "))

                        if player2_monster_zones[target-1] == None or player2_monster_zones[target-1] == "Set Card":
                            print("Not a valid target.")

                        else:
                            if target - 1 == 0:
                                p2_monster1.attack += 300
                                p2_monster1.defense += 300
                                
                                if p1_pair_monster_equip1 == None:
                                    p1_pair_monster_equip1 = (p2_monster1, [card], [card_zone-1], which_player)

                                else:
                                    p1_pair_monster_equip1[1].append(card)
                                    p1_pair_monster_equip1[2].append(card_zone-1)

                                break

                            elif target - 1 == 1:
                                p2_monster2.attack += 300
                                p2_monster2.defense += 300
                               
                                if p1_pair_monster_equip2 == None:
                                    p1_pair_monster_equip2 = (p2_monster2, [card], [card_zone-1], which_player)

                                else:
                                    p1_pair_monster_equip2[1].append(card)
                                    p1_pair_monster_equip2[2].append(card_zone-1)

                                break

                            elif target - 1 == 2:
                                p2_monster3.attack += 300
                                p2_monster3.defense += 300
                                
                                if p1_pair_monster_equip3 == None:
                                    p1_pair_monster_equip3 = (p2_monster3, [card], [card_zone-1], which_player)

                                else:
                                    p1_pair_monster_equip3[1].append(card)
                                    p1_pair_monster_equip3[2].append(card_zone-1)

                                break

                    break
        
        elif curr_player == 2:
            while(1):
                which_player = int(input("Target Your (1) or Opponent (2) Monster: "))

                if which_player == 2:
                    while(1):
                        target = int(input("Choose zone: "))

                        if player1_monster_zones[target-1] == None or player1_monster_zones[target-1] == "Set Card":
                            print("Not a valid target.")

                        else:
                            if target - 1 == 0:
                                p1_monster1.attack += 300
                                p1_monster1.defense += 300

                                if p2_pair_monster_equip1 == None:
                                    p2_pair_monster_equip1 = (p1_monster1, [card], [card_zone-1], which_player)

                                else:
                                    p2_pair_monster_equip1[1].append(card)
                                    p2_pair_monster_equip1[2].append(card_zone-1)

                                break

                            elif target - 1 == 1:
                                p1_monster2.attack += 300
                                p1_monster2.defense += 300
                                
                                if p2_pair_monster_equip2 == None:
                                    p2_pair_monster_equip2 = (p1_monster2, [card], [card_zone-1], which_player)

                                else:
                                    p2_pair_monster_equip2[1].append(card)
                                    p2_pair_monster_equip2[2].append(card_zone-1)

                                break

                            elif target - 1 == 2:
                                p1_monster3.attack += 300
                                p1_monster3.defense += 300
                                
                                if p2_pair_monster_equip3 == None:
                                    p2_pair_monster_equip3 = (p1_monster3, [card], [card_zone-1], which_player)

                                else:
                                    p2_pair_monster_equip3[1].append(card)
                                    p2_pair_monster_equip3[2].append(card_zone-1)

                                break

                    break

                elif which_player == 1:
                    while(1):
                        target = int(input("Choose zone: "))

                        if player2_monster_zones[target-1] == None or player2_monster_zones[target-1] == "Set Card":
                            print("Not a valid target.")

                        else:
                            if target - 1 == 0:
                                p2_monster1.attack += 300
                                p2_monster1.defense += 300
                                
                                if p2_pair_monster_equip1 == None:
                                    p2_pair_monster_equip1 = (p2_monster1, [card], [card_zone-1], which_player)

                                else:
                                    p2_pair_monster_equip1[1].append(card)
                                    p2_pair_monster_equip1[2].append(card_zone-1)

                                break

                            elif target - 1 == 1:
                                p2_monster2.attack += 300
                                p2_monster2.defense += 300
                                
                                if p2_pair_monster_equip2 == None:
                                    p2_pair_monster_equip2 = (p2_monster2, [card], [card_zone-1], which_player)

                                else:
                                    p2_pair_monster_equip2[1].append(card)
                                    p2_pair_monster_equip2[2].append(card_zone-1)

                                break

                            elif target - 1 == 2:
                                p2_monster3.attack += 300
                                p2_monster3.defense += 300
                                
                                if p2_pair_monster_equip3 == None:
                                    p2_pair_monster_equip3 = (p2_monster3, [card], [card_zone-1], which_player)

                                else:
                                    p2_pair_monster_equip3[1].append(card)
                                    p2_pair_monster_equip3[2].append(card_zone-1)

                                break

                    break

    elif card == forest:
        if curr_player == 1:
            if p1_just_activated_field == True:
                if p1_monster1 != None:
                    if p1_monster1.monster_type == "Insect" or p1_monster1.monster_type == "Beast" or p1_monster1.monster_type == "Plant" or p1_monster1.monster_type == "Beast-Warrior":
                        p1_monster1.attack += 200
                        p1_monster1.defense += 200

                if p1_monster2 != None:
                    if p1_monster2.monster_type == "Insect" or p1_monster2.monster_type == "Beast" or p1_monster2.monster_type == "Plant" or p1_monster2.monster_type == "Beast-Warrior":
                        p1_monster2.attack += 200
                        p1_monster2.defense += 200

                if p1_monster3 != None:
                    if p1_monster3.monster_type == "Insect" or p1_monster3.monster_type == "Beast" or p1_monster3.monster_type == "Plant" or p1_monster3.monster_type == "Beast-Warrior":
                        p1_monster3.attack += 200
                        p1_monster3.defense += 200

                if p2_monster1 != None:
                    if p2_monster1.monster_type == "Insect" or p2_monster1.monster_type == "Beast" or p2_monster1.monster_type == "Plant" or p2_monster1.monster_type == "Beast-Warrior":
                        p2_monster1.attack += 200
                        p2_monster1.defense += 200

                if p2_monster2 != None:
                    if p2_monster2.monster_type == "Insect" or p2_monster2.monster_type == "Beast" or p2_monster2.monster_type == "Plant" or p2_monster2.monster_type == "Beast-Warrior":
                        p2_monster2.attack += 200
                        p2_monster2.defense += 200

                if p2_monster3 != None:
                    if p2_monster3.monster_type == "Insect" or p2_monster3.monster_type == "Beast" or p2_monster3.monster_type == "Plant" or p2_monster3.monster_type == "Beast-Warrior":
                        p2_monster3.attack += 200
                        p2_monster3.defense += 200

                p1_just_activated_field = False

        elif curr_player == 2:
            if p2_just_activated_field == True:
                if p1_monster1 != None:
                    if p1_monster1.monster_type == "Insect" or p1_monster1.monster_type == "Beast" or p1_monster1.monster_type == "Plant" or p1_monster1.monster_type == "Beast-Warrior":
                        p1_monster1.attack += 200
                        p1_monster1.defense += 200

                if p1_monster2 != None:
                    if p1_monster2.monster_type == "Insect" or p1_monster2.monster_type == "Beast" or p1_monster2.monster_type == "Plant" or p1_monster2.monster_type == "Beast-Warrior":
                        p1_monster2.attack += 200
                        p1_monster2.defense += 200

                if p1_monster3 != None:
                    if p1_monster3.monster_type == "Insect" or p1_monster3.monster_type == "Beast" or p1_monster3.monster_type == "Plant" or p1_monster3.monster_type == "Beast-Warrior":
                        p1_monster3.attack += 200
                        p1_monster3.defense += 200

                if p2_monster1 != None:
                    if p2_monster1.monster_type == "Insect" or p2_monster1.monster_type == "Beast" or p2_monster1.monster_type == "Plant" or p2_monster1.monster_type == "Beast-Warrior":
                        p2_monster1.attack += 200
                        p2_monster1.defense += 200

                if p2_monster2 != None:
                    if p2_monster2.monster_type == "Insect" or p2_monster2.monster_type == "Beast" or p2_monster2.monster_type == "Plant" or p2_monster2.monster_type == "Beast-Warrior":
                        p2_monster2.attack += 200
                        p2_monster2.defense += 200

                if p2_monster3 != None:
                    if p2_monster3.monster_type == "Insect" or p2_monster3.monster_type == "Beast" or p2_monster3.monster_type == "Plant" or p2_monster3.monster_type == "Beast-Warrior":
                        p2_monster3.attack += 200
                        p2_monster3.defense += 200

                p2_just_activated_field = False 

    elif card == wasteland:
        return

    elif card == mountain:
        return

    elif card == sogen:
        return

    elif card == umi:
        return

    elif card == yami:
        return

    elif card == dark_hole:
        index = 0
        for i in player1_monster_zones:
            if i != None:
                player1_grave.append(i)

            player1_monster_zones[index] = None
            index += 1

        index = 0
        for i in player2_monster_zones:
            if i != None:
                player2_grave.append(i)

            player2_monster_zones[index] = None
            index += 1

    elif card == raigeki:
        if curr_player == 1:
            index = 0
            for i in player2_monster_zones:
                if i != None:
                    player2_grave.append(i)

                player2_monster_zones[index] = None
                index += 1

        elif curr_player == 2:
            index = 0
            for i in player1_monster_zones:
                if i != None:
                    player1_grave.append(i)

                player1_monster_zones[index] = None
                index += 1

    elif card == red_medicine:
        if curr_player == 1:
            player1_lp += 500
            print("Player 1 LP: " + str(player1_lp))

        elif curr_player == 2:
            player2_lp += 500
            print("Player 2 LP: " + str(player2_lp))

    elif card == sparks:
        if curr_player == 1:
            player2_lp -= 200
            print("Player 2 LP: " + str(player2_lp))

        elif curr_player == 2:
            player1_lp -= 200
            print("Player 1 LP: " + str(player1_lp))

    elif card == hinotama:
        if curr_player == 1:
            player2_lp -= 500
            print("Player 2 LP: " + str(player2_lp))

        elif curr_player == 2:
            player1_lp -= 500
            print("Player 1 LP: " + str(player1_lp))

    elif card == fissure:
        if curr_player == 1:
            p2_card1 = get_card(player2_monster_zones[0])
            p2_card2 = get_card(player2_monster_zones[1])
            p2_card3 = get_card(player2_monster_zones[2])

            p2_card1_attack = 0
            p2_card2_attack = 0
            p2_card3_attack = 0

            if p2_card1 == None:
                p2_card1_attack = 9999
            else:
                p2_card1_attack = p2_card1.attack

            if p2_card2 == None:
                p2_card2_attack = 9999
            else:
                p2_card2_attack = p2_card2.attack

            if p2_card3 == None:
                p2_card3_attack = 9999
            else:
                p2_card3_attack = p2_card3.attack

            list_of_attacks = [p2_card1_attack, p2_card2_attack, p2_card3_attack]

            target = min(list_of_attacks)

            list_of_targets = [index for index in range(len(list_of_attacks)) if list_of_attacks[index] == target]

            if len(list_of_targets) < 2:
                player2_grave.append(player2_monster_zones[list_of_targets[0]])
                player2_monster_zones[list_of_targets[0]] = None

            else:
                while(1):
                    action = int(input("Choose monster to destroy: "))

                    if action - 1 not in list_of_targets:
                        print("Not a valid choice.")

                    else:
                        player2_grave.append(player2_monster_zones[action-1])
                        player2_monster_zones[action-1] = None
                        break

        elif curr_player == 2:
            p1_card1 = get_card(player1_monster_zones[0])
            p1_card2 = get_card(player1_monster_zones[1])
            p1_card3 = get_card(player1_monster_zones[2])

            p2_card1_attack = 0
            p2_card2_attack = 0
            p2_card3_attack = 0

            if p2_card1 == None:
                p2_card1_attack = 9999
            else:
                p2_card1_attack = p2_card1.attack

            if p2_card2 == None:
                p2_card2_attack = 9999
            else:
                p2_card2_attack = p2_card2.attack

            if p2_card3 == None:
                p2_card3_attack = 9999
            else:
                p2_card3_attack = p2_card3.attack

            list_of_attacks = [p2_card1_attack, p2_card2_attack, p2_card3_attack]

            target = min(list_of_attacks)

            list_of_targets = [index for index in range(len(list_of_attacks)) if list_of_attacks[index] == target]

            if len(list_of_targets) < 2:
                player1_grave.append(player1_monster_zones[list_of_targets[0]])
                player1_monster_zones[list_of_targets[0]] = None

            else:
                while(1):
                    action = int(input("Choose monster to destroy: "))

                    if action - 1 not in list_of_targets:
                        print("Not a valid choice.")

                    else:
                        player1_grave.append(player1_monster_zones[action-1])
                        player1_monster_zones[action-1] = None
                        break          

    elif card == polymerization:
        if curr_player == 1:
            while(1):
                view_extra(1)

                fusion = input("Choose Monster to Summon: ")

                if fusion == "Flame Swordsman":
                    if (flame_manipulator in player1_hand.player_hand or flame_manipulator in player1_monster_zones) and (masaki_the_legendary_swordsman in player1_hand.player_hand or masaki_the_legendary_swordsman in player1_monster_zones) and flame_swordsman in player1_extra:
                        if flame_manipulator in player1_hand.player_hand and flame_manipulator in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(flame_manipulator)

                                elif action == "field":
                                    index = player1_monster_zones.index(flame_manipulator.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif flame_manipulator in player1_hand.player_hand:
                            player1_hand.player_hand.remove(flame_manipulator)

                        elif flame_manipulator in player1_monster_zones:
                            index = player1_monster_zones.index(flame_manipulator.card_name)
                            player1_monster_zones[index] = None

                        if masaki_the_legendary_swordsman in player1_hand.player_hand and masaki_the_legendary_swordsman in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(masaki_the_legendary_swordsman)

                                elif action == "field":
                                    index = player1_monster_zones.index(masaki_the_legendary_swordsman.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif masaki_the_legendary_swordsman in player1_hand.player_hand:
                            player1_hand.player_hand.remove(masaki_the_legendary_swordsman)

                        elif masaki_the_legendary_swordsman in player1_monster_zones:
                            index = player1_monster_zones.index(masaki_the_legendary_swordsman.card_name)
                            player1_monster_zones[index] = None

                        player1_grave.append(flame_manipulator)
                        player1_grave.append(masaki_the_legendary_swordsman)

                        zone = int(input("Choose zone for Flame Swordsman: "))

                        player1_extra.remove(flame_swordsman)
                        player1_monster_zones[zone-1] = flame_swordsman.card_name
                        break

                elif fusion == "Charubin the Fire Knight":
                    if (monster_egg in player1_hand.player_hand or monster_egg in player1_monster_zones) and (hinotama_soul in player1_hand.player_hand or hinotama_soul in player1_monster_zones) and charubin_the_fire_knight in player1_extra:
                        if monster_egg in player1_hand.player_hand and monster_egg in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(monster_egg)

                                elif action == "field":
                                    index = player1_monster_zones.index(monster_egg.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif monster_egg in player1_hand.player_hand:
                            player1_hand.player_hand.remove(monster_egg)

                        elif monster_egg in player1_monster_zones:
                            index = player1_monster_zones.index(monster_egg.card_name)
                            player1_monster_zones[index] = None

                        if hinotama_soul in player1_hand.player_hand and hinotama_soul in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(hinotama_soul)

                                elif action == "field":
                                    index = player1_monster_zones.index(hinotama_soul.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif hinotama_soul in player1_hand.player_hand:
                            player1_hand.player_hand.remove(hinotama_soul)

                        elif hinotama_soul in player1_monster_zones:
                            index = player1_monster_zones.index(hinotama_soul.card_name)
                            player1_monster_zones[index] = None

                        player1_grave.append(monster_egg)
                        player1_grave.append(hinotama_soul)

                        zone = int(input("Choose zone for Charubin the Fire Knight: "))

                        player1_extra.remove(charubin_the_fire_knight)
                        player1_monster_zones[zone-1] = charubin_the_fire_knight.card_name
                        break

                elif fusion == "Darkfire Dragon":
                    if (firegrass in player1_hand.player_hand or firegrass in player1_monster_zones) and (petit_dragon in player1_hand.player_hand or petit_dragon in player1_monster_zones) and darkfire_dragon in player1_extra:
                        if firegrass in player1_hand.player_hand and firegrass in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(firegrass)

                                elif action == "field":
                                    index = player1_monster_zones.index(firegrass.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif firegrass in player1_hand.player_hand:
                            player1_hand.player_hand.remove(firegrass)

                        elif firegrass in player1_monster_zones:
                            index = player1_monster_zones.index(firegrass.card_name)
                            player1_monster_zones[index] = None

                        if petit_dragon in player1_hand.player_hand and petit_dragon in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(petit_dragon)

                                elif action == "field":
                                    index = player1_monster_zones.index(petit_dragon.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif petit_dragon in player1_hand.player_hand:
                            player1_hand.player_hand.remove(petit_dragon)

                        elif petit_dragon in player1_monster_zones:
                            index = player1_monster_zones.index(petit_dragon.card_name)
                            player1_monster_zones[index] = None

                        player1_grave.append(firegrass)
                        player1_grave.append(petit_dragon)

                        zone = int(input("Choose zone for Darkfire Dragon: "))

                        player1_extra.remove(darkfire_dragon)
                        player1_monster_zones[zone-1] = darkfire_dragon.card_name
                        break

                elif fusion == "Fusionist":
                    if (petit_angel in player1_hand.player_hand or petit_angel in player1_monster_zones) and (mystical_sheep_2 in player1_hand.player_hand or mystical_sheep_2 in player1_monster_zones) and fusionist in player1_extra:
                        if petit_angel in player1_hand.player_hand and petit_angel in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(petit_angel)

                                elif action == "field":
                                    index = player1_monster_zones.index(petit_angel.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif petit_angel in player1_hand.player_hand:
                            player1_hand.player_hand.remove(petit_angel)

                        elif petit_angel in player1_monster_zones:
                            index = player1_monster_zones.index(petit_angel.card_name)
                            player1_monster_zones[index] = None

                        if mystical_sheep_2 in player1_hand.player_hand and mystical_sheep_2 in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(mystical_sheep_2)

                                elif action == "field":
                                    index = player1_monster_zones.index(mystical_sheep_2.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif mystical_sheep_2 in player1_hand.player_hand:
                            player1_hand.player_hand.remove(mystical_sheep_2)

                        elif mystical_sheep_2 in player1_monster_zones:
                            index = player1_monster_zones.index(mystical_sheep_2.card_name)
                            player1_monster_zones[index] = None

                        player1_grave.append(petit_angel)
                        player1_grave.append(mystical_sheep_2)

                        zone = int(input("Choose zone for Fusionist: "))

                        player1_extra.remove(fusionist)
                        player1_monster_zones[zone-1] = fusionist.card_name
                        break

                elif fusion == "Flame Ghost":
                    if (skull_servant in player1_hand.player_hand or skull_servant in player1_monster_zones) and (dissolverock in player1_hand.player_hand or dissolverock in player1_monster_zones) and flame_ghost in player1_extra:
                        if skull_servant in player1_hand.player_hand and skull_servant in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(skull_servant)

                                elif action == "field":
                                    index = player1_monster_zones.index(skull_servant.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif skull_servant in player1_hand.player_hand:
                            player1_hand.player_hand.remove(skull_servant)

                        elif skull_servant in player1_monster_zones:
                            index = player1_monster_zones.index(skull_servant.card_name)
                            player1_monster_zones[index] = None

                        if dissolverock in player1_hand.player_hand and dissolverock in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(dissolverock)

                                elif action == "field":
                                    index = player1_monster_zones.index(dissolverock.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif dissolverock in player1_hand.player_hand:
                            player1_hand.player_hand.remove(dissolverock)

                        elif dissolverock in player1_monster_zones:
                            index = player1_monster_zones.index(dissolverock.card_name)
                            player1_monster_zones[index] = None

                        player1_grave.append(skull_servant)
                        player1_grave.append(dissolverock)

                        zone = int(input("Choose zone for Flame Ghost: "))

                        player1_extra.remove(flame_ghost)
                        player1_monster_zones[zone-1] = flame_ghost.card_name
                        break

                elif fusion == "Karbonala Warrior":
                    if (m_warrior_1 in player1_hand.player_hand or m_warrior_1 in player1_monster_zones) and (m_warrior_2 in player1_hand.player_hand or m_warrior_2 in player1_monster_zones) and karbonala_warrior in player1_extra:
                        if m_warrior_1 in player1_hand.player_hand and m_warrior_1 in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(m_warrior_1)

                                elif action == "field":
                                    index = player1_monster_zones.index(m_warrior_1.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif m_warrior_1 in player1_hand.player_hand:
                            player1_hand.player_hand.remove(m_warrior_1)

                        elif m_warrior_1 in player1_monster_zones:
                            index = player1_monster_zones.index(m_warrior_1.card_name)
                            player1_monster_zones[index] = None

                        if m_warrior_2 in player1_hand.player_hand and m_warrior_2 in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(m_warrior_2)

                                elif action == "field":
                                    index = player1_monster_zones.index(m_warrior_2.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif m_warrior_2 in player1_hand.player_hand:
                            player1_hand.player_hand.remove(m_warrior_2)

                        elif m_warrior_2 in player1_monster_zones:
                            index = player1_monster_zones.index(m_warrior_2.card_name)
                            player1_monster_zones[index] = None

                        player1_grave.append(m_warrior_1)
                        player1_grave.append(m_warrior_2)

                        zone = int(input("Choose zone for Karbonala Warrior: "))

                        player1_extra.remove(karbonala_warrior)
                        player1_monster_zones[zone-1] = karbonala_warrior.card_name
                        break

                elif fusion == "Dragoness the Wicked Knight":
                    if (armaill in player1_hand.player_hand or armaill in player1_monster_zones) and (one_eyed_shield_dragon in player1_hand.player_hand or one_eyed_shield_dragon in player1_monster_zones) and dragoness_the_wicked_knight in player1_extra:
                        if armaill in player1_hand.player_hand and armaill in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(armaill)

                                elif action == "field":
                                    index = player1_monster_zones.index(armaill.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif armaill in player1_hand.player_hand:
                            player1_hand.player_hand.remove(armaill)

                        elif armaill in player1_monster_zones:
                            index = player1_monster_zones.index(armaill.card_name)
                            player1_monster_zones[index] = None

                        if one_eyed_shield_dragon in player1_hand.player_hand and one_eyed_shield_dragon in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(one_eyed_shield_dragon)

                                elif action == "field":
                                    index = player1_monster_zones.index(one_eyed_shield_dragon.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif one_eyed_shield_dragon in player1_hand.player_hand:
                            player1_hand.player_hand.remove(one_eyed_shield_dragon)

                        elif one_eyed_shield_dragon in player1_monster_zones:
                            index = player1_monster_zones.index(one_eyed_shield_dragon.card_name)
                            player1_monster_zones[index] = None

                        player1_grave.append(armaill)
                        player1_grave.append(one_eyed_shield_dragon)

                        zone = int(input("Choose zone for Dragoness the Wicked Knight: "))

                        player1_extra.remove(dragoness_the_wicked_knight)
                        player1_monster_zones[zone-1] = dragoness_the_wicked_knight.card_name
                        break

                elif fusion == "Metal Dragon":
                    if (steel_ogre_grotto_1 in player1_hand.player_hand or steel_ogre_grotto_1 in player1_monster_zones) and (lesser_dragon in player1_hand.player_hand or lesser_dragon in player1_monster_zones) and metal_dragon in player1_extra:
                        if steel_ogre_grotto_1 in player1_hand.player_hand and steel_ogre_grotto_1 in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(steel_ogre_grotto_1)

                                elif action == "field":
                                    index = player1_monster_zones.index(steel_ogre_grotto_1.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif steel_ogre_grotto_1 in player1_hand.player_hand:
                            player1_hand.player_hand.remove(steel_ogre_grotto_1)

                        elif steel_ogre_grotto_1 in player1_monster_zones:
                            index = player1_monster_zones.index(steel_ogre_grotto_1.card_name)
                            player1_monster_zones[index] = None

                        if lesser_dragon in player1_hand.player_hand and lesser_dragon in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(lesser_dragon)

                                elif action == "field":
                                    index = player1_monster_zones.index(lesser_dragon.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif lesser_dragon in player1_hand.player_hand:
                            player1_hand.player_hand.remove(lesser_dragon)

                        elif lesser_dragon in player1_monster_zones:
                            index = player1_monster_zones.index(lesser_dragon.card_name)
                            player1_monster_zones[index] = None

                        player1_grave.append(steel_ogre_grotto_1)
                        player1_grave.append(lesser_dragon)

                        zone = int(input("Choose zone for Metal Dragon: "))

                        player1_extra.remove(metal_dragon)
                        player1_monster_zones[zone-1] = metal_dragon.card_name
                        break

                elif fusion == "Flower Wolf":
                    if (silver_fang in player1_hand.player_hand or silver_fang in player1_monster_zones) and (darkworld_thorns in player1_hand.player_hand or darkworld_thorns in player1_monster_zones) and flower_wolf in player1_extra:
                        if silver_fang in player1_hand.player_hand and silver_fang in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(silver_fang)

                                elif action == "field":
                                    index = player1_monster_zones.index(silver_fang.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif silver_fang in player1_hand.player_hand:
                            player1_hand.player_hand.remove(silver_fang)

                        elif silver_fang in player1_monster_zones:
                            index = player1_monster_zones.index(silver_fang.card_name)
                            player1_monster_zones[index] = None

                        if darkworld_thorns in player1_hand.player_hand and darkworld_thorns in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(darkworld_thorns)

                                elif action == "field":
                                    index = player1_monster_zones.index(darkworld_thorns.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif darkworld_thorns in player1_hand.player_hand:
                            player1_hand.player_hand.remove(darkworld_thorns)

                        elif darkworld_thorns in player1_monster_zones:
                            index = player1_monster_zones.index(darkworld_thorns.card_name)
                            player1_monster_zones[index] = None

                        player1_grave.append(silver_fang)
                        player1_grave.append(darkworld_thorns)

                        zone = int(input("Choose zone for Flower Wolf: "))

                        player1_extra.remove(flower_wolf)
                        player1_monster_zones[zone-1] = flower_wolf.card_name
                        break

                elif fusion == "Gaia the Dragon Champion":
                    if (gaia_the_fierce_knight in player1_hand.player_hand or gaia_the_fierce_knight in player1_monster_zones) and (curse_of_dragon in player1_hand.player_hand or curse_of_dragon in player1_monster_zones) and gaia_the_dragon_champion in player1_extra:
                        if gaia_the_fierce_knight in player1_hand.player_hand and gaia_the_fierce_knight in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(gaia_the_fierce_knight)

                                elif action == "field":
                                    index = player1_monster_zones.index(gaia_the_fierce_knight.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif gaia_the_fierce_knight in player1_hand.player_hand:
                            player1_hand.player_hand.remove(gaia_the_fierce_knight)

                        elif gaia_the_fierce_knight in player1_monster_zones:
                            index = player1_monster_zones.index(gaia_the_fierce_knight.card_name)
                            player1_monster_zones[index] = None

                        if curse_of_dragon in player1_hand.player_hand and curse_of_dragon in player1_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player1_hand.player_hand.remove(curse_of_dragon)

                                elif action == "field":
                                    index = player1_monster_zones.index(curse_of_dragon.card_name)
                                    player1_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif curse_of_dragon in player1_hand.player_hand:
                            player1_hand.player_hand.remove(curse_of_dragon)

                        elif curse_of_dragon in player1_monster_zones:
                            index = player1_monster_zones.index(curse_of_dragon.card_name)
                            player1_monster_zones[index] = None

                        player1_grave.append(gaia_the_fierce_knight)
                        player1_grave.append(curse_of_dragon)

                        zone = int(input("Choose zone for Gaia the Dragon Champion: "))

                        player1_extra.remove(gaia_the_dragon_champion)
                        player1_monster_zones[zone-1] = gaia_the_dragon_champion.card_name
                        break

                else:
                    print("Not a valid Fusion target.")

        elif curr_player == 2:
            while(1):
                view_extra(2)

                fusion = input("Choose Monster to Summon: ")

                if fusion == "Flame Swordsman":
                    if (flame_manipulator in player2_hand.player_hand or flame_manipulator in player2_monster_zones) and (masaki_the_legendary_swordsman in player2_hand.player_hand or masaki_the_legendary_swordsman in player2_monster_zones) and flame_swordsman in player2_extra:
                        if flame_manipulator in player2_hand.player_hand and flame_manipulator in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(flame_manipulator)

                                elif action == "field":
                                    index = player2_monster_zones.index(flame_manipulator.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif flame_manipulator in player2_hand.player_hand:
                            player2_hand.player_hand.remove(flame_manipulator)

                        elif flame_manipulator in player2_monster_zones:
                            index = player2_monster_zones.index(flame_manipulator.card_name)
                            player2_monster_zones[index] = None

                        if masaki_the_legendary_swordsman in player2_hand.player_hand and masaki_the_legendary_swordsman in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(masaki_the_legendary_swordsman)

                                elif action == "field":
                                    index = player2_monster_zones.index(masaki_the_legendary_swordsman.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif masaki_the_legendary_swordsman in player2_hand.player_hand:
                            player2_hand.player_hand.remove(masaki_the_legendary_swordsman)

                        elif masaki_the_legendary_swordsman in player2_monster_zones:
                            index = player2_monster_zones.index(masaki_the_legendary_swordsman.card_name)
                            player2_monster_zones[index] = None

                        player2_grave.append(flame_manipulator)
                        player2_grave.append(masaki_the_legendary_swordsman)

                        zone = int(input("Choose zone for Flame Swordsman: "))

                        player2_extra.remove(flame_swordsman)
                        player2_monster_zones[zone-1] = flame_swordsman.card_name
                        break

                elif fusion == "Charubin the Fire Knight":
                    if (monster_egg in player2_hand.player_hand or monster_egg in player2_monster_zones) and (hinotama_soul in player2_hand.player_hand or hinotama_soul in player2_monster_zones) and charubin_the_fire_knight in player2_extra:
                        if monster_egg in player2_hand.player_hand and monster_egg in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(monster_egg)

                                elif action == "field":
                                    index = player2_monster_zones.index(monster_egg.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif monster_egg in player2_hand.player_hand:
                            player2_hand.player_hand.remove(monster_egg)

                        elif monster_egg in player2_monster_zones:
                            index = player2_monster_zones.index(monster_egg.card_name)
                            player2_monster_zones[index] = None

                        if hinotama_soul in player2_hand.player_hand and hinotama_soul in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(hinotama_soul)

                                elif action == "field":
                                    index = player2_monster_zones.index(hinotama_soul.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif hinotama_soul in player2_hand.player_hand:
                            player2_hand.player_hand.remove(hinotama_soul)

                        elif hinotama_soul in player2_monster_zones:
                            index = player2_monster_zones.index(hinotama_soul.card_name)
                            player2_monster_zones[index] = None

                        player2_grave.append(monster_egg)
                        player2_grave.append(hinotama_soul)

                        zone = int(input("Choose zone for Charubin the Fire Knight: "))

                        player2_extra.remove(charubin_the_fire_knight)
                        player2_monster_zones[zone-1] = charubin_the_fire_knight.card_name
                        break

                elif fusion == "Darkfire Dragon":
                    if (firegrass in player2_hand.player_hand or firegrass in player2_monster_zones) and (petit_dragon in player2_hand.player_hand or petit_dragon in player2_monster_zones) and darkfire_dragon in player2_extra:
                        if firegrass in player2_hand.player_hand and firegrass in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(firegrass)

                                elif action == "field":
                                    index = player2_monster_zones.index(firegrass.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif firegrass in player2_hand.player_hand:
                            player2_hand.player_hand.remove(firegrass)

                        elif firegrass in player2_monster_zones:
                            index = player2_monster_zones.index(firegrass.card_name)
                            player2_monster_zones[index] = None

                        if petit_dragon in player2_hand.player_hand and petit_dragon in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(petit_dragon)

                                elif action == "field":
                                    index = player2_monster_zones.index(petit_dragon.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif petit_dragon in player2_hand.player_hand:
                            player2_hand.player_hand.remove(petit_dragon)

                        elif petit_dragon in player2_monster_zones:
                            index = player2_monster_zones.index(petit_dragon.card_name)
                            player2_monster_zones[index] = None

                        player2_grave.append(firegrass)
                        player2_grave.append(petit_dragon)

                        zone = int(input("Choose zone for Darkfire Dragon: "))

                        player2_extra.remove(darkfire_dragon)
                        player2_monster_zones[zone-1] = darkfire_dragon.card_name
                        break

                elif fusion == "Fusionist":
                    if (petit_angel in player2_hand.player_hand or petit_angel in player2_monster_zones) and (mystical_sheep_2 in player2_hand.player_hand or mystical_sheep_2 in player2_monster_zones) and fusionist in player2_extra:
                        if petit_angel in player2_hand.player_hand and petit_angel in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(petit_angel)

                                elif action == "field":
                                    index = player2_monster_zones.index(petit_angel.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif petit_angel in player2_hand.player_hand:
                            player2_hand.player_hand.remove(petit_angel)

                        elif petit_angel in player2_monster_zones:
                            index = player2_monster_zones.index(petit_angel.card_name)
                            player2_monster_zones[index] = None

                        if mystical_sheep_2 in player2_hand.player_hand and mystical_sheep_2 in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(mystical_sheep_2)

                                elif action == "field":
                                    index = player2_monster_zones.index(mystical_sheep_2.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif mystical_sheep_2 in player2_hand.player_hand:
                            player2_hand.player_hand.remove(mystical_sheep_2)

                        elif mystical_sheep_2 in player2_monster_zones:
                            index = player2_monster_zones.index(mystical_sheep_2.card_name)
                            player2_monster_zones[index] = None

                        player2_grave.append(petit_angel)
                        player2_grave.append(mystical_sheep_2)

                        zone = int(input("Choose zone for Fusionist: "))

                        player2_extra.remove(fusionist)
                        player2_monster_zones[zone-1] = fusionist.card_name
                        break

                elif fusion == "Flame Ghost":
                    if (skull_servant in player2_hand.player_hand or skull_servant in player2_monster_zones) and (dissolverock in player2_hand.player_hand or dissolverock in player2_monster_zones) and flame_ghost in player2_extra:
                        if skull_servant in player2_hand.player_hand and skull_servant in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(skull_servant)

                                elif action == "field":
                                    index = player2_monster_zones.index(skull_servant.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif skull_servant in player2_hand.player_hand:
                            player2_hand.player_hand.remove(skull_servant)

                        elif skull_servant in player2_monster_zones:
                            index = player2_monster_zones.index(skull_servant.card_name)
                            player2_monster_zones[index] = None

                        if dissolverock in player2_hand.player_hand and dissolverock in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(dissolverock)

                                elif action == "field":
                                    index = player2_monster_zones.index(dissolverock.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif dissolverock in player2_hand.player_hand:
                            player2_hand.player_hand.remove(dissolverock)

                        elif dissolverock in player2_monster_zones:
                            index = player2_monster_zones.index(dissolverock.card_name)
                            player2_monster_zones[index] = None

                        player2_grave.append(skull_servant)
                        player2_grave.append(dissolverock)

                        zone = int(input("Choose zone for Flame Ghost: "))

                        player2_extra.remove(flame_ghost)
                        player2_monster_zones[zone-1] = flame_ghost.card_name
                        break

                elif fusion == "Karbonala Warrior":
                    if (m_warrior_1 in player2_hand.player_hand or m_warrior_1 in player2_monster_zones) and (m_warrior_2 in player2_hand.player_hand or m_warrior_2 in player2_monster_zones) and karbonala_warrior in player2_extra:
                        if m_warrior_1 in player2_hand.player_hand and m_warrior_1 in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(m_warrior_1)

                                elif action == "field":
                                    index = player2_monster_zones.index(m_warrior_1.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif m_warrior_1 in player2_hand.player_hand:
                            player2_hand.player_hand.remove(m_warrior_1)

                        elif m_warrior_1 in player2_monster_zones:
                            index = player2_monster_zones.index(m_warrior_1.card_name)
                            player2_monster_zones[index] = None

                        if m_warrior_2 in player2_hand.player_hand and m_warrior_2 in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(m_warrior_2)

                                elif action == "field":
                                    index = player2_monster_zones.index(m_warrior_2.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif m_warrior_2 in player2_hand.player_hand:
                            player2_hand.player_hand.remove(m_warrior_2)

                        elif m_warrior_2 in player2_monster_zones:
                            index = player2_monster_zones.index(m_warrior_2.card_name)
                            player2_monster_zones[index] = None

                        player2_grave.append(m_warrior_1)
                        player2_grave.append(m_warrior_2)

                        zone = int(input("Choose zone for Karbonala Warrior: "))

                        player2_extra.remove(karbonala_warrior)
                        player2_monster_zones[zone-1] = karbonala_warrior.card_name
                        break

                elif fusion == "Dragoness the Wicked Knight":
                    if (armaill in player2_hand.player_hand or armaill in player2_monster_zones) and (one_eyed_shield_dragon in player2_hand.player_hand or one_eyed_shield_dragon in player2_monster_zones) and dragoness_the_wicked_knight in player2_extra:
                        if armaill in player2_hand.player_hand and armaill in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(armaill)

                                elif action == "field":
                                    index = player2_monster_zones.index(armaill.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif armaill in player2_hand.player_hand:
                            player2_hand.player_hand.remove(armaill)

                        elif armaill in player2_monster_zones:
                            index = player2_monster_zones.index(armaill.card_name)
                            player2_monster_zones[index] = None

                        if one_eyed_shield_dragon in player2_hand.player_hand and one_eyed_shield_dragon in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(one_eyed_shield_dragon)

                                elif action == "field":
                                    index = player2_monster_zones.index(one_eyed_shield_dragon.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif one_eyed_shield_dragon in player2_hand.player_hand:
                            player2_hand.player_hand.remove(one_eyed_shield_dragon)

                        elif one_eyed_shield_dragon in player2_monster_zones:
                            index = player2_monster_zones.index(one_eyed_shield_dragon.card_name)
                            player2_monster_zones[index] = None

                        player2_grave.append(armaill)
                        player2_grave.append(one_eyed_shield_dragon)

                        zone = int(input("Choose zone for Dragoness the Wicked Knight: "))

                        player2_extra.remove(dragoness_the_wicked_knight)
                        player2_monster_zones[zone-1] = dragoness_the_wicked_knight.card_name
                        break

                elif fusion == "Metal Dragon":
                    if (steel_ogre_grotto_1 in player2_hand.player_hand or steel_ogre_grotto_1 in player2_monster_zones) and (lesser_dragon in player2_hand.player_hand or lesser_dragon in player2_monster_zones) and metal_dragon in player2_extra:
                        if steel_ogre_grotto_1 in player2_hand.player_hand and steel_ogre_grotto_1 in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(steel_ogre_grotto_1)

                                elif action == "field":
                                    index = player2_monster_zones.index(steel_ogre_grotto_1.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif steel_ogre_grotto_1 in player2_hand.player_hand:
                            player2_hand.player_hand.remove(steel_ogre_grotto_1)

                        elif steel_ogre_grotto_1 in player2_monster_zones:
                            index = player2_monster_zones.index(steel_ogre_grotto_1.card_name)
                            player2_monster_zones[index] = None

                        if lesser_dragon in player2_hand.player_hand and lesser_dragon in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(lesser_dragon)

                                elif action == "field":
                                    index = player2_monster_zones.index(lesser_dragon.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif lesser_dragon in player2_hand.player_hand:
                            player2_hand.player_hand.remove(lesser_dragon)

                        elif lesser_dragon in player2_monster_zones:
                            index = player2_monster_zones.index(lesser_dragon.card_name)
                            player2_monster_zones[index] = None

                        player2_grave.append(steel_ogre_grotto_1)
                        player2_grave.append(lesser_dragon)

                        zone = int(input("Choose zone for Metal Dragon: "))

                        player2_extra.remove(metal_dragon)
                        player2_monster_zones[zone-1] = metal_dragon.card_name
                        break

                elif fusion == "Flower Wolf":
                    if (silver_fang in player2_hand.player_hand or silver_fang in player2_monster_zones) and (darkworld_thorns in player2_hand.player_hand or darkworld_thorns in player2_monster_zones) and flower_wolf in player2_extra:
                        if silver_fang in player2_hand.player_hand and silver_fang in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(silver_fang)

                                elif action == "field":
                                    index = player2_monster_zones.index(silver_fang.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif silver_fang in player2_hand.player_hand:
                            player2_hand.player_hand.remove(silver_fang)

                        elif silver_fang in player2_monster_zones:
                            index = player2_monster_zones.index(silver_fang.card_name)
                            player2_monster_zones[index] = None

                        if darkworld_thorns in player2_hand.player_hand and darkworld_thorns in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(darkworld_thorns)

                                elif action == "field":
                                    index = player2_monster_zones.index(darkworld_thorns.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif darkworld_thorns in player2_hand.player_hand:
                            player2_hand.player_hand.remove(darkworld_thorns)

                        elif darkworld_thorns in player2_monster_zones:
                            index = player2_monster_zones.index(darkworld_thorns.card_name)
                            player2_monster_zones[index] = None

                        player2_grave.append(silver_fang)
                        player2_grave.append(darkworld_thorns)

                        zone = int(input("Choose zone for Flower Wolf: "))

                        player2_extra.remove(flower_wolf)
                        player2_monster_zones[zone-1] = flower_wolf.card_name
                        break

                elif fusion == "Gaia the Dragon Champion":
                    if (gaia_the_fierce_knight in player2_hand.player_hand or gaia_the_fierce_knight in player2_monster_zones) and (curse_of_dragon in player2_hand.player_hand or curse_of_dragon in player2_monster_zones) and gaia_the_dragon_champion in player2_extra:
                        if gaia_the_fierce_knight in player2_hand.player_hand and gaia_the_fierce_knight in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(gaia_the_fierce_knight)

                                elif action == "field":
                                    index = player2_monster_zones.index(gaia_the_fierce_knight.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif gaia_the_fierce_knight in player2_hand.player_hand:
                            player2_hand.player_hand.remove(gaia_the_fierce_knight)

                        elif gaia_the_fierce_knight in player2_monster_zones:
                            index = player2_monster_zones.index(gaia_the_fierce_knight.card_name)
                            player2_monster_zones[index] = None

                        if curse_of_dragon in player2_hand.player_hand and curse_of_dragon in player2_monster_zones:
                            while(1):
                                action = input("Choose Monster in hand or field: ")

                                if action == "hand":
                                    player2_hand.player_hand.remove(curse_of_dragon)

                                elif action == "field":
                                    index = player2_monster_zones.index(curse_of_dragon.card_name)
                                    player2_monster_zones[index] = None

                                else:
                                    print("Not a valid option.")

                        elif curse_of_dragon in player2_hand.player_hand:
                            player2_hand.player_hand.remove(curse_of_dragon)

                        elif curse_of_dragon in player2_monster_zones:
                            index = player2_monster_zones.index(curse_of_dragon.card_name)
                            player2_monster_zones[index] = None

                        player2_grave.append(gaia_the_fierce_knight)
                        player2_grave.append(curse_of_dragon)

                        zone = int(input("Choose zone for Gaia the Dragon Champion: "))

                        player2_extra.remove(gaia_the_dragon_champion)
                        player2_monster_zones[zone-1] = gaia_the_dragon_champion.card_name
                        break

                else:
                    print("Not a valid Fusion target.")

    elif card == remove_trap:
        if curr_player == 1:
            card1 = get_card(player2_st_zones[0])
            card2 = get_card(player2_st_zones[1])
            card3 = get_card(player2_st_zones[2])

            if card1 == None and card2 == None and card3 == None:
                return print("No valid target.")

            elif card1.super_type != "Trap" and card2.super_type != "Trap" and card3.super_type != "Trap":
                return print("No valid target.")

            else:
                while(1):
                    target = int(input("Choose Trap to destroy: "))

                    if target - 1 == 0:
                        if card1.super_type != "Trap":
                            print("Not a valid target.")
                        else:
                            player2_grave.append(player2_st_zones[target-1])
                            player2_st_zones[target-1] = None
                            break

                    elif target - 1 == 1:
                        if card2.super_type != "Trap":
                            print("Not a valid target.")
                        else:
                            player2_grave.append(player2_st_zones[target-1])
                            player2_st_zones[target-1] = None
                            break

                    elif target - 1 == 2:
                        if card3.super_type != "Trap":
                            print("Not a valid target.")
                        else:
                            player2_grave.append(player2_st_zones[target-1])
                            player2_st_zones[target-1] = None
                            break

        elif curr_player == 2:
            card1 = get_card(player1_st_zones[0])
            card2 = get_card(player1_st_zones[1])
            card3 = get_card(player1_st_zones[2])

            if card1 == None and card2 == None and card3 == None:
                return print("No valid target.")

            elif card1.super_type != "Trap" and card2.super_type != "Trap" and card3.super_type != "Trap":
                return print("No valid target.")

            else:
                while(1):
                    target = int(input("Choose Trap to destroy: "))

                    if target - 1 == 0:
                        if card1.super_type != "Trap":
                            print("Not a valid target.")
                        else:
                            player1_grave.append(player1_st_zones[target-1])
                            player1_st_zones[target-1] = None
                            break

                    elif target - 1 == 1:
                        if card2.super_type != "Trap":
                            print("Not a valid target.")
                        else:
                            player1_grave.append(player1_st_zones[target-1])
                            player1_st_zones[target-1] = None
                            break

                    elif target - 1 == 2:
                        if card3.super_type != "Trap":
                            print("Not a valid target.")
                        else:
                            player1_grave.append(player1_st_zones[target-1])
                            player1_st_zones[target-1] = None
                            break

    elif card == gravedigger_ghoul:
        if curr_player == 1:
            count = 0

            while(count < 2):
                view_grave(2)

                if len(player2_grave) == 0:
                    break

                else:
                    target = int(input("Choose a Monster or type -1 to stop: "))

                    if target - 1 > len(player2_grave):
                        print("Not a valid target.")

                    elif target - 1 < 0:
                        print("Not a valid target.")

                    elif target == -1:
                        break

                    else:
                        player2_banished.append(player2_grave[target-1])
                        player2_grave.pop(target-1)
                        count += 1

        elif curr_player == 2:
            count = 0

            while(count < 2):
                view_grave(1)

                if len(player1_grave) == 0:
                    break

                else:
                    target = int(input("Choose a Monster or type -1 to stop: "))

                    if target - 1 > len(player1_grave):
                        print("Not a valid target.")

                    elif target - 1 < 0:
                        print("Not a valid target.")

                    elif target == -1:
                        break

                    else:
                        player1_banished.append(player1_grave[target-1])
                        player1_grave.pop(target-1)
                        count += 1

    elif card == stop_defense:
        if curr_player == 1:
            while(1):
                target = int(input("Choose a Monster: "))

                if player2_monster_zones[target-1] == None:
                    print("Not a valid target.")

                elif player2_monster_zones[target-1] == "Set Card":
                    if target - 1 == 0:
                        player2_monster_zones[target-1] = p2_set1.card.card_name
                        break

                    elif target - 1 == 1:
                        player2_monster_zones[target-1] = p2_set2.card.card_name
                        break

                    elif target - 1 == 2:
                        player2_monster_zones[target-1] = p2_set3.card.card_name
                        break

                elif player2_monster_zones[target-1][len(player2_monster_zones[target-1])-3:len(player2_monster_zones[target-1])] == "(D)":
                    if target - 1 == 0:
                        player2_monster_zones[target-1] = player2_monster_zones[target-1][0:len(player2_monster_zones[target-1])-4]
                        break

                    elif target - 1 == 1:
                        player2_monster_zones[target-1] = player2_monster_zones[target-1][0:len(player2_monster_zones[target-1])-4]
                        break

                    elif target - 1 == 2:
                        player2_monster_zones[target-1] = player2_monster_zones[target-1][0:len(player2_monster_zones[target-1])-4]
                        break

                else:
                    print("Not a valid target.")

        elif curr_player == 2:
            while(1):
                target = int(input("Choose a Monster: "))

                if player1_monster_zones[target-1] == None:
                    print("Not a valid target.")

                elif player1_monster_zones[target-1] == "Set Card":
                    if target - 1 == 0:
                        player1_monster_zones[target-1] = p1_set1.card.card_name
                        break

                    elif target - 1 == 1:
                        player1_monster_zones[target-1] = p1_set2.card.card_name
                        break

                    elif target - 1 == 2:
                        player1_monster_zones[target-1] = p1_set3.card.card_name
                        break

                elif player1_monster_zones[target-1][len(player1_monster_zones[target-1])-3:len(player1_monster_zones[target-1])] == "(D)":
                    if target - 1 == 0:
                        player1_monster_zones[target-1] == player1_monster_zones[target-1][0:len(player1_monster_zones[target-1])-4]
                        break

                    elif target - 1 == 1:
                        player1_monster_zones[target-1] == player1_monster_zones[target-1][0:len(player1_monster_zones[target-1])-4]
                        break

                    elif target - 1 == 2:
                        player1_monster_zones[target-1] == player1_monster_zones[target-1][0:len(player1_monster_zones[target-1])-4]
                        break

                else:
                    print("Not a valid target.")

    elif card == goblins_secret_remedy:
        if curr_player == 1:
            player1_lp += 600

        elif curr_player == 2:
            player2_lp += 600

    elif card == final_flame:
        if curr_player == 1:
            player2_lp -= 600

        elif curr_player == 2:
            player1_lp -= 600

    elif card == swords_of_revealing_light:
        if curr_player == 1:
            swords_index = player1_st_zones.index("Swords of Revealing Light")

            if swords_index == 0:
                if p1_swords_counter1 == 0:
                    for i in range(3):
                        if player2_monster_zones[i] == "Set Card":
                            if i == 0:
                                player2_monster_zones.pop(i)
                                player2_monster_zones.insert(i, p2_set1.card.card_name + " (D)")

                            elif i == 1:
                                player2_monster_zones.pop(i)
                                player2_monster_zones.insert(i, p2_set2.card.card_name + " (D)")

                            elif i == 2:
                                player2_monster_zones.pop(i)
                                player2_monster_zones.insert(i, p2_set3.card.card_name + " (D)")

            elif swords_index == 1:
                if p1_swords_counter2 == 0:
                    for i in range(3):
                        if player2_monster_zones[i] == "Set Card":
                            if i == 0:
                                player2_monster_zones.pop(i)
                                player2_monster_zones.insert(i, p2_set1.card.card_name + " (D)")

                            elif i == 1:
                                player2_monster_zones.pop(i)
                                player2_monster_zones.insert(i, p2_set2.card.card_name + " (D)")

                            elif i == 2:
                                player2_monster_zones.pop(i)
                                player2_monster_zones.insert(i, p2_set3.card.card_name + " (D)")

            elif swords_index == 2:
                if p1_swords_counter3 == 0:
                    for i in range(3):
                        if player2_monster_zones[i] == "Set Card":
                            if i == 0:
                                player2_monster_zones.pop(i)
                                player2_monster_zones.insert(i, p2_set1.card.card_name + " (D)")

                            elif i == 1:
                                player2_monster_zones.pop(i)
                                player2_monster_zones.insert(i, p2_set2.card.card_name + " (D)")

                            elif i == 2:
                                player2_monster_zones.pop(i)
                                player2_monster_zones.insert(i, p2_set3.card.card_name + " (D)")

        elif curr_player == 2:
            swords_index = player2_st_zones.index("Swords of Revealing Light")

            if swords_index == 0:
                if p2_swords_counter1 == 0:
                    for i in range(3):
                        if player1_monster_zones[i] == "Set Card":
                            if i == 0:
                                player1_monster_zones.pop(i)
                                player1_monster_zones.insert(i, p1_set1.card.card_name + " (D)")

                            elif i == 1:
                                player1_monster_zones.pop(i)
                                player1_monster_zones.insert(i, p1_set2.card.card_name + " (D)")

                            elif i == 2:
                                player1_monster_zones.pop(i)
                                player1_monster_zones.insert(i, p1_set3.card.card_name + " (D)")

            elif swords_index == 1:
                if p2_swords_counter2 == 0:
                    for i in range(3):
                        if player1_monster_zones[i] == "Set Card":
                            if i == 0:
                                player1_monster_zones.pop(i)
                                player1_monster_zones.insert(i, p1_set1.card.card_name + " (D)")

                            elif i == 1:
                                player1_monster_zones.pop(i)
                                player1_monster_zones.insert(i, p1_set2.card.card_name + " (D)")

                            elif i == 2:
                                player1_monster_zones.pop(i)
                                player1_monster_zones.insert(i, p1_set3.card.card_name + " (D)")

            elif swords_index == 2:
                if p2_swords_counter3 == 0:
                    for i in range(3):
                        if player1_monster_zones[i] == "Set Card":
                            if i == 0:
                                player1_monster_zones.pop(i)
                                player1_monster_zones.insert(i, p1_set1.card.card_name + " (D)")

                            elif i == 1:
                                player1_monster_zones.pop(i)
                                player1_monster_zones.insert(i, p1_set2.card.card_name + " (D)")

                            elif i == 2:
                                player1_monster_zones.pop(i)
                                player1_monster_zones.insert(i, p1_set3.card.card_name + " (D)")

    elif card == monster_reborn:
        if curr_player == 1:
            while(1):
                print("Your Graveyard: " + str(view_grave(1)))
                print("Opponent's Graveyard: " + str(view_grave(2)))
                target = input("Choose monster: ")

                if target in player1_grave and target in player2_grave:
                    while(1):
                        which_player = int(input("From your (1) or opponent (2) Graveyard: "))

                        if which_player == 1:
                            index = player1_grave.index(target)

                            player1_grave.pop(index)

                            while(1):
                                zone = int(input("Choose a zone: "))
                                monster = get_card(target)

                                if zone - 1 < 0 or zone - 1 > 2 or player1_monster_zones[zone-1] != None:
                                    print("Not a valid zone.")

                                else:
                                    player1_monster_zones[zone-1] = monster.card_name
                                    dragon_capture_jar_on_summon(zone)
                                    break

                            break

                        elif which_player == 2:
                            index = player2_grave.index(target)

                            player2_grave.pop(index)

                            while(1):
                                zone = int(input("Choose a zone: "))
                                monster = get_card(target)

                                if zone - 1 < 0 or zone - 1 > 2 or player1_monster_zones[zone-1] != None:
                                    print("Not a valid zone.")

                                else:
                                    player1_monster_zones[zone-1] = monster.card_name
                                    dragon_capture_jar_on_summon(zone)
                                    break

                            break

                        else:
                            print("Not a valid player.")

                    break

                elif target in player1_grave and target not in player2_grave:
                    index = player1_grave.index(target)

                    player1_grave.pop(index)

                    while(1):
                        zone = int(input("Choose a zone: "))
                        monster = get_card(target)

                        if zone - 1 < 0 or zone - 1 > 2 or player1_monster_zones[zone-1] != None:
                            print("Not a valid zone.")

                        else:
                            player1_monster_zones[zone-1] = monster.card_name
                            dragon_capture_jar_on_summon(zone)
                            break

                    break

                elif target in player2_grave and target not in player1_grave:
                    index = player2_grave.index(target)

                    player2_grave.pop(index)

                    while(1):
                        zone = int(input("Choose a zone: "))
                        monster = get_card(target)

                        if zone - 1 < 0 or zone - 1 > 2 or player1_monster_zones[zone-1] != None:
                            print("Not a valid zone.")

                        else:
                            player1_monster_zones[zone-1] = monster.card_name
                            dragon_capture_jar_on_summon(zone)
                            break

                    break

                else:
                    print("Not a valid target.")

        elif curr_player == 2:
            while(1):
                print("Your Graveyard: " + str(view_grave(2)))
                print("Opponent's Graveyard: " + str(view_grave(1)))
                target = input("Choose monster: ")

                if target not in player1_grave or target not in player2_grave:
                    print("Not a valid target.")

                elif target in player1_grave and target in player2_grave:
                    while(1):
                        which_player = int(input("From your (1) or opponent (2) Graveyard: "))

                        if which_player == 1:
                            index = player2_grave.index(target)

                            player2_grave.pop(index)

                            while(1):
                                zone = int(input("Choose a zone: "))
                                monster = get_card(target)

                                if zone - 1 < 0 or zone - 1 > 2 or player2_monster_zones[zone-1] != None:
                                    print("Not a valid zone.")

                                else:
                                    player2_monster_zones[zone-1] = monster.card_name
                                    dragon_capture_jar_on_summon(zone)
                                    break

                            break

                        elif which_player == 2:
                            index = player1_grave.index(target)

                            player1_grave.pop(index)

                            while(1):
                                zone = int(input("Choose a zone: "))
                                monster = get_card(target)

                                if zone - 1 < 0 or zone - 1 > 2 or player2_monster_zones[zone-1] != None:
                                    print("Not a valid zone.")

                                else:
                                    player2_monster_zones[zone-1] = monster.card_name
                                    dragon_capture_jar_on_summon(zone)
                                    break

                            break

                elif target in player1_grave and target not in player2_grave:
                    index = player1_grave.index(target)

                    player1_grave.pop(index)

                    while(1):
                        zone = int(input("Choose a zone: "))
                        monster = get_card(target)

                        if zone - 1 < 0 or zone - 1 > 2 or player2_monster_zones[zone-1] != None:
                            print("Not a valid zone.")

                        else:
                            player2_monster_zones[zone-1] = monster.card_name
                            dragon_capture_jar_on_summon(zone)
                            break

                    break

                elif target in player2_grave and target not in player1_grave:
                    index = player2_grave.index(target)

                    player2_grave.pop(index)

                    while(1):
                        zone = int(input("Choose a zone: "))
                        monster = get_card(target)

                        if zone - 1 < 0 or zone - 1 > 2 or player2_monster_zones[zone-1] != None:
                            print("Not a valid zone.")

                        else:
                            player2_monster_zones[zone-1] = monster.card_name
                            dragon_capture_jar_on_summon(zone)
                            break

                    break

                else:
                    print("Not a valid player.")

    elif card == pot_of_greed:
        if curr_player == 1:
            draw_card(player1_deck, player1_hand)
            draw_card(player1_deck, player1_hand)
            view_hand(player1_hand.player_hand)
    
        if curr_player == 2:
            draw_card(player2_deck, player2_hand)
            draw_card(player2_deck, player2_hand)
            view_hand(player2_hand.player_hand)

    elif card == trap_hole:
        if curr_player == 1:
            if p2_just_summoned_zone1 == True:
                player2_grave.append(player2_monster_zones[0])
                player2_monster_zones[0] = None

            elif p2_just_summoned_zone2 == True:
                player2_grave.append(player2_monster_zones[1])
                player2_monster_zones[1] = None

            elif p2_just_summoned_zone3 == True:
                player2_grave.append(player2_monster_zones[2])
                player2_monster_zones[2] = None

        elif curr_player == 2:
            if p1_just_summoned_zone1 == True:
                player1_grave.append(player1_monster_zones[0])
                player1_monster_zones[0] = None

            elif p1_just_summoned_zone2 == True:
                player1_grave.append(player1_monster_zones[1])
                player1_monster_zones[1] = None

            elif p1_just_summoned_zone3 == True:
                player1_grave.append(player1_monster_zones[2])
                player1_monster_zones[2] = None

    elif card == two_pronged_attack:
        if curr_player == 1 and curr_phase == "bp":
            while(1):
                while(1):
                    tribute1 = int(input("Choose first Tribute: "))
                    if player2_monster_zones[tribute1] == None:
                        print("Not a valid target.")

                    elif player2_monster_zones[tribute1] == "Set Card":
                        if tribute1 - 1 == 0:
                            player2_grave.append(p2_set1.card.card_name)
                            player2_monster_zones[tribute1] = None
                            break

                        elif tribute1 - 1 == 1:
                            player2_grave.append(p2_set2.card.card_name)
                            player2_monster_zones[tribute1] = None
                            break

                        elif tribute1 - 1 == 2:
                            player2_grave.append(p2_set3.card.card_name)
                            player2_monster_zones[tribute1] = None
                            break

                    elif player2_monster_zones[tribute1][len(player2_monster_zones[tribute1])-3:len(player2_monster_zones[tribute1])] == "(D)":
                        player2_grave.append(player2_monster_zones[tribute1][0:len(player2_monster_zones[tribute1])-4])
                        player2_monster_zones[tribute1] = None
                        break

                    else:
                        player2_grave.append(player2_monster_zones[tribute1])
                        player2_monster_zones[tribute1] = None
                        break

                while(1):
                    tribute2 = int(input("Choose second Tribute: "))
                    if player2_monster_zones[tribute2] == None:
                        print("Not a valid target.")

                    elif player2_monster_zones[tribute2] == "Set Card":
                        if tribute2 - 1 == 0:
                            player2_grave.append(p2_set1.card.card_name)
                            player2_monster_zones[tribute2] = None
                            break

                        elif tribute2 - 1 == 1:
                            player2_grave.append(p2_set2.card.card_name)
                            player2_monster_zones[tribute2] = None
                            break

                        elif tribute2 - 1 == 2:
                            player2_grave.append(p2_set3.card.card_name)
                            player2_monster_zones[tribute2] = None
                            break

                    elif player2_monster_zones[tribute2][len(player2_monster_zones[tribute2])-3:len(player2_monster_zones[tribute2])] == "(D)":
                        player2_grave.append(player2_monster_zones[tribute2][0:len(player2_monster_zones[tribute2])-4])
                        player2_monster_zones[tribute2] = None
                        break

                    else:
                        player2_grave.append(player2_monster_zones[tribute2])
                        player2_monster_zones[tribute2] = None
                        break

                while(1):
                    target = int(input("Choose opponent Monster: "))
                    if player1_monster_zones[target] == None:
                        print("Not a valid target.")

                    elif player1_monster_zones[target] == "Set Card":
                        if target - 1 == 0:
                            player1_grave.append(p1_set1.card.card_name)
                            player1_monster_zones[target] = None
                            break

                        elif target - 1 == 1:
                            player1_grave.append(p1_set2.card.card_name)
                            player1_monster_zones[target] = None
                            break

                        elif target - 1 == 2:
                            player1_grave.append(p1_set3.card.card_name)
                            player1_monster_zones[target] = None
                            break

                    elif player1_monster_zones[target][len(player1_monster_zones[target])-3:len(player1_monster_zones[target])] == "(D)":
                        player1_grave.append(player1_monster_zones[target][0:len(player1_monster_zones[target])-4])
                        player1_monster_zones[target] = None
                        break

                    else:
                        player1_grave.append(player1_monster_zones[target])
                        player1_monster_zones[target] = None
                        break

                break

        elif curr_player == 2 and curr_phase == "bp":
            while(1):
                while(1):
                    tribute1 = int(input("Choose first Tribute: "))
                    if player1_monster_zones[tribute1] == None:
                        print("Not a valid target.")

                    elif player1_monster_zones[tribute1] == "Set Card":
                        if tribute1 - 1 == 0:
                            player1_grave.append(p1_set1.card.card_name)
                            player1_monster_zones[tribute1] = None
                            break

                        elif tribute1 - 1 == 1:
                            player1_grave.append(p1_set2.card.card_name)
                            player1_monster_zones[tribute1] = None
                            break

                        elif tribute1 - 1 == 2:
                            player1_grave.append(p1_set3.card.card_name)
                            player1_monster_zones[tribute1] = None
                            break

                    elif player1_monster_zones[tribute1][len(player1_monster_zones[tribute1])-3:len(player1_monster_zones[tribute1])] == "(D)":
                        player1_grave.append(player1_monster_zones[tribute1][0:len(player1_monster_zones[tribute1])-4])
                        player1_monster_zones[tribute1] = None
                        break

                    else:
                        player1_grave.append(player1_monster_zones[tribute1])
                        player1_monster_zones[tribute1] = None
                        break

                while(1):
                    tribute2 = int(input("Choose second Tribute: "))
                    if player1_monster_zones[tribute2] == None:
                        print("Not a valid target.")

                    elif player1_monster_zones[tribute2] == "Set Card":
                        if tribute2 - 1 == 0:
                            player1_grave.append(p1_set1.card.card_name)
                            player1_monster_zones[tribute2] = None
                            break

                        elif tribute2 - 1 == 1:
                            player1_grave.append(p1_set2.card.card_name)
                            player1_monster_zones[tribute2] = None
                            break

                        elif tribute2 - 1 == 2:
                            player1_grave.append(p1_set3.card.card_name)
                            player1_monster_zones[tribute2] = None
                            break

                    elif player1_monster_zones[tribute2][len(player1_monster_zones[tribute2])-3:len(player1_monster_zones[tribute2])] == "(D)":
                        player1_grave.append(player1_monster_zones[tribute2][0:len(player1_monster_zones[tribute2])-4])
                        player1_monster_zones[tribute2] = None
                        break

                    else:
                        player1_grave.append(player1_monster_zones[tribute2])
                        player1_monster_zones[tribute2] = None
                        break

                while(1):
                    target = int(input("Choose opponent Monster: "))
                    if player2_monster_zones[target] == None:
                        print("Not a valid target.")

                    elif player2_monster_zones[target] == "Set Card":
                        if target - 1 == 0:
                            player2_grave.append(p2_set1.card.card_name)
                            player2_monster_zones[target] = None
                            break

                        elif target - 1 == 1:
                            player2_grave.append(p2_set2.card.card_name)
                            player2_monster_zones[target] = None
                            break

                        elif target - 1 == 2:
                            player2_grave.append(p2_set3.card.card_name)
                            player2_monster_zones[target] = None
                            break

                    elif player2_monster_zones[target][len(player2_monster_zones[target])-3:len(player2_monster_zones[target])] == "(D)":
                        player2_grave.append(player2_monster_zones[target][0:len(player2_monster_zones[target])-4])
                        player2_monster_zones[target] = None
                        break

                    else:
                        player2_grave.append(player2_monster_zones[target])
                        player2_monster_zones[target] = None
                        break

                break

        elif curr_player == 1:
            while(1):
                while(1):
                    tribute1 = int(input("Choose first Tribute: "))
                    if player1_monster_zones[tribute1] == None:
                        print("Not a valid target.")

                    elif player1_monster_zones[tribute1] == "Set Card":
                        if tribute1 - 1 == 0:
                            player1_grave.append(p1_set1.card.card_name)
                            player1_monster_zones[tribute1] = None
                            break

                        elif tribute1 - 1 == 1:
                            player1_grave.append(p1_set2.card.card_name)
                            player1_monster_zones[tribute1] = None
                            break

                        elif tribute1 - 1 == 2:
                            player1_grave.append(p1_set3.card.card_name)
                            player1_monster_zones[tribute1] = None
                            break

                    elif player1_monster_zones[tribute1][len(player1_monster_zones[tribute1])-3:len(player1_monster_zones[tribute1])] == "(D)":
                        player1_grave.append(player1_monster_zones[tribute1][0:len(player1_monster_zones[tribute1])-4])
                        player1_monster_zones[tribute1] = None
                        break

                    else:
                        player1_grave.append(player1_monster_zones[tribute1])
                        player1_monster_zones[tribute1] = None
                        break

                while(1):
                    tribute2 = int(input("Choose second Tribute: "))
                    if player1_monster_zones[tribute2] == None:
                        print("Not a valid target.")

                    elif player1_monster_zones[tribute2] == "Set Card":
                        if tribute2 - 1 == 0:
                            player1_grave.append(p1_set1.card.card_name)
                            player1_monster_zones[tribute2] = None
                            break

                        elif tribute2 - 1 == 1:
                            player1_grave.append(p1_set2.card.card_name)
                            player1_monster_zones[tribute2] = None
                            break

                        elif tribute2 - 1 == 2:
                            player1_grave.append(p1_set3.card.card_name)
                            player1_monster_zones[tribute2] = None
                            break

                    elif player1_monster_zones[tribute2][len(player1_monster_zones[tribute2])-3:len(player1_monster_zones[tribute2])] == "(D)":
                        player1_grave.append(player1_monster_zones[tribute2][0:len(player1_monster_zones[tribute2])-4])
                        player1_monster_zones[tribute2] = None
                        break

                    else:
                        player1_grave.append(player1_monster_zones[tribute2])
                        player1_monster_zones[tribute2] = None
                        break

                while(1):
                    target = int(input("Choose opponent Monster: "))
                    if player2_monster_zones[target] == None:
                        print("Not a valid target.")

                    elif player2_monster_zones[target] == "Set Card":
                        if target - 1 == 0:
                            player2_grave.append(p2_set1.card.card_name)
                            player2_monster_zones[target] = None
                            break

                        elif target - 1 == 1:
                            player2_grave.append(p2_set2.card.card_name)
                            player2_monster_zones[target] = None
                            break

                        elif target - 1 == 2:
                            player2_grave.append(p2_set3.card.card_name)
                            player2_monster_zones[target] = None
                            break

                    elif player2_monster_zones[target][len(player2_monster_zones[target])-3:len(player2_monster_zones[target])] == "(D)":
                        player2_grave.append(player2_monster_zones[target][0:len(player2_monster_zones[target])-4])
                        player2_monster_zones[target] = None
                        break

                    else:
                        player2_grave.append(player2_monster_zones[target])
                        player2_monster_zones[target] = None
                        break

                break

        elif curr_player == 2:
            while(1):
                while(1):
                    tribute1 = int(input("Choose first Tribute: "))
                    if player2_monster_zones[tribute1] == None:
                        print("Not a valid target.")

                    elif player2_monster_zones[tribute1] == "Set Card":
                        if tribute1 - 1 == 0:
                            player2_grave.append(p2_set1.card.card_name)
                            player2_monster_zones[tribute1] = None
                            break

                        elif tribute1 - 1 == 1:
                            player2_grave.append(p2_set2.card.card_name)
                            player2_monster_zones[tribute1] = None
                            break

                        elif tribute1 - 1 == 2:
                            player2_grave.append(p2_set3.card.card_name)
                            player2_monster_zones[tribute1] = None
                            break

                    elif player2_monster_zones[tribute1][len(player2_monster_zones[tribute1])-3:len(player2_monster_zones[tribute1])] == "(D)":
                        player2_grave.append(player2_monster_zones[tribute1][0:len(player2_monster_zones[tribute1])-4])
                        player2_monster_zones[tribute1] = None
                        break

                    else:
                        player2_grave.append(player2_monster_zones[tribute1])
                        player2_monster_zones[tribute1] = None
                        break

                while(1):
                    tribute2 = int(input("Choose second Tribute: "))
                    if player2_monster_zones[tribute2] == None:
                        print("Not a valid target.")

                    elif player2_monster_zones[tribute2] == "Set Card":
                        if tribute2 - 1 == 0:
                            player2_grave.append(p2_set1.card.card_name)
                            player2_monster_zones[tribute2] = None
                            break

                        elif tribute2 - 1 == 1:
                            player2_grave.append(p2_set2.card.card_name)
                            player2_monster_zones[tribute2] = None
                            break

                        elif tribute2 - 1 == 2:
                            player2_grave.append(p2_set3.card.card_name)
                            player2_monster_zones[tribute2] = None
                            break

                    elif player2_monster_zones[tribute2][len(player2_monster_zones[tribute2])-3:len(player2_monster_zones[tribute2])] == "(D)":
                        player2_grave.append(player2_monster_zones[tribute2][0:len(player2_monster_zones[tribute2])-4])
                        player2_monster_zones[tribute2] = None
                        break

                    else:
                        player2_grave.append(player2_monster_zones[tribute2])
                        player2_monster_zones[tribute2] = None
                        break

                while(1):
                    target = int(input("Choose opponent Monster: "))
                    if player1_monster_zones[target] == None:
                        print("Not a valid target.")

                    elif player1_monster_zones[target] == "Set Card":
                        if target - 1 == 0:
                            player1_grave.append(p1_set1.card.card_name)
                            player1_monster_zones[target] = None
                            break

                        elif target - 1 == 1:
                            player1_grave.append(p1_set2.card.card_name)
                            player1_monster_zones[target] = None
                            break

                        elif target - 1 == 2:
                            player1_grave.append(p1_set3.card.card_name)
                            player1_monster_zones[target] = None
                            break

                    elif player1_monster_zones[target][len(player1_monster_zones[target])-3:len(player1_monster_zones[target])] == "(D)":
                        player1_grave.append(player1_monster_zones[target][0:len(player1_monster_zones[target])-4])
                        player1_monster_zones[target] = None
                        break

                    else:
                        player1_grave.append(player1_monster_zones[target])
                        player1_monster_zones[target] = None
                        break

                break

    elif card == dragon_capture_jar:
        if p1_monster1 != None:
            if p1_monster1.monster_type == "Dragon":
                player1_monster_zones[0] = p1_monster1.card_name + " (D)"

        if p1_monster2 != None:
            if p1_monster2.monster_type == "Dragon":
                player1_monster_zones[1] = p1_monster2.card_name + " (D)"

        if p1_monster3 != None:
            if p1_monster3.monster_type == "Dragon":
                player1_monster_zones[2] = p1_monster3.card_name + " (D)"

        if p2_monster1 != None:
            if p2_monster1.monster_type == "Dragon":
                player2_monster_zones[0] = p2_monster1.card_name + " (D)"

        if p2_monster2 != None:
            if p2_monster2.monster_type == "Dragon":
                player2_monster_zones[1] = p2_monster2.card_name + " (D)"

        if p2_monster3 != None:
            if p2_monster3.monster_type == "Dragon":
                player2_monster_zones[2] = p2_monster3.card_name + " (D)"

    elif card == reaper_of_the_cards:
        if curr_player == 1 and curr_phase == "bp":
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone: "))

                if which_player == 1:
                    if player1_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p1_st_set1.card.card_name)

                            if p1_st_set1.card.super_type == "Trap":
                                player1_grave.append(p1_st_set1.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p1_st_set2.card.card_name)

                            if p1_st_set2.card.super_type == "Trap":
                                player1_grave.append(p1_st_set2.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p1_st_set3.card.card_name)

                            if p1_st_set3.card.super_type == "Trap":
                                player1_grave.append(p1_st_set3.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                    elif get_card(player1_st_zones[target-1]).super_type != "Trap":
                        print("Not a valid target.")

                    else:
                        player1_grave.append(player1_st_zones[target-1])
                        player1_st_zones[target-1] = None

                        break

                elif which_player == 0:
                    if player2_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p2_st_set1.card.card_name)

                            if p2_st_set1.card.super_type == "Trap":
                                player2_grave.append(p2_st_set1.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p2_st_set2.card.card_name)

                            if p2_st_set2.card.super_type == "Trap":
                                player1_grave.append(p2_st_set2.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p2_st_set3.card.card_name)

                            if p2_st_set3.card.super_type == "Trap":
                                player2_grave.append(p2_st_set3.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                    elif get_card(player2_st_zones[target-1]).super_type != "Trap":
                        print("Not a valid target.")

                    else:
                        player2_grave.append(player1_st_zones[target-1])
                        player2_st_zones[target-1] = None

                        break

        elif curr_player == 2 and curr_phase == "bp":
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone: "))

                if which_player == 0:
                    if player1_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p1_st_set1.card.card_name)

                            if p1_st_set1.card.super_type == "Trap":
                                player1_grave.append(p1_st_set1.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p1_st_set2.card.card_name)

                            if p1_st_set2.card.super_type == "Trap":
                                player1_grave.append(p1_st_set2.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p1_st_set3.card.card_name)

                            if p1_st_set3.card.super_type == "Trap":
                                player1_grave.append(p1_st_set3.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                    elif get_card(player1_st_zones[target-1]).super_type != "Trap":
                        print("Not a valid target.")

                    else:
                        player1_grave.append(player1_st_zones[target-1])
                        player1_st_zones[target-1] = None

                        break

                elif which_player == 1:
                    if player2_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p2_st_set1.card.card_name)

                            if p2_st_set1.card.super_type == "Trap":
                                player2_grave.append(p2_st_set1.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p2_st_set2.card.card_name)

                            if p2_st_set2.card.super_type == "Trap":
                                player1_grave.append(p2_st_set2.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p2_st_set3.card.card_name)

                            if p2_st_set3.card.super_type == "Trap":
                                player2_grave.append(p2_st_set3.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                    elif get_card(player2_st_zones[target-1]).super_type != "Trap":
                        print("Not a valid target.")

                    else:
                        player2_grave.append(player1_st_zones[target-1])
                        player2_st_zones[target-1] = None

                        break

        elif curr_player == 1:
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone: "))

                if which_player == 0:
                    if player1_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p1_st_set1.card.card_name)

                            if p1_st_set1.card.super_type == "Trap":
                                player1_grave.append(p1_st_set1.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p1_st_set2.card.card_name)

                            if p1_st_set2.card.super_type == "Trap":
                                player1_grave.append(p1_st_set2.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p1_st_set3.card.card_name)

                            if p1_st_set3.card.super_type == "Trap":
                                player1_grave.append(p1_st_set3.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                    elif get_card(player1_st_zones[target-1]).super_type != "Trap":
                        print("Not a valid target.")

                    else:
                        player1_grave.append(player1_st_zones[target-1])
                        player1_st_zones[target-1] = None

                        break

                elif which_player == 1:
                    if player2_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p2_st_set1.card.card_name)

                            if p2_st_set1.card.super_type == "Trap":
                                player2_grave.append(p2_st_set1.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p2_st_set2.card.card_name)

                            if p2_st_set2.card.super_type == "Trap":
                                player1_grave.append(p2_st_set2.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p2_st_set3.card.card_name)

                            if p2_st_set3.card.super_type == "Trap":
                                player2_grave.append(p2_st_set3.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                    elif get_card(player2_st_zones[target-1]).super_type != "Trap":
                        print("Not a valid target.")

                    else:
                        player2_grave.append(player1_st_zones[target-1])
                        player2_st_zones[target-1] = None

                        break

        elif curr_player == 2:
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone: "))

                if which_player == 1:
                    if player1_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p1_st_set1.card.card_name)

                            if p1_st_set1.card.super_type == "Trap":
                                player1_grave.append(p1_st_set1.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p1_st_set2.card.card_name)

                            if p1_st_set2.card.super_type == "Trap":
                                player1_grave.append(p1_st_set2.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p1_st_set3.card.card_name)

                            if p1_st_set3.card.super_type == "Trap":
                                player1_grave.append(p1_st_set3.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                    elif get_card(player1_st_zones[target-1]).super_type != "Trap":
                        print("Not a valid target.")

                    else:
                        player1_grave.append(player1_st_zones[target-1])
                        player1_st_zones[target-1] = None

                        break

                elif which_player == 0:
                    if player2_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p2_st_set1.card.card_name)

                            if p2_st_set1.card.super_type == "Trap":
                                player2_grave.append(p2_st_set1.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p2_st_set2.card.card_name)

                            if p2_st_set2.card.super_type == "Trap":
                                player1_grave.append(p2_st_set2.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p2_st_set3.card.card_name)

                            if p2_st_set3.card.super_type == "Trap":
                                player2_grave.append(p2_st_set3.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                    elif get_card(player2_st_zones[target-1]).super_type != "Trap":
                        print("Not a valid target.")

                    else:
                        player2_grave.append(player1_st_zones[target-1])
                        player2_st_zones[target-1] = None

                        break

    elif card == armed_ninja:
        if curr_player == 1 and curr_phase == "bp":
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone (type -1 to target Field Spell): "))

                if which_player == 1:
                    if target == -1:
                        if p1_field_zone[0] == None:
                            print("Not a valid target.")

                        else:
                            if p1_field_zone[0] == "Set Card":
                                print("The Set card is: " + p1_field_set.card.card_name)

                                player1_grave.append(p1_field_set.card.card_name)
                                p1_field_zone[0] = None

                            else:
                                remove_field_buff(p1_field_zone[0])
                                player1_grave.append(p1_field_zone[0])
                                p1_field_zone[0] = None

                    elif player1_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p1_st_set1.card.card_name)

                            if p1_st_set1.card.super_type == "Spell":
                                player1_grave.append(p1_st_set1.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p1_st_set2.card.card_name)

                            if p1_st_set2.card.super_type == "Spell":
                                player1_grave.append(p1_st_set2.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p1_st_set3.card.card_name)

                            if p1_st_set3.card.super_type == "Spell":
                                player1_grave.append(p1_st_set3.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                    elif get_card(player1_st_zones[target-1]).super_type != "Spell":
                        print("Not a valid target.")

                    else:
                        player1_grave.append(player1_st_zones[target-1])
                        player1_st_zones[target-1] = None

                        break

                elif which_player == 0:
                    if target == -1:
                        if p2_field_zone[0] == None:
                            print("Not a valid target.")

                        else:
                            if p2_field_zone[0] == "Set Card":
                                print("The Set card is: " + p2_field_set.card.card_name)

                                player2_grave.append(p2_field_set.card.card_name)
                                p2_field_zone[0] = None

                            else:
                                remove_field_buff(p2_field_zone[0])
                                player2_grave.append(p2_field_zone[0])
                                p2_field_zone[0] = None

                    elif player2_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p2_st_set1.card.card_name)

                            if p2_st_set1.card.super_type == "Spell":
                                player2_grave.append(p2_st_set1.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p2_st_set2.card.card_name)

                            if p2_st_set2.card.super_type == "Spell":
                                player1_grave.append(p2_st_set2.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p2_st_set3.card.card_name)

                            if p2_st_set3.card.super_type == "Spell":
                                player2_grave.append(p2_st_set3.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                    elif get_card(player2_st_zones[target-1]).super_type != "Trap":
                        print("Not a valid target.")

                    else:
                        player2_grave.append(player1_st_zones[target-1])
                        player2_st_zones[target-1] = None

                        break

        elif curr_player == 2 and curr_phase == "bp":
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone: "))

                if which_player == 0:
                    if target == -1:
                        if p1_field_zone[0] == None:
                            print("Not a valid target.")

                        else:
                            if p1_field_zone[0] == "Set Card":
                                print("The Set card is: " + p1_field_set.card.card_name)

                                player1_grave.append(p1_field_set.card.card_name)
                                p1_field_zone[0] = None

                            else:
                                remove_field_buff(p1_field_zone[0])
                                player1_grave.append(p1_field_zone[0])
                                p1_field_zone[0] = None

                    elif player1_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p1_st_set1.card.card_name)

                            if p1_st_set1.card.super_type == "Trap":
                                player1_grave.append(p1_st_set1.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p1_st_set2.card.card_name)

                            if p1_st_set2.card.super_type == "Trap":
                                player1_grave.append(p1_st_set2.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p1_st_set3.card.card_name)

                            if p1_st_set3.card.super_type == "Trap":
                                player1_grave.append(p1_st_set3.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                    elif get_card(player1_st_zones[target-1]).super_type != "Trap":
                        print("Not a valid target.")

                    else:
                        player1_grave.append(player1_st_zones[target-1])
                        player1_st_zones[target-1] = None

                        break

                elif which_player == 1:
                    if target == -1:
                        if p2_field_zone[0] == None:
                            print("Not a valid target.")

                        else:
                            if p2_field_zone[0] == "Set Card":
                                print("The Set card is: " + p2_field_set.card.card_name)

                                player2_grave.append(p2_field_set.card.card_name)
                                p2_field_zone[0] = None

                            else:
                                remove_field_buff(p2_field_zone[0])
                                player2_grave.append(p2_field_zone[0])
                                p2_field_zone[0] = None

                    elif player2_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p2_st_set1.card.card_name)

                            if p2_st_set1.card.super_type == "Trap":
                                player2_grave.append(p2_st_set1.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p2_st_set2.card.card_name)

                            if p2_st_set2.card.super_type == "Trap":
                                player1_grave.append(p2_st_set2.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p2_st_set3.card.card_name)

                            if p2_st_set3.card.super_type == "Trap":
                                player2_grave.append(p2_st_set3.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                    elif get_card(player2_st_zones[target-1]).super_type != "Trap":
                        print("Not a valid target.")

                    else:
                        player2_grave.append(player1_st_zones[target-1])
                        player2_st_zones[target-1] = None

                        break

        elif curr_player == 1:
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone: "))

                if which_player == 0:
                    if target == -1:
                        if p1_field_zone[0] == None:
                            print("Not a valid target.")

                        else:
                            if p1_field_zone[0] == "Set Card":
                                print("The Set card is: " + p1_field_set.card.card_name)

                                player1_grave.append(p1_field_set.card.card_name)
                                p1_field_zone[0] = None

                            else:
                                remove_field_buff(p1_field_zone[0])
                                player1_grave.append(p1_field_zone[0])
                                p1_field_zone[0] = None

                    elif player1_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p1_st_set1.card.card_name)

                            if p1_st_set1.card.super_type == "Trap":
                                player1_grave.append(p1_st_set1.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p1_st_set2.card.card_name)

                            if p1_st_set2.card.super_type == "Trap":
                                player1_grave.append(p1_st_set2.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p1_st_set3.card.card_name)

                            if p1_st_set3.card.super_type == "Trap":
                                player1_grave.append(p1_st_set3.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                    elif get_card(player1_st_zones[target-1]).super_type != "Trap":
                        print("Not a valid target.")

                    else:
                        player1_grave.append(player1_st_zones[target-1])
                        player1_st_zones[target-1] = None

                        break

                elif which_player == 1:
                    if target == -1:
                        if p2_field_zone[0] == None:
                            print("Not a valid target.")

                        else:
                            if p2_field_zone[0] == "Set Card":
                                print("The Set card is: " + p2_field_set.card.card_name)

                                player2_grave.append(p2_field_set.card.card_name)
                                p2_field_zone[0] = None

                            else:
                                remove_field_buff(p2_field_zone[0])
                                player2_grave.append(p2_field_zone[0])
                                p2_field_zone[0] = None

                    elif player2_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p2_st_set1.card.card_name)

                            if p2_st_set1.card.super_type == "Trap":
                                player2_grave.append(p2_st_set1.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p2_st_set2.card.card_name)

                            if p2_st_set2.card.super_type == "Trap":
                                player1_grave.append(p2_st_set2.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p2_st_set3.card.card_name)

                            if p2_st_set3.card.super_type == "Trap":
                                player2_grave.append(p2_st_set3.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                    elif get_card(player2_st_zones[target-1]).super_type != "Trap":
                        print("Not a valid target.")

                    else:
                        player2_grave.append(player1_st_zones[target-1])
                        player2_st_zones[target-1] = None

                        break

        elif curr_player == 2:
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone: "))

                if which_player == 1:
                    if target == -1:
                        if p1_field_zone[0] == None:
                            print("Not a valid target.")

                        else:
                            if p1_field_zone[0] == "Set Card":
                                print("The Set card is: " + p1_field_set.card.card_name)

                                player1_grave.append(p1_field_set.card.card_name)
                                p1_field_zone[0] = None

                            else:
                                remove_field_buff(p1_field_zone[0])
                                player1_grave.append(p1_field_zone[0])
                                p1_field_zone[0] = None

                    elif player1_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p1_st_set1.card.card_name)

                            if p1_st_set1.card.super_type == "Spell":
                                player1_grave.append(p1_st_set1.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p1_st_set2.card.card_name)

                            if p1_st_set2.card.super_type == "Spell":
                                player1_grave.append(p1_st_set2.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p1_st_set3.card.card_name)

                            if p1_st_set3.card.super_type == "Spell":
                                player1_grave.append(p1_st_set3.card.card_name)
                                player1_st_zones[target-1] = None

                            break

                    elif get_card(player1_st_zones[target-1]).super_type != "Spell":
                        print("Not a valid target.")

                    else:
                        player1_grave.append(player1_st_zones[target-1])
                        player1_st_zones[target-1] = None

                        break

                elif which_player == 0:
                    if target == -1:
                        if p2_field_zone[0] == None:
                            print("Not a valid target.")

                        else:
                            if p2_field_zone[0] == "Set Card":
                                print("The Set card is: " + p2_field_set.card.card_name)

                                player2_grave.append(p2_field_set.card.card_name)
                                p2_field_zone[0] = None

                            else:
                                remove_field_buff(p2_field_zone[0])
                                player2_grave.append(p2_field_zone[0])
                                p2_field_zone[0] = None

                    elif player2_st_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_st_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            print("The Set card is: " + p2_st_set1.card.card_name)

                            if p2_st_set1.card.super_type == "Spell":
                                player2_grave.append(p2_st_set1.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            print("The Set card is: " + p2_st_set2.card.card_name)

                            if p2_st_set2.card.super_type == "Spell":
                                player1_grave.append(p2_st_set2.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            print("The Set card is: " + p2_st_set3.card.card_name)

                            if p2_st_set3.card.super_type == "Spell":
                                player2_grave.append(p2_st_set3.card.card_name)
                                player2_st_zones[target-1] = None

                            break

                    elif get_card(player2_st_zones[target-1]).super_type != "Trap":
                        print("Not a valid target.")

                    else:
                        player2_grave.append(player1_st_zones[target-1])
                        player2_st_zones[target-1] = None

                        break

    elif card == man_eater_bug:
        if curr_player == 1 and curr_phase == "bp":
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone: "))

                if which_player == 1:
                    if player1_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player1_grave.append(p1_set1.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player1_grave.append(p1_set2.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player1_grave.append(p1_set3.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                    else:
                        player1_grave.append(player1_monster_zones[target-1])
                        player1_monster_zones[target-1] = None

                        break

                elif which_player == 0:
                    if player2_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player2_grave.append(p2_set1.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player2_grave.append(p2_set2.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player2_grave.append(p2_set3.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                    else:
                        player2_grave.append(player2_monster_zones[target-1])
                        player2_monster_zones[target-1] = None

                        break

        elif curr_player == 2 and curr_phase == "bp":
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone: "))

                if which_player == 0:
                    if player1_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player1_grave.append(p1_set1.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player1_grave.append(p1_set2.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player1_grave.append(p1_set3.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                    else:
                        player1_grave.append(player1_monster_zones[target-1])
                        player1_monster_zones[target-1] = None

                        break

                elif which_player == 1:
                    if player2_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player2_grave.append(p2_set1.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player2_grave.append(p2_set2.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player2_grave.append(p2_set3.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                    else:
                        player2_grave.append(player2_monster_zones[target-1])
                        player2_monster_zones[target-1] = None

                        break

        elif curr_player == 1:
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone: "))

                if which_player == 0:
                    if player1_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player1_grave.append(p1_set1.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player1_grave.append(p1_set2.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player1_grave.append(p1_set3.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                    else:
                        player1_grave.append(player1_monster_zones[target-1])
                        player1_monster_zones[target-1] = None

                        break

                elif which_player == 1:
                    if player2_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player2_grave.append(p2_set1.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player2_grave.append(p2_set2.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player2_grave.append(p2_set3.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                    else:
                        player2_grave.append(player2_monster_zones[target-1])
                        player2_monster_zones[target-1] = None

                        break

        elif curr_player == 2:
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone: "))

                if which_player == 1:
                    if player1_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player1_grave.append(p1_set1.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player1_grave.append(p1_set2.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player1_grave.append(p1_set3.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                    else:
                        player1_grave.append(player1_monster_zones[target-1])
                        player1_monster_zones[target-1] = None

                        break

                elif which_player == 0:
                    if player2_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player2_grave.append(p2_set1.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player2_grave.append(p2_set2.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player2_grave.append(p2_set3.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                    else:
                        player2_grave.append(player2_monster_zones[target-1])
                        player2_monster_zones[target-1] = None

                        break

    elif card == hane_hane:
        if curr_player == 1 and curr_phase == "bp":
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone: "))

                if which_player == 1:
                    if player1_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player1_hand.player_hand.append(p1_set1.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player1_hand.player_hand.append(p1_set2.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player1_hand.player_hand.append(p1_set3.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                    else:
                        player1_hand.player_hand.append(player1_monster_zones[target-1])
                        player1_monster_zones[target-1] = None

                        break

                elif which_player == 0:
                    if player2_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player2_hand.player_hand.append(p2_set1.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player2_hand.player_hand.append(p2_set2.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player2_hand.player_hand.append(p2_set3.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                    else:
                        player2_hand.player_hand.append(player2_monster_zones[target-1])
                        player2_monster_zones[target-1] = None

                        break

        elif curr_player == 2 and curr_phase == "bp":
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone: "))

                if which_player == 0:
                    if player1_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player1_hand.player_hand.append(p1_set1.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player1_hand.player_hand.append(p1_set2.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player1_hand.player_hand.append(p1_set3.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                    else:
                        player1_hand.player_hand.append(player1_monster_zones[target-1])
                        player1_monster_zones[target-1] = None

                        break

                elif which_player == 1:
                    if player2_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player2_hand.player_hand.append(p2_set1.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player2_hand.player_hand.append(p2_set2.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player2_hand.player_hand.append(p2_set3.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                    else:
                        player2_hand.player_hand.append(player2_monster_zones[target-1])
                        player2_monster_zones[target-1] = None

                        break

        elif curr_player == 1:
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone: "))

                if which_player == 0:
                    if player1_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player1_hand.player_hand.append(p1_set1.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player1_hand.player_hand.append(p1_set2.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player1_hand.player_hand.append(p1_set3.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                    else:
                        player1_hand.player_hand.append(player1_monster_zones[target-1])
                        player1_monster_zones[target-1] = None

                        break

                elif which_player == 1:
                    if player2_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player2_hand.player_hand.append(p2_set1.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player2_hand.player_hand.append(p2_set2.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player2_hand.player_hand.append(p2_set3.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                    else:
                        player2_hand.player_hand.append(player2_monster_zones[target-1])
                        player2_monster_zones[target-1] = None

                        break

        elif curr_player == 2:
            while(1):
                which_player = int(input("Choose target player (You = 0 / Opp = 1): "))
                target = int(input("Choose target zone: "))

                if which_player == 1:
                    if player1_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player1_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player1_hand.player_hand.append(p1_set1.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player1_hand.player_hand.append(p1_set2.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player1_hand.player_hand.append(p1_set3.card.card_name)
                            player1_monster_zones[target-1] = None

                            break

                    else:
                        player1_hand.player_hand.append(player1_monster_zones[target-1])
                        player1_monster_zones[target-1] = None

                        break

                elif which_player == 0:
                    if player2_monster_zones[target-1] == None:
                        print("Not a valid target.")

                    elif player2_monster_zones[target-1] == "Set Card":
                        if target - 1 == 0:
                            player2_hand.player_hand.append(p2_set1.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 1:
                            player2_hand.player_hand.append(p2_set2.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                        elif target - 1 == 2:
                            player2_hand.player_hand.append(p2_set3.card.card_name)
                            player2_monster_zones[target-1] = None

                            break

                    else:
                        player2_hand.player_hand.append(player2_monster_zones[target-1])
                        player2_monster_zones[target-1] = None

                        break

    else:
        return print("This card does not have an effect.")

    return

# Handle switching phases
def phase_handler(player, phase):
    if curr_phase == "mp" and phase == "dp":
        print("Cannot enter Draw Phase")

    if curr_phase == "mp" and phase == "sp":
        print("Cannot enter Standby Phase")

    if curr_phase == "mp" and phase == "bp" and curr_player == player:
        battle_phase()
    
    if curr_phase == "mp" and phase == "ep" and curr_player == player:
        end_phase()

    if curr_phase == "bp" and phase == "ep" and curr_player == player:
        end_phase()

    if curr_phase == "bp" and (phase == "dp" or phase == "sp" or phase == "mp"):
        print("Cannot go back to previous phases")

# Draw phase, where the turn player draws one card from the top of their deck
def draw_phase():
    global curr_phase
    curr_phase = "dp"

    print("Entering Draw Phase")
    if curr_player == 1:
        draw_card(player1_deck, player1_hand)
        view_hand(player1_hand.player_hand)
    
    if curr_player == 2:
        draw_card(player2_deck, player2_hand)
        view_hand(player2_hand.player_hand)

    curr_phase = "sp"

# Standby phase, only traps can be activated during this phase
def standby_phase():
    print("Entering Standby Phase")
    time.sleep(0.5)

    if curr_player == 1:
        while(p2_st_set1 != None and p2_st_set2 != None and p2_st_set3 != None):
            inp = input("P2: Activate Trap (y/n): ")

            if inp == "y":
                activate_trap(2)

            else:
                break

    elif curr_player == 2:
        while(p1_st_set1 != None and p1_st_set2 != None and p1_st_set3 != None):
            inp = input("P1: Activate Trap (y/n): ")

            if inp == "y":
                activate_trap(1)

            else:
                break

    global curr_phase
    curr_phase = "mp"

# Main phase, the turn player can summon monsters during this phase. The turn player can activate Spells during this phase. Both players can activate Traps 
# during this phase
def main_phase():
    print("Entering Main Phase")
    global curr_player, has_summoned, just_set
    global p1_just_summoned_zone1, p1_just_summoned_zone2, p1_just_summoned_zone3
    global p2_just_summoned_zone1, p2_just_summoned_zone2, p2_just_summoned_zone3

    has_summoned = False
    
    p1_just_set1 = False
    p1_just_set2 = False
    p1_just_set3 = False
    p2_just_set1 = False
    p2_just_set2 = False
    p2_just_set3 = False

    p1_just_summoned_zone1 = False
    p1_just_summoned_zone2 = False
    p1_just_summoned_zone3 = False
    p2_just_summoned_zone1 = False
    p2_just_summoned_zone2 = False
    p2_just_summoned_zone3 = False

    while(1):
        if curr_player == 1:
            view_hand(player1_hand.player_hand)
        elif curr_player == 2:
            view_hand(player2_hand.player_hand)

        action = input("Choose action (type help for all options): ")

        if action == "summon":
            if has_summoned == True:
                print("Cannot summon twice in one turn.")
            else:
                monster = int(input("Choose monster: "))

                if curr_player == 1 and player1_hand.player_hand[monster-1].super_type != "Monster":
                    print("Cannot Summon a non-Monster card.")

                elif curr_player == 2 and player2_hand.player_hand[monster-1].super_type != "Monster":
                    print("Cannot Summon a non-Monster card.")

                else:
                    zone = int(input("Choose zone: "))

                    position = input("Normal Summon (ns) or Set (set): ")

                    if curr_player == 1 and player1_hand.player_hand[monster-1].level <= 4 and position == "set":
                        set_monster(monster, zone)

                        while(p2_st_set1 != None and p2_st_set2 != None and p2_st_set3 != None):
                            inp = input("P2: Activate Trap (y/n): ")

                            if inp == "y":
                                activate_trap(2)

                            else:
                                break

                    elif curr_player == 1 and player1_hand.player_hand[monster-1].level > 4 and position == "ns":
                        tribute_summon(monster, zone)

                        while(p2_st_set1 != None and p2_st_set2 != None and p2_st_set3 != None):
                            inp = input("P2: Activate Trap (y/n): ")

                            if inp == "y":
                                activate_trap(2)

                            else:
                                break

                        activate_field_on_summon(zone, p1_field_zone[0], p2_field_zone[0], curr_player)
                        dragon_capture_jar_on_summon(zone)

                    elif curr_player == 1 and player1_hand.player_hand[monster-1].level > 4 and position == "set":
                        tribute_set(monster, zone)

                        while(p2_st_set1 != None and p2_st_set2 != None and p2_st_set3 != None):
                            inp = input("P2: Activate Trap (y/n): ")

                            if inp == "y":
                                activate_trap(2)

                            else:
                                break

                    elif curr_player == 2 and player2_hand.player_hand[monster-1].level <= 4 and position == "set":
                        set_monster(monster, zone)

                        while(p1_st_set1 != None and p1_st_set2 != None and p1_st_set3 != None):
                            inp = input("P1: Activate Trap (y/n): ")

                            if inp == "y":
                                activate_trap(1)

                            else:
                                break

                    elif curr_player == 2 and player2_hand.player_hand[monster-1].level > 4 and position == "ns":
                        tribute_summon(monster, zone)

                        while(p1_st_set1 != None and p1_st_set2 != None and p1_st_set3 != None):
                            inp = input("P1: Activate Trap (y/n): ")

                            if inp == "y":
                                activate_trap(1)

                            else:
                                break

                        activate_field_on_summon(zone, p1_field_zone[0], p2_field_zone[0], curr_player)
                        dragon_capture_jar_on_summon(zone)

                    elif curr_player == 2 and player2_hand.player_hand[monster-1].level > 4 and position == "set":
                        tribute_set(monster, zone)

                        while(p1_st_set1 != None and p1_st_set2 != None and p1_st_set3 != None):
                            inp = input("P1: Activate Trap (y/n): ")

                            if inp == "y":
                                activate_trap(1)

                            else:
                                break

                    else:
                        normal_summon(monster, zone)

                        if curr_player == 1:
                            while(p2_st_set1 != None and p2_st_set2 != None and p2_st_set3 != None):
                                inp = input("P2: Activate Trap (y/n): ")

                                if inp == "y":
                                    activate_trap(2)

                                else:
                                    break

                        elif curr_player == 2:
                            while(p1_st_set1 != None and p1_st_set2 != None and p1_st_set3 != None):
                                inp = input("P1: Activate Trap (y/n): ")

                                if inp == "y":
                                    activate_trap(1)

                                else:
                                    break

                        activate_field_on_summon(zone, p1_field_zone[0], p2_field_zone[0], curr_player)
                        dragon_capture_jar_on_summon(zone)

        elif action == "flip":
            zone = int(input("Choose zone: "))

            flip_summon(zone)

            if curr_player == 1:
                while(p2_st_set1 != None and p2_st_set2 != None and p2_st_set3 != None):
                    inp = input("P2: Activate Trap (y/n): ")

                    if inp == "y":
                        activate_trap(2)

                    else:
                        break

            elif curr_player == 2:
                while(p1_st_set1 != None and p1_st_set2 != None and p1_st_set3 != None):
                    inp = input("P1: Activate Trap (y/n): ")

                    if inp == "y":
                        activate_trap(1)

                    else:
                        break

            activate_field_on_summon(zone, p1_field_zone[0], p2_field_zone[0], curr_player)
            dragon_capture_jar_on_summon(zone)

            view_field(curr_player)

            if curr_player == 1:
                flipped_card = get_card(player1_monster_zones[zone-1])

                if flipped_card.sub_type == "Flip":
                    can_activate = check_activation_requirement(flipped_card)

                    if can_activate:
                        activate_effect(flipped_card, zone)

            elif curr_player == 2:
                flipped_card = get_card(player2_monster_zones[zone-1])

                if flipped_card.sub_type == "Flip":
                    can_activate = check_activation_requirement(flipped_card)

                    if can_activate:
                        activate_effect(flipped_card)

        elif action == "switch":
            zone = int(input("Choose zone: "))

            switch_position(zone)

        elif action == "hand":
            if curr_player == 1:
                view_hand(player1_hand.player_hand)
            elif curr_player == 2:
                view_hand(player2_hand.player_hand)

        elif action == "field":
            view_field(curr_player)

        elif action == "grave":
            if curr_player == 1:
                while(1):
                    value = int(input("Your's (1) or Opponents (2): "))

                    if value == 1:
                        view_grave(1)
                        break

                    elif value == 2:
                        view_grave(2)
                        break

                    else:
                        print("Not a valid option.")

            elif curr_player == 2:
                while(1):
                    value = int(input("Your's (1) or Opponents (2): "))

                    if value == 1:
                        view_grave(2)
                        break

                    elif value == 2:
                        view_grave(1)
                        break

                    else:
                        print("Not a valid option.")

        elif action == "stats":
            card = input("Enter card: ")
            card_stats(card)

        elif action == "set":
            if curr_player == 1:
                while(1):
                    card = input("Choose card: ")

                    if get_card(card) not in player1_hand.player_hand:
                        print("Not a valid option.")

                    else:
                        if get_card(card).sub_type == "Field":
                            p1_field_set.card = get_card(card)
                            p1_field_zone[0] = p1_field_set.label

                            while(p2_st_set1 != None and p2_st_set2 != None and p2_st_set3 != None):
                                inp = input("P2: Activate Trap (y/n): ")

                                if inp == "y":
                                    activate_trap(2)

                                else:
                                    break

                        else:
                            while(1):
                                zone = int(input("Choose zone: "))

                                if player1_st_zones[zone-1] != None:
                                    print("Not a valid zone.")

                                else:
                                    if zone - 1 == 0:
                                        p1_st_set1.card = get_card(card)
                                        player1_st_zones[zone-1] = p1_st_set1.label
                                        player1_hand.player_hand.remove(get_card(card))
                                        break

                                    elif zone - 1 == 1:
                                        p1_st_set2.card = get_card(card)
                                        player1_st_zones[zone-1] = p1_st_set2.label
                                        player1_hand.player_hand.remove(get_card(card))
                                        break

                                    elif zone - 1 == 2:
                                        p1_st_set3.card = get_card(card)
                                        player1_st_zones[zone-1] = p1_st_set3.label
                                        player1_hand.player_hand.remove(get_card(card))
                                        break

                                    while(p2_st_set1 != None and p2_st_set2 != None and p2_st_set3 != None):
                                        inp = input("P2: Activate Trap (y/n): ")

                                        if inp == "y":
                                            activate_trap(2)

                                        else:
                                            break

                            break

            elif curr_player == 2:
                while(1):
                    card = input("Choose card: ")

                    if get_card(card) not in player2_hand.player_hand:
                        print("Not a valid option.")

                    else:
                        if get_card(card).sub_type == "Field":
                            p2_field_set.card = get_card(card)
                            p2_field_zone[0] = p2_field_set.label

                            while(p1_st_set1 != None and p1_st_set2 != None and p1_st_set3 != None):
                                inp = input("P1: Activate Trap (y/n): ")

                                if inp == "y":
                                    activate_trap(1)

                                else:
                                    break

                        else:
                            while(1):
                                zone = int(input("Choose zone: "))

                                if player2_st_zones[zone-1] != None:
                                    print("Not a valid zone.")

                                else:
                                    if zone - 1 == 0:
                                        p2_st_set1.card = get_card(card)
                                        player2_st_zones[zone-1] = p2_st_set1.label
                                        player2_hand.player_hand.remove(get_card(card))
                                        break

                                    elif zone - 1 == 1:
                                        p2_st_set2.card = get_card(card)
                                        player2_st_zones[zone-1] = p2_st_set2.label
                                        player2_hand.player_hand.remove(get_card(card))
                                        break

                                    elif zone - 1 == 2:
                                        p2_st_set3.card = get_card(card)
                                        player2_st_zones[zone-1] = p2_st_set3.label
                                        player2_hand.player_hand.remove(get_card(card))
                                        break

                                    while(p1_st_set1 != None and p1_st_set2 != None and p1_st_set3 != None):
                                        inp = input("P1: Activate Trap (y/n): ")

                                        if inp == "y":
                                            activate_trap(1)

                                        else:
                                            break

                            break

        elif action == "activate":
            if curr_player == 1:
                from_where = input("From field or hand: ")

                if from_where == "field":
                    activate = input("Choose card: ")

                    card = get_card(activate)

                    if card != p1_st_set1.card and card != p1_st_set2.card and card != p1_st_set3.card and card != p1_field_set.card:
                        print(card.card_name + " is not on your field.")

                    elif card.super_type == "Spell":
                        can_activate = check_activation_requirement(card)

                        if card.sub_type == "Field":
                            p1_field_zone[0] = p1_field_set.card.card_name
                            activate_effect(card, 0)

                            while(p2_st_set1 != None and p2_st_set2 != None and p2_st_set3 != None):
                                inp = input("P2: Activate Trap (y/n): ")

                                if inp == "y":
                                    activate_trap(2)

                                else:
                                    break

                        else:
                            while(can_activate):
                                if card == p1_st_set1.card:
                                    if card == swords_of_revealing_light:
                                        player1_st_zones[0] = card.card_name
                                        activate_effect(card, 0)
                                        break

                                    elif card.sub_type == "Equip":
                                        player1_st_zones[0] = card.card_name
                                        activate_effect(card, 0)
                                        break

                                    else:
                                        player1_st_zones[0] = p1_st_set1.card.card_name
                                        activate_effect(card, 0)
                                        player1_st_zones[0] = None
                                        player1_grave.append(card.card_name)

                                        if check_win_conditions == True:
                                            return

                                        break

                                elif card == p1_st_set2.card:
                                    if card == swords_of_revealing_light:
                                        player1_st_zones[1] = card.card_name
                                        activate_effect(card, 1)
                                        break

                                    elif card.sub_type == "Equip":
                                        player1_st_zones[1] = card.card_name
                                        activate_effect(card, 1)
                                        break

                                    else:
                                        player1_st_zones[1] = p1_st_set2.card.card_name
                                        activate_effect(card, 1)
                                        player1_st_zones[1] = None
                                        player1_grave.append(card.card_name)

                                        if check_win_conditions == True:
                                            return

                                        break

                                elif card == p1_st_set3.card:
                                    if card == swords_of_revealing_light:
                                        player1_st_zones[2] = card.card_name
                                        activate_effect(card, 2)
                                        break

                                    elif card.sub_type == "Equip":
                                        player1_st_zones[2] = card.card_name
                                        activate_effect(card, 2)
                                        break

                                    else:
                                        player1_st_zones[2] = p1_st_set3.card.card_name
                                        activate_effect(card, 2)
                                        player1_st_zones[2] = None
                                        player1_grave.append(card.card_name)

                                        if check_win_conditions == True:
                                            return

                                        break

                            while(p2_st_set1 != None and p2_st_set2 != None and p2_st_set3 != None):
                                inp = input("P2: Activate Trap (y/n): ")

                                if inp == "y":
                                    activate_trap(2)

                                else:
                                    break

                            
                elif from_where == "hand":
                    activate = input("Choose card: ")

                    card = get_card(activate)

                    if card not in player1_hand.player_hand:
                        print(card.card_name + " is not in your hand.")

                    elif card.super_type == "Spell":
                        can_activate = check_activation_requirement(card)

                        if card.sub_type == "Field":
                            p1_field_zone[0] = card.card_name
                            player1_hand.player_hand.remove(card)
                            activate_effect(card, 0)

                        else:
                            while(can_activate):
                                zone = int(input("Choose zone: "))

                                if zone - 1 > 2 or zone - 1 < 0:
                                    print("Not a valid zone.")

                                elif player1_st_zones[zone-1] != None:
                                    print("Not a valid zone.")

                                else:
                                    if card == swords_of_revealing_light:
                                        player1_st_zones[zone-1] = card.card_name
                                        player1_hand.player_hand.remove(card)
                                        activate_effect(card, zone)
                                        break

                                    elif card.sub_type == "Equip":
                                        player1_st_zones[zone-1] = card.card_name
                                        player1_hand.player_hand.remove(card)
                                        activate_effect(card, zone)
                                        break

                                    else:
                                        player1_st_zones[zone-1] = card.card_name
                                        player1_hand.player_hand.remove(card)
                                        activate_effect(card, zone)
                                        player1_st_zones[zone-1] = None
                                        player1_grave.append(card.card_name)

                                        if check_win_conditions == True:
                                            return

                                        break

                    while(p2_st_set1 != None and p2_st_set2 != None and p2_st_set3 != None):
                        inp = input("P2: Activate Trap (y/n): ")

                        if inp == "y":
                            activate_trap(2)

                        else:
                            break

            elif curr_player == 2:
                from_where = input("From field or hand: ")

                if from_where == "field":
                    activate = input("Choose card: ")

                    card = get_card(activate)

                    if card != p2_st_set1.card and card != p2_st_set2.card and card != p2_st_set3.card:
                        print(card.card_name + " is not on your field.")

                    elif card.super_type == "Spell":
                        can_activate = check_activation_requirement(card)

                        if card.sub_type == "Field":
                            p2_field_zone[0] = p2_field_set.card.card_name
                            activate_effect(card, 0)

                            while(p1_st_set1 != None and p1_st_set2 != None and p1_st_set3 != None):
                                inp = input("P1: Activate Trap (y/n): ")

                                if inp == "y":
                                    activate_trap(1)

                                else:
                                    break

                        else:
                            while(can_activate):
                                if card == p2_st_set1.card:
                                    if card == swords_of_revealing_light:
                                        player2_st_zones[0] = card.card_name
                                        activate_effect(card, 0)
                                        break

                                    elif card.sub_type == "Equip":
                                        player2_st_zones[0] = card.card_name
                                        activate_effect(card, 0)
                                        break

                                    else:
                                        player2_st_zones[0] = p2_st_set1.card.card_name
                                        activate_effect(card, 0)
                                        player2_st_zones[0] = None
                                        player2_grave.append(card.card_name)

                                        if check_win_conditions == True:
                                            return

                                        break

                                elif card == p2_st_set2.card:
                                    if card == swords_of_revealing_light:
                                        player2_st_zones[1] = card.card_name
                                        activate_effect(card, 1)
                                        break

                                    elif card.sub_type == "Equip":
                                        player2_st_zones[1] = card.card_name
                                        activate_effect(card, 1)
                                        break

                                    else:
                                        player2_st_zones[1] = p2_st_set2.card.card_name
                                        activate_effect(card, 1)
                                        player2_st_zones[1] = None
                                        player2_grave.append(card.card_name)

                                        if check_win_conditions == True:
                                            return

                                        break

                                elif card == p2_st_set3.card:
                                    if card == swords_of_revealing_light:
                                        player2_st_zones[2] = card.card_name
                                        activate_effect(card, 2)
                                        break

                                    elif card.sub_type == "Equip":
                                        player2_st_zones[2] = card.card_name
                                        activate_effect(card, 2)
                                        break

                                    else:
                                        player2_st_zones[2] = p2_st_set3.card.card_name
                                        activate_effect(card, 2)
                                        player2_st_zones[2] = None
                                        player2_grave.append(card.card_name)

                                        if check_win_conditions == True:
                                            return

                                        break

                            while(p1_st_set1 != None and p1_st_set2 != None and p1_st_set3 != None):
                                inp = input("P1: Activate Trap (y/n): ")

                                if inp == "y":
                                    activate_trap(1)

                                else:
                                    break

                elif from_where == "hand":
                    activate = input("Choose card: ")

                    card = get_card(activate)

                    if card not in player2_hand.player_hand:
                        print(card.card_name + " is not in your hand.")

                    elif card.super_type == "Spell":
                        can_activate = check_activation_requirement(card)

                        if card.sub_type == "Field":
                            p2_field_zone[0] = card.card_name
                            player2_hand.player_hand.remove(card)
                            activate_effect(card, 0)

                        else:
                            while(can_activate):
                                zone = int(input("Choose zone: "))

                                if zone - 1 > 2 or zone - 1 < 0:
                                    print("Not a valid zone.")

                                elif player2_st_zones[zone-1] != None:
                                    print("Not a valid zone.")

                                else:
                                    if card == swords_of_revealing_light:
                                        player2_st_zones[zone-1] = card.card_name
                                        player2_hand.player_hand.remove(card)
                                        activate_effect(card, zone)
                                        break

                                    elif card.sub_type == "Equip":
                                        player2_st_zones[zone-1] = card.card_name
                                        player2_hand.player_hand.remove(card)
                                        activate_effect(card, zone)
                                        break

                                    else:
                                        player2_st_zones[zone-1] = card.card_name
                                        player2_hand.player_hand.remove(card)
                                        activate_effect(card, zone)
                                        player2_st_zones[zone-1] = None
                                        player2_grave.append(card.card_name)

                                        if check_win_conditions == True:
                                            return

                                        break

                    while(p1_st_set1 != None and p1_st_set2 != None and p1_st_set3 != None):
                                inp = input("P1: Activate Trap (y/n): ")

                                if inp == "y":
                                    activate_trap(1)

                                else:
                                    break

        elif action == "help":
            list_actions()

        elif action == "end":
            return

# Battle phase, the turn player can target opponent's monsters for attack. During an attack, if the attack of one monster is higher than the other, the monster
# with less attack is destroyed and sent to the Graveyard and deal damage to the player who controlled the monster with less attack equal to the difference in attack. 
# If the defense of a monster is higher than the attack of an attacking monster, deal damage to the player who attacked equal to the difference between defense and attack,
# but the attacking monster is not destroyed.
def battle_phase():
    global curr_player, curr_phase, turn_counter, player1_lp, player2_lp
    global p1_monster1, p1_monster2, p1_monster3
    global p2_monster1, p2_monster2, p2_monster3
    global p1_has_attacked_zone1, p1_has_attacked_zone2, p1_has_attacked_zone3
    global p2_has_attacked_zone1, p2_has_attacked_zone2, p2_has_attacked_zone3
    global player1_monster_zones, player2_monster_zones
    global p1_pair_monster_equip1, p1_pair_monster_equip2, p1_pair_monster_equip3
    global p2_pair_monster_equip1, p2_pair_monster_equip2, p2_pair_monster_equip3

    curr_phase = "bp"

    #if turn_counter == 1:
    #    return print("Cannot enter Battle Phase on Turn 1.")

    print("Entering Battle Phase")

    p1_has_monster = has_monster(player1_monster_zones)
    p2_has_monster = has_monster(player2_monster_zones)

    # Reset has_attacked variables
    if curr_player == 1:
        p1_has_attacked_zone1 = False
        p1_has_attacked_zone2 = False
        p1_has_attacked_zone3 = False
    elif curr_player == 2:
        p2_has_attacked_zone1 = False
        p2_has_attacked_zone2 = False
        p2_has_attacked_zone3 = False

    if swords_of_revealing_light.card_name in player1_st_zones or swords_of_revealing_light.card_name in player2_st_zones:
        if curr_player == 1 and swords_of_revealing_light.card_name in player2_st_zones:
            p1_has_attacked_zone1 = True
            p1_has_attacked_zone2 = True
            p1_has_attacked_zone3 = True

        elif curr_player == 2 and swords_of_revealing_light.card_name in player1_st_zones:
            p2_has_attacked_zone1 = True
            p2_has_attacked_zone2 = True
            p2_has_attacked_zone3 = True

    while(1):
        view_field(curr_player)
        action = int(input("Choose monster to attack with or type -1 to end Battle Phase: "))
        if action == -1:
            break

        # Handles choosing a zone with no monster.
        elif curr_player == 1 and player1_monster_zones[action-1] == None:
            print("There is no monster at this zone.")
        elif curr_player == 2 and player2_monster_zones[action-1] == None:
            print("There is no monster at this zone.")

        # Handles trying to attack with the same monster multiple times in one turn.
        elif (action - 1 == 0 and p1_has_attacked_zone1 == True) or (action - 1 == 1 and p1_has_attacked_zone2 == True) or (action - 1 == 2 and p1_has_attacked_zone3 == True):
            print("This monster already attacked this turn.")
        elif (action - 1 == 0 and p2_has_attacked_zone1 == True) or (action - 1 == 1 and p2_has_attacked_zone2 == True) or (action - 1 == 2 and p2_has_attacked_zone3 == True):
            print("This monster already attacked this turn.")

        # Handles when player 1 attacks player 2 directly.
        elif curr_player == 1 and player2_monster_zones == [None, None, None]:
            if action - 1 == 0:
                player2_lp -= p1_monster1.attack
                print("Player 2 Lifepoints: " + str(player2_lp))

                p1_has_attacked_zone1 = True
            elif action - 1 == 1:
                player2_lp -= p1_monster2.attack
                print("Player 2 Lifepoints: " + str(player2_lp))

                p1_has_attacked_zone2 = True
            elif action - 1 == 2:
                player2_lp -= p1_monster3.attack
                print("Player 2 Lifepoints: " + str(player2_lp))

                p1_has_attacked_zone3 = True

        # Handles when player 1 attacks player 2 while player 2 has a monster.
        elif curr_player == 1 and p2_has_monster == True:
            target_zone = int(input("Choose opponent's monster to attack: "))

            if player2_monster_zones[target_zone-1] == None:
                print("There is no monster at this zone.")

            elif player2_monster_zones[target_zone-1] == "Set Card":
                attacking_set(target_zone)
                view_field(curr_player)

                if action - 1 == 0 and target_zone - 1 == 0:
                    if p1_monster1.attack > p2_monster1.defense:
                        if p2_monster1.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster1)

                            if can_activate:
                                activate_effect(p2_monster1, target_zone)

                        player2_grave.append(p2_monster1)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone1 = True

                    elif p1_monster1.attack < p2_monster1.defense:
                        player1_lp -= p2_monster1.defense - p1_monster1.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone1 = True

                        if p2_monster1.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster1)

                            if can_activate:
                                activate_effect(p2_monster1, target_zone)

                elif action - 1 == 0 and target_zone - 1 == 1:
                    if p1_monster1.attack > p2_monster2.defense:
                        if p2_monster2.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster2)

                            if can_activate:
                                activate_effect(p2_monster2, target_zone)

                        player2_grave.append(p2_monster2)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone1 = True

                    elif p1_monster1.attack < p2_monster2.defense:
                        player1_lp -= p2_monster2.defense - p1_monster1.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone1 = True

                        if p2_monster2.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster2)

                            if can_activate:
                                activate_effect(p2_monster2, target_zone)

                elif action - 1 == 0 and target_zone - 2 == 2:
                    if p1_monster1.attack > p2_monster3.defense:
                        if p2_monster3.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster3)

                            if can_activate:
                                activate_effect(p2_monster3, target_zone)

                        player2_grave.append(p2_monster3)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone1 = True

                    elif p1_monster1.attack < p2_monster3.defense:
                        player1_lp -= p2_monster3.defense - p1_monster1.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone1 = True

                        if p2_monster3.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster3)

                            if can_activate:
                                activate_effect(p2_monster3, target_zone)

                elif action - 1 == 1 and target_zone - 1 == 0:
                    if p1_monster2.attack > p2_monster1.defense:
                        if p2_monster1.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster1)

                            if can_activate:
                                activate_effect(p2_monster1, target_zone)

                        player2_grave.append(p2_monster1)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone2 = True

                    elif p1_monster2.attack < p2_monster1.defense:
                        player1_lp -= p2_monster1.defense - p1_monster2.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone2 = True

                        if p2_monster1.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster1)

                            if can_activate:
                                activate_effect(p2_monster1, target_zone)

                elif action - 1 == 1 and target_zone - 1 == 1:
                    if p1_monster2.attack > p2_monster2.defense:
                        if p2_monster2.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster2)

                            if can_activate:
                                activate_effect(p2_monster2, target_zone)

                        player2_grave.append(p2_monster2)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone2 = True

                    elif p1_monster2.attack < p2_monster2.defense:
                        player1_lp -= p2_monster2.defense - p1_monster2.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone2 = True

                        if p2_monster2.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster2)

                            if can_activate:
                                activate_effect(p2_monster2, target_zone)

                elif action - 1 == 1 and target_zone - 1 == 2:
                    if p1_monster2.attack > p2_monster3.defense:
                        if p2_monster3.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster3)

                            if can_activate:
                                activate_effect(p2_monster3, target_zone)

                        player2_grave.append(p2_monster3)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone2 = True

                    elif p1_monster2.attack < p2_monster3.defense:
                        player1_lp -= p2_monster3.defense - p1_monster2.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone2 = True

                        if p2_monster3.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster3)

                            if can_activate:
                                activate_effect(p2_monster3, target_zone)

                elif action - 1 == 2 and target_zone - 1 == 0:
                    if p1_monster3.attack > p2_monster1.defense:
                        if p2_monster1.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster1)

                            if can_activate:
                                activate_effect(p2_monster1, target_zone)

                        player2_grave.append(p2_monster1)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone3 = True

                    elif p1_monster3.attack < p2_monster1.defense:
                        player1_lp -= p2_monster1.defense - p1_monster3.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone3 = True

                        if p2_monster1.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster1)

                            if can_activate:
                                activate_effect(p2_monster1, target_zone)

                elif action - 1 == 2 and target_zone - 1 == 1:
                    if p1_monster2.attack > p2_monster2.defense:
                        if p2_monster2.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster2)

                            if can_activate:
                                activate_effect(p2_monster2, target_zone)
                        
                        player2_grave.append(p2_monster2)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone3 = True

                    elif p1_monster2.attack < p2_monster2.defense:
                        player1_lp -= p2_monster2.defense - p1_monster2.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone3 = True

                        if p2_monster2.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster2)

                            if can_activate:
                                activate_effect(p2_monster2, target_zone)

                elif action - 1 == 2 and target_zone - 1 == 2:
                    if p1_monster3.attack > p2_monster3.defense:
                        if p2_monster3.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster3)

                            if can_activate:
                                activate_effect(p2_monster3, target_zone)

                        player2_grave.append(p2_monster3)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone3 = True

                    elif p1_monster3.attack < p2_monster3.defense:
                        player1_lp -= p2_monster3.defense - p1_monster3.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone3 = True

                        if p2_monster3.sub_type == "Flip":
                            can_activate = check_activation_requirement(p2_monster3)

                            if can_activate:
                                activate_effect(p2_monster3, target_zone)

            elif player2_monster_zones[target_zone-1][len(player2_monster_zones[target_zone-1])-3:len(player2_monster_zones[target_zone-1])] == "(D)":
                if action - 1 == 0 and target_zone - 1 == 0:
                    if p1_monster1.attack > p2_monster1.defense:
                        player2_grave.append(p2_monster1)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone1 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster1.attack < p2_monster1.defense:
                        player1_lp -= p2_monster1.defense - p1_monster1.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone1 = True

                elif action - 1 == 0 and target_zone - 1 == 1:
                    if p1_monster1.attack > p2_monster2.defense:
                        player2_grave.append(p2_monster2)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone1 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster1.attack < p2_monster2.defense:
                        player1_lp -= p2_monster2.defense - p1_monster1.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone1 = True

                elif action - 1 == 0 and target_zone - 2 == 2:
                    if p1_monster1.attack > p2_monster3.defense:
                        player2_grave.append(p2_monster3)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone1 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster1.attack < p2_monster3.defense:
                        player1_lp -= p2_monster3.defense - p1_monster1.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone1 = True

                elif action - 1 == 1 and target_zone - 1 == 0:
                    if p1_monster2.attack > p2_monster1.defense:
                        player2_grave.append(p2_monster1)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone2 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster2.attack < p2_monster1.defense:
                        player1_lp -= p2_monster1.defense - p1_monster2.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone2 = True

                elif action - 1 == 1 and target_zone - 1 == 1:
                    if p1_monster2.attack > p2_monster2.defense:
                        player2_grave.append(p2_monster2)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone2 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster2.attack < p2_monster2.defense:
                        player1_lp -= p2_monster2.defense - p1_monster2.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone2 = True

                elif action - 1 == 1 and target_zone - 1 == 2:
                    if p1_monster2.attack > p2_monster3.defense:
                        player2_grave.append(p2_monster3)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone2 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster2.attack < p2_monster3.defense:
                        player1_lp -= p2_monster3.defense - p1_monster2.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone2 = True

                elif action - 1 == 2 and target_zone - 1 == 0:
                    if p1_monster3.attack > p2_monster1.defense:
                        player2_grave.append(p2_monster1)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone3 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster3.attack < p2_monster1.defense:
                        player1_lp -= p2_monster1.defense - p1_monster3.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone3 = True

                elif action - 1 == 2 and target_zone - 1 == 1:
                    if p1_monster2.attack > p2_monster2.defense:
                        player2_grave.append(p2_monster2)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone3 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster2.attack < p2_monster2.defense:
                        player1_lp -= p2_monster2.defense - p1_monster2.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone3 = True

                elif action - 1 == 2 and target_zone - 1 == 2:
                    if p1_monster3.attack > p2_monster3.defense:
                        player2_grave.append(p2_monster3)
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone3 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster3.attack < p2_monster3.defense:
                        player1_lp -= p2_monster3.defense - p1_monster3.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        p1_has_attacked_zone3 = True

            else:
                # Both players have at least one monster, both monsters are in Attack Position, and both monsters are in the left 
                # zone
                if action - 1 == 0 and target_zone - 1 == 0:
                    if p1_monster1.attack > p2_monster1.attack:
                        player2_lp -= p1_monster1.attack - p2_monster1.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone1 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster1.attack < p2_monster1.attack:
                        player1_lp -= p2_monster1.attack - p1_monster1.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[action-1])
                        player1_monster_zones[action-1] = None

                        check_remove_equips(action, 1)

                    else:
                        player1_grave.append(player1_monster_zones[action-1])
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player1_monster_zones[action-1] = None
                        player2_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 2)
                        check_remove_equips(action, 1)

                # Both players have at least one monster, both monsters are in Attack Position, and player 1's monster is in the 
                # left zone while player 2's monster is in the middle zone
                elif action - 1 == 0 and target_zone - 1 == 1:
                    if p1_monster1.attack > p2_monster2.attack:
                        player2_lp -= p1_monster1.attack - p2_monster2.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone1 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster1.attack < p2_monster2.attack:
                        player1_lp -= p2_monster2.attack - p1_monster1.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[action-1])
                        player1_monster_zones[action-1] = None

                        check_remove_equips(action, 1)

                    else:
                        player1_grave.append(player1_monster_zones[action-1])
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player1_monster_zones[action-1] = None
                        player2_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 2)
                        check_remove_equips(action, 1)

                # Both players have at least one monster, both monsters are in Attack Position, and player 1's monster is in the 
                # left zone while player 2's monster is in the right zone
                elif action - 1 == 0 and target_zone - 1 == 2:
                    if p1_monster1.attack > p2_monster3.attack:
                        player2_lp -= p1_monster1.attack - p2_monster3.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone1 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster1.attack < p2_monster3.attack:
                        player1_lp -= p2_monster3.attack - p1_monster1.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[action-1])
                        player1_monster_zones[action-1] = None

                        check_remove_equips(action, 1)

                    else:
                        player1_grave.append(player1_monster_zones[action-1])
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player1_monster_zones[action-1] = None
                        player2_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 2)
                        check_remove_equips(action, 1)

                # Both players have at least one monster, both monsters are in Attack Position, and player 1's monster is in the 
                # middle zone while player 2's monster is in the left zone
                elif action - 1 == 1 and target_zone - 1 == 0:
                    if p1_monster2.attack > p2_monster1.attack:
                        player2_lp -= p1_monster2.attack - p2_monster1.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone2 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster2.attack < p2_monster1.attack:
                        player1_lp -= p2_monster1.attack - p1_monster2.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[action-1])
                        player1_monster_zones[action-1] = None

                        check_remove_equips(action, 1)

                    else:
                        player1_grave.append(player1_monster_zones[action-1])
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player1_monster_zones[action-1] = None
                        player2_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 2)
                        check_remove_equips(action, 1)

                # Both players have at least one monster, both monsters are in Attack Position, and both monsters are in the middle
                # zone
                elif action - 1 == 1 and target_zone - 1 == 1:
                    if p1_monster2.attack > p2_monster2.attack:
                        player2_lp -= p1_monster2.attack - p2_monster2.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone2 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster2.attack < p2_monster2.attack:
                        player1_lp -= p2_monster2.attack - p1_monster2.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[action-1])
                        player1_monster_zones[action-1] = None

                        check_remove_equips(action, 1)

                    else:
                        player1_grave.append(player1_monster_zones[action-1])
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player1_monster_zones[action-1] = None
                        player2_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 2)
                        check_remove_equips(action, 1)

                # Both players have at least one monster, both monsters are in Attack Position, and player 1's monster is in the
                # middle zone while player 2's monster is in the right zone
                elif action - 1 == 1 and target_zone - 1 == 2:
                    if p1_monster2.attack > p2_monster3.attack:
                        player2_lp -= p1_monster2.attack - p2_monster3.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone2 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster2.attack < p2_monster3.attack:
                        player1_lp -= p2_monster3.attack - p1_monster2.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[action-1])
                        player1_monster_zones[action-1] = None

                        check_remove_equips(action, 1)

                    else:
                        player1_grave.append(player1_monster_zones[action-1])
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player1_monster_zones[action-1] = None
                        player2_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 2)
                        check_remove_equips(action, 1)

                # Both players have at least one monster, both monsters are in Attack Position, and player 1's monster is in the 
                # right zone while player 2's monster is in the left zone
                elif action - 1 == 2 and target_zone - 1 == 0:
                    if p1_monster3.attack > p2_monster1.attack:
                        player2_lp -= p1_monster3.attack - p2_monster1.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone3 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster3.attack < p2_monster1.attack:
                        player1_lp -= p2_monster1.attack - p1_monster3.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[action-1])
                        player1_monster_zones[action-1] = None

                        check_remove_equips(action, 1)

                    else:
                        player1_grave.append(player1_monster_zones[action-1])
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player1_monster_zones[action-1] = None
                        player2_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 2)
                        check_remove_equips(action, 1)

                # Both players have at least one monster, both monsters are in Attack Position, and player 1's monster is in the
                # right zone while player 2's monster is in the middle zone
                elif action - 1 == 2 and target_zone - 1 == 1:
                    if p1_monster3.attack > p2_monster2.attack:
                        player2_lp -= p1_monster3.attack - p2_monster2.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone3 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster3.attack < p2_monster2.attack:
                        player1_lp -= p2_monster2.attack - p1_monster3.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[action-1])
                        player1_monster_zones[action-1] = None

                        check_remove_equips(action, 1)

                    else:
                        player1_grave.append(player1_monster_zones[action-1])
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player1_monster_zones[action-1] = None
                        player2_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 2)
                        check_remove_equips(action, 1)

                # Both players have at least one monster, both monsters are in Attack Position, and both monsters are in the right
                # zone
                elif action - 1 == 2 and target_zone - 1 == 2:
                    if p1_monster3.attack > p2_monster3.attack:
                        player2_lp -= p1_monster3.attack - p2_monster3.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player2_monster_zones[target_zone-1] = None
                        p1_has_attacked_zone3 = True

                        check_remove_equips(target_zone, 2)

                    elif p1_monster3.attack < p2_monster3.attack:
                        player1_lp -= p2_monster3.attack - p1_monster3.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[action-1])
                        player1_monster_zones[action-1] = None

                        check_remove_equips(action, 1)

                    else:
                        player1_grave.append(player1_monster_zones[action-1])
                        player2_grave.append(player2_monster_zones[target_zone-1])
                        player1_monster_zones[action-1] = None
                        player2_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 2)
                        check_remove_equips(action, 1)

        # Handles if player 2 attacks player 1 directly.
        elif curr_player == 2 and player1_monster_zones == [None, None, None]:
            if action - 1 == 0:
                player1_lp -= p2_monster1.attack
                print("Player 1 Lifepoints: " + str(player1_lp))

                p2_has_attacked_zone1 = True
            elif action - 1 == 1:
                player1_lp -= p2_monster2.attack
                print("Player 1 Lifepoints: " + str(player1_lp))

                p2_has_attacked_zone2 = True
            elif action - 1 == 2:
                player1_lp -= p2_monster3.attack
                print("Player 1 Lifepoints: " + str(player1_lp))

                p2_has_attacked_zone3 = True

        # Handles if player 2 attacks player 1 while player 1 have a monster.
        elif curr_player == 2 and p1_has_monster == True:
            target_zone = int(input("Choose opponent's monster to attack: "))

            if player1_monster_zones[target_zone-1] == None:
                print("There is no monster at this zone.")

            elif player1_monster_zones[target_zone-1] == "Set Card":
                attacking_set(target_zone)
                view_field(curr_player)

                if action - 1 == 0 and target_zone - 1 == 0:
                    if p2_monster1.attack > p1_monster1.defense:
                        if p1_monster1.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster1)

                            if can_activate:
                                activate_effect(p1_monster1, target_zone)

                        player1_grave.append(p1_monster1)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone1 = True

                    elif p2_monster1.attack < p1_monster1.defense:
                        player2_lp -= p1_monster1.defense - p2_monster1.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone1 = True

                        if p1_monster1.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster1)

                            if can_activate:
                                activate_effect(p1_monster1, target_zone)

                elif action - 1 == 0 and target_zone - 1 == 1:
                    if p2_monster1.attack > p1_monster2.defense:
                        if p1_monster2.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster2)

                            if can_activate:
                                activate_effect(p1_monster2, target_zone)

                        player1_grave.append(p1_monster2)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone1 = True

                    elif p2_monster1.attack < p1_monster2.defense:
                        player2_lp -= p1_monster2.defense - p2_monster1.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone1 = True

                        if p1_monster2.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster2)

                            if can_activate:
                                activate_effect(p1_monster2, target_zone)

                elif action - 1 == 0 and target_zone - 2 == 2:
                    if p2_monster1.attack > p1_monster3.defense:
                        if p1_monster3.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster3)

                            if can_activate:
                                activate_effect(p1_monster3, target_zone)

                        player1_grave.append(p1_monster3)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone1 = True

                    elif p2_monster1.attack < p1_monster3.defense:
                        player2_lp -= p1_monster3.defense - p2_monster1.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone1 = True

                        if p1_monster3.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster3)

                            if can_activate:
                                activate_effect(p1_monster3, target_zone)

                elif action - 1 == 1 and target_zone - 1 == 0:
                    if p2_monster2.attack > p1_monster1.defense:
                        if p1_monster1.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster1)

                            if can_activate:
                                activate_effect(p1_monster1, target_zone)

                        player1_grave.append(p1_monster1)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone2 = True

                    elif p2_monster2.attack < p1_monster1.defense:
                        player2_lp -= p1_monster1.defense - p2_monster2.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone2 = True

                        if p1_monster1.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster1)

                            if can_activate:
                                activate_effect(p1_monster1, target_zone)

                elif action - 1 == 1 and target_zone - 1 == 1:
                    if p2_monster2.attack > p1_monster2.defense:
                        if p1_monster2.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster2)

                            if can_activate:
                                activate_effect(p1_monster2, target_zone)

                        player1_grave.append(p1_monster2)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone2 = True

                    elif p2_monster2.attack < p1_monster2.defense:
                        player2_lp -= p1_monster2.defense - p2_monster2.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone2 = True

                        if p1_monster2.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster2)

                            if can_activate:
                                activate_effect(p1_monster2, target_zone)

                elif action - 1 == 1 and target_zone - 1 == 2:
                    if p2_monster2.attack > p1_monster3.defense:
                        if p1_monster3.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster3)

                            if can_activate:
                                activate_effect(p1_monster3, target_zone)

                        player1_grave.append(p1_monster3)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone2 = True

                    elif p2_monster2.attack < p1_monster3.defense:
                        player2_lp -= p1_monster3.defense - p2_monster2.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone2 = True

                        if p1_monster3.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster3)

                            if can_activate:
                                activate_effect(p1_monster3, target_zone)

                elif action - 1 == 2 and target_zone - 1 == 0:
                    if p2_monster3.attack > p1_monster1.defense:
                        if p1_monster1.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster1)

                            if can_activate:
                                activate_effect(p1_monster1, target_zone)

                        player1_grave.append(p1_monster1)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone3 = True

                    elif p2_monster3.attack < p1_monster1.defense:
                        player2_lp -= p1_monster1.defense - p2_monster3.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone3 = True

                        if p1_monster1.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster1)

                            if can_activate:
                                activate_effect(p1_monster1, target_zone)

                elif action - 1 == 2 and target_zone - 1 == 1:
                    if p2_monster2.attack > p1_monster2.defense:
                        if p1_monster2.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster2)

                            if can_activate:
                                activate_effect(p1_monster2, target_zone)

                        player1_grave.append(p1_monster2)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone3 = True

                    elif p2_monster2.attack < p1_monster2.defense:
                        player2_lp -= p1_monster2.defense - p2_monster2.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone3 = True

                        if p1_monster2.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster2)

                            if can_activate:
                                activate_effect(p1_monster2, target_zone)

                elif action - 1 == 2 and target_zone - 1 == 2:
                    if p2_monster3.attack > p1_monster3.defense:
                        if p1_monster3.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster3)

                            if can_activate:
                                activate_effect(p1_monster3, target_zone)

                        player1_grave.append(p1_monster3)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone3 = True

                    elif p2_monster3.attack < p1_monster3.defense:
                        player2_lp -= p1_monster3.defense - p2_monster3.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone3 = True

                        if p1_monster3.sub_type == "Flip":
                            can_activate = check_activation_requirement(p1_monster3)

                            if can_activate:
                                activate_effect(p1_monster3, target_zone)

            elif player1_monster_zones[target_zone-1][len(player1_monster_zones[target_zone-1])-3:len(player1_monster_zones[target_zone-1])] == "(D)":
                if action - 1 == 0 and target_zone - 1 == 0:
                    if p2_monster1.attack > p1_monster1.defense:
                        player1_grave.append(p1_monster1)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone1 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster1.attack < p1_monster1.defense:
                        player2_lp -= p1_monster1.defense - p2_monster1.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone1 = True

                elif action - 1 == 0 and target_zone - 1 == 1:
                    if p2_monster1.attack > p1_monster2.defense:
                        player1_grave.append(p1_monster2)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone1 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster1.attack < p1_monster2.defense:
                        player2_lp -= p1_monster2.defense - p2_monster1.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone1 = True

                elif action - 1 == 0 and target_zone - 2 == 2:
                    if p2_monster1.attack > p1_monster3.defense:
                        player1_grave.append(p1_monster3)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone1 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster1.attack < p1_monster3.defense:
                        player2_lp -= p1_monster3.defense - p2_monster1.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone1 = True

                elif action - 1 == 1 and target_zone - 1 == 0:
                    if p2_monster2.attack > p1_monster1.defense:
                        player1_grave.append(p1_monster1)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone2 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster2.attack < p1_monster1.defense:
                        player2_lp -= p1_monster1.defense - p2_monster2.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone2 = True

                elif action - 1 == 1 and target_zone - 1 == 1:
                    if p2_monster2.attack > p1_monster2.defense:
                        player1_grave.append(p1_monster2)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone2 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster2.attack < p1_monster2.defense:
                        player2_lp -= p1_monster2.defense - p2_monster2.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone2 = True

                elif action - 1 == 1 and target_zone - 1 == 2:
                    if p2_monster2.attack > p1_monster3.defense:
                        player1_grave.append(p1_monster3)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone2 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster2.attack < p1_monster3.defense:
                        player2_lp -= p1_monster3.defense - p2_monster2.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone2 = True

                elif action - 1 == 2 and target_zone - 1 == 0:
                    if p2_monster3.attack > p1_monster1.defense:
                        player1_grave.append(p1_monster1)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone3 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster3.attack < p1_monster1.defense:
                        player2_lp -= p1_monster1.defense - p2_monster3.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone3 = True

                elif action - 1 == 2 and target_zone - 1 == 1:
                    if p2_monster2.attack > p1_monster2.defense:
                        player1_grave.append(p1_monster2)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone3 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster2.attack < p1_monster2.defense:
                        player2_lp -= p1_monster2.defense - p2_monster2.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone3 = True

                elif action - 1 == 2 and target_zone - 1 == 2:
                    if p2_monster3.attack > p1_monster3.defense:
                        player1_grave.append(p1_monster3)
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone3 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster3.attack < p1_monster3.defense:
                        player2_lp -= p1_monster3.defense - p2_monster3.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        p2_has_attacked_zone3 = True

            else:
                if action - 1 == 0 and target_zone - 1 == 0:
                    if p2_monster1.attack > p1_monster1.attack:
                        player1_lp -= p2_monster1.attack - p1_monster1.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone1 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster1.attack < p1_monster1.attack:
                        player2_lp -= p1_monster1.attack - p2_monster1.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[action-1])
                        player2_monster_zones[action-1] = None

                        check_remove_equips(action, 2)

                    else:
                        player2_grave.append(player2_monster_zones[action-1])
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player2_monster_zones[action-1] = None
                        player1_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 1)
                        check_remove_equips(action, 2)

                elif action - 1 == 0 and target_zone - 1 == 1:
                    if p2_monster1.attack > p1_monster2.attack:
                        player1_lp -= p2_monster1.attack - p1_monster2.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone1 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster1.attack < p1_monster2.attack:
                        player2_lp -= p1_monster2.attack - p2_monster1.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[action-1])
                        player2_monster_zones[action-1] = None

                        check_remove_equips(action, 2)

                    else:
                        player2_grave.append(player2_monster_zones[action-1])
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player2_monster_zones[action-1] = None
                        player1_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 1)
                        check_remove_equips(action, 2)

                elif action - 1 == 0 and target_zone - 1 == 2:
                    if p2_monster1.attack > p1_monster3.attack:
                        player1_lp -= p2_monster1.attack - p1_monster3.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone1 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster1.attack < p1_monster3.attack:
                        player2_lp -= p1_monster3.attack - p2_monster1.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[action-1])
                        player2_monster_zones[action-1] = None

                        check_remove_equips(action, 2)

                    else:
                        player2_grave.append(player2_monster_zones[action-1])
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player2_monster_zones[action-1] = None
                        player1_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 1)
                        check_remove_equips(action, 2)

                elif action - 1 == 1 and target_zone - 1 == 0:
                    if p2_monster2.attack > p1_monster1.attack:
                        player1_lp -= p2_monster2.attack - p1_monster1.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone2 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster2.attack < p1_monster1.attack:
                        player2_lp -= p1_monster1.attack - p2_monster2.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[action-1])
                        player2_monster_zones[action-1] = None

                        check_remove_equips(action, 2)

                    else:
                        player2_grave.append(player2_monster_zones[action-1])
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player2_monster_zones[action-1] = None
                        player1_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 1)
                        check_remove_equips(action, 2)

                elif action - 1 == 1 and target_zone - 1 == 1:
                    if p2_monster2.attack > p1_monster2.attack:
                        player1_lp -= p2_monster2.attack - p1_monster2.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone2 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster2.attack < p1_monster2.attack:
                        player2_lp -= p1_monster2.attack - p2_monster2.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[action-1])
                        player2_monster_zones[action-1] = None

                        check_remove_equips(action, 2)

                    else:
                        player2_grave.append(player2_monster_zones[action-1])
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player2_monster_zones[action-1] = None
                        player1_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 1)
                        check_remove_equips(action, 2)

                elif action - 1 == 1 and target_zone - 1 == 2:
                    if p2_monster2.attack > p1_monster3.attack:
                        player1_lp -= p2_monster2.attack - p1_monster3.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone2 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster2.attack < p1_monster3.attack:
                        player2_lp -= p1_monster3.attack - p2_monster2.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[action-1])
                        player2_monster_zones[action-1] = None

                        check_remove_equips(action, 2)

                    else:
                        player2_grave.append(player2_monster_zones[action-1])
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player2_monster_zones[action-1] = None
                        player1_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 1)
                        check_remove_equips(action, 2)

                elif action - 1 == 2 and target_zone - 1 == 0:
                    if p2_monster3.attack > p1_monster1.attack:
                        player1_lp -= p2_monster3.attack - p1_monster1.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone3 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster3.attack < p1_monster1.attack:
                        player2_lp -= p1_monster1.attack - p2_monster3.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[action-1])
                        player2_monster_zones[action-1] = None

                        check_remove_equips(action, 2)

                    else:
                        player2_grave.append(player2_monster_zones[action-1])
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player2_monster_zones[action-1] = None
                        player1_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 1)
                        check_remove_equips(action, 2)

                elif action - 1 == 2 and target_zone - 1 == 1:
                    if p2_monster3.attack > p1_monster2.attack:
                        player1_lp -= p2_monster3.attack - p1_monster2.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone3 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster3.attack < p1_monster2.attack:
                        player2_lp -= p1_monster2.attack - p2_monster3.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[action-1])
                        player2_monster_zones[action-1] = None

                        check_remove_equips(action, 2)

                    else:
                        player2_grave.append(player2_monster_zones[action-1])
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player2_monster_zones[action-1] = None
                        player1_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 1)
                        check_remove_equips(action, 2)

                elif action - 1 == 2 and target_zone - 1 == 2:
                    if p2_monster3.attack > p1_monster3.attack:
                        player1_lp -= p2_monster3.attack - p1_monster3.attack
                        print("Player 1 Lifepoints: " + str(player1_lp))
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player1_monster_zones[target_zone-1] = None
                        p2_has_attacked_zone3 = True

                        check_remove_equips(target_zone, 1)

                    elif p2_monster3.attack < p1_monster3.attack:
                        player2_lp -= p1_monster3.attack - p2_monster3.attack
                        print("Player 2 Lifepoints: " + str(player2_lp))
                        player2_grave.append(player2_monster_zones[action-1])
                        player2_monster_zones[action-1] = None

                        check_remove_equips(action, 2)

                    else:
                        player2_grave.append(player2_monster_zones[action-1])
                        player1_grave.append(player1_monster_zones[target_zone-1])
                        player2_monster_zones[action-1] = None
                        player1_monster_zones[target_zone-1] = None

                        check_remove_equips(target_zone, 1)
                        check_remove_equips(action, 2)

# End phase, traps can be activated during this phase. Transition to next player's Draw Phase.
def end_phase():
    print("Entering End Phase")
    global turn_counter, curr_player, curr_phase
    global p1_swords_counter1, p1_swords_counter2, p1_swords_counter3
    global p2_swords_counter1, p2_swords_counter2, p2_swords_counter3

    curr_phase = "ep"

    if curr_player == 1:
        while(p2_st_set1 != None and p2_st_set2 != None and p2_st_set3 != None):
            inp = input("P2: Activate Trap (y/n): ")

            if inp == "y":
                activate_trap(2)

            else:
                break

    elif curr_player == 2:
        while(p1_st_set1 != None and p1_st_set2 != None and p1_st_set3 != None):
            inp = input("P1: Activate Trap (y/n): ")

            if inp == "y":
                activate_trap(1)

            else:
                break

    if curr_player == 1:
        if swords_of_revealing_light.card_name in player2_st_zones:
            swords_index = player2_st_zones.index(swords_of_revealing_light.card_name)

            if swords_index == 0:
                p2_swords_counter1 += 1

                if p2_swords_counter1 >= 3:
                    player2_grave.append(swords_of_revealing_light.card_name)
                    player2_st_zones[swords_index] = None

            elif swords_index == 1:
                p2_swords_counter2 += 1

                if p2_swords_counter2 >= 3:
                    player2_grave.append(swords_of_revealing_light.card_name)
                    player2_st_zones[swords_index] = None

            elif swords_index == 2:
                p2_swords_counter3 += 1

                if p2_swords_counter3 >= 3:
                    player2_grave.append(swords_of_revealing_light.card_name)
                    player2_st_zones[swords_index] = None

        curr_player = 2
        turn_counter += 1

    elif curr_player == 2:
        if swords_of_revealing_light.card_name in player1_st_zones:
            swords_index = player1_st_zones.index(swords_of_revealing_light.card_name)

            if swords_index == 0:
                p1_swords_counter1 += 1

                if p1_swords_counter1 >= 3:
                    player1_grave.append(swords_of_revealing_light.card_name)
                    player1_st_zones[swords_index] = None

            elif swords_index == 1:
                p1_swords_counter2 += 1

                if p1_swords_counter2 >= 3:
                    player1_grave.append(swords_of_revealing_light.card_name)
                    player1_st_zones[swords_index] = None

            elif swords_index == 2:
                p1_swords_counter3 += 1

                if p1_swords_counter3 >= 3:
                    player1_grave.append(swords_of_revealing_light.card_name)
                    player1_st_zones[swords_index] = None

        curr_player = 1
        turn_counter += 1

# Normal summon a monster from hand. To normal summon, the monster must be level 4 or lower. There is a total of 3 monster zones per player. If all 3 zones are occupied,
# then that player cannot summon any monsters. 
def normal_summon(monster, zone):
    global curr_player, has_summoned
    global p1_monster1, p1_monster2, p1_monster3
    global p2_monster1, p2_monster2, p2_monster3
    global p1_just_summoned_zone1, p1_just_summoned_zone2, p1_just_summoned_zone3
    global p2_just_summoned_zone1, p2_just_summoned_zone2, p2_just_summoned_zone3

    if curr_player == 1:
        if player1_monster_zones[zone-1] != None:
            return print("A monster already occupies that zone.")

        else:
            if zone - 1 == 0:
                p1_monster1 = copy(player1_hand.player_hand[monster-1])
                player1_monster_zones[zone-1] = p1_monster1.card_name
                player1_hand.player_hand.pop(monster-1)
                p1_just_summoned_zone1 = True

            elif zone - 1 == 1:
                p1_monster2 = copy(player1_hand.player_hand[monster-1])
                player1_monster_zones[zone-1] = p1_monster2.card_name
                player1_hand.player_hand.pop(monster-1)
                p1_just_summoned_zone2 = True

            elif zone - 1 == 2:
                p1_monster3 = copy(player1_hand.player_hand[monster-1])
                player1_monster_zones[zone-1] = p1_monster3.card_name
                player1_hand.player_hand.pop(monster-1)
                p1_just_summoned_zone3 = True

            has_summoned = True

    elif curr_player == 2:
        if player2_monster_zones[zone-1] != None:
            return print("A monster already occupies that zone.")

        else:
            if zone - 1 == 0:
                p2_monster1 = copy(player2_hand.player_hand[monster-1])
                player2_monster_zones[zone-1] = p2_monster1.card_name
                player2_hand.player_hand.pop(monster-1)
                p2_just_summoned_zone1 = True

            elif zone - 1 == 1:
                p2_monster2 = copy(player2_hand.player_hand[monster-1])
                player2_monster_zones[zone-1] = p2_monster2.card_name
                player2_hand.player_hand.pop(monster-1)
                p2_just_summoned_zone2 = True

            elif zone - 1 == 2:
                p2_monster3 = copy(player2_hand.player_hand[monster-1])
                player2_monster_zones[zone-1] = p2_monster3.card_name
                player2_hand.player_hand.pop(monster-1)
                p2_just_summoned_zone3 = True

            has_summoned = True

# Handles summoning a Monster in the Set position. This summons the monster in face-down defense position.
def set_monster(monster, zone):
    global curr_player, has_summoned, just_set
    global p1_set1, p1_set2, p1_set3
    global p2_set1, p2_set2, p2_set3
    global p1_monster1, p1_monster2, p1_monster3
    global p2_monster1, p2_monster2, p2_monster3
    global p1_just_summoned_zone1, p1_just_summoned_zone2, p1_just_summoned_zone3
    global p2_just_summoned_zone1, p2_just_summoned_zone2, p2_just_summoned_zone3

    if curr_player == 1:
        if player1_monster_zones[zone-1] != None:
            return print("A monster already occupies that zone.")
        else:
            if zone - 1 == 0:
                p1_set1.card = player1_hand.player_hand[monster-1]

                player1_monster_zones.pop(zone-1)
                player1_monster_zones.insert(zone-1, p1_set1.label)
                player1_hand.player_hand.pop(monster-1)
                p1_monster1 = copy(p1_set1.card)

                p1_just_set1 = True
                has_summoned = True
                p1_just_summoned_zone1 = True

            elif zone - 1 == 1:
                p1_set2.card = player1_hand.player_hand[monster-1]

                player1_monster_zones.pop(zone-1)
                player1_monster_zones.insert(zone-1, p1_set2.label)
                player1_hand.player_hand.pop(monster-1)
                p1_monster2 = copy(p1_set2.card)

                p1_just_set2 = True
                has_summoned = True
                p1_just_summoned_zone2 = True

            elif zone - 1 == 2:
                p1_set3.card = player1_hand.player_hand[monster-1]

                player1_monster_zones.pop(zone-1)
                player1_monster_zones.insert(zone-1, p1_set3.label)
                player1_hand.player_hand.pop(monster-1)
                p1_monster3 = copy(p1_set3.card)

                p1_just_set3 = True
                has_summoned = True
                p1_just_summoned_zone3 = True

    elif curr_player == 2:
        if player2_monster_zones[zone-1] != None:
            return print("A monster already occupies that zone.")
        else:
            if zone - 1 == 0:
                p2_set1.card = player2_hand.player_hand[monster-1]

                player2_monster_zones.pop(zone-1)
                player2_monster_zones.insert(zone-1, p2_set1.label)
                player2_hand.player_hand.pop(monster-1)
                p2_monster1 = copy(p2_set1.card)

                p2_just_set1 = True
                has_summoned = True
                p2_just_summoned_zone1 = True

            elif zone - 1 == 1:
                p2_set2.card = player2_hand.player_hand[monster-1]

                player2_monster_zones.pop(zone-1)
                player2_monster_zones.insert(zone-1, p2_set2.label)
                player2_hand.player_hand.pop(monster-1)
                p2_monster2 = copy(p2_set2.card)

                p2_just_set2 = True
                has_summoned = True
                p2_just_summoned_zone2 = True

            elif zone - 1 == 2:
                p2_set3.card = player2_hand.player_hand[monster-1]

                player2_monster_zones.pop(zone-1)
                player2_monster_zones.insert(zone-1, p2_set3.label)
                player2_hand.player_hand.pop(monster-1)
                p2_monster3 = copy(p2_set3.card)

                p2_just_set3 = True
                has_summoned = True
                p2_just_summoned_zone3 = True

# Handles Flip Summoning a Set Monster. This takes a monster which is in the Set position, and changes it to face-up attack position.
def flip_summon(zone):
    global curr_player
    global p1_monster1, p1_monster2, p1_monster3
    global p2_monster1, p2_monster2, p2_monster3
    global p1_set1, p1_set2, p1_set3
    global p2_set1, p2_set2, p2_set3
    global p1_just_set1, p1_just_set2, p1_just_set3
    global p2_just_set1, p2_just_set2, p2_just_set3
    global p1_just_summoned_zone1, p1_just_summoned_zone2, p1_just_summoned_zone3
    global p2_just_summoned_zone1, p2_just_summoned_zone2, p2_just_summoned_zone3

    if curr_player == 1:
        if player1_monster_zones[zone - 1] != "Set Card":
            return print("Cannot Flip Summon this monster.")

        else:
            if zone - 1 == 0:
                if p1_just_set1 == True:
                    return print("Cannot Flip Summon the same turn it was Set.")

                p1_monster1 = copy(p1_set1.card)
                player1_monster_zones[zone-1] = p1_monster1.card_name
                p1_just_summoned_zone1 = True

            elif zone - 1 == 1:
                if p1_just_set2 == True:
                    return print("Cannot Flip Summon the same turn it was Set.")

                p1_monster2 = copy(p1_set2.card)
                player1_monster_zones[zone-1] = p1_monster2.card_name
                p1_just_summoned_zone2 = True

            elif zone - 1 == 2:
                if p1_just_set3 == True:
                    return print("Cannot Flip Summon the same turn it was Set.")

                p1_monster3 = copy(p1_set3.card)
                player1_monster_zones[zone-1] = p1_monster3.card_name
                p1_just_summoned_zone3 = True

            else:
                return print("Not a choosable Monster zone.")

    elif curr_player == 2:
        if player2_monster_zones[zone - 1] != "Set Card":
            return print("Cannot Flip Summon this monster.")
        else:
            if zone - 1 == 0:
                if p2_just_set1 == True:
                    return print("Cannot Flip Summon the same turn it was Set.")

                p2_monster1 = copy(p2_set1.card)
                player2_monster_zones[zone-1] = p2_monster1.card_name
                p2_just_summoned_zone1 = True

            elif zone - 1 == 1:
                if p2_just_set2 == True:
                    return print("Cannot Flip Summon the same turn it was Set.")

                p2_monster2 = copy(p2_set2.card)
                player2_monster_zones[zone-1] = p2_monster2.card_name
                p2_just_summoned_zone2 = True

            elif zone - 1 == 2:
                if p2_just_set3 == True:
                    return print("Cannot Flip Summon the same turn it was Set.")

                p2_monster3 = copy(p2_set3.card)
                player2_monster_zones[zone-1] = p2_monster3.card_name
                p2_just_summoned_zone3 = True

            else:
                return print("Not a choosable Monster zone.")

# Handles Tribute Summoning. Monsters with levels greater than 4 must be Tribute Summoned. A monster whose level is either 5 or 6 
# needs only 1 tribute. A monster whose level is greater than 6 needs 2 tributes. Tributed monsters are sent to the Graveyard.
def tribute_summon(monster, zone):
    global curr_player, has_summoned
    global p1_monster1, p1_monster2, p1_monster3
    global p2_monster1, p2_monster2, p2_monster3
    global p1_just_summoned_zone1, p1_just_summoned_zone2, p1_just_summoned_zone3
    global p2_just_summoned_zone1, p2_just_summoned_zone2, p2_just_summoned_zone3

    if curr_player == 1:
        if player1_hand.player_hand[monster-1].level == 5 or player1_hand.player_hand[monster-1].level == 6:
            view_field(curr_player)
            action = int(input("Choose a monster to tribute: "))

            player1_grave.append(player1_monster_zones[action-1])
            player1_monster_zones.pop(action-1)

            if zone - 1 == 0:
                p1_monster1 = copy(player1_hand.player_hand[monster-1])
                player1_monster_zones.insert(zone-1, p1_monster1.card_name)
                player1_hand.player_hand.pop(monster-1)

                p1_just_summoned_zone1 = True

            elif zone - 1 == 1:
                p1_monster2 = copy(player1_hand.player_hand[monster-1])
                player1_monster_zones.insert(zone-1, p1_monster2.card_name)
                player1_hand.player_hand.pop(monster-1)

                p1_just_summoned_zone2 = True

            elif zone - 1 == 2:
                p1_monster3 = copy(player1_hand.player_hand[monster-1])
                player1_monster_zones.insert(zone-1, p1_monster3.card_name)
                player1_hand.player_hand.pop(monster-1)

                p1_just_summoned_zone3 = True

            has_summoned = True

        elif player1_hand.player_hand[monster-1].level > 6:
            view_field(curr_player)
            action1 = int(input("Choose the first monster to tribute: "))
            action2 = int(input("Choose the second monster to tribute: "))

            player1_grave.append(player1_monster_zones[action1-1])
            player1_grave.append(player1_monster_zones[action2-1])

            if action1 > action2:
                player1_monster_zones.pop(action1-1)
                player1_monster_zones.pop(action2-1)
            elif action1 < action2:
                player1_monster_zones.pop(action2-1)
                player1_monster_zones.pop(action1-1)

            player1_monster_zones.insert(action1-1, None)
            player1_monster_zones.insert(action2-1, None)
            player1_monster_zones.pop(zone-1)

            if zone - 1 == 0:
                p1_monster1 = copy(player1_hand.player_hand[monster-1])
                player1_monster_zones.insert(zone-1, p1_monster1.card_name)
                player1_hand.player_hand.pop(monster-1)

                p1_just_summoned_zone1 = True

            elif zone - 1 == 1:
                p1_monster2 = copy(player1_hand.player_hand[monster-1])
                player1_monster_zones.insert(zone-1, p1_monster2.card_name)
                player1_hand.player_hand.pop(monster-1)

                p1_just_summoned_zone2 = True

            elif zone - 1 == 2:
                p1_monster3 = copy(player1_hand.player_hand[monster-1])
                player1_monster_zones.insert(zone-1, p1_monster3.card_name)
                player1_hand.player_hand.pop(monster-1)

                p1_just_summoned_zone3 = True

            has_summoned = True

    elif curr_player == 2:
        if player2_hand.player_hand[monster-1].level == 5 or player2_hand.player_hand[monster-1].level == 6:
            view_field(curr_player)
            action = int(input("Choose a monster to tribute: "))

            player2_grave.append(player2_monster_zones[action-1])
            player2_monster_zones.pop(action-1)
            
            if zone - 1 == 0:
                p2_monster1 = copy(player2_hand.player_hand[monster-1])
                player2_monster_zones.insert(zone-1, p2_monster1.card_name)
                player2_hand.player_hand.pop(monster-1)

                p2_just_summoned_zone1 = True

            elif zone - 1 == 1:
                p2_monster2 = copy(player2_hand.player_hand[monster-1])
                player2_monster_zones.insert(zone-1, p2_monster2.card_name)
                player2_hand.player_hand.pop(monster-1)

                p2_just_summoned_zone2 = True

            elif zone - 1 == 2:
                p2_monster3 = copy(player2_hand.player_hand[monster-1])
                player2_monster_zones.insert(zone-1, p2_monster3.card_name)
                player2_hand.player_hand.pop(monster-1)

                p2_just_summoned_zone3 = True

            has_summoned = True

        elif player2_hand.player_hand[monster-1].level > 6:
            view_field(curr_player)
            action1 = int(input("Choose the first monster to tribute: "))
            action2 = int(input("Choose the second monster to tribute: "))

            player2_grave.append(player2_monster_zones[action1-1])
            player2_grave.append(player2_monster_zones[action2-1])

            if action1 > action2:
                player2_monster_zones.pop(action1-1)
                player2_monster_zones.pop(action2-1)
            elif action1 < action2:
                player2_monster_zones.pop(action2-1)
                player2_monster_zones.pop(action1-1)

            player2_monster_zones.insert(action1-1, None)
            player2_monster_zones.insert(action2-1, None)
            player2_monster_zones.pop(zone-1)

            if zone - 1 == 0:
                p2_monster1 = copy(player2_hand.player_hand[monster-1])
                player2_monster_zones.insert(zone-1, p2_monster1.card_name)
                player2_hand.player_hand.pop(monster-1)

                p2_just_summoned_zone1 = True

            elif zone - 1 == 1:
                p2_monster2 = copy(player2_hand.player_hand[monster-1])
                player2_monster_zones.insert(zone-1, p2_monster2.card_name)
                player2_hand.player_hand.pop(monster-1)

                p2_just_summoned_zone2 = True

            elif zone - 1 == 2:
                p2_monster3 = copy(player2_hand.player_hand[monster-1])
                player2_monster_zones.insert(zone-1, p2_monster3.card_name)
                player2_hand.player_hand.pop(monster-1)

                p2_just_summoned_zone3 = True

            has_summoned = True

# Handles summoning a monster that requires tributes in the Set position. 
def tribute_set(monster, zone):
    global curr_player, has_summoned, just_set
    global p1_set1, p1_set2, p1_set3
    global p2_set1, p2_set2, p2_set3
    global p1_just_summoned_zone1, p1_just_summoned_zone2, p1_just_summoned_zone3
    global p2_just_summoned_zone1, p2_just_summoned_zone2, p2_just_summoned_zone3

    if curr_player == 1:
        if player1_hand.player_hand[monster-1].level == 5 or player1_hand.player_hand[monster-1].level == 6:
            view_field(curr_player)
            action = int(input("Choose a monster to tribute: "))

            player1_grave.append(player1_monster_zones[action-1])
            player1_monster_zones.pop(action-1)

            if zone - 1 == 0:
                p1_set1.card = player1_hand.player_hand[monster-1]

                player1_monster_zones.insert(zone-1, p1_set1.label)
                player1_hand.player_hand.pop(monster-1)

                just_set = True
                has_summoned = True
                p1_just_summoned_zone1 = True

            elif zone - 1 == 1:
                p1_set2.card = player1_hand.player_hand[monster-1]

                player1_monster_zones.insert(zone-1, p1_set2.label)
                player1_hand.player_hand.pop(monster-1)

                just_set = True
                has_summoned = True
                p1_just_summoned_zone2 = True

            elif zone - 1 == 2:
                p1_set3.card = player1_hand.player_hand[monster-1]

                player1_monster_zones.insert(zone-1, p1_set3.label)
                player1_hand.player_hand.pop(monster-1)

                just_set = True
                has_summoned = True
                p1_just_summoned_zone3 = True

        elif player1_hand.player_hand[monster-1].level > 6:
            view_field(curr_player)
            action1 = int(input("Choose the first monster to tribute: "))
            action2 = int(input("Choose the second monster to tribute: "))

            player1_grave.append(player1_monster_zones[action1-1])
            player1_grave.append(player1_monster_zones[action2-1])

            if action1 > action2:
                player1_monster_zones.pop(action1-1)
                player1_monster_zones.pop(action2-1)
            elif action1 < action2:
                player1_monster_zones.pop(action2-1)
                player1_monster_zones.pop(action1-1)

            player1_monster_zones.insert(action1-1, None)
            player1_monster_zones.insert(action2-1, None)
            player1_monster_zones.pop(zone-1)

            if zone - 1 == 0:
                p1_set1.card = player1_hand.player_hand[monster-1]

                player1_monster_zones.insert(zone-1, p1_set1.label)
                player1_hand.player_hand.pop(monster-1)

                just_set = True
                has_summoned = True
                p1_just_summoned_zone1 = True

            elif zone - 1 == 1:
                p1_set2.card = player1_hand.player_hand[monster-1]

                player1_monster_zones.insert(zone-1, p1_set2.label)
                player1_hand.player_hand.pop(monster-1)

                just_set = True
                has_summoned = True
                p1_just_summoned_zone2 = True

            elif zone - 1 == 2:
                p1_set3.card = player1_hand.player_hand[monster-1]

                player1_monster_zones.insert(zone-1, p1_set3.label)
                player1_hand.player_hand.pop(monster-1)

                just_set = True
                has_summoned = True
                p1_just_summoned_zone3 = True

    elif curr_player == 2:
        if player2_hand.player_hand[monster-1].level == 5 or player2_hand.player_hand[monster-1].level == 6:
            view_field(curr_player)
            action = int(input("Choose a monster to tribute: "))

            player2_grave.append(player2_monster_zones[action-1])
            player2_monster_zones.pop(action-1)
            
            if zone - 1 == 0:
                p2_set1.card = player2_hand.player_hand[monster-1]

                player2_monster_zones.pop(zone-1)
                player2_monster_zones.insert(zone-1, p2_set1.label)
                player2_hand.player_hand.pop(monster-1)

                just_set = True
                has_summoned = True
                p2_just_summoned_zone1 = True

            elif zone - 1 == 1:
                p2_set2.card = player2_hand.player_hand[monster-1]

                player2_monster_zones.pop(zone-1)
                player2_monster_zones.insert(zone-1, p2_set2.label)
                player2_hand.player_hand.pop(monster-1)

                just_set = True
                has_summoned = True
                p2_just_summoned_zone2 = True

            elif zone - 1 == 2:
                p2_set3.card = player2_hand.player_hand[monster-1]

                player2_monster_zones.pop(zone-1)
                player2_monster_zones.insert(zone-1, p2_set3.label)
                player2_hand.player_hand.pop(monster-1)

                just_set = True
                has_summoned = True
                p2_just_summoned_zone3 = True

        elif player2_hand.player_hand[monster-1].level > 6:
            view_field(curr_player)
            action1 = int(input("Choose the first monster to tribute: "))
            action2 = int(input("Choose the second monster to tribute: "))

            player2_grave.append(player2_monster_zones[action1-1])
            player2_grave.append(player2_monster_zones[action2-1])

            if action1 > action2:
                player2_monster_zones.pop(action1-1)
                player2_monster_zones.pop(action2-1)
            elif action1 < action2:
                player2_monster_zones.pop(action2-1)
                player2_monster_zones.pop(action1-1)

            player2_monster_zones.insert(action1-1, None)
            player2_monster_zones.insert(action2-1, None)
            player2_monster_zones.pop(zone-1)

            if zone - 1 == 0:
                p2_set1.card = player2_hand.player_hand[monster-1]

                player2_monster_zones.pop(zone-1)
                player2_monster_zones.insert(zone-1, p2_set1.label)
                player2_hand.player_hand.pop(monster-1)

                just_set = True
                has_summoned = True
                p2_just_summoned_zone1 = True

            elif zone - 1 == 1:
                p2_set2.card = player2_hand.player_hand[monster-1]

                player2_monster_zones.pop(zone-1)
                player2_monster_zones.insert(zone-1, p2_set2.label)
                player2_hand.player_hand.pop(monster-1)

                just_set = True
                has_summoned = True
                p2_just_summoned_zone2 = True

            elif zone - 1 == 2:
                p2_set3.card = player2_hand.player_hand[monster-1]

                player2_monster_zones.pop(zone-1)
                player2_monster_zones.insert(zone-1, p2_set3.label)
                player2_hand.player_hand.pop(monster-1)

                just_set = True
                has_summoned = True
                p2_just_summoned_zone3 = True

# Handles switching a monster from attack to defense position or defense to attack position.
def switch_position(zone):
    global curr_player
    global p1_just_summoned_zone1, p1_just_summoned_zone2, p1_just_summoned_zone3
    global p2_just_summoned_zone1, p2_just_summoned_zone2, p2_just_summoned_zone3

    if curr_player == 1:
        card = player1_monster_zones[zone-1]

        if player1_monster_zones[zone-1] == None:
            return print("No monster to switch.")

        elif player1_monster_zones[zone-1][len(card)-3:len(card)] == "(D)":
            player1_monster_zones[zone-1] = card[0:len(card)-4]

            if zone - 1 == 0:
                p1_just_summoned_zone1 = True
            elif zone - 1 == 1:
                p1_just_summoned_zone2 = True
            elif zone - 1 == 2:
                p1_just_summoned_zone3 = True

        else:
            if zone - 1 == 0:
                if p1_just_summoned_zone1 == True:
                    return print("Cannot switch positions the turn it is Summoned.")
                else:
                    player1_monster_zones[zone-1] = card + " (D)"
                    p1_just_summoned_zone1 = True
            elif zone - 1 == 1:
                if p1_just_summoned_zone2 == True:
                    return print("Cannot switch positions the turn it is Summoned.")
                else:
                    player1_monster_zones[zone-1] = card + " (D)"
                    p1_just_summoned_zone2 = True
            elif zone - 1 == 2:
                if p1_just_summoned_zone3 == True:
                    return print("Cannot switch positions the turn it is Summoned.")
                else:
                    player1_monster_zones[zone-1] = card + " (D)"
                    p1_just_summoned_zone3 = True

    elif curr_player == 2:
        card = player2_monster_zones[zone-1]

        if player2_monster_zones[zone-1] == None:
            return print("No monster to switch.")

        elif player2_monster_zones[zone-1][len(card)-3:len(card)] ==  "(D)":
            player2_monster_zones[zone-1] = card[0:len(card)-4]

            if zone - 1 == 0:
                p2_just_summoned_zone1 = True
            elif zone - 1 == 1:
                p2_just_summoned_zone2 = True
            elif zone - 1 == 2:
                p2_just_summoned_zone3 = True

        else:
            if zone - 1 == 0:
                if p2_just_summoned_zone1 == True:
                    return print("Cannot switch positions the turn it is Summoned.")
                else:
                    player2_monster_zones[zone-1] = card + " (D)"
                    p2_just_summoned_zone1 = True
            elif zone - 1 == 1:
                if p2_just_summoned_zone2 == True:
                    return print("Cannot switch positions the turn it is Summoned.")
                else:
                    player2_monster_zones[zone-1] = card + " (D)"
                    p2_just_summoned_zone2 = True
            elif zone - 1 == 2:
                if p2_just_summoned_zone3 == True:
                    return print("Cannot switch positions the turn it is Summoned.")
                else:
                    player2_monster_zones[zone-1] = card + " (D)"
                    p2_just_summoned_zone3 = True


    



def game_loop():
    global curr_player, curr_phase, player1_lp, player2_lp, turn_counter, player1_deckout, player2_deckout

    for i in range(3):
        draw_card(player1_deck, player1_hand)
    
    for i in range(3):
        draw_card(player2_deck, player2_hand)

    while(1):
        print()
        if curr_player == 1:
            print("Turn " + str(turn_counter) + ": Player 1 turn")
            draw_phase()

            if check_win_conditions == True:
                break

            standby_phase()
            main_phase()

            if check_win_conditions == True:
                break

            while(1):
                action = input("Choose phase: ")
                if action == "bp":
                    phase_handler(curr_player, action)

                if action == "ep":
                    phase_handler(curr_player, action)
                    break

        print()
        if curr_player == 2:
            print("Turn " + str(turn_counter) + ": Player 2 turn")
            draw_phase()

            if check_win_conditions == True:
                break

            standby_phase()
            main_phase()

            if check_win_conditions == True:
                break

            while(1):
                action = input("Choose phase: ")
                if action == "bp":
                    phase_handler(curr_player, action)

                if action == "ep":
                    phase_handler(curr_player, action)
                    break

    if player1_deckout == True:
        return print("Player 2 has won.")
    elif player2_deckout == True:
        return print("Player 1 has won.")
    elif player1_lp == 0:
        return print("Player 2 has won.")
    elif player2_lp == 0:
        return print("Player 1 has won.")
    elif right_leg_exodia in player1_hand.player_hand and left_leg_exodia in player1_hand.player_hand and right_arm_exodia in player1_hand.player_hand and left_arm_exodia in player1_hand.player_hand and exodia_the_forbidden_one in player1_hand.player_hand:
        return print("Player 1 won by the effect of Exodia the Forbidden One.")
    elif right_leg_exodia in player2_hand.player_hand and left_leg_exodia in player2_hand.player_hand and right_arm_exodia in player2_hand.player_hand and left_arm_exodia in player2_hand.player_hand and exodia_the_forbidden_one in player2_hand.player_hand:
        return print("Player 2 won by the effect of Exodia the Forbidden One.")
    else:
        return print("The game ended in a draw.")

    
    print("The game has concluded.")



game_loop()
