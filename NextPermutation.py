class NextPermutation:
    def nextPermutation(self, arr):
        if not arr or len(arr)<=1:
            return False
        last=len(arr)-1
        mid=last-1
        #Partition the sequence into two sequences
        while mid>=0 and arr[mid]>=arr[mid+1]:
            mid-=1
        
        if mid < 0:
            return False
        #find am, the first value larger than aj. 
        pivot=last
        while mid<pivot and arr[mid]>=arr[pivot]:
            pivot-=1
            
        arr[mid], arr[pivot]=arr[pivot], arr[mid]
        
        #reverse
        mid+=1
        while last>mid:
            arr[mid], arr[last]=arr[last], arr[mid]
            last-=1
            mid+=1
        return True
