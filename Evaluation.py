class Evaluation:
    #?????expr??
    def eva(self,expr,begin,end):
        if begin > end:
            return 0
        
        mul,plus,sgn=-1,-1,1
        num=0
        
        for i in xrange(begin,end+1):
            if expr[i]== '+':
                plus=i
                sgn=1
            elif expr[i]=='-':
                plus=i
                sgn=-1
            elif expr[i]=='*':
                mul=i
            
            if expr[i].isdigit():
                num=num*10+(int)(expr[i])-(int)('0')
            
        if plus!=-1:
            return self.eva(expr,begin,plus-1)+sgn*(self.eva(expr,plus+1,end))
        
        if mul!=-1:
            return self.eva(expr,begin,mul-1)*self.eva(expr,mul+1,end)
        
        return num
        
    def evaluate(self, expr):
        length=len(expr)
        result=self.eva(expr,0,length-1)
        return result