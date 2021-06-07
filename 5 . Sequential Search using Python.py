''' The Sequential search algorithm is a searching algorithm. To implement this algorithm, we start by searching for the target value from the beginning of the array and continue till we find the target value. In this , I will take you through the implementation of Sequential Search using Python.

Sequential Search Algorithm
The searching algorithms are the algorithms that are used to search a particular value in a data structure such as lists in Python. The sequential search is a searching algorithm that checks each item in a data structure from the beginning to find the target value.

For example, imagine that you are trying to find a specific card from a deck of cards. You will go through each card in the deck one by one until you find the card you are looking for. Once you got the card you were looking for you will stop. This is how the sequential search algorithm works. Now, in the section below, I will take you through an implementation of sequential search using the Python programming language.

Sequential Search using Python
I hope you now know what a sequential search algorithm is and how it works. To implement this algorithm, we need to check each element from the beginning until we find the value we are looking for. Now let’s see how to implement sequential search using Python:'''
def sequential_search(list_, n):
    found = False
    for i in list_:
        if i == n:
            found = True
            break
    return found
numbers = list(range(0, 20))
print(sequential_search(numbers, 3))
