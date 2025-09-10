using System;

public class Game
{
    //this is an empty space
    public static string empty = ".";

    //Player Token
    public static string player = "@";

    //Where the Player is loacated on the map on x axis
    public static int player_x = 1;

    //Where the Player will be located once position is updated on x axis
    public static int player_dx = 1;

    //Where the Player is loacated on the map on y axis
    public static int player_y = 2;

    //Where the Player will be located once position is updated on y axis
    public static int player_dy = 2;

    //Gameboard it initalizes where the player starts
    public static string[,] game_map = {{empty, empty, empty}, {empty, empty, empty}, {empty, player, empty}};

    //What direction the player will be moving in
    public static string direction = "";

    //Main Game Loop
    public static void Main()
    {
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
                player_dy -= 1;
                break;
            case "south":
                player_dy += 1;
                break;
            case "east":
                player_dx -= 1;
                break;
            case "west":
                player_dx += 1;
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
        Console.WriteLine(game_map[0, 0] + game_map[0, 1] + game_map[0,2]);
        Console.WriteLine(game_map[1, 0] + game_map[1, 1] + game_map[1,2]);
        Console.WriteLine(game_map[2, 0] + game_map[2, 1] + game_map[2,2]);
    }
    public static void UpdatePlayPosition()
    {
        //Places The Player Token at the new Position
        game_map[player_dy, player_dx] = game_map[player_y, player_x];
        //Deletes the player Token from the old position
        game_map[player_y, player_x] = empty;
        //Sets the Players current Position to the Delta Versions
        player_x = player_dx;
        player_y = player_dy;
    }
}