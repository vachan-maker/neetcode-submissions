class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap_t = {}
        if len(s) != len(t):
            return False
        for index in range(len(s)):
            if(s[index] in hashmap and hashmap[s[index]] != t[index]):
                return False
            if(t[index] in hashmap_t and hashmap_t[t[index]]!=s[index]):
                return False
            hashmap[s[index]] = t[index]
            hashmap_t[t[index]] = s[index]
        return True




        