class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

       
        if len(s) != len(t):
            return False
        # list_s = list(s)
        # list_t = list(t)


        dict_s = {}
        dict_t = {}

        for element in s:
            if element in dict_s:
                dict_s[element] += 1
            else:
                dict_s[element] = 1

        for element in t:
            if element in dict_t:
                dict_t[element] += 1
            else:
                dict_t[element] = 1

        for key in dict_s:
            if key not in dict_t or dict_s[key] != dict_t[key]:
                return False
        
        return True
