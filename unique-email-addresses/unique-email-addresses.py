class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        hashset = set()
        for email in emails:
            
            name, domain = email.split('@')
            name = name.replace('.','')
            
            plus_ind = name.find('+')
            if plus_ind != -1:
                hashset.add(name[:plus_ind] + '@' + domain)
                continue
                
            hashset.add(name + '@' + domain)
        
        return len(hashset)
            