def climbStairs(n: int) -> int:
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# 2: 1,1; 2;
# 3: 1,1,1; 1,2; 2,1;
# 4: 1,1,1,1; 1,1,2; 2,1,1; 1,2,1; 2,2;
# 5: 8

n = 4
print(climbStairs(n))