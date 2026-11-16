from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            course_map[course].append(prereq)
        
        visited = set()
        visiting = set()
        res = []

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            for prereq in course_map[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)

            visited.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res
