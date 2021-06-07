''' Counting occurrences of a character in a string means counting all substrings of a character from the input string.  In this , I’ll walk you through how to count character occurrences using Python.


 
Count Character Occurrences using Python
To count the occurrences of a character, we need to write an algorithm that returns the number of times each character appears in the input string. The algorithm must iterate through each character from the beginning to count the number of times each character appears in the string. Here’s how to write an algorithm for counting character occurrences using Python:
'''
def count_characters(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
print(count_characters("mohammedsameer"))
