"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 40         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.
def mc_trial(board, player):
    """
    start trial
    """
    if board.check_win() != None:
        return
    move = board.get_empty_squares()[random.randrange(0, len(board.get_empty_squares()))]
    board.move(move[0],move[1],player)
    mc_trial(board, provided.switch_player(player))
        
def mc_update_scores(scores, board, player):
    """
    update game score
    """
    state = board.check_win()
    player_square = 0.0
    oppossite_square = 0.0
    if state == player:
        player_square = SCORE_CURRENT
        oppossite_square = -SCORE_OTHER
    elif state == provided.switch_player(player):
        player_square = -SCORE_CURRENT
        oppossite_square = SCORE_OTHER
    else:
        return
    for width in range(board.get_dim()):
        for height in range(board.get_dim()):
            if board.square(width,height) == player:
                scores[width][height] += player_square
            elif board.square(width,height) == provided.EMPTY :
                continue
            else:
                 scores[width][height] +=  oppossite_square
            
            
    
def get_best_move(board, scores): 
    """
    get game best move
    """
    print "best move" 
    best_move = []
    best_move_score = None
    if len(scores):
        for pair in board.get_empty_squares():
            width = pair[0]
            height = pair[1]
            if best_move_score == None:
                best_move_score = scores[width][height]
            if scores[width][height] > best_move_score:
                best_move_score = scores[width][height]
                best_move = [pair]
            elif scores[width][height] == best_move_score:
                best_move.append(pair)         
        return best_move[random.randrange(0, len(best_move))]
    else:
        return board.get_empty_squares()[random.randrange(0, len(board.get_empty_squares()))]

def mc_move(board, player, trials): 
    """
    make a move in game
    """
    best_scores = [[0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]
    for dummy_trial in range(trials):
        new_board = board.clone()
        mc_trial(new_board,player)
        mc_update_scores(best_scores,new_board,player)
    return get_best_move(board, best_scores)

        


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, 70, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, 40, False)
