# your code goes here!
# Class Anagram in anagram.py returns an empty list if the input list contains no words that match the initialized word. F                                                                                   [ 60%]
# Class Anagram in anagram.py returns a list with one element when one element of the input list matches the initialized word. F                                                                             [ 80%]
# Class Anagram in anagram.py returns a list with two elements when two elements of the input list match the initialized word. F                                                                             [100%]

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, words):
        anagrams = []
        for word in words:
            if sorted(word) == sorted(self.word):
                anagrams.append(word)
        return anagrams