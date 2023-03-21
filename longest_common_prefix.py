class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        min_word = min(strs)
        for i in range(len(min_word)):
            #count_letters = 0
            for word in strs:
                if word[i] != min_word[i]:
                    return prefix
            prefix += min_word[i]
        return prefix