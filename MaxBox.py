class MaxBox:
    def maxBoxes(self, boxes):
        if not boxes:
            return 0
        n=len(boxes)
        boxes=sorted(boxes,key=lambda x:x.vol)
        dp=[1]*n
        for i in range(1,n):
            for j in range(i):
                if boxes[j].weight < boxes[i].weight and boxes[j].vol < boxes[i].vol:
                    dp[i]=dp[j]+1 if (dp[j]+1)>dp[i] else dp[i]
        try:
            result=max(dp)
        except ValueError:
            return 0
        return result