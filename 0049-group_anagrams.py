class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        for s in strs:
            sort_s = ''.join(sorted(s))
            word_list = word_map.get(sort_s, [])
            word_list.append(s)
            word_map[sort_s] = word_list

        anagrams = [word_map.get(k) for k in word_map]
        return(anagrams)
