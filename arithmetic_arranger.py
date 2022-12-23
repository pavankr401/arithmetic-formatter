import re

def arithmetic_arranger(*args):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    
    if(len(args[0]) > 5):
        return "Error: Too many problems."
    
    for equation in args[0]:
        num1, operator, num2 = equation.split()
        
        try:
            if(int(num1) and int(num2)):
                pass
        except:
            return "Error: Numbers must only contain digits."
        
        if(len(num1) > 4 or len(num2) > 4): return "Error: Numbers cannot be more than four digits."
        
        res = 0
        if(operator == '+'):
            res = int(num1) + int(num2)
            res = str(res)
        elif(operator == '-'):
            res = int(num1) - int(num2)
            res = str(res)
        else:
            return "Error: Operator must be '+' or '-'."

        if(len(num1) > len(num2)):
            num2 = " " * (len(num1) - len(num2) ) + num2
        elif(len(num1) < len(num2)):
            num1 = " " * (len(num2) - len(num1) ) + num1

        line1 += "  " + num1 + " " * 4
        line2 += operator + " " + num2 + " " * 4
        line3 += "--" + '-' * len(num1) + " " * 4
        
        if(len(res) > len(num2)):
            line4 += " " + res + " " * 4
        else:
            line4 += "  " + res + " " * 4

    line1 = re.sub(' *$', '', line1)
    line2 = re.sub(' *$', '', line2)
    line3 = re.sub(' *$', '', line3)
    line4 = re.sub(' *$', '', line4)
    
    solution = line1 + '\n' + line2 + '\n' + line3

    if(len(args) > 1 and args[1]):
        solution += '\n' + line4
            
    return solution
