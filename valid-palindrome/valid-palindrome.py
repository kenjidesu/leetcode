class Solution(object):
    def isPalindrome(self, s):
        # isalnum(), checks if character is alphanumeric
        palindro = "".join(i for i in s.lower() if i.isalnum())
        # alpanumeric s compare to the reverse alpanumeric s
        return palindro == palindro[::-1]