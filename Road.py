class SelectGasStation:
    def selectGasStation(self, a, g):
        result=0
        n=len(a)
        if sum(a) < sum(g):
            return -1
        if n != len(g):
            return -1
        gap=[x-y for indx, x in enumerate(a) for indy,y in enumerate(g) if indx==indy]
        summ=0.0
        cnt=0
        i=0
        while cnt < n: 
            summ+=gap[i]
            cnt+=1
            if summ < 0:
                summ=0.0
                #cnt=0
                result= i+1
            i= i+1 if i+1<n else 1
        return result
        
