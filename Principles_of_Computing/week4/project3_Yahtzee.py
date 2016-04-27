"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """    
    item_count = [hand.count(item)*item for item in hand]
    return max(item_count)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcome = range( 1,num_die_sides + 1)
    print outcome
    score_result = 0
    result = gen_all_sequences(outcome, num_free_dice)
    for item in result:
        score_result += score(held_dice + item) 
    return float(score_result) / len(result)

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    result = [()]
    for dice in hand:
        for subset in result:
            result = result + [subset + (dice,)]
    return set(result)



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    result = (0.0, ())
    all_holds = gen_all_holds(hand)
    for hold in all_holds:  
        expected = expected_value(hold,num_die_sides,len(hand) - len(hold))
        if result[0] < expected:
            result = (expected , hold)
    print "Max Value", result    
    return result


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    #all_rolls = gen_all_sequences([1, 2, 3, 4, 5, 6], 3)

    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    
    hand = (1,2,3)
    hand_score, hold = strategy(hand, num_die_sides)
    
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
#print score((1,))  
#run_example()
#print expected_value((2,2),6,2)


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    



