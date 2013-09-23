class Grid:
    def totalPath(self, blocked):
        n = len(blocked)
        m = len(blocked[0])
        dp = [[0 for col in range(m)] for row in range(n)]
        dp[0][0] = 0 if blocked[0][0] else 1
        for i in range(1,n):
            dp[i][0] = 0 if blocked[i][0] else dp[i-1][0]
        for j in range(1,m):
            dp[0][j] = 0 if blocked[0][j] else dp[0][j-1]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = 0 if blocked[i][j] else dp[i-1][j]+dp[i][j-1]
        return dp[n-1][m-1]
