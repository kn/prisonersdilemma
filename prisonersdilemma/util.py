from collections import defaultdict


def generate_round_robin_pair(players):
    """
    Takes a list of integers and returns fixtures in
    a round robin tournament fashion.
    """
    rotation = list(players)  # copy players list
    if len(rotation) % 2:  # odd number of players
        rotation.append(None)
    n = len(rotation)
    fixtures = []
    for _ in range(n - 1):
        matches = []
        for i in range(n / 2):
            matches.append((players[i], players[n - 1 - i]))
        players.insert(1, players.pop())
        fixtures.insert(len(fixtures) / 2, matches)
    for fixture in fixtures:
        for pair in fixture:
            yield pair


def simulate_prisoners_dillema(score_matrix, players, iterations):
    action_history = defaultdict(lambda: defaultdict(list))
    score_history = defaultdict(lambda: defaultdict(list))

    for _ in range(iterations):
        for pair in generate_round_robin_pair(range(len(players))):
            player_1 = pair[0]
            player_2 = pair[1]
            action_1 = players[player_1](action_history[player_2][player_1])
            action_2 = players[player_2](action_history[player_1][player_2])
            score_1 = score_matrix[action_1][action_2]
            score_2 = score_matrix[action_2][action_1]
            action_history[player_1][player_2].append(action_1)
            action_history[player_2][player_1].append(action_2)
            score_history[player_1][player_2].append(score_1)
            score_history[player_2][player_1].append(score_2)

    return action_history, score_history


def calculate_avg_score_by_strategy(players, score_history):
    total_score_by_strategy = defaultdict(int)
    total_players_by_strategy = defaultdict(int)

    players_by_score = sorted([i for i in range(len(players))],
        key=lambda i: -sum([sum(s) for p, s in score_history[i].items()]))
    for i in players_by_score:
        strategy = players[i].__name__
        total_score = sum([sum(s) for p, s in score_history[i].items()])
        total_score_by_strategy[strategy] += total_score
        total_players_by_strategy[strategy] += 1

    return {strategy: total_score / float(total_players_by_strategy[strategy])
        for strategy, total_score in total_score_by_strategy.items()}
