class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_count = {}
        chart_count = {}
        if len(s) == len(t):
            for s_char in s:
                chars_count[s_char] = chars_count.get(s_char, 0) + 1
            for t_char in t:
                chart_count[t_char] = chart_count.get(t_char, 0) + 1
            return chart_count == chars_count
        else: return False





