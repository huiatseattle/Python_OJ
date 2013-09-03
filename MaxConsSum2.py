class MaxConsSum2:
    def maxConsSum2(self, arr):
        n=len(arr)
        sum_max=0
        #first, max stay in 0-(n-1)
        a=0
        i=0
        sum_temp=0
        while i<n:
            sum_temp+=arr[i]
            if sum_temp<0:
                sum_temp=0
            else:
                a = sum_temp if a<sum_temp else a
            i+=1
        #second, find min sum, total sum - min sum
        b=0
        i=0
        sum_temp=0
        total_sum=0
        while i<n:
            total_sum+=arr[i]
            sum_temp+=arr[i]
            if sum_temp>0:
                sum_temp=0
            else:
                b = sum_temp if b>sum_temp else b
            i+=1
        b=total_sum-b
        sum_max=a if b<a else b
        return sum_max