class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize an empty string to store the merged result
        merged_string = ""
        # Loop through the combined length of word1 and word2
        for _ in range(len(word1) + len(word2)):
            # If word1 is not empty, append its first character to merged_string and remove it from word1
            if word1:
                merged_string += word1[0]
                word1 = word1[1:]
            # If word2 is not empty, append its first character to merged_string and remove it from word2
            if word2:
                merged_string += word2[0]
                word2 = word2[1:]
        
        return merged_string
        # The time complexity of this code is O(n + m) where n is the length of word1 and m is the length of word2.
        # This is because the loop iterates through the combined length of both strings,
        # and string concatenation inside the loop is O(1) since it's appending a single character each time.
