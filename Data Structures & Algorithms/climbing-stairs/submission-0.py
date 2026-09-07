class Solution:
    def climbStairs(self, n: int) -> int:
        states = [1, 1]
        for _ in range(1, n):
            states.append(states[-1] + states[-2])
        
        return states[-1]