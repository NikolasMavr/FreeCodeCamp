def arithmetic_arranger(problems, solve = False):

    if len(problems) > 5:
        return "Error: Too many problems."
    first = ""
    second = ""
    lines = ""
    sumx = ""

    for items in problems:

        number1 = items.split()[0]
        operator = items.split()[1]
        number2 = items.split()[2]

        if number1.isdigit() is False or number2.isdigit() is False:
            return "Error: Numbers must only contain digits."

        if operator == '*' or operator == '/':
            return "Error: Operator must be '+' or '-'."

        if len(number1) > 4 or len(number2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == '+':
            sum = int(number1) + int(number2)
        else:
            sum = int(number1) - int(number2)

        length = max(len(number1), len(number2)) + 2
        top = number1.rjust(length)
        bot = operator + number2.rjust(length - 1)
        line = ""
        res = str(sum).rjust(length)

        for s in range(length):
            line += "-"

        if items != problems[-1]:
            first += top + '    '
            second += bot + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            first += top
            second += bot
            lines += line
            sumx += res

    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines
    return string


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
