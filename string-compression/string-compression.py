class Solution:
    def compress(self, chars: List[str]) -> int:
        L, R = 0, 0
        
        while R < len(chars):
		
            chars[L] = chars[R]
            count = 1
			
            while R + 1 < len(chars) and chars[R] == chars[R+1]:
                R += 1
                count += 1
			
            if count > 1:
                for c in str(count):
                    chars[L+1] = c
                    L += 1
            R += 1
            L += 1
        
        return L