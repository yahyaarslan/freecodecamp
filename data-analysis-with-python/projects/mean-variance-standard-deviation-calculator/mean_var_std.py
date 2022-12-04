import numpy as np


def calculate(list):
    # Make matrix
    list = np.array(list, dtype=np.uint8)

    try:
        list = list.reshape(3, 3)
    except:
        raise ValueError("List must contain nine numbers.")

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
    max_columns = np.amax(list, axis=0)
    column1 = max_columns[0]
    column2 = max_columns[1]
    column3 = max_columns[2]
    max_columns = [column1, column2, column3]

    ## Rows
    max_rows = np.amax(list, axis=1)
    row1 = max_rows[0]
    row2 = max_rows[1]
    row3 = max_rows[2]
    max_rows = [row1, row2, row3]

    ## Flattened
    max_flat = np.amax(list)

    # Calc. Minimum
    ## Column
    min_columns = np.amin(list, axis=0)
    column1 = min_columns[0]
    column2 = min_columns[1]
    column3 = min_columns[2]
    min_columns = [column1, column2, column3]

    ## Rows
    min_rows = np.amin(list, axis=1)
    row1 = min_rows[0]
    row2 = min_rows[1]
    row3 = min_rows[2]
    min_rows = [row1, row2, row3]

    ## Flattened
    min_flat = np.amin(list)

    # Calc. Sum
    ## Column
    column1 = np.sum(list, where=[True, False, False])
    column2 = np.sum(list, where=[False, True, False])
    column3 = np.sum(list, where=[False, False, True])
    sum_columns = [column1, column2, column3]

    ## Rows
    row1 = np.sum(list, where=[[True], [False], [False]])
    row2 = np.sum(list, where=[[False], [True], [False]])
    row3 = np.sum(list, where=[[False], [False], [True]])
    sum_rows = [row1, row2, row3]

    ## Flattened
    sum_flat = np.sum(list)

    # Dict
    calculations = {
        'mean': [mean_colums, mean_rows, mean_flat],
        'variance': [var_columns, var_rows, var_flat],
        'standard deviation': [std_columns, std_rows, std_flat],
        'max': [max_columns, max_rows, max_flat],
        'min': [min_columns, min_rows, min_flat],
        'sum': [sum_columns, sum_rows, sum_flat]
    }

    # Test
    #print(calculations)

    return calculations
