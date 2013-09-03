class MinAllOne:
    def findMinAllOne(self, a):
        if a==0:
            return -1
        #(x*10+1)%y=((x%y)*10+1)%y
        num=1
        count=1
        r=num%a
        res=set()
        #n distinct residules, repeated will result in cycle
        while r and count<=a:
            num=r*10+1
            r=num%a
            if r and r in res:
                return -1
            res.add(r)
            count+=1
        if r:
            return -1
        else:
            return count