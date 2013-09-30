class Candy:
    #返回最少需要的糖果数
    def minimalCandies(self, ratings):
        if not ratings:
            return 0
        n=len(ratings)
        
        candys=[1]*n
        for i in range(1,n,1):
            if ratings[i-1]<ratings[i]:
                candys[i]=candys[i-1]+1
        
        for i in range(n-2,-1,-1):
            if ratings[i+1]<ratings[i]:
                if candys[i] == 1:
                    candys[i]=candys[i+1]+1
                else:
                    candys[i]=max(candys[i+1]+1,candys[i])
                    
        return sum(candys)
