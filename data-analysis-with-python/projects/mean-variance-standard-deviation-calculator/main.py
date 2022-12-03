# This entrypoint file to be used in development. Start by reading README.md
# %%
import mean_var_std
from unittest import main

import numpy as np


def calculate(list):
    # Make matrix
    list = np.array(list, dtype=np.uint8)
    list = list.reshape(3, 3)

    # Calc. Mean
    ## Column
    column1 = np.mean(list, where=[True, False, False])
    column2 = np.mean(list, where=[False, True, False])
    column3 = np.mean(list, where=[False, False, True])
    mean_colums = [column1, column2, column3]

    ## Rows
    row1 = np.mean(list, where=[[True], [False], [False]])
    row2 = np.mean(list, where=[[False], [True], [False]])
    row3 = np.mean(list, where=[[False], [False], [True]])
    mean_rows = [row1, row2, row3]

    ## Flattened
    mean_flat = list.mean()

    # Calc. Variance
    ## Column
    column1 = np.var(list, where=[True, False, False])
    column2 = np.var(list, where=[False, True, False])
    column3 = np.var(list, where=[False, False, True])
    var_columns = [column1, column2, column3]

    ## Rows
    row1 = np.var(list, where=[[True], [False], [False]])
    row2 = np.var(list, where=[[False], [True], [False]])
    row3 = np.var(list, where=[[False], [False], [True]])
    var_rows = [row1, row2, row3]

    ## Flattened
    var_flat = np.var(list)

    # Calc. Standard deviation
    ## Column
    column1 = np.std(list, where=[True, False, False])
    column2 = np.std(list, where=[False, True, False])
    column3 = np.std(list, where=[False, False, True])
    std_columns = [column1, column2, column3]

    ## Rows
    row1 = np.std(list, where=[[True], [False], [False]])
    row2 = np.std(list, where=[[False], [True], [False]])
    row3 = np.std(list, where=[[False], [False], [True]])
    std_rows = [row1, row2, row3]

    ## Flattened
    std_flat = np.std(list)

    # Calc. Max
    ## Column
    np.max
    column1 = np.max(list, where=[True, False, False])
    column2 = np.max(list, where=[False, True, False])
    column3 = np.max(list, where=[False, False, True])
    max_columns = [column1, column2, column3]

    ## Rows
    row1 = np.max(list, where=[[True], [False], [False]])
    row2 = np.max(list, where=[[False], [True], [False]])
    row3 = np.max(list, where=[[False], [False], [True]])
    max_rows = [row1, row2, row3]

    ## Flattened
    max_flat = np.max(list)

    # Dict
    dictionary = {
        'mean': [mean_colums, mean_rows, mean_flat],
        'variance': [var_columns, var_rows, var_flat],
        'standard deviation': [std_columns, std_rows, std_flat],
        'max' : [max_columns, max_rows, max_flat],
    }

    # Test
    print(dictionary)

    #return calculations


(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

# Run unit tests automatically
# main(module='test_module', exit=False)

# %%
