from collections import defaultdict
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Create a dictionary to store words by their current target character
        waiting = defaultdict(list)
        for word in words:
            waiting[word[0]].append(iter(word[1:]))
        
        count = 0
        # Iterate through the characters in string s
        for char in s:
            # Get all words waiting for this character
            matching = waiting[char]
            waiting[char] = []
            for it in matching:
                next_char = next(it, None)
                if next_char is None:
                    # If there are no more characters, it's a match
                    count += 1
                else:
                    # Otherwise, append it to the next character's list
                    waiting[next_char].append(it)
        
        return count

        