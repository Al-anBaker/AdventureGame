using System;


//Player Class to neaten code
public class User {

    //Players Token
    public string token = "@";

    //Where the Player is loacated on the map on x axis
    public int x = 2;

    //Where the Player will be located once position is updated on x axis
    public int dx = 2;

    //Where the Player is loacated on the map on y axis
    public int y = 4;

    //Where the Player will be located once position is updated on y axis
    public int dy = 4; 
}


public class Game
{
    //Direction player is going
    public static string direction = "";

    //Empty Tile
    public static string empty = ".";

    //Player object
    public static User Player = new User();

    //Game Map
    public static string[,] game_map = {{empty, empty, empty, empty, empty}, {empty, empty, empty, empty, empty}, {empty, empty, empty, empty, empty}, {empty, empty, empty, empty, empty}, {empty, empty, empty, empty, empty}};

    //Main Game Loop
    public static void Main()
    {
        //Places the Player at start Position
        game_map[Player.y, Player.x] = Player.token;
        //Draws the Inital Game map
        Draw_Game();

        //Ask the Player what direction they want to go in
        Console.WriteLine("What Direction do you want to go north, south, east, west: ");
        //Sets the direction fo the users input
        direction = Console.ReadLine();
        //Switches based on where user wants to go and adjusts the Delta Position depending on the result
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
        //Update the Player's Position
        UpdatePlayPosition();
        //Loop the game to ask user again
        Main();

    }
    //Draws the Game Map as a 2D array
    public static void Draw_Game()
    {
        //for the Length of the Y Axis run this code
       for (int y = 0; y < game_map.GetLength(0); y++)
       {
        //for the Length of the X axis run this code
        for (int x = 0; x < game_map.GetLength(1); x++ )
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
        //Places The Player Token at the new Position
        game_map[Player.dy, Player.dx] = game_map[Player.y, Player.x];
        //Deletes the player Token from the old position
        game_map[Player.y, Player.x] = empty;
        //Sets the Players current Position to the Delta Versions
        Player.x = Player.dx;
        Player.y = Player.dy;
    }
}