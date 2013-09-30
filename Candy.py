class Candy:
    def minimalCandies(self, ratings):
        size = len(ratings)
        left2right = [1] * size
        for i in range(1, size):
            if ratings[i] > ratings[i-1]:
                left2right[i] = left2right[i-1]+1
        right2left = [1] * size
        for i in range(size-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                right2left[i] = right2left[i+1]+1
        final = [1] * size
        for i in range(size):
            final[i] = max(left2right[i], right2left[i])
        return sum(final)