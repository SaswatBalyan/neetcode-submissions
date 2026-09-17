class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=1,1
        for i in range(n-1):
            temp=a
            a=b+a
            b=temp
        return a