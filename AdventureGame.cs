using System;

//Player Class to neaten code
public class Character
{
    //Players Token
    public string token = "@";

    //Where the Player is loacated on the map on x axis
    public int x = 7;

    //Where the Player will be located once position is updated on x axis
    public int dx = 7;

    //Where the Player is loacated on the map on y axis
    public int y = 13;

    //Where the Player will be located once position is updated on y axis
    public int dy = 13;

    //If the Character Object is a NPC
    public bool NPC = false;

    //Defines the base ATK for the Player
    public int ATK = 5;

    //Defines the base DEF for the Player
    public int DEF = 5;

    //Defines the base HP for the Player
    public int HP = 10;
}

//Main Game
public class Game
{


    //Direction player is going
    public static string command = "";

    //Empty Tile
    public static string empty = "░";

    //Wall Tile, essentally a solid object
    public static string wall = "█";

    //Chest usually have hold in it or HP
    public static string chest = "C";

    //TODO
    public static string lava = "L";

    //TODO: will be able to move between rooms
    public static string door = "║";

    //If the Player was the last to move
    public static bool playerLastMove = true;

    //Player object
    public static Character Player = new Character();

    //Test Enemy object
    public static Character Enemy = new Character();

    public static int lastMove = 0;

    //Game Map
    public static string[,] game_map =
    {
{wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall}, 
{wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall}, 
{wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall}, 
{wall, empty, chest, empty, empty, empty, empty, empty, empty, empty, empty, empty, lava, empty, wall}, 
{wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall}, 
{wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall}, 
{wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall}, 
{wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall}, 
{wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall}, 
{wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall}, 
{wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall}, 
{wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall}, 
{wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall}, 
{wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall}, 
{wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall}
    };


    //Main Game Loop
    public static void Main()
    {

        //Sets Enemies Stats
        InitaliseFoes();

        //Sets Characters to Inital Places
        UpdatePositions();

        //Starts the Main Game Loop
        Game_Loop();
    }
    //Draws the Game Map as a 2D array
    public static void Draw_Game()
    {
        //for the Length of the Y Axis run this code
        for (int y = 0; y < game_map.GetLength(0); y++)
        {
            //for the Length of the X axis run this code
            for (int x = 0; x < game_map.GetLength(1); x++)
            {
                //Print the game at each cordinate
                Console.Write(game_map[y, x]);
            }
            //After a row has been completed print a new line to start the next row until the loop ends
            Console.WriteLine("");
        }
        Console.WriteLine("Enemy X: "+ Enemy.x);
        Console.WriteLine("Enemy Y: "+ Enemy.y);
    }

    //Update Player Position when this is called
    public static void UpdatePositions()
    {
        //If the Enemy's HP is = 0 or less that 0 then remove the Enemy and set it to empty
        if (Enemy.HP <= 0)
        {
            game_map[Enemy.y, Enemy.x] = empty;
        }

        // If the Player is going to walk into the Enemy Call Combat instead
        if (game_map[Player.dy, Player.dx] == game_map[Enemy.y, Enemy.x])
        {
            Combat();
        }

        //else run through normal
        else
        {
            if (game_map[Player.dy, Player.dx] == wall)
            {
                Console.WriteLine("Unable to move there wall in the way!");
                Player.dx = Player.x;
                Player.dy = Player.y;
                Game_Loop();
            }
            else if (game_map[Enemy.dy, Enemy.dx] == wall)
            {
                Enemy.dx = Enemy.x;
                Enemy.dy = Enemy.y;
                Game_Loop();
            }

            //Places The Player Token at the new Position
            game_map[Player.dy, Player.dx] = game_map[Player.y, Player.x];
            game_map[Enemy.dy, Enemy.dx] = game_map[Enemy.y, Enemy.x];

            //Deletes the player Token from the old position
            game_map[Player.y, Player.x] = empty;
            game_map[Enemy.y, Enemy.x] = empty;
            //Sets the Players current Position to the Delta Versions
            Player.x = Player.dx;
            Player.y = Player.dy;
            Enemy.x = Enemy.dx;
            Enemy.y = Enemy.dy;
            //Sets the Player to where they are located
            game_map[Player.y, Player.x] = Player.token;
            game_map[Enemy.y, Enemy.x] = Enemy.token;
        }
    }

    public static void InitaliseFoes()
    {
        //Enemy's Base Position
        Enemy.x = 7;
        Enemy.y = 2;
        Enemy.dx = 7;
        Enemy.dy = 2;

        //Enemy's Token
        Enemy.token = "%";

        //Enemy's Base Stats
        Enemy.DEF = 0;
        Enemy.ATK = 0;
        Enemy.HP = 2;

        //Sets the Token to the Enemy's current location
        game_map[Enemy.y, Enemy.x] = Enemy.token;
    }

    public static void Combat()
    {
        //If the Player was last to move is true
        if (playerLastMove == true)
        {
            //Then its considered to be the Player attacking then chect to see if the Player is stronger than the Enemy
            if (Player.ATK > Enemy.DEF)
            {
                //If so then Update the Enemys HP to be decremented by 1
                Enemy.HP = Enemy.HP - 1;
                //Tell the player what happened
                Console.WriteLine("Player hit Enemy for 1 damage");
                Console.WriteLine("Enemy has " + Enemy.HP + " HP remaining!");
                return;
            }
            //If the Player is stronger or Equal to the enemy, then change no values and report to the player that They are unable to pierce the Enemy
            else if ((Player.ATK < Enemy.DEF) || (Player.ATK == Enemy.DEF))
            {
                Console.WriteLine("Player Unable to Damage Enemy!");
                return;
            }
        }

        //If the player wasnt the last to move
        else if (playerLastMove == false)
        {
            //Then we treat it as the Enemy attacked the Player
            if (Enemy.ATK > Player.DEF)
            {
                // If Enemy stronger than Player then Decrement Player's HP by 1
                Player.HP = Player.HP - 1;
                //And inform the Player
                Console.WriteLine("Enemy attacked Player for 1 damage");
                Console.WriteLine("Player has " + Player.HP + " HP remaining!");
                return;
            }

            //Again, if Enemy atk is weaker then or equal to Player Defence then change no values and inform the player
            else if ((Enemy.ATK < Player.DEF) || (Enemy.ATK == Player.DEF))
            {
                Console.WriteLine("Enemy Unable to Damage Player!");
                return;
            }
        }
    }

    //Main Game Loop
    public static void Game_Loop()
    {
        UpdatePositions();
        //Draws the Inital Game map
        Draw_Game();
        //Updates Players Position if they Moved


        playerLastMove = true;
        //Ask the Player what command they want to go in
        Console.WriteLine("Do you want to look at stats or move: ");
        
        //Sets the command for the users input
        command = Console.ReadLine();

        //If user wants to look at stats 
        if (command == "stats")
        {

            //Print User stats
            Console.WriteLine("Player's Attack: "+ Player.ATK);
            Console.WriteLine("Player's Defence: "+ Player.DEF);
            Console.WriteLine("Player's Health: "+ Player.HP);
        }



        //Else if the user is using Text Control then use that instead
        else if (command == "move")
        {
            //Switches based on where user wants to go and adjusts the Delta Position depending on the result
            Console.WriteLine("north, south, east, west: ");
            string direction = Console.ReadLine();
            switch (direction)
            {
                case "north":
                    Player.dy -= 1;
                    break;
                case "south":
                    Player.dy += 1;
                    break;
                case "east":
                    Player.dx -= 1;
                    break;
                case "west":
                    Player.dx += 1;
                    break;
            }
        }
        EnemyMove();
    }


    public static void EnemyMove()
    {
        
        playerLastMove = false;
        Random rnd = new Random();
        int aiMove;

        aiMove = rnd.Next(0, 3);

        if (aiMove == 0)
        {
            Enemy.dy -= 1;
            Game_Loop();
        }
        else if (aiMove == 1)
        {
            Enemy.dy += 1;
            Game_Loop();
        }
        else if (aiMove == 2)
        {
            Enemy.dx -= 1;
            Game_Loop();
        }
        else if (aiMove == 3)
        {
            Enemy.dx += 1;
            Game_Loop();
        }
    }
}
