import pandas as pd
from math import floor


def sudoku(puzzle):
    def _options(related_cells):
        l = {puzz[ic].iloc[ir] for ir, ic in related_cells if puzz[ic].iloc[ir] > 0}
        return [i for i in range(1, 10) if i not in l]

    def _related_cells(irow, icol):
        row_cells = [(irow, i) for i in range(9) if i != icol]
        col_cells = [(i, icol) for i in range(9) if i != irow]
        sqr_cells = [(ir, ic) for ir in
                     range(floor(irow / 3) * 3, (floor(irow / 3) * 3) + 3) for ic in
                     range(floor(icol / 3) * 3, (floor(icol / 3) * 3) + 3) if (ir, ic) != (irow, icol)]
        return set(row_cells + col_cells + sqr_cells)

    puzz = pd.DataFrame(puzzle).astype(dtype='object')
    cells_to_solve = dict()

    for irow, row in puzz.iterrows():
        icol: int
        irow: int
        for icol, value in enumerate(row):
            if value > 0:
                continue
            related_cells = _related_cells(irow, icol)
            options = _options(related_cells)
            cells_to_solve[(irow, icol)] = {
                'options': options,
                'related': related_cells
            }

    for cell, cell_dict in cells_to_solve.items():
        cells_to_solve[cell]['related'] = [rc for rc in cell_dict['related'] if rc in cells_to_solve.keys()]

    while cells_to_solve:
        cell = sorted(cells_to_solve.items(), key=lambda x: len(x[1]['options']))[0][0]
        cell_dict = cells_to_solve.pop(cell)
        if len(cell_dict['options']) > 1:
            return None

        irow, icol = cell
        puzz[icol].iloc[irow] = cell_dict['options'][0]
        for related_cell in cell_dict['related']:
            cells_to_solve[related_cell]['related'].remove(cell)
            try:
                cells_to_solve[related_cell]['options'].remove(cell_dict['options'][0])
            except ValueError:
                pass

    return puzz.values.tolist()


if __name__ == '__main__':
    puzzle, solution = (
        [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]],
        [[5, 3, 4, 6, 7, 8, 9, 1, 2],
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    )
    ans = sudoku(puzzle)
    if not ans == solution:
        print(str(ans))
        print(str(solution))
    else:
        print(ans == solution)
