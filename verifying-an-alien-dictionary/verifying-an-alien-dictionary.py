class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # O(N*M)
        order_dict = {order[i]:i for i in range(len(order))}
        
        k = 0
        while k < len(words) - 1:
            i = 0
            while i < len(words[k]) - 1 and i < len(words[k+1]) - 1 and words[k][i] == words[k+1][i]:
                i+=1
            
            if order_dict[words[k][i]] > order_dict[words[k+1][i]] or words[k][i] == words[k+1][i] and len(words[k]) > len(words[k+1]):
                return(False)
            k+=1
        return(True)
            