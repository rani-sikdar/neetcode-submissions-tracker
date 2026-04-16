class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Key Idea:
        # Number of rows in result = number of columns in original
        # res[i][j] = matrix[j][i]

        
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
                
        for j in range(cols):          # iterate over columns
            new_row = []
            for i in range(rows):      # iterate over rows
                new_row.append(matrix[i][j])
            res.append(new_row)

        return res
            

                