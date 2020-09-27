# 54. Spiral Matrix
# Straightforward solution simulating matrix.
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # two conditions where you change directions:
        # 1. you see something you've already seen
        # 2. you reach a boundary

        # to keep track of things we've seen, substitute "$"
        # to keep track of validity, check to see if a coord is valid
        # direction changes are: right -> down, down -> left, left -> up, up-> right
        def isValid(i, j):
            valid_row = i >= 0 and i < len(matrix)
            valid_col = j >= 0 and j < len(matrix[0])
            return valid_row and valid_col

        direction_change = {
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
            (0, 1): (1, 0)
        }
        r_list = []
        START_COORD = (0, 0)
        START_DIRECTION = (0, 1)
        coord = START_COORD
        direction = START_DIRECTION
        if len(matrix) == 0:
            return r_list
        while len(r_list) != len(matrix) * len(matrix[0]):
            row = coord[0]
            col = coord[1]
            r_list.append(matrix[row][col])
            matrix[row][col] = "$seen"
            new_coord = (coord[0] + direction[0], coord[1] + direction[1])
            if isValid(new_coord[0], new_coord[1]) and matrix[new_coord[0]][new_coord[1]] != "$seen":
                coord = new_coord
            else:
                direction = direction_change[direction]
                new_coord = (coord[0] + direction[0], coord[1] + direction[1])
                coord = new_coord
        return r_list

# Rotate Matrix
# Remember that you need to switch things in place
# if you're to use O(1) memory.
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # get the rotated coordinates
        def calculate_rotated_coords(coords, length):
            return (coords[1], length - 1 - coords[0])

        # starting from coords, swap a group of
        # four in a given matrix
        def swap_four_coords(coords, matrix):
            swap_in_value = matrix[coords[0]][coords[1]]
            for i in range(4):
                new_coords = calculate_rotated_coords(coords, len(matrix))
                temp = matrix[new_coords[0]][new_coords[1]]
                matrix[new_coords[0]][new_coords[1]] = swap_in_value
                coords = new_coords
                swap_in_value = temp

        num_layers = len(matrix) // 2
        for layer in range(num_layers):
            for j in range(layer, len(matrix) - 1 - layer):
                swap_four_coords((layer, j), matrix)

# Merge K-Sorted Lists
# Classic implementation; can use either a heap
# or divide and conquer in order to get optimal
# solution.
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # pseudocode:
        # create a heap
        # add all of the current k elements into the heap
        # pop the smallest element off and add it to the return list
        # add that element's next into the heap.
        # when the heap is empty, return the created list.
        # this would run in log(k) * k * n time.

        # create a dummy node
        head = ptr = ListNode(0)
        pq = PriorityQueue()
        for i in lists:
            if i is not None:
                pq.put((i.val, i))
        while not pq.empty():
            node_tuple = pq.get()
            value = node_tuple[0]
            node = node_tuple[1]
            ptr.next = ListNode(value)
            ptr = ptr.next
            node = node.next
            if node is not None:
                pq.put((node.val, node))
        return head.next
