from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            courses[course].append(prereq)

        visiting = set()
        done = set()
        
        def dfs(course):
            if course in visiting:
                return False
            if course in done:
                return True

            visiting.add(course)
            for prereq in courses[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            done.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
