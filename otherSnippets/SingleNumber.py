''''
Find single number in a array which contains every other elements twice
TC - O(N)
arr = [2,2,1,1,3] 
o/p - 3
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        xor = 0
        for i in range(len(A)):
            xor = xor ^ A[i]
        return xor

print(Solution().singleNumber([2,1,2,1,3]))