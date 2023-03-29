def arithmetic_arranger(problems, solution=False):
    toppart = ""
    bottompart = ""
    middlepart = ""
    endpart = ""
    total = 0
    if len(problems) > 5:
        return "Error: Too many problems."
    for math in problems:
        y = math.split(" ")
        if len(y) < 3:
            return "Error: Please enter a valid format"
        topsize = len(y[0])
        bottomsize = len(y[2])
        length = abs(topsize - bottomsize)
        if topsize > 4 or bottomsize > 4:
            return "Error: Numbers cannot be more than four digits."
        elif y[1] != '+' and y[1] != '-':
            return "Error: Operator must be '+' or '-'."
        elif y[0].isdigit() is False or y[2].isdigit() is False:
            return "Error: Numbers must only contain digits."
        if y[1] == "+":
            total = str(int(y[0]) + int(y[2]))
        elif y[1] == "-":
            total = str(int(y[0]) - int(y[2]))
        if topsize < bottomsize:
            toppart += 2 * " " + length * " " + y[0] + 4 * " "
            bottompart += y[1] + " " + y[2] + 4 * " "
            middlepart += (bottomsize + 2) * "-" + 4 * " "
        elif bottomsize < topsize:
            toppart += 2 * " " + (length - topsize) * " " + y[0] + 4 * " "
            middlepart += (topsize + 2) * "-" + 4 * " "
            bottompart += y[1] + (length + 1) * " " + y[2] + 4 * " "
        else:
            toppart += 2 * " " + y[0] + 4 * " "
            bottompart += y[1] + " " + y[2] + 4 * " "
            middlepart += (bottomsize + 2) * "-" + 4 * " "
        if solution is True:
            if int(total) < 0:
                endpart += " " + total + 4 * " "
            else:
                if bottomsize < topsize:
                    endpart += (2 - (len(total) - topsize)) * " " + total + 4 * " "
                elif topsize < bottomsize:
                    endpart += (2 - (len(total) - bottomsize)) * " " + total + 4 * " "
                else:
                    endpart += 2 * " " + total + 4 * " "
    return (toppart.rstrip() + "\n" + bottompart.rstrip() + "\n" + middlepart.rstrip() + "\n" + endpart.rstrip()).rstrip()
