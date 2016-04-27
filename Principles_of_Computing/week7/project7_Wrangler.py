"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    result = []
    max_id = len(list1)
    for idx,value in enumerate(list1):
        if idx +1 < max_id:
            if value == list1[idx+1]:
                continue
        result.append(value)
    
    return result

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    result = []
    len_l1 = len(list1)-1
    len_l2 = len(list2)-1
    while len_l1>=0 and len_l2>=0:
        if list1[len_l1] == list2[len_l2]:
            result.append(list1[len_l1])
            len_l1 -=1
            len_l2 -=1
        elif list1[len_l1] < list2[len_l2]:
            len_l2 -=1
        elif list1[len_l1] > list2[len_l2]:
            len_l1 -=1
    
    return result[::-1]

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    result = []
    idx1 = 0
    idx2 = 0
    while idx1 < len(list1) and idx2< len(list2):
        if list1[idx1] < list2[idx2]:
            result.append(list1[idx1])
            idx1 +=1
        else :
            result.append(list2[idx2])
            idx2 +=1
    if idx1 < len(list1):
        result.extend(list1[idx1:])
    elif idx2 < len(list2):
        result.extend(list2[idx2:])
        
    return result
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    print "in"
    if len(list1) <= 1:
        print "out"
        return list1
    mid = int(len(list1)//2)
    list2 = merge_sort(list1[:mid])
    list3 = merge_sort(list1[mid:])
    print "res",list2,list3
    result = merge(list2,list3)
    return result

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return [""]     
    if len(word) == 1:
        return ["", word]

    letter = word[0]
    result = []
    rest_strings = gen_all_strings(word[1:])
    print "rest", rest_strings
    for item in rest_strings:
        for pos in range(len(item)+1):
            result.append(item[:pos] + letter + item[pos:])                    
    result.extend(rest_strings)
    return result

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
#run()
 
print gen_all_strings("ab")
