class MergeSortedArray:
    def mergeSortedArray(self, arr1, arr2, n, m):
        idx1 = n-1
        idx2 = m-1
        for i in range(n+m):
            idx = n+m-1-i
            if idx1>=0 and idx2>=0:
                if arr1[idx1] >= arr2[idx2]:
                    arr1[idx] = arr1[idx1]
                    idx1 -= 1
                elif arr1[idx1] < arr2[idx2]:
                    arr1[idx] = arr2[idx2]
                    idx2 -= 1
            elif idx1>=0:
                arr1[idx] = arr1[idx1]
                idx1 -= 1
            elif idx2>=0:
                arr1[idx] = arr2[idx2]
                idx2 -= 1
