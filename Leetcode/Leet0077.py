#https://leetcode.com/problems/combinations/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return list(combinations(range(1,n+1),k))
#wow! both list of lists and list of tuples are considered