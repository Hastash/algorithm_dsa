from collections import deque

def canFinish(numCourses, prerequisites):
    # Build a graph representation using adjacency list and calculate in-degrees
    graph = [[] for _ in range(numCourses)]
    in_degrees = [0] * numCourses 
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        in_degrees[course] += 1
    
    # Initialized the queue with nodes haveing in-degree 0
    queue = deque([course for course in range (numCourses) if in_degrees[course] == 0])
    
    # Perform BFS and update in-degrees as we process nodes
    while queue:
        course = queue.popleft()
        numCourses -= 1 # Decrease number of remaining courses
        for neighbor in graph[course]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)
    
    # If all courses are processed (no cycles), return True, otherwise return False
    return numCourses == 0

if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2]]
    print(canFinish(numCourses, prerequisites))