class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            key = "".join(sorted(word))  # sorted string as key
            anagrams[key].append(word)
        
        return list(anagrams.values())