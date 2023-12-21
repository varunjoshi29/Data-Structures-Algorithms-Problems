class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def pathFinder(graph, cost, src, dest):

            visited = set()
            parent_map = {}

            q = [src]
            visited.add(src)

            found = False
            while len(q) > 0:
                current = q.pop(0)
                if current == dest:
                    found = True
                    break
                
                for node in graph[current]:
                    if node not in visited:
                        visited.add(node)
                        q.append(node)
                        parent_map[node] = current

            if found:
                ans = 1.0
                curr = dest
                while curr in parent_map:
                    parent = parent_map[curr]
                    ans = ans * cost[parent + "_" + curr]
                    curr = parent
                cost[src + "_" + dest] = ans
                cost[dest + "_" + src] = 1/ans
                graph[src].append(dest)
                graph[dest].append(src)
                return ans
            else:
                return -1.0
        
        graph = {}
        cost = {}
        for i in range(len(equations)):
            src, dest = equations[i]
            price = values[i]
            if src in graph:
                graph[src].append(dest)
            else:
                graph[src] = [dest]
            
            if dest in graph:
                graph[dest].append(src)
            else:
                graph[dest] = [src]
            
            cost[src+"_"+dest] = price
            cost[dest+"_"+src] = 1/price
        
        output = []
        for query in queries:
            src, dest = query
            if src in graph and dest in graph:
                output.append(pathFinder(graph, cost, src, dest))
            else:
                output.append(-1.0)
        
        return output
