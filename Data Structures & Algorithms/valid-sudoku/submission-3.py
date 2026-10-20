class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                number = board[r][c]

                if number == ".":
                    continue
                
                box_index = (r//3) * 3 + (c//3)

                if (number in rows[r] or number in columns[c] or number in boxes[box_index]):
                    return False
                
                rows[r].add(number)
                columns[c].add(number)
                boxes[box_index].add(number)
        
        return True
                    
        