class Edge:
    def __init__(self,u,v,w=1):
        self.u=u
        self.v=v
        self.w=w
class Graph:
    def __init__(self,v,dircted=False,weight=False):
        self.V=v
        self.Adjacecy_Matrix={}
        for i in range(v):
            self.Adjacecy_Matrix[i]=list()

    def __str__(self):
        return 'graph'

    def makeAdjacencyMatrix(self,edge):
        re=[edge.v,edge.w]
        self.Adjacecy_Matrix[edge.u].append(re)



    def show_adjancency_list(self,u):
        for i in self.Adjacecy_Matrix[u]:
            print(i)
g=Graph(6,weight=True)
a1=Edge(0,1,234)
a2=Edge(0,2,324)
a3=Edge(0,4,3243)
a4=Edge(2,3,45)
g.makeAdjacencyMatrix(a1)
g.makeAdjacencyMatrix(a2)
g.makeAdjacencyMatrix(a3)
g.makeAdjacencyMatrix(a4)
g.show_adjancency_list(0)