using System;

public class Game
{
    public static string empty = ".";
    public static string player = "@";
    public static int player_x = 1;
    public static int player_dx = 1;
    public static int player_y = 2;
    public static int player_dy = 2;
    public static string[,] game_map = {{empty, empty, empty}, {empty, empty, empty}, {empty, player, empty}};
    public static string direction = "";
    public static void Main()
    {
        Draw_Game();
        Console.WriteLine("What Direction do you want to go north, south, east, west: ");
        direction = Console.ReadLine();
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
        UpdatePlayPosition();
        Main();

    }

    public static void Draw_Game()
    {
        Console.WriteLine(game_map[0, 0] + game_map[0, 1] + game_map[0,2]);
        Console.WriteLine(game_map[1, 0] + game_map[1, 1] + game_map[1,2]);
        Console.WriteLine(game_map[2, 0] + game_map[2, 1] + game_map[2,2]);
    }
    public static void UpdatePlayPosition()
    {
        game_map[player_dy, player_dx] = game_map[player_y, player_x];
        game_map[player_y, player_x] = empty;
        player_x = player_dx;
        player_y = player_dy;
    }
}