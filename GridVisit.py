class GridVisit:
    #//如果存在满足条件的遍历,返回True,否则返回False
    def existPath(self, x, y):
        if not x or not y:
            return True
        
        k=len(x)
        
        n=max(x)+1
        m=max(y)+1
        
        adj=[[0 for j in xrange(m)] for j in xrange(n)]
        degl=[0]*n
        degr=[0]*m
        
        for i in xrange(k):
            adj[x[i]][y[i]]=1
            degl[x[i]]+=1
            degr[y[i]]+=1
        
        rel=[indx for indx,j in enumerate(degl) if j%2]
        rer=[indx for indx,j in enumerate(degr) if j%2]
        
        #no more than two odds
        if len(rel)+len(rer)>2:
            return False
        
        # check connectivity
        
        
        return True
                
