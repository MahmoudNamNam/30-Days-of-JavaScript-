class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if not s :
            return 0
        cnt=1
        current=1
        for i in range(1,len(s)):
            if ord(s[i]) - ord(s[i-1]) ==1:
                current +=1
            else:
                current =1
            cnt = max(current,cnt)
        return cnt
