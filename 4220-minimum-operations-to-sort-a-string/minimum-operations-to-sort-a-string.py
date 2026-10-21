class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # 1. alerady sorted
        if s == ''.join(sorted(s)):
            return 0
        
        # 2. if lenth of string is 2 then return -1
        if n == 2:
            return -1

        min_char = min(s)
        max_char = max(s)

        # 3. min id first or max is last
        if s[0] == min_char or s[n-1] == max_char:
            return 1

        # 4. min and max in middle
        for c in s[1:-1]:
            if c == min_char or c == max_char:
                return 2

        return 3 
