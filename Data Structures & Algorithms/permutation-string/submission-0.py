class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        c1 = Counter(s1)
        for i in range(len(s2)):
            print(c1, Counter(s2[i:i+k]))
            if c1 == Counter(s2[i:i+k]): 
                return True
        return False

        