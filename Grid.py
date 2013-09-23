class Grid:
    def totalPath(self, blocked):
        if not blocked:
            return 0
        n=len(blocked)
        if not n:
            return 0
        m=len(blocked[0])
        
        dp=[[0]*m for x in range(n)]
        
        dp[0][0]=1
        
        for i in range(1,n):
            if not blocked[i][0]:
                dp[i][0]=1
            else:
                break
        
        for j in xrange(1,m):
            if not blocked[0][j]:
                dp[0][j]=1
            else:
                break
        
        for i in range(1,n):
            for j in range(1,m):
                if not blocked[i][j]:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                else:
                    dp[i][j]=0
        
        return dp[n-1][m-1]