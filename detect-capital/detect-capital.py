class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # O(n)
        if len(word) <= 1:
            return True
        
        first_letter = word[0].isupper()
        second_letter = word[1].isupper()
        
        if not first_letter and second_letter:
            return False
        
        for i in range(2, len(word)):
            if first_letter and (word[i].isupper() != second_letter):
                return False
            elif not first_letter and word[i].isupper():
                return False
            
        return True
                