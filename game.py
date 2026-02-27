#Imports
import random
import os
import re


#Main Map Defenition
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


#Map Tile sets, these are the token for static Tiles on the map
water = "~"
empty = "░"
lava = "L"
wall = "█"
door = ">"


#For the Regex this replaces the Hex codes with the varble name for the Tiles on the map
value_map = {
    "0xff000000": wall,
    "0xffff0000": water,
    "0x00000000": empty,
    "0xff0000ff": lava
}

#In Colour Map we asign colours to each of the Tiles using ANSI codes this helps with making the game look better
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

#Here we are generating the map based on the C Array provided
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



#Game Varibles
command = ""
current_map = "map1"
playerLastMove = True

#Here we set the Game Map to the first Map
game_map = maps[current_map]

#Add Doors so the Player can move between maps
maps["map1"][1][15] = door
maps["map2"][1][0] = door


#System Method allows up to clear the console to make the game feel more real
def clear():
    os.system("cls" if os.name == "nt" else "clear")


#Class Definitions
    #The Item Class right now is resposible for Stat Boosts, this is a Class so make scailability easier
class Item():
    def __init__(self, token, item, x, y, active):
        self.token = token
        self.item = item
        self.x = x
        self.y = y
        self.active = active

#The Character Class is here to both avoid dulicated code with the Foe and makes it easy to add new Characters to the map
class Character():
    #Character Vars
    def __init__(self, token, x, y, NPC, ATK, DEF, HP, current_map):

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

        self.current_map = current_map

#Here we initilise the two current characters with their attrbutes
Player = Character("@", 7, 13, False, 5, 5, 10, "map1")

Foe = Character("%", 2, 2, True, 0, 0, 2, "map1")

#And here we initalise the Item Object
Chest = Item("C", "Chest", 13, 1, False)

Chest.x, Chest.y = 13, 1
maps["map2"][Chest.y][Chest.x] = Chest.token

#Draw_Game prints the Map onto the console, we do this by interating through both the x axis and y axis 
def Draw_Game():
    for row in game_map:
        for tile in row:
            print(color_map[tile], end="")
        print()


#This Deals with PVE combat
def Combat():
    if Foe.current_map != current_map:
        return

    if abs(Player.x-Foe.x)+abs(Player.y-Foe.y)==1 and Foe.HP>0:
        if Player.ATK>Foe.DEF:
            Foe.HP -= 1
            print("Hit Foe for 1 damage!")
        if Foe.ATK>Player.DEF:
            Player.HP -= 1
            print("Foe hits you for 1 damage!")

#Try_Move replaces the old delta positions that were used previosly, this new system works better allowing for more expansion
def Try_Move(character, dx, dy):
    global game_map, current_map
    new_x = character.x + dx
    new_y = character.y + dy
    tile = game_map[new_y][new_x]


    if not (0 <= new_y < len(game_map) and 0 <= new_x < len(game_map[0])):
        return False
    
    if tile in [wall, water]:
        return False
    
    if current_map == "map2" and Player.x == Chest.x and Player.y == Chest.y:
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

    if tile == door and character == Player:
        if current_map == "map1":
            current_map = "map2"
            Player.x, Player.y = 1, 1
        else:
            current_map = "map1"
            character.x, character.y = 14, 1
        game_map = maps[current_map]
        return True
    return True

#Update_Positions Deletes the old characters
def Update_Positions():
    for y in range(len(game_map)):
        for x in range(len(game_map[0])):
            # Only erase Player and Foe, leave other map objects intact
            if game_map[y][x] in [Player.token, Foe.token]:
                game_map[y][x] = empty

    if Foe.HP > 0 and Foe.current_map == current_map:
        game_map[Foe.y][Foe.x] = Foe.token
    game_map[Player.y][Player.x] = Player.token


#Show the Player's Stats at the top of the screen
def Print_Stats():
    print("Defence: "+ str(Player.DEF))
    print("Attack: "+ str(Player.ATK))
    print("Health: "+ str(Player.HP))

#This is to move the NPC
def Foe_Move():
    if Foe.current_map != current_map:
        return
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
        Combat()
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
