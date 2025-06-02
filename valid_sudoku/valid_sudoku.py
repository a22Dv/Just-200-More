from typing import List, Set
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # We need to create a counter for all 9 rows, columns, and subgrids.
        rows: List[Set[str]] = []
        columns: List[Set[str]] = []
        subgrids: List[Set[str]] = []
        for unit in (rows, columns, subgrids):
            for _ in range(9):
                unit.append(set(["1", "2", "3", "4", "5", "6", "7", "8", "9"]))
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                # i is what row that cell belongs, with j being the column.
                if cell == ".":
                    continue

                # This means cells with rows 0 to 2 have (i // 3) * 3 = 0
                # subgrids behind them. 6 to 8 have 6 subgrids behind them.
                # Columns 0, 1, 2 have no subgrids behind them, 6 to 8 have 2 behind them.
                subgrid_count = ((i // 3) * 3) + (j // 3)
                if all(
                    [
                        cell in rows[i],
                        cell in columns[j],
                        cell in subgrids[subgrid_count],
                    ]
                ):
                    rows[i].remove(cell)
                    columns[j].remove(cell)
                    subgrids[subgrid_count].remove(cell)
                else:
                    return False
        return True
