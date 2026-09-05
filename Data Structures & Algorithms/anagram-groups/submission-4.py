class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        in_groups = {}
        for string in strs:
            if "".join(sorted(string)) in in_groups.keys():
                in_groups["".join(sorted(string))].append(string)
            else:
                in_groups["".join(sorted(string))] = [string]
        
        groups = []
        for group in in_groups.values():
            groups.append(group)
        
        return groups
