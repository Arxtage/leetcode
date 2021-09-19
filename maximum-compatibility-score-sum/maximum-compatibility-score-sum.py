from scipy.optimize import linear_sum_assignment
import numpy as np

class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        # Hungarian Algorithm
        # O(n^3)
        
        matrix = np.zeros(shape=(len(students), len(mentors)), dtype=np.int)
        
        for i in range(len(students)):
            for j in range(len(mentors)):
                sm = 0
                for k in range(len(students[i])):
                    if students[i][k] == mentors[j][k]:
                        sm += 1
                matrix[i,j] = -sm
        rows, cols = linear_sum_assignment(matrix)
        return -matrix[rows, cols].sum()