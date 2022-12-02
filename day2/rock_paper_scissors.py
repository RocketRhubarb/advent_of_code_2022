def read_input(input='input.txt'):
    with open(input) as file:
        return file.read().splitlines()


def split_space_separated_columns(input):
    return [row.split() for row in input]


def game_outcome(game):
    outcomes = {
        'B X': 'loss',
        'C Y': 'loss',
        'A Z': 'loss',
        'A X': 'draw',
        'B Y': 'draw',
        'C Z': 'draw',
        'A Y': 'win',
        'B Z': 'win',
        'C X': 'win',
    }
    return outcomes[game]


def count_score_with_first_rules(game):
    shape_points = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

    outcome_points = {
        'loss': 0,
        'draw': 3,
        'win': 6,
    }

    return shape_points[game.split()[1]] + outcome_points[game_outcome(game)]


def count_all_scores_according_to_first_rules(games):
    return sum(map(count_score_with_first_rules, games))


def shape(game):
    outcomes = {
        'B X': 'rock',
        'C Y': 'scissors',
        'A Z': 'paper',
        'A X': 'scissors',
        'B Y': 'paper',
        'C Z': 'rock',
        'A Y': 'rock',
        'B Z': 'scissors',
        'C X': 'paper',
    }
    return outcomes[game]


def second_game_outcome(game):
    outcome = {
        'X': 'loss',
        'Y': 'draw',
        'Z': 'win',
    }
    return outcome[game]


def count_score_with_second_rules(game):
    outcome_points = {
        'loss': 0,
        'draw': 3,
        'win': 6,
    }

    shape_points = {
        'rock': 1,
        'paper': 2,
        'scissors': 3,
    }

    return shape_points[shape(game)] + outcome_points[second_game_outcome(game.split()[1])]


def count_all_scores_according_to_second_rules(games):
    return sum(map(count_score_with_second_rules, games))


if __name__ == '__main__':
    games = read_input()
    print(count_all_scores_according_to_first_rules(games))
    print(count_all_scores_according_to_second_rules(games))
