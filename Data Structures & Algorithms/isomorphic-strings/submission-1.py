class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t):
            return False
        for index in range(len(s)):
            if(s[index] not in hashmap):
                hashmap[s[index]] = t[index]
            elif(s[index] in hashmap and hashmap[s[index]] != t[index]):
                return False
        return True




        