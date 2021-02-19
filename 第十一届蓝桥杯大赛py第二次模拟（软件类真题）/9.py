#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

import math




n = 4  # 村庄数量
numEdges =int(( n * (n - 1)) /2)
test = [[1, 1, 3],
        [9, 9, 7],
        [8, 8, 6],
        [4, 5, 4]]

class EdgeNode:
    def __init__(self):
        self.adjvex = 0
        self.weight = 0
        self.next = None


class VertexNode:
    def __init__(self):
        self.firstedge = None
        self.data = 0

class GraphAdjList:
    def __init__(self,numVertexes,numEdges):

        self.numVertexes = numVertexes
        self.adjList = [VertexNode() for _ in range(n*n)]
        self.numEdges=numEdges

class MGraph:
    def __init__(self):
        self.graphAdjList=GraphAdjList(n,numEdges)
        self.vexs = [0 for _ in range(n)]
        self.arc = [self.vexs.copy() for _ in range(n)]


    def createMGraph(self):
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1, h1 = test[i]
                x2, y2, h2 = test[j]
                cost = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)) \
                       + math.pow(h1 - h2, 2)
                cost=round(cost,2)
                self.arc[i][j] = cost
                self.arc[j][i] = self.arc[i][j]
    def createALGraph(self):

        count=0

        for i in range(self.graphAdjList.numVertexes):
            self.graphAdjList.adjList[i].data=i
            self.graphAdjList.adjList[i].firstedge=None
            count+=1
        for j in range(self.graphAdjList.numEdges):
            e = EdgeNode()
            e.adjvex=j
            e.next=self.graphAdjList.adjList[count].firstedge
            self.graphAdjList.adjList[count].firstedge=e
            e = EdgeNode()
            e.adjvex=i
            e.next=self.graphAdjList.adjList[j].firstedge
            self.graphAdjList.adjList[j].firstedge
    def showMGraph(self):
        for a in self.arc:
            print(a)
    def showALGraph(self):
        for a in self.graphAdjList.adjList:
            print(a)
    def dfsTraverse(self,i):
        """
        :type i: 遍历开始的结点
        """
        visisted=[False for _ in range(n)]
        def DFS(i):
            visisted[i]=True
            print(self.vexs[i])
            for j in range(n):
                if(self.arc[i][j]==1 and (not visisted[j])):
                    DFS(i)

        for i in range(n):
            if(not visisted[i]):
                DFS(i)
    def prim(self):
        min=65535
        adjvex=[0 for _ in range(n)] #相关顶点下标
        lowcost=[0 for _ in range(n)]#相关顶点间的权值
        for i in range(n):
            lowcost[i]=self.arc[0][i]

        for i in range(1,n):
            min=65536
            j=1
            k=0
            while(j<n):
                if lowcost[j]!=0 and lowcost[j]<min:
                    min=lowcost[j]
                    k=j
                j+=1
            print("({}<->{})".format(adjvex[k],k))
            lowcost[k]=0
            for j in range(1,n):
                if(lowcost[j]!=0 and self.arc[k][j]<lowcost[j]):
                    lowcost[j]=self.arc[k][j]
                    adjvex[j]=k
        print('lowcost=', lowcost)
        print('adjvex',adjvex)

        # 计算总共的代价
        sum=0
        for i,v in enumerate(adjvex):

            sum+=self.arc[i][v]
        print("sum=",sum)

g = MGraph()
g.createMGraph()
g.showMGraph()
# g.dfsTraverse(0)
g.prim()


# g.createALGraph()
# g.showALGraph()
#