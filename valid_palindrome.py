class Solution:
    def isPalindrome(self, s: str) -> bool:
        symbols = ' `~\!@#$%^&}*())_+=-?:;"№.,<>/|[]{' + "'"
        s = s.lower()
        new_string = ''
        for symbol in s:
            if symbol not in symbols:
                new_string += symbol
        return new_string == new_string[::-1]