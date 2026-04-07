class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}
        for i in range(n):
            adj_list[i]=[]
        ####################
        for s,d,w in edges:
            adj_list[s].append([d,w])
            adj_list[d].append([s,w])
        
        visit = set()
        mst=[]
        min_heap = []

        visit.add(0)

        for d,w in adj_list[0]:
            heapq.heappush(min_heap,[w,0,d])
        total_wt=0
        res=0
        while min_heap:
            w1,n1,n2 = heapq.heappop(min_heap)
            if n2 in visit:
                continue
            res+=w1
            mst.append([n1,n2])
            visit.add(n2)

            for nei,wt in adj_list[n2]:
                if nei in visit:
                    continue
                heapq.heappush(min_heap,[wt,n2,nei])      
        return res if len(visit) == n else -1 

        
        