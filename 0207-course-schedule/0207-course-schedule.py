class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj= {course: [] for course in range(numCourses)}

        for course, pre in prerequisites:
            adj[course].append(pre)
        
        for course in range(numCourses):
            stack = [(course, set())]
            while stack:
                cur_course, visited = stack.pop()
                if cur_course in visited:
                    return False
                visited.add(cur_course)
                for pre in adj[cur_course]:
                    stack.append((pre, visited.copy()))
            adj[course] = []
        return True
                    
        