from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for string in strs:
            sorted_s = "".join(sorted(string))
            results[sorted_s].append(string)
        return list(results.values())
                