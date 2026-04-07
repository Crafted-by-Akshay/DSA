from collections import defaultdict, deque
from typing import List

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacency_list = defaultdict(list)
        in_degree = [0] * n
        
        for src,dst in edges:
            adjacency_list[src].append(dst)
            #graph[edge[0]].append(edge[1])
            in_degree[dst] += 1

        queue = deque([node for node in range(n) if in_degree[node] == 0])
        result = []

        while queue:
            current_node = queue.popleft()
            result.append(current_node)

            for neighbor in adjacency_list[current_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) == n:
            return result
        else:
            # Graph has a cycle
            return []
