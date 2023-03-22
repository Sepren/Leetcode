class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        new_num = 0
        for i in range(len(s) - 1):
            if numbers[s[i]] < numbers[s[i + 1]]:
                new_num -= numbers[s[i]]
            else:
                new_num += numbers[s[i]]
        return new_num + numbers[s[-1]]