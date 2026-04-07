from collections import deque
from typing import List
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_degree = [0]*n
        for src,dst in edges:
            adj_list[src].append(dst)
            in_degree[dst]+=1
        
        queue = deque([node for node in range(n) if in_degree[node]==0])
        res = []
        while queue:
            curr_node = queue.popleft()
            res.append(curr_node)
            for nei in adj_list[curr_node]:
                in_degree[nei]-=1
                if in_degree[nei]==0:
                    queue.append(nei)
        
        if len(res)==n:
            #return res
            #print('res,',res)
            #common_ancestor = [res.index(node) for node in range(n)]
            #print('common_ancestor',common_ancestor)
            return res
        else:
            return []

        