#!/bin/python3

import os

def climbingLeaderboard(ranked, player):
    """
    Determine player's rank after each game score.
    Uses dense ranking (no gaps in ranking numbers).
    
    Args:
        ranked: Leaderboard scores in descending order
        player: Player's scores in ascending order
    
    Returns:
        List of player's ranks after each game
    """
    # Remove duplicates and keep sorted in descending order
    unique_ranked = sorted(set(ranked), reverse=True)
    result = []
    rank_index = len(unique_ranked) - 1
    
    for score in player:
        # Move up the leaderboard while player's score is higher
        while rank_index >= 0 and score >= unique_ranked[rank_index]:
            rank_index -= 1
        
        # Rank is index + 2 (1-indexed and one position below current)
        result.append(rank_index + 2)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w')
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
