class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_list = {}
        for i in range(n):
            adj_list[i]=[]
        for s,d,w in edges:
            adj_list[s].append([d,w])
        
        min_heap = []
        shortest = {}
        min_heap.append([0,src])

        while min_heap:
            w1,n1 =heapq.heappop(min_heap)
            if n1 in shortest:
                continue
            shortest[n1]=w1

            for n2,w2 in adj_list[n1]:
                if n2 in shortest:
                    continue
                heapq.heappush(min_heap,[w1+w2,n2])
        
        for i in range(n):
            if i not in shortest:
                shortest[i]=-1

        return shortest

            
