class MaxConsSum:
    def maxConsSum(self, arr):
        n=len(arr)
        sum_max=0
        i=0
        sum_temp=0
        while i<n:
            sum_temp+=arr[i]
            if sum_temp<0:
                sum_temp=0
            else:
                sum_max= sum_temp if sum_max<sum_temp else sum_max
            i+=1
        return sum_max