class MergeSortedArray:
    def mergeSortedArray(self, arr1, arr2, n, m):
        if not m and not n:
            return
        
        i=m-1
        j=n-1
        x=n+m-1
        while i>=0 and j>=0:
            if arr2[i]>arr1[j]:
                arr1[x]=arr2[i]
                i-=1
            else: 
                arr1[x]=arr1[j]
                j-=1
            x-=1
            
        if i>=0:
            arr1[0:x+1]=arr2[0:i+1]