using System;


//Player Class to neaten code
public class Character
{

    //Players Token
    public string token = "@";

    //Where the Player is loacated on the map on x axis
    public int x = 2;

    //Where the Player will be located once position is updated on x axis
    public int dx = 2;

    //Where the Player is loacated on the map on y axis
    public int y = 2;

    //Where the Player will be located once position is updated on y axis
    public int dy = 2;

    public bool NPC = false;

    public int ATK = 5;

    public int DEF = 5;

    public int HP = 10;
}


public class Game
{
    //Direction player is going
    public static string command = "";

    //Empty Tile
    public static string empty = ".";

    public static bool playerLastMove = true;

    //Player object
    public static Character Player = new Character();

    public static Character Enemy = new Character();

    //Game Map
    public static string[,] game_map = { { empty, empty, empty, empty, empty }, { empty, empty, empty, empty, empty }, { empty, empty, empty, empty, empty }, { empty, empty, empty, empty, empty }, { empty, empty, empty, empty, empty } };

    //Main Game Loop
    public static void Main()
    {
        
        //Places the Player at start Position
        game_map[Player.y, Player.x] = Player.token;
        InitaliseFoes();
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
    }

    //Update Player Position when this is called
    public static void UpdatePlayPosition()
    {
        if (game_map[Player.dy, Player.dx] == Enemy.token)
        {
            Combat();
        }
        else {
            //Places The Player Token at the new Position
            game_map[Player.dy, Player.dx] = game_map[Player.y, Player.x];
            //Deletes the player Token from the old position
            game_map[Player.y, Player.x] = empty;
            //Sets the Players current Position to the Delta Versions
            Player.x = Player.dx;
            Player.y = Player.dy;
        }

    }

    public static void InitaliseFoes()
    {
        Enemy.x = 2;
        Enemy.token = "%";
        Enemy.y = 0;
        Enemy.DEF = 0;
        Enemy.ATK = 0;
        Enemy.HP = 2;
        game_map[Enemy.y, Enemy.x] = Enemy.token;
    }

    public static void Combat()
    {
        if (playerLastMove == true)
        {
            if (Player.ATK > Enemy.DEF)
            {
                Enemy.HP = Enemy.HP - 1;
                Console.WriteLine("Player hit Enemy for 1 damage");
                Console.WriteLine("Enemy has "+Enemy.HP +" remaining!");
                return;

            }
            else if ((Player.ATK < Enemy.DEF) || (Player.ATK == Enemy.DEF))
            {
                Console.WriteLine("Player Unable to Damage Enemy!");
                return;

            }
        }
        else if (playerLastMove == false)
        {
            if (Enemy.ATK > Player.DEF)
            {
                Player.HP = Player.HP - 1;
                Console.WriteLine("Enemy attacked Player for 1 damage");
                Console.WriteLine("Player has " +Player.HP + " remaining!");
                return;

            }
            else if ((Enemy.ATK < Player.DEF) || (Enemy.ATK == Player.DEF))
            {
                Console.WriteLine("Enemy Unable to Damage Player!");
                return;

            }
        }
    }

    public static void Game_Loop()
    {
        //Draws the Inital Game map
        Draw_Game();

        //Ask the Player what command they want to go in
        Console.WriteLine("Do you want to look at stats or move: ");
        //Sets the command fo the users input
        command = Console.ReadLine();
        //Switches based on where user wants to go and adjusts the Delta Position depending on the result
        if (command == "stats")
        {
            Console.WriteLine("Player's Attack: "+ Player.ATK);
            Console.WriteLine("Player's Defence: "+ Player.DEF);
            Console.WriteLine("Player's Health: "+ Player.HP);
        }
        else if (command == "move")
        {
            Console.WriteLine("north, south, east, west: ");
            command = Console.ReadLine();
            switch (command)
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

        UpdatePlayPosition();
        //Loop the game to ask user again
        Game_Loop();
    }
}