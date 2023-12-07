# Accepted game: only 12 red cubes, 13 green cubes, and 14 blue cubes
# result: Sum all game numbers

# f = "sample.txt"
f = "input.txt"


def is_valid_game(game):
    if 'red' in game and game['red'] > 12:
        return False
    if 'green' in game and game['green'] > 13:
        return False
    if 'blue' in game and game['blue'] > 14:
        return False
    return True

def validate_game(game_sets):
    for game in game_sets:
        if not is_valid_game(game):
            return False
    return True


if __name__ == '__main__':
    result = 0
    with open(f, 'r') as file:
        for line in file:
            game_number = line.split(" ")[1].replace(":","")
            game_sets_parsed = line.split(":")[1].split(";")
            game_sets = []
            for game_set in game_sets_parsed:
                scores = game_set.split(",")
                set = {}
                for score in scores:
                    points, color = score.strip().split(" ")
                    set[color.strip()] = int(points.strip())
                game_sets.append(set)
            if validate_game(game_sets):
                result += int(game_number)
    print(result)
