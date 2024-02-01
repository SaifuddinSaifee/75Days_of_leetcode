class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize an empty string to store the merged result
        merged_string = ""
        # Use while loop instead of for loop
        while word1 or word2:
            # If word1 is not empty, append its first character to merged_string and remove it from word1
            if word1:
                merged_string += word1[0]
                word1 = word1[1:]
            # If word2 is not empty, append its first character to merged_string and remove it from word2
            if word2:
                merged_string += word2[0]
                word2 = word2[1:]
        
        return merged_string
        # The time complexity of this code remains O(n + m) where n is the length of word1 and m is the length of word2.
        # Using a while loop doesn't change the overall complexity, as the operations within the loop are the same.