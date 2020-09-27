# 73. Set Matrix Zeroes
# Came up with an excessively complicated recursive solution
# when all you needed to do was connect the idea of using certain
# parts of the matrix as flags. Here's the recursive solution, using
# a recursive "crawler":

def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # the basic idea is we have some sort of function
    # crawl. When crawl sees a zero, it recursively crawls
    # all of the available directions.
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    def isValid(i, j):
        valid_i = i < len(matrix) and i >= 0
        valid_j = j < len(matrix[0]) and j >= 0
        return valid_i and valid_j
    def isEdge(i, j):
        return i == 0 or i == len(matrix) - 1 or j == 0 or j == len(matrix[0]) - 1

    def crawl(direction, i, j):
        if matrix[i][j] == 0:
            matrix[i][j] = None
            for d in directions:
                new_i = d[0] + i
                new_j = d[1] + j
                if isValid(new_i, new_j):
                    crawl(d, new_i, new_j)
        if matrix[i][j] != 0:
            matrix[i][j] = None
            new_i = direction[0] + i
            new_j = direction[1] + j
            if isValid(new_i, new_j):
                crawl(direction, new_i, new_j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                crawl(directions[0], i, j)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == None:
                matrix[i][j] = 0

# A significantly simpler and more optimized solution involves using
# the first item of every row and column as a flag for the rest of the
# matrix, taking advantage of our iteration order to avoid conflicts. You
# can implement this another day.

# 1143. Longest Common Subsequence
# Got all of the major ideas for this one - including all of the DP steps,
# but you struggled to make the connection at the latest between dp[i - 1][j - 1]
# and the answer. Make sure not to get bogged down and think about WHY
# the code isn't working as opposed to excessive debugging.

def longestCommonSubsequence(text1, text2):
    dp_array = [[0 for i in range(len(text1))] for j in range(len(text2))]
    if text1[0] == text2[0]:
        dp_array[0][0] = 1
    for i in range(1, len(text1)):
        if text1[i] == text2[0]:
            dp_array[0][i] = 1
        else:
            dp_array[0][i] = dp_array[0][i - 1]

    for j in range(1, len(text2)):
        if text2[j] == text1[0]:
            dp_array[j][0] = 1
        else:
            dp_array[j][0] = dp_array[j - 1][0]

    for i in range(1, len(text2)):
        for j in range(1, len(text1)):
            if text2[i] == text1[j]:
                dp_array[i][j] = 1 + dp_array[i - 1][j - 1]
            else:
                dp_array[i][j] = max(dp_array[i - 1][j], dp_array[i][j - 1])
    return dp_array[len(text2) - 1][len(text1) - 1]
