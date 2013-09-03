class IntervalIntersected:
    def intersected(self, starts, ends, isIntersected):
        def isInt(s1,e1,s2,e2):
            if s2>e1 or s1>e2:
                return False
            else:
                return True
        
        n=len(starts)
        if n<=1:
            return
        
        #independent intervals
        s=set([0]);
        i=1
        while i<n:
            for x in s:
                if isInt(starts[i],ends[i],starts[x],ends[x]):
                    isIntersected[i]=1
                    isIntersected[x]=1
                    #expand x
                    start=starts[i] if starts[i]<starts[x] else starts[x]
                    end=ends[i] if ends[i]>ends[x] else ends[x]
                    starts[x]=start
                    ends[x]=end
                    #end expand
            if not isIntersected[i]:
                s.add(i)
            i+=1
        return