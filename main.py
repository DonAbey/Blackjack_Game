import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Jack':10, 'Nine':9, 'Ten':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self) -> None:
        self.all_cards = [Card(suit,rank) for suit in suits for rank in ranks]
        
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    
class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.all_cards = []
        
    def add_card(self, new_cards):
        if (type(new_cards)) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def cal_hand_value(self):
        total_value = sum(card.value for card in self.all_cards)
        #getting the total of Ace
        num_aces = sum(card.rank == 'Ace' for card in self.all_cards)
        #if greater than 21 changing the Ace value from 11 to 1
        while total_value > 21 and num_aces:
            total_value -= 10
            num_aces -= 1
        return total_value
    
    def __str__(self) -> str:
        return f"Player {self.name} has {len(self.all_cards)} cards"
    
def display_hand(player, hide_first_card=False):
    print(f"\n{player.name}'s hand: ")
    for i,card in enumerate(player.all_cards):
        if hide_first_card and i == 0:
            print("Hidden card")
        else:
            print(card)
    if not hide_first_card:
        print(f"Total value: {player.cal_hand_value()}")
            
def player_decision():
    while True:
        decision = input("Do you want to hit or stand? [Hit/Stand]: ").lower()
        if decision in  ['hit','stand']:
            return decision
        else:
            print("Invalid input. Please enter 'Hit' or 'Stand'")

def check_winner(player, dealer):
    player_value = player.cal_hand_value()
    dealer_value = dealer.cal_hand_value()
    
    if player_value > 21:
        return "Dealer wins! Player busted"
    elif dealer_value > 21:
        return "Player wins! Dealer busted"
    elif dealer_value > player_value:
        return "Dealer wins!"
    elif dealer_value < player_value:
        return " Player wins!"
    else:
        return "Its a tie"
    
if __name__ == '__main__':
    print("Welcome to Blackjack Game")
    game_on = True
    
    while game_on:
        try:
            player_name = input("Please enter your name: ")
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting game")
            game_on = False
            break
        
        print("Lets begin")
    
        player = Player(player_name)
        dealer = Player("Dealer")
        deck = Deck()
        deck.shuffle()
        
        #Dealing intial two cards
        
        for x in range(2):
            player.add_card(deck.deal_one())
            dealer.add_card(deck.deal_one())
        
        #Player's turn
        while True:
            display_hand(player)
            display_hand(dealer, hide_first_card=True)
            
            decision = player_decision()
            
            if decision == 'hit':
                player.add_card(deck.deal_one())
                if player.cal_hand_value() > 21:
                    break
            else:
                break
            
        #Dealers turn
        while dealer.cal_hand_value() < 17:
            dealer.add_card(deck.deal_one())
            
        #final results
        display_hand(player)
        display_hand(dealer)
        
        print(check_winner(player,dealer))
    
        while True:
            continue_game = input("\nDo you want to play another round? [Yes/No]: ").lower()
            if continue_game in ['yes', 'no', 'y', 'n']:
                break
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")

        if continue_game not in ['yes', 'y']:
            game_on = False
            print("Thank you for playing Blackjack!")