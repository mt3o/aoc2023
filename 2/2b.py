# Accepted game: only 12 red cubes, 13 green cubes, and 14 blue cubes
# result: Sum all game numbers

# f = "sample.txt"
f = "input.txt"


def get_min_number_of_cubes(game_sets):
    response = {
        'red': 0,
        'blue': 0,
        'green': 0
    }
    for game_set in game_sets:
        if 'red' in game_set:
            response['red'] = max(response['red'], game_set['red'])
        if 'blue' in game_set:
            response['blue'] = max(response['blue'], game_set['blue'])
        if 'green' in game_set:
            response['green'] = max(response['green'], game_set['green'])
    return response

if __name__ == '__main__':
    result = 0
    with open(f, 'r') as file:
        for line in file:
            game_number = line.split(" ")[1].replace(":", "")
            game_sets_parsed = line.split(":")[1].split(";")
            game_sets = []
            for game_set in game_sets_parsed:
                scores = game_set.split(",")
                set = {}
                for score in scores:
                    points, color = score.strip().split(" ")
                    set[color.strip()] = int(points.strip())
                    game_sets.append(set)
            cube_count = get_min_number_of_cubes(game_sets)
            game_power = cube_count['red'] * cube_count['green'] * cube_count['blue']
            result += game_power
        print(result)
