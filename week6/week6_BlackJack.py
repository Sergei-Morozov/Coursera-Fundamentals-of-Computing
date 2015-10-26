# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

image_back = simplegui.load_image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3xgPf1DzZAI8Xrb3TmuUYrslleWAzxVWcEDppuYybf_TgFUWX")
# initialize some useful global variables
in_play = False
outcome = ""
score = 0


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self._cards = []
            # create Hand object

    def __str__(self):
        result = "Hand content: "
        for card in self._cards:
            result += str(card) + " "
        return result

    def add_card(self, card):
        self._cards.append(card)

    def get_value(self):
        result  = 0
        ace_present = False
        for card in self._cards:
            result += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                ace_present = True
        if ace_present:
            if result <= 11:
                result += 10
        return result
                
    def draw(self, canvas, pos):
        for card in self._cards:
            card.draw(canvas, pos )
            pos = (pos[0] + CARD_SIZE[0], pos[1])
            

        
# define deck class 
class Deck:
    def __init__(self):
        self._cards = []
        self.shuffle()
        
    def shuffle(self):
        self._cards = [ Card(suit,rank) for rank in RANKS for suit in SUITS]
        random.shuffle(self._cards)

    def deal_card(self):
        return self._cards.pop()
    
    def __str__(self):
        result = "Deck len: " + str(len(self._cards)) +  " content: "
        for card in self._cards:
            result += str(card) + " "
        return result


#define event handlers for buttons


def game_state():
    global outcome, score
    
    if player.get_value() == 21:
        outcome = "Player wins"
        score +=1
    elif dealer.get_value() == 21:
        outcome = "Dealer wins"
        score -=1
    elif dealer.get_value() > 21:
        outcome = "Dealer busted"
        score +=1
    elif player.get_value() > 21:
        outcome = "Player busted"
        score -=1
    else:
        #stil in game
        return True
    return False

def deal():
    global outcome, in_play, dealer, player, score, deck
    outcome = ""
    if in_play:
        score -= 1
    in_play = True
    deck = Deck()
    dealer = Hand()
    player = Hand()
    
    deck.shuffle()
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    
    in_play = game_state()
    
    print "Player",player.get_value(), player
    print "Dealer",dealer.get_value(), dealer
def hit():
    global outcome, score, in_play
    
    if in_play:
        player.add_card(deck.deal_card())
        in_play = game_state()
        print "Player",player.get_value(), player
        print "Dealer",dealer.get_value(), dealer  
def stand():
    global in_play,outcome,score
    
    if in_play:
        while dealer.get_value() < 17 :
            dealer.add_card(deck.deal_card())
        in_play = game_state()
    
    if in_play:
        if player.get_value() > dealer.get_value():
            outcome = "Player wins"
            score += 1
        else:
            outcome = "Dealer wins"
            score -= 1   
        in_play = False
        print "Player",player.get_value(), player
        print "Dealer",dealer.get_value(), dealer
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    if image_back.get_width() != 0 and image_back.get_height() != 0:
        canvas.draw_image(image_back, (image_back.get_width()//2,image_back.get_height()//2), (image_back.get_width(),image_back.get_height()), (300,300), (600,600))

    canvas.draw_text("Dealer", (50, 80), 32, 'White',"sans-serif")
    player.draw(canvas, (50,300))
    canvas.draw_text("Player", (50, 280), 32, 'White',"sans-serif")
    dealer.draw(canvas, (50,100))
    canvas.draw_text("Score: " + str(score), (350, 80), 22, 'Red')
    canvas.draw_text("Outcome: " + outcome, (350, 120), 22, 'Red')
    canvas.draw_text("BlackJack", (200, 40), 32, 'Yellow')
    if in_play:
        canvas.draw_text("Hit or stand?", (350, 280), 32, 'Red')
        pos = (50,100)
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

    else:
        canvas.draw_text("New Deal?", (350, 280), 36, 'Red')

    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)

frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric