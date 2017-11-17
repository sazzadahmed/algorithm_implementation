class edge:
    def __init__(self,u,v,w,):
        pass
'''
this is the adjacency list graph implementation
'''
class graph:
    def __init__(self,V,is_directed=False):
        self.V=V
        self.adjacency_list=None
        self.is_directed=self.is_directed
        self.edge_list=[]
        self.adjancy_matrix=None
    def add_edge(self,u,v,w=None):
        self.edge_list.append([u,v,w if w else 1 ])
        if not self.is_directed:
            self.edge_list.append([v,u,w if w else 1])
    def adjacency_list(self):
        self.adjacency_list={i:[] for i in range(self.V)}
        for i in self.edge_list:
            val={i[1]:i[2]}
            self.adjacency_list[i[0]].append(val)











Graph=graph()