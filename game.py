#Imports
import random
import os
import re
import time
import sys
import pygame
pygame.init()

TILE_SIZE = 16
MOVE_DELAY = 120
last_move_time = 0

font = pygame.font.Font("Perfect DOS VGA 437.ttf", TILE_SIZE)

clock = pygame.time.Clock()

MAP_PIXEL_WIDTH = 55 * TILE_SIZE
MAP_PIXEL_HEIGHT = 20 * TILE_SIZE
UI_HEIGHT = 80

screen = pygame.display.set_mode(
    (MAP_PIXEL_WIDTH, MAP_PIXEL_HEIGHT + UI_HEIGHT)
)

pygame.display.set_caption("DEMO")

import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

font_path = resource_path("Perfect DOS VGA 437.ttf")
font = pygame.font.Font(font_path, TILE_SIZE)

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
empty = chr(176)
wall = chr(219)
door = ">"



#For the Regex this replaces the Hex codes with the varble name for the Tiles on the map
value_map = {
    "0xff000000": wall,
    "0xffff0000": water,
    "0x00000000": empty,
}

#In Colour Map we asign colours to each of the Tiles using ANSI codes this helps with making the game look better
color_map = {
    wall: (200, 200, 200),
    empty: (40, 40, 40),
    water: (0, 0, 255),
    "@": (255, 255, 0),
    "%": (255, 0, 255),
    "[": (0, 255, 0),
    "/": (0, 255, 0),
    "!": (0, 255, 0),
    ">": (0, 255, 255),
    "g": (255, 0, 0),
    "o": (255, 0, 0),
    "D": (255, 50, 50)
}

def get_color(char):
    return color_map.get(char, (255, 255, 255))


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
inventory_open = False
inventory_selected = 0
message_log = []
MAX_LOG_LINES = 2



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
        add_message(f"YOu have picked up a: {item.name}")

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
        add_message("Used Potion")
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
            self.spawn_foes()

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

    def spawn_foes(self):

        if not hasattr(self, "rooms"):
            return
        
        base_count = random.randint(3, 6)

        for _ in range(base_count):
            room = random.choice(self.rooms)

            spawn_room = self.rooms[0]
            if room == spawn_room:
                continue

            rx, ry, rw, rh = room

            x = random.randint(rx + 1, rx + rw - 2)
            y = random.randint(ry + 1, ry + rh - 2)

            if self.grid[y][x] != empty:
                continue
            if any(e.x == x and e.y == y for e in self.entities):
                continue

            roll = random.random()

            if roll < 0.6:
                foe = Character("g", x, y, True, 2, 1 , 4)
            elif roll < 0.9:
                foe = Character("o", x, y, True, 3, 2, 6)
            else:
                foe = Character("D", x, y, True, 5, 3, 10)

            self.add_entity(foe)
    

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


#And we add them to each maps Entity List
Map1.add_entity(Player)

#Set the current Map to Map1 for the first level
current_map = Map1

#Draw_Game prints the Map onto the console, we do this by interating through both the x axis and y axis 
def Draw_Game():
    screen.fill((0, 0, 0))

    current_map.update_visibility(Player)

    for y in range(current_map.height):
        for x in range(current_map.width):

        # If never seen → draw black
            if not current_map.discovered[y][x]:
                continue

            char = current_map[y][x]

            # Draw entity only if visible
            if current_map.visible[y][x]:
                for entity in current_map.entities:
                    if entity.x == x and entity.y == y:
                        char = entity.token

            color = get_color(char)

            # Darken if not currently visible
            if not current_map.visible[y][x]:
                color = tuple(c // 3 for c in color)

            text = font.render(char, True, color)
            screen.blit(text, (x * TILE_SIZE, y * TILE_SIZE))

            if inventory_open:
                overlay = pygame.Surface((MAP_PIXEL_WIDTH - 200, MAP_PIXEL_HEIGHT - 100))
                overlay.set_alpha(220)
                overlay.fill((20, 20, 20))

                screen.blit(overlay, (100, 50))

                title = font.render("INVENTORY", True, (255,255,255))
                screen.blit(title, (120, 60))

                weapon_text = font.render(f"Weapon: {Player.weapon.name if Player.weapon else 'None'}", True, (200,200,200))
                armour_text = font.render(f"Armour: {Player.armour.name if Player.armour else 'None'}", True, (200,200,200))

                screen.blit(weapon_text, (120, 90))
                screen.blit(armour_text, (120, 110))

                for i, item in enumerate(Player.inventory):
                    color = (255,255,0) if i == inventory_selected else (200,200,200)
                    text = font.render(item.name, True, color)
                    screen.blit(text, (120, 150 + i * 25))

    footer_rect = pygame.Rect(
        0,
        MAP_PIXEL_HEIGHT,
        MAP_PIXEL_WIDTH,
        UI_HEIGHT
    )

    pygame.draw.rect(screen, (25, 25, 25), footer_rect)
    pygame.draw.line(
        screen,
        (80, 80, 80),
        (0, MAP_PIXEL_HEIGHT),
        (MAP_PIXEL_WIDTH, MAP_PIXEL_HEIGHT),
        2
    )

    stats_text = f"ATK: {Player.ATK}  DEF: {Player.DEF}  HP: {Player.HP}"
    stats_surface = font.render(stats_text, True, (255, 255, 255))
    screen.blit(stats_surface, (10, MAP_PIXEL_HEIGHT + 5))


    log_x = 10
    log_y = MAP_PIXEL_HEIGHT + 30

    for i, msg in enumerate(message_log):
        text_surface = font.render(msg, True, (180, 180, 180))
        screen.blit(text_surface, (log_x, log_y + i * 20))

    pygame.display.flip()



def add_message(text):
    global message_log

    message_log.append(text)

    if len(message_log) > MAX_LOG_LINES:
        message_log.pop(0)


#This Deals with PVE combat
def Combat():

    for entity in current_map.entities[:]:

        # Only process Characters
        if not isinstance(entity, Character):
            continue

        # Only process enemies
        if not entity.NPC:
            continue

        if entity.HP <= 0:
            continue

        # Check if adjacent to player
        if abs(Player.x - entity.x) + abs(Player.y - entity.y) == 1:

            if Player.ATK > entity.DEF:
                entity.HP -= 1
                add_message("You hit the Foe")

            if entity.ATK > Player.DEF:
                Player.HP -= 1
                add_message("You have been Attacked")

            if entity.HP <= 0:
                current_map.entities.remove(entity)
                add_message("Foe Defeated")

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
    
    # Block walking into enemies
    for entity in current_map.entities:
        if isinstance(entity, Character) and entity.NPC:
            if entity.NPC and entity.x == new_x and entity.y == new_y:
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

    for entity in current_map.entities:

        if isinstance(entity, Character) and entity.NPC:

            move = random.choice([(0, -1),(0, 1), (-1, 0), (1,0)])
            Try_Move(entity, *move)

#Here we have the main Game Loop
def Game_Loop():
    global playerLastMove, last_move_time, inventory_open, inventory_selected

    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if inventory_open:

                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_e:
                        inventory_open = False

                    elif event.key == pygame.K_UP:
                        inventory_selected = max(0, inventory_selected - 1)

                    elif event.key == pygame.K_DOWN:
                        inventory_selected = min(len(Player.inventory)-1, inventory_selected + 1)

                    elif event.key == pygame.K_RETURN:
                        if Player.inventory:
                            item = Player.inventory[inventory_selected]

                            if item.type == "potion":
                                Player.use_potion(item)
                                Player.inventory.remove(item)
                            else:
                                Player.equip_item(item)

                else:
                    if event.key == pygame.K_q:
                        running = False
                    elif event.key == pygame.K_e:
                        inventory_open = True

        if not inventory_open:
            keys = pygame.key.get_pressed()

            move_x = 0
            move_y = 0

            if keys[pygame.K_w]:
                move_y = -1
            elif keys[pygame.K_s]:
                move_y = 1
            elif keys[pygame.K_a]:
                move_x = -1
            elif keys[pygame.K_d]:
                move_x = 1

            current_time = pygame.time.get_ticks()

            if move_x != 0 or move_y != 0:
                if current_time - last_move_time > MOVE_DELAY:
                    Try_Move(Player, move_x, move_y)
                    Combat()
                    Foe_Move()
                    last_move_time = current_time
        Draw_Game()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    Game_Loop()