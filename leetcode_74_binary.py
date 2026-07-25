class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def search_for_row():

            low = 0
            high = len(matrix) - 1

            while low<=high:

                mid = (low+high) // 2

            
                first = matrix[mid][0]
                last = matrix[mid][-1]

                # check targat lie in row 

                if first <= target <= last:
                    return mid

                elif target > last:
                    low = mid + 1

                else:
                    high = mid -1

            return -1


        def search_on_row(row):

            low = 0
            high = len(matrix[row]) - 1

            while low<=high:

                mid = (low + high) // 2

                value = matrix[row][mid]

                if value == target:
                    return True

                elif value < target:
                    low = mid +1

                else:
                    high = mid -1

            return False


        row = search_for_row()

        # If no valid row exists
        if row == -1:
            return False

        # Search inside the identified row
        return search_on_row(row)



        
