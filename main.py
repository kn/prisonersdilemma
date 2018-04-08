"""
A main function to simulate Prisoner's Dilemma game.
It takes a list of strategies as a CSV files.
"""
import argparse
from collections import defaultdict
import random

from prisonersdilemma import strategies
from prisonersdilemma.util import (
    calculate_avg_score_by_strategy,
    generate_round_robin_pair,
    simulate_prisoners_dillema,
)


parser = argparse.ArgumentParser(description='Takes a file path to CSV with a list of strageties.')
parser.add_argument('population', type=argparse.FileType('r'))
parser.add_argument('iterations', type=int)

# The Prisoner's Dilemma game matrix.
# T > R > P > S and
# R > (S + T)/2
parser.add_argument('-r', type=int, default=3)  # Reward for mutual cooporation
parser.add_argument('-t', type=int, default=5)  # Temptation to defect
parser.add_argument('-s', type=int, default=0)  # Sucker's payoff
parser.add_argument('-p', type=int, default=1)  # Punishment for mutual defection
args = parser.parse_args()

score_matrix = [[args.r, args.s], [args.t, args.p]]

players = []

for line in args.population:
    strategy, num = line.strip().split(',')
    print('Read {} players with {} strategy.'.format(num, strategy))
    players.extend([getattr(strategies, strategy) for _ in range(int(num))])

assert len(players) % 2 == 0, 'The number of players need to be even.'

print('There are {} players in total.'.format(len(players)))

random.shuffle(players)

action_history, score_history = simulate_prisoners_dillema(score_matrix, players, args.iterations)

print('')
print('Ranking:')

print('')
print('Results:')

for player, results in action_history.items():
    print('Player{} ({}):'.format(player, players[player].__name__))
    for other_player, actions in results.items():
        print('    Player{} ({}):'.format(other_player, players[other_player].__name__))
        print('        Actions: {}'.format(' | '.join(map(str, actions))))
        print('        Scores:  {}'.format(' | '.join(map(str, score_history[player][other_player]))))

print('')
print('Average:')

for strategy, avg in calculate_avg_score_by_strategy(players, score_history).items():
    print('{} had avg. {}'.format(strategy, avg))
