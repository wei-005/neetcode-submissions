class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]

        count_dict = {}
        
        for string in strs:
            count = [0] * 26

            for ch in string:
                count[ord(ch) - ord('a')] += 1

            count = tuple(count)
            
            if count not in count_dict:
                count_dict[count] = [string]
            else:
                count_dict[count].append(string)

        return list(count_dict.values())