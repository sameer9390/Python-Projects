''' There are so many card games today where you choose a card at random from a deck of cards to create an event. This is the feature of every card game today because you have to choose a card at random and once you choose a card it becomes an event. So in this , I am going to walk you through a tutorial on how to pick a random card using Python.
 
Pick a Random Card using Python
To pick a random card using Python you first have to store all the cards in a data structure. So before storing a card in a data structure let’s understand what types of cards are there in a deck of cards. Below is a table that shows the type of cards present in a deck of cards:

Spade	Club	Diamond	Heart
1 King	1 King	1 King	1 King
1 Queen	1 Queen	1 Queen	1 Queen
1 Jack	1 Jack	1 Jack	1 Jack
1 Ace	1 Ace	1 Ace	1 Ace
2-10 Cards	2-10 Cards	2-10 Cards	2-10 Cards
Total = 13	Total = 13	Total = 13	Total = 13
So according to the above table, a deck of cards have four sets of cards including hearts, clubs, spades and diamonds. These sets of cards are known as suites, each suite has thirteen cards which starts from 2 to 10 and then are continued with Jack, Queen, king and Ace in each suite.

So to pick a random card from a deck of cards, I will create two Python lists:

one for storing the suits
another for storing the ranks of cards.
So below is how we can write a Python program to pick a random card:
'''

import random
cards = ["Diamonds", "Spades", "Hearts", "Clubs"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

def pick_a_card():
    card = random.choices(cards)
    rank = random.choices(ranks)
    return(f"The {rank} of {card}")

print(pick_a_card())
