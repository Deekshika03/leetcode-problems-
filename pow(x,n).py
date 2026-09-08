"""50. Pow(x, n)
Medium level question :
                          Example 1:
                              Input: x = 2.00000, n = 10
                              Output: 1024.00000   """

#solution 

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1

        while n:
            if n % 2:
                ans *= x
            x *= x
            n //= 2

        return ans
