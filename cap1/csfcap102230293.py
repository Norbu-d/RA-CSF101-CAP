################################
# norbu dhendup
# software Engineer
# 02230293
################################
# REFERENCES
# Links that you referred while solving 
# the problem
# http://link.to.an.article/video.com 
################################
# SOLUTION
# Your Solution Score:36513
# Put your number here 17301606
################################

# giving  ABC as rock paper scissors

moves = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}

#  scoring system 
score_mapping = {'rock': 1, 'paper': 2, 'scissors': 3}
outcome_scores = {'lose': 0, 'draw': 3, 'win': 6}

def calculate_round_score(opponent_move, desired_outcome):
    # Determining the correct move to make
    correct_move = moves[opponent_move]
    if desired_outcome == 'Y': # Draw
        correct_move = moves[opponent_move]
    elif desired_outcome == 'X': # Lose
        correct_move = 'rock' if moves[opponent_move] == 'scissors' else 'scissors' if moves[opponent_move] == 'paper' else 'paper'
    else: # Win
        correct_move = 'scissors' if moves[opponent_move] == 'rock' else 'rock' if moves[opponent_move] == 'scissors' else 'paper'

    # Calculate the score for the round
    score = score_mapping[correct_move]
    if correct_move == desired_outcome:
        score += outcome_scores['win'] # You won
    elif correct_move != moves[opponent_move]:
        score += outcome_scores['draw'] #  a draw

    return score
def calculate_total_score(filename):
    total_score = 0

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        opponent_move, desired_outcome = line.strip().split()
        round_score = calculate_round_score(opponent_move, desired_outcome)
        total_score += round_score

    return total_score
print(calculate_total_score('cap1/input_3_cap1 (4).txt'))

