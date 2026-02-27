import random
import os
import re

map1_array = """
{
{
0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 
0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 
0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 
0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 
0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 
0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 
0xff000000, 0x00000000, 0x00000000, 0xffff0000, 0xffff0000, 0xffff0000, 0xffff0000, 0x00000000, 0xffff0000, 0xffff0000, 0xffff0000, 0xffff0000, 0xffff0000, 0x00000000, 0x00000000, 0xff000000, 
0xff000000, 0x00000000, 0xffff0000, 0xffff0000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xffff0000, 0xffff0000, 0xffff0000, 0xff000000, 
0xff000000, 0xffff0000, 0xffff0000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 
0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 
0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 
0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 
0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 
0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 
0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 
0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000
}
};
"""



water = "~"
empty = "░"
lava = "L"
wall = "█"
door = ">"


value_map = {
    "0xff000000": wall,
    "0xffff0000": water,
    "0x00000000": empty,
    "0xff0000ff": lava
}

color_map = {
    wall: "\033[1;37m█\033[0m",
    empty: "\033[0;30m░\033[0m",
    water: "\033[0;34m~\033[0m",
    lava: "\033[1;31mL\033[0m",
    "@": "\033[33m@\033[0m",    
    "%": "\033[35m%\033[0m",    
    "C": "\033[32mC\033[0m",
    ">": "\033[36m>\033[0m"  
}


values = re.findall(r'0x[0-9a-fA-F]+', map1_array)

width = 16

python_grid = []
for i in range(0, len(values), width):
    row = values[i:i+width]
    converted_row = [value_map[val.lower()] for val in row]
    python_grid.append(converted_row)

maps = {
    "map1": python_grid,
    "map2": [
        [wall]*16,
        [wall] + [empty]*14 + [wall],
        [wall] + [empty]*14 + [wall],
        [wall]*16
    ]
}

current_map = "map1"

#Game Varibles
command = ""

playerLastMove = True
lastMove = 0

#This is the Game Map in a List
game_map = maps[current_map]

maps["map1"][1][15] = door
maps["map2"][1][0] = door


def clear():
    os.system("cls" if os.name == "nt" else "clear")

class Item():
    def __init__(self, token, item, x, y):
        self.token = token
        self.item = item
        self.x = x
        self.y = y

#The Character Class is here to both avoid dulicated code with the Foe and makes it easy to add new Characters to the map
class Character():
    #Character Vars
    def __init__(self, token, x, y, NPC, ATK, DEF, HP):

        #token is how the character looks on the Map
        self.token = token

        #Global positions including delta positions
        self.x = x
        self.y = y

        #If the character is a Non Player Character
        self.NPC = NPC
        
        #Base Character Stats
        self.ATK = ATK
        self.DEF = DEF
        self.HP = HP

#Here we initilise the two current characters with their attrbutes
Player = Character("@", 7, 13, False, 5, 5, 10)

Foe = Character("%", 2, 2, True, 0, 0, 2)

Chest = Item("C", "Chest", 7, 10)

#Draw_Game prints the Map onto the console, we do this by interating through both the x axis and y axis 
def Draw_Game():
    for row in game_map:
        for tile in row:
            print(color_map[tile], end="")
        print()

game_map[Chest.y][Chest.x] = Chest.token


def Try_Move(character, dx, dy):
    global game_map, current_map
    new_x = character.x + dx
    new_y = character.y + dy
    tile = game_map[new_y][new_x]


    if not (0 <= new_y < len(game_map) and 0 <= new_x < len(game_map[0])):
        return False
    
    if tile in [wall, water]:
        return False
    
    if Player.x == Chest.x and Player.y == Chest.y:
        game_map[Chest.y][Chest.x] = empty
        Player.ATK += 5
        Player.DEF += 2
        Player.HP += 2
        print("Player has found a lost item stats are improved!")
        Chest.x = -1
        Chest.y = -1
        return True
    

    character.x = new_x
    character.y = new_y

    if tile == door:
        if current_map == "map1":
            current_map = "map2"
            character.x, character.y = 1, 1
            Foe.x, Foe.y = 2, 2
        else:
            current_map = "map1"
            character.x, character.y = 14, 1
            Foe.x, Foe.y = 2, 2  
        game_map = maps[current_map]
        return True
    return True

#Update_Positions moves the Chracters to their Delta Positions
def Update_Positions():
    for y in range(len(game_map)):
        for x in range(len(game_map[0])):
            if game_map[y][x] in [Player.token, Foe.token, Chest.token]:
                game_map[y][x] = empty if (x, y) != (Chest.x, Chest.y) else Chest.token

    if Foe.HP > 0:
        game_map[Foe.y][Foe.x] = Foe.token
    game_map[Player.y][Player.x] = Player.token


def Print_Stats():
    print("Defence: "+ str(Player.DEF))
    print("Attack: "+ str(Player.ATK))
    print("Health: "+ str(Player.HP))

#This is to move the NPC
def Foe_Move():
    aiMove = random.randrange(0, 4)
    if aiMove == 0: Try_Move(Foe, 0, -1)   # up
    elif aiMove == 1: Try_Move(Foe, 0, 1)  # down
    elif aiMove == 2: Try_Move(Foe, -1, 0) # left
    elif aiMove == 3: Try_Move(Foe, 1, 0)  # right

#Here we have the main Game Loop
def Game_Loop():
    global playerLastMove
    while True:
        Update_Positions()
        clear()
        Print_Stats()
        Draw_Game()

        playerLastMove = True
        command = input("WASD to move | Q quit: ").lower()

        if command == "w":
            Try_Move(Player, 0, -1)
        elif command == "s":
            Try_Move(Player, 0, 1)
        elif command == "a":
            Try_Move(Player, -1, 0)
        elif command == "d":
            Try_Move(Player, 1, 0)
        elif command == "q":
            quit()

        Foe_Move()
Game_Loop()
