class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            dict = {}
            for letter in string:
                dict[letter] = dict.get(letter, 0) + 1
        
            key = tuple(sorted(dict.items()))

            if key not in groups:
                groups[key] = []
            
            groups[key].append(string)

        return list(groups.values())
