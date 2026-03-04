#Imports
import random
import os
import re
import time
import sys

#This first if-else statment checks to see what OS type the Player Has, if its an NT or Windows Based system it will import msvcrt to handle keyboard interaction
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
        elif key in [b'e', b'E']:
            return 'e'
        elif key in [b'u', b'U']:
            return 'u'
        return None
#However if the USers System is Unix based it will use tty and termios to get Keyboard input
else:
    import tty, termios
    def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
            if key.lower() in ['w', 'a', 's', 'd', 'q', 'e', 'u']:
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
wall = "█"
door = ">"



#For the Regex this replaces the Hex codes with the varble name for the Tiles on the map
value_map = {
    "0xff000000": wall,
    "0xffff0000": water,
    "0x00000000": empty,
}

#In Colour Map we asign colours to each of the Tiles using ANSI codes this helps with making the game look better
color_map = {
    wall: "\033[1;37m█\033[0m",
    empty: "\033[0;30m░\033[0m",
    water: "\033[0;34m~\033[0m",
    "@": "\033[33m@\033[0m",    
    "%": "\033[35m%\033[0m",    
    "[": "\033[32m[\033[0m",
    "/": "\033[32m/\033[0m",
    "!": "\033[32m!\033[0m",
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



#Global Varibles
command = ""
playerLastMove = True
dungeon_level = 0

#System Method allows up to clear the console to make the game feel more real
def clear():
    os.system("cls" if os.name == "nt" else "clear")


#Class Definitions
    #The Item Class right now is resposible for Stat Boosts, this is a Class so make scailability easier
class Item():
    def __init__(self, token, name, x, y, item_type, atk=0, defn=0, hp=0, active=True):
        self.token = token
        self.name = name
        self.x = x
        self.y = y
        self.type = item_type
        self.atk = atk
        self.defn = defn
        self.hp = hp
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

        self.inventory = []

        self.weapon = None
        self.armour = None

    def pickup_item(self, item):
        self.inventory.append(item)

    def equip_item(self, item):
        if item.type == "weapon":
            if self.weapon:
                self.ATK -= self.weapon.atk
            self.weapon = item
            self.ATK += item.atk

        elif item.type == "armour":
            if self.armour:
                self.DEF -= self.armour.defn
            self.armour = item
            self.DEF += item.defn

    def unequip_item(self, slot):
        if slot == "weapon" and self.weapon:
            self.ATK -= self.weapon.atk
            self.weapon = None
        elif slot == "armour" and self.armour:
            self.DEF -= self.armour.defn
            self.armour = None

    def use_potion(self, item):
        self.HP += item.hp
        if self.HP > 20:
            self.HP = 20

#GameMap is an Object that holds the current Maps name, grid and its dimensions, it is also respoonsible in adding doors and entities
class GameMap:
    def __init__(self, name, grid=None, width=None, height=None):
        self.name = name
        self.entities = []

        # Case 1: Static map passed in
        if isinstance(grid, list):
            self.grid = grid
            self.height = len(grid)
            self.width = len(grid[0])

        # Case 2: Procedural map requested
        elif width is not None and height is not None:
            self.width = width
            self.height = height
            self.grid = self.generate_procedural_map()
            self.spawn_random_items()

        else:
            raise ValueError("Invalid GameMap initialization")

        self.visible = [[False for _ in range(self.width)]
                        for _ in range(self.height)]
        self.discovered = [[False for _ in range(self.width)]
                           for _ in range(self.height)]

    def __getitem__(self, index):
        return self.grid[index]

    def add_entity(self, entity):
        self.entities.append(entity)
        entity.current_map = self

    def spawn_random_items(self):
        if not hasattr(self, "rooms"):
            return
        
        item_count = random.randint(2, 5)

        for _ in range(item_count):
            room = random.choice(self.rooms)

            rx, ry, rw, rh = room

            x = random.randint(rx + 1, rx + rw - 2)
            y = random.randint(ry + 1, ry + rh - 2)

            if self.grid != empty:
                continue
        
        roll = random.random()

        if roll < 0.4:
            item = Item("!", "Health Potion", x, y, item_type="potion", hp=5)
        elif roll < 0.7:
            item = Item("/", "Dagger", x, y, item_type="weapon", atk=2)
        else:
            item = Item("[", "Leather Armour", x, y, item_type="armour", defn=2)

        self.entities.append(item)

    def enter_map(self, player, x, y):
        global current_map
        current_map = self
        if hasattr(self, "spawn_point") and self.spawn_point:
            player.x, player.y = self.spawn_point
        else:
            player.x = x
            player.y = y
        self.add_entity(player)

    def add_door(self, x, y):
        self.grid[y][x] = door

    def update_visibility(self, player, radius=8):
        # Clear current visibility
        for y in range(self.height):
            for x in range(self.width):
                self.visible[y][x] = False

        px, py = player.x, player.y

        # Bresenham line algorithm
        def line(x0, y0, x1, y1):
            points = []
            dx = abs(x1 - x0)
            dy = abs(y1 - y0)
            x, y = x0, y0
            sx = 1 if x0 < x1 else -1
            sy = 1 if y0 < y1 else -1

            if dx > dy:
                err = dx / 2.0
                while x != x1:
                    points.append((x, y))
                    err -= dy
                    if err < 0:
                        y += sy
                        err += dx
                    x += sx
            else:
                err = dy / 2.0
                while y != y1:
                    points.append((x, y))
                    err -= dx
                    if err < 0:
                        x += sx
                        err += dy
                    y += sy

            points.append((x1, y1))
            return points

        # Cast rays to every tile in square around player
        for y in range(py - radius, py + radius + 1):
            for x in range(px - radius, px + radius + 1):

                if not (0 <= x < self.width and 0 <= y < self.height):
                    continue

                if abs(x - px) + abs(y - py) > radius:
                    continue

                for lx, ly in line(px, py, x, y):

                    if not (0 <= lx < self.width and 0 <= ly < self.height):
                        break

                    self.visible[ly][lx] = True
                    self.discovered[ly][lx] = True

                    # Stop ray if wall hit (but wall itself is visible)
                    if self.grid[ly][lx] == wall and (lx, ly) != (px, py):
                        break
    def draw(self):
        self.update_visibility(Player)

        temp_grid = [row[:] for row in self.grid]

        for entity in self.entities:
            if (0 <= entity.y < self.height and 
                0 <= entity.x < self.width and
                self.visible[entity.y][entity.x]):
                temp_grid[entity.y][entity.x] = entity.token

        for y in range(self.height):
            for x in range(self.width):
                if not self.discovered[y][x]:
                    print(" ", end="")
                elif not self.visible[y][x]:
                    # dim explored tiles
                    print("\033[2m" + color_map.get(self.grid[y][x], self.grid[y][x]) + "\033[0m", end="")
                else:
                    print(color_map.get(temp_grid[y][x], temp_grid[y][x]), end="")
            print()

    def generate_procedural_map(self):
        grid = [[wall for _ in range(self.width)]
                for _ in range(self.height)]

        rooms = []
        max_rooms = 9
        max_attempts = 50
        attempts = 0
        min_size = 3
        max_size = 9
        self.spawn_point = None

        while len(rooms) < max_rooms and attempts < max_attempts:
            attempts += 1

            w = random.randint(min_size, max_size)
            h = random.randint(min_size, max_size)
            x = random.randint(1, self.width - w - 1)
            y = random.randint(1, self.height - h - 1)

            new_room = (x, y, w, h)

            failed = False
            for other in rooms:
                if (x < other[0] + other[2] and
                    x + w > other[0] and
                    y < other[1] + other[3] and
                    y + h > other[1]):
                    failed = True
                    break

            if failed:
                continue

            # Carve room
            for i in range(x, x + w):
                for j in range(y, y + h):
                    grid[j][i] = empty

            # Connect to previous room
            if rooms:
                prev_x = rooms[-1][0] + rooms[-1][2] // 2
                prev_y = rooms[-1][1] + rooms[-1][3] // 2
                new_x_center = x + w // 2
                new_y_center = y + h // 2

                if random.choice([True, False]):
                    for i in range(min(prev_x, new_x_center),
                                max(prev_x, new_x_center) + 1):
                        grid[prev_y][i] = empty

                    for j in range(min(prev_y, new_y_center),
                                max(prev_y, new_y_center) + 1):
                        grid[j][new_x_center] = empty
                else:
                    for j in range(min(prev_y, new_y_center),
                                max(prev_y, new_y_center) + 1):
                        grid[j][prev_x] = empty

                    for i in range(min(prev_x, new_x_center),
                                max(prev_x, new_x_center) + 1):
                        grid[new_y_center][i] = empty

            rooms.append(new_room)


        if not rooms:
            # emergency fallback room
            x = self.width // 2 - 3
            y = self.height // 2 - 3
            for i in range(x, x + 6):
                for j in range(y, y + 6):
                    grid[j][i] = empty
            rooms.append((x, y, 6, 6))

        # Spawn in first room
        first = rooms[0]
        spawn_x = first[0] + first[2] // 2
        spawn_y = first[1] + first[3] // 2
        self.spawn_point = (spawn_x, spawn_y)

        # Door in last room
        last = rooms[-1]
        door_x = last[0] + last[2] // 2
        door_y = last[1] + last[3] // 2

        # Prevent spawn and door overlap
        if (door_x, door_y) == self.spawn_point:
            door_x += 1

        grid[door_y][door_x] = door
        self.rooms = rooms
        return grid
#Here we generate the first 2 entrance levels 
map1_grid = parse_map(map1_array)
map2_grid = [
    [wall]*16,
    [wall] + [empty]*14 + [wall],
    [wall] + [empty]*14 + [wall],
    [wall]*16
]

#And then we Save the name and the grid of each to Map Objects
Map1 = GameMap("map1", map1_grid)
Map2 = GameMap("map2", map2_grid)

#Adding Doors to each map to allow moving between maps
Map1.add_door(15,1)
Map2.add_door(0,1)
Map2.add_door(14, 2)

#Here we initilise the two current characters with their attrbutes
Player = Character("@", 7, 13, False, 5, 5, 5)
Foe = Character("%", 2, 2, True, 0, 0, 2)


#And we add them to each maps Entity List
Map1.add_entity(Player)
Map1.add_entity(Foe)

#Set the current Map to Map1 for the first level
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

#Try_Move is responisble for moving the Player and handling Player and Entity Interaction
def Try_Move(character, dx, dy):
    global dungeon_level, current_map
    new_x = character.x + dx
    new_y = character.y + dy

    if not (0 <= new_y < len(current_map.grid) and 0 <= new_x < len(current_map.grid[0])):
        return False

    tile = current_map.grid[new_y][new_x]

    if tile in [wall, water]:
        return False
    
    character.x = new_x
    character.y = new_y

    #Here if the Player encounters an Active Chest they will pick it up and have their stats improved
    for entity in current_map.entities[:]:
        if isinstance(entity, Item):
            if entity.x == Player.x and entity.y == Player.y:
                Player.pickup_item(entity)
                current_map.entities.remove(entity)


    #This handles Player and Door Interation allowing for Players to move between Levels, and if needed Generate New Levels
    if tile == door and character == Player:

        if current_map.name == "map1":
            Map2.enter_map(Player, 1, 1)

        elif current_map.name == "map2":

            if new_x == 0 and new_y == 1:
                Map1.enter_map(Player, 14, 1)

            else:
                dungeon_level = 1

                new_floor = GameMap(
                    f"Dungeon {dungeon_level}",
                    width = 55,
                    height= 20
                )
                new_floor.enter_map(Player, 1, 1)

        elif current_map.name.startswith("Dungeon"):

            dungeon_level += 1

            new_floor = GameMap(
                f"Dungeon {dungeon_level}",
                width=55,
                height=20
            )
            new_floor.enter_map(Player, 1, 1)


#This is to move the NPC
def Foe_Move():
    if Foe.current_map != current_map:
        return
    move = random.choice([(0, -1),(0, 1), (-1, 0), (1,0)])
    Try_Move(Foe, *move)

#Show the Player's Stats at the top of the screen and what floor they are on
def Print_Stats():
    print(f"Defence: {Player.DEF} | Attack: {Player.ATK} | Health {Player.HP}")
    if current_map.name.startswith("Dungeon"):
        print(f"Dungeon Level: {dungeon_level}")
    else:
        print("Dungeon Level: Entrance")
        

def Inventory():
    while True:
        clear()
        print("====== INVENTORY ======\n")

        print(f"Weapon: {Player.weapon.name if Player.weapon else 'None'}")
        print(f"Armour: {Player.armour.name if Player.armour else 'None'}")

        if not Player.inventory:
            print("Inventory is empty")
        else: 
            for index, item in enumerate(Player.inventory):
                letter = chr(ord('a') + index)
                print(f"{letter}) {item.name}")

        print("\nSelect item to equip/use")
        print("U = Unequip Weapon")
        print("I = Unequip Armour")
        print("Q = Exit")

        key = None
        while key is None:
            key = get_key()
            time.sleep(0.01)

        if key == 'q':
            return
        if key == 'u':
            Player.unequip_item("weapon")
            continue
        if key == 'i':
            Player.unequip_item("armour")
            continue

        if Player.inventory:
            index = ord(key) - ord('a')
            if 0 <= index < len(Player.inventory):
                item = Player.inventory[index]

                if item.type == "potion":
                    Player.use_potion(item)
                    Player.inventory.remove(item)
                
                else:
                    Player.equip_item(item)

def Print_Controls():
    print("WASD to Move | Q to Quit | E to open Inventory")

#Here we have the main Game Loop
def Game_Loop():
    global playerLastMove
    while True:
        clear()
        Print_Stats()
        Draw_Game()
        Print_Controls()
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
        elif command == "e":
            Inventory()
        Foe_Move()
Game_Loop()
