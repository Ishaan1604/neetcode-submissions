class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        n = len(s)
        sett = set()
        max_length = 0
        while r < n:
            if s[r] in sett:
                sett.remove(s[l])
                l += 1
                continue
            
            sett.add(s[r])
            r += 1
            max_length = max(max_length, r - l)
        
        return max_length