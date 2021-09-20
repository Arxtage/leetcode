"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # DFS
        
        emap = {e.id: e for e in employees}
        
        def dfs(id_):
            employee = emap[id_]
            return (employee.importance + sum(dfs(id_) for id_ in employee.subordinates))
        return dfs(id)