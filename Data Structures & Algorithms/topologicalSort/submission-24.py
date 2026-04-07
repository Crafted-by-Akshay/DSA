from collections import defaultdict
class Solution:
    def dfs(self,node,adj_list,visit,path,res):
        if node in path:
            return False
        if node in visit:
            return True
        visit.add(node)
        path.add(node)
        for nei in adj_list[node]:
            if not self.dfs(nei,adj_list,visit,path,res):
                return False
        path.remove(node)
        res.append(node)
        return True


    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]: 
        adj_list = defaultdict(list)
        for src,dst in edges:
            adj_list[src].append(dst)
        #print('adj_list',adj_list)
        path = set()
        visit = set()
        res = []
        for i in range(0,n):
            if not self.dfs(i,adj_list,visit,path,res):
                return []
        res.reverse()
        return res
