class GridVisit:
    def existPath(self, x, y):
        left = sort(set(x))
        right = sort(set(y))
        edge = []
        k = len(x)
        leftdegree = [0] * len(left)
        rightdegree = [0] * len(right)
        for i in range(k):
            edge.append([left.index(x[i]), right.index(y[i])])
            leftdegree[left.index(x[i])] += 1
            rightdegree[right.index(y[i])] += 1
        leftdegreecheck = [0 for j in leftdegree if j%2==0 else 1]
        rightdegreecheck = [0 for j in rightdegree if j%2==0 else 1]
        if sum(leftdegreecheck)+sum(rightdegreecheck) > 2:
            return False
        vertexset = [edge[0][0]]
        while len(vertexset) > lastsize:
            for p in vertexset:
                