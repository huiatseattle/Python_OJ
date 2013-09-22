class MaxBox:
    def maxBoxes(self, boxes):
        if not boxes:
            return 0
        if len(boxes)==0:
            return 0
        boxes = sorted(boxes, key=lambda box:box.vol)
        weights = [box.weight for box in boxes]
        dp = [1]*len(weights)
        for i in range(len(weights)):
            flag = 0
            maxDp = 0
            maxIdx = 0
            for j in range(i):
                if weights[j]<weights[i] and maxDp<dp[j] and boxes[j].vol<boxes[i].vol:
                    maxDp = dp[j]
                    maxIdx = j
                    flag = 1
            if flag == 1:
                dp[i] = dp[maxIdx]+1
        return max(dp)
