class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r , window, maxlen = 0,0, set(), 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            maxlen = max(maxlen, r-l+1)
            window.add(s[r])
        return maxlen
         


        