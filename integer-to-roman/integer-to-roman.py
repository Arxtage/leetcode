class Solution:
    def intToRoman(self, num: int) -> str:
        # O(13)
        hashmap = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M',
        } # 13 val
        
        keys = list(hashmap.keys())
        res = ''
        
        for key in reversed(keys):
            whole = num/key
            # if whole >= 1:
            #     res += int(whole) * hashmap[key]
            #     num = num - int(whole) * key

            res += int(whole) * hashmap[key]
            num = num - int(whole) * key
        return res
                 