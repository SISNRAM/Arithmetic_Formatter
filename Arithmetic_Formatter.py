
def arithmetic_arranger(x, answer=False):
    first_line = []
    second_line = []
    opt = []
    test = True
    if(test == True):
        # **********Operator error***********
        for i in range(len(x)):
            for j in range(len(x)):
                if(x[i][j] == "*" or x[i][j] == "/"):
                    print("Error: Operator must be '+' or '-'.")
                    test = False
                    break

        # *********problems number error********
        if len(x) > 5:
            print("Error: Too many problems.")
            test = False
        # *********Digits only check & Length check************
        for i in range(len(x)):
            tmp = str(x[i])
            for char in x[i]:
                if (char == '-'):
                    opt.append("-")
                    h = tmp.split(' - ')
                    for i in range(len(h)):
                        if len(h[i]) > 4:
                            print("Error: Numbers cannot be more than four digits.")
                            test = False
                    first_line.append(h[0])
                    second_line.append(h[1])
                    tmp = tmp.replace(' - ', '')
                    break

                elif(char == '+'):
                    opt.append("+")
                    h = tmp.split(' + ')
                    for i in range(len(h)):
                        if len(h[i]) > 4:
                            print("Error: Numbers cannot be more than four digits.")
                            test = False
                    first_line.append(h[0])
                    second_line.append(h[1])
                    tmp = tmp.replace(' + ', '')
                    break

            if not (tmp.isdigit()):
                print("Error: Numbers must only contain digits.")
                print(tmp)
                test = False
                break
# ********Code d'affichage des lignes************
    if test == True:
        for i in range(len(first_line)):
            S = len(second_line[i])-len(first_line[i]
                                        ) if len(second_line[i])-len(first_line[i]) > 0 else 0
            print(" "*2 + S*" " + first_line[i], end=" "*4)
        print("")
        for j in range(len(second_line)):
            S = len(first_line[j])-len(second_line[j]
                                       ) if len(first_line[i])-len(second_line[i]) > 0 else 0
            print(opt[j]+" " + " "*S + second_line[j], end=" "*4)
        print("")
        for k in range(len(second_line)):
            S = len(second_line[k]) if len(second_line[k]) > len(
                first_line[k]) else len(first_line[k])
            print("-"*S+"--", end=" "*4)

        print("")
        # ****** Result logic*******
        if answer == True:
            for z in range(len(first_line)):
                a = int(first_line[z])
                b = int(second_line[z])
                # Biggest argument
                S = len(second_line[z]) if len(second_line[z]) > len(
                    first_line[z]) else len(first_line[z])
                # result
                # case 1
                if(opt[z] == "+"):
                    M = a+b
                    res = abs((len(str(M))-1) - S)
                    print(" " + " "*res + str(M), end=" "*4)
                # case 2
                elif(opt[z] == "-"):
                    m = a-b
                    res = abs((len(str(m))-1) - S)

                    print(" " + " "*res + str(m), end=" "*4)


arithmetic_arranger(
    ["122 - 682", "301 - 22", "4 + 4", "123 + 49"], True)
