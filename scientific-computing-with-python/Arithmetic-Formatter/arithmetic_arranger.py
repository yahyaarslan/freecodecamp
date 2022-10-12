def arithmetic_arranger(problems, showAnswer=False):
    # Allow only five problems.
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize the output.
    upper = []
    lower = []
    operator = []

    for problem in problems:
        temp = problem.split()
        upper.append(temp[0])
        operator.append(temp[1])
        lower.append(temp[2])

    # Define range.
    range_ = range(len(upper))

    # Allow only addition and subtraction.
    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."
    if "+" not in operator or "-" not in operator:
        return "Error: Operator must be '+' or '-'."

    # Allow only digits
    for i in range_:
        if not (upper[i].isdigit() and lower[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # Allow only four digits.
    for i in range_:
        if len(upper[i]) > 4 or len(lower[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # Calculate the length of the longest number.
    upper_row = []
    lower_row = []
    line_row = []
    solution_row = []

    # Propose upper row.
    for i in range_:
        if len(upper[i]) > len(lower[i]):
            upper_row.append(" "*2 + upper[i])
        else:
            upper_row.append(
                " "*(len(lower[i]) - len(upper[i]) + 2) + upper[i])

    # Propose lower row.
    for i in range_:
        if len(lower[i]) > len(upper[i]):
            lower_row.append(operator[i] + " " + lower[i])
        else:
            lower_row.append(
                operator[i] + " "*(len(upper[i]) - len(lower[i]) + 1) + lower[i])

    # Propose line row.
    for i in range_:
        line_row.append("-"*(max(len(upper[i]), len(lower[i])) + 2))

    # Propose solution row.
    if showAnswer:
        for i in range_:
            if operator[i] == "+":
                ans = str(int(upper[i]) + int(lower[i]))
            else:
                ans = str(int(upper[i]) - int(lower[i]))

            if len(ans) > max(len(upper[i]), len(lower[i])):
                solution_row.append(" " + ans)
            else:
                solution_row.append(
                    " "*(max(len(upper[i]), len(lower[i])) - len(ans) + 2) + ans)
        return ("    ".join(upper_row) + "\n" + "    ".join(lower_row) + "\n" + "    ".join(line_row) + "\n" + "    ".join(solution_row))
    else:
        return ("    ".join(upper_row) + "\n" + "    ".join(lower_row) + "\n" + "    ".join(line_row))
