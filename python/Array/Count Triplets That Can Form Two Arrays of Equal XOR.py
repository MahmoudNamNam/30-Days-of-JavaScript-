from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
        
        count = 0
        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    count += (k - i)
        
        return count
    

sol = Solution()
print(sol.countTriplets([2, 3, 1, 6, 7]))  # Output: 4
print(sol.countTriplets([1, 1, 1, 1, 1]))  # Output: 10