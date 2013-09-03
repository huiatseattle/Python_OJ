class HorseJump2:
    #http://www.itint5.com/discuss/16/
    #http://www.cnblogs.com/drizzlecrj/archive/2007/09/14/892340.html
    def canJump(self, p, q, x, y, x2, y2):
        def gcd(x,y):
            #gcd(a,b) = gcd(b,a mod b)
            return gcd(y,x%y) if y else x
        
        if p==0 and q==0:
            return x==x2 and y==y2
        if x==x2 and y==y2:
            return True
        dx=x-x2
        dy=y-y2
        g=gcd(p,q)
        if dx%g or dy%g:
            return False
        p1=p/g
        q1=q/g
        dx=dx/g
        dy=dy/g
        if (p1-q1)%2:
            return True
        else:
            return not (dx-dy)%2
