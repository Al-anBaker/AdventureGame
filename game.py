#Imports
import random
import os
import re
import time
import sys


if os.name == "nt":
    import msvcrt
    def get_key():
        key = msvcrt.getch()
        if key in [b'w', b'W']:
            return 'w'
        elif key in [b's', b'S']:
            return 's'
        elif key in [b'a', b'A']:
            return 'a'
        elif key in [b'd', b'D']:
            return 'd'
        elif key in [b'q', b'Q']:
            return 'q'
        return None
else:
    import tty, termios
    def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
            if key.lower() in ['w', 'a', 's', 'd', 'q']:
                return key.lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None


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
def parse_map(array_str, width = 16):
    #Here we are generating the map based on the C Array provided
    clean_str = re.sub(r'[\{\}\s]', '', array_str)
    values = re.findall(r'0x[0-9a-fA-F]+', clean_str)
    grid = []
    for i in range(0, len(values), width):
        row = values[i:i+width]
        converted_row = [value_map[val.lower()] for val in row]
        grid.append(converted_row)
    return grid



#Game Varibles
command = ""
playerLastMove = True


#System Method allows up to clear the console to make the game feel more real
def clear():
    os.system("cls" if os.name == "nt" else "clear")


#Class Definitions
    #The Item Class right now is resposible for Stat Boosts, this is a Class so make scailability easier
class Item():
    def __init__(self, token, item, x, y, active=True):
        self.token = token
        self.item = item
        self.x = x
        self.y = y
        self.active = active

#The Character Class is here to both avoid dulicated code with the Foe and makes it easy to add new Characters to the map
class Character():
    #Character Vars
    def __init__(self, token, x, y, NPC, ATK, DEF, HP, current_map=None):

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

class GameMap:
    def __init__(self, name, grid):
        self.name = name
        self.grid = grid
        self.entities = []
        self.doors = []

    def add_entity(self, entity):
        entity.current_map = self
        self.entities.append(entity)

    def add_door(self, x, y):
        self.grid[y][x] = door
        self.doors.append((x, y))

    def draw(self):
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                entity_here = next((e.token for e in self.entities if e.x == x and e.y == y and e.current_map == self), None)
                if entity_here:
                    print(color_map[entity_here], end="")
                else:
                    print(color_map[tile], end="")
            print()

    def enter_map(self, player, x, y):
        player.x = x
        player.y = y
        player.current_map = self
        global current_map
        current_map = self

        if player not in self.entities:
            self.entities.append(player)

map1_grid = parse_map(map1_array)
map2_grid = [
    [wall]*16,
    [wall] + [empty]*14 + [wall],
    [wall] + [empty]*14 + [wall],
    [wall]*16
]

Map1 = GameMap("map1", map1_grid)
Map2 = GameMap("map2", map2_grid)

Map1.add_door(15,1)
Map2.add_door(0,1)

#Here we initilise the two current characters with their attrbutes
Player = Character("@", 7, 13, False, 5, 5, 5)
Foe = Character("%", 2, 2, True, 0, 0, 2)
Chest = Item("C", "Chest", 13, 1)

Map1.add_entity(Player)
Map1.add_entity(Foe)
Map2.add_entity(Chest)

current_map = Map1

#Draw_Game prints the Map onto the console, we do this by interating through both the x axis and y axis 
def Draw_Game():
    current_map.draw()

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
    global current_map
    new_x = character.x + dx
    new_y = character.y + dy

    if not (0 <= new_y < len(current_map.grid) and 0 <= new_x < len(current_map.grid[0])):
        return False

    tile = current_map.grid[new_y][new_x]

    if tile in [wall, water]:
        return False

    if current_map == Map2 and Player.x == Chest.x and Player.y == Chest.y:
        current_map[Chest.y][Chest.x] = empty  # remove the chest from the map
        Player.ATK += 5
        Player.DEF += 2
        Player.HP += 2
        print("Player has found a lost item! Stats are improved!")
        Chest.x = -1  # deactivate the chest
        Chest.y = -1
        Chest.active = False
        return True
    
    character.x = new_x
    character.y = new_y

    if tile == door and character == Player:
        if current_map == Map1:
            Map2.enter_map(Player, 1, 1)
        else:
            Map1.enter_map(Player, 14, 1)
    return True

#This is to move the NPC
def Foe_Move():
    if Foe.current_map != current_map:
        return
    move = random.choice([(0, -1),(0, 1), (-1, 0), (1,0)])
    Try_Move(Foe, *move)
#Show the Player's Stats at the top of the screen
def Print_Stats():
    print(f"Defence: {Player.DEF} | Attack: {Player.ATK} | Health {Player.HP}")

#Here we have the main Game Loop
def Game_Loop():
    global playerLastMove
    while True:
        clear()
        Print_Stats()
        Draw_Game()
        Combat()
        playerLastMove = True
        command = None
        while command is None:
            command = get_key()
            time.sleep(0.01)

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
