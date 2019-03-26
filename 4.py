def lssepinput ():
    sep = input('give me a separator\n')
    for i in range(0, len(sep)):
        if sep[i].isdigit() == True:
            exit("Error, separator doesn't allow digits")
    print('give me intigers divided by \" ', sep,' \"')
    l = input()
    j = []
    k = ''
    for i in range (0,len(l)):
        if l[i]!=sep and l[i] != ' ':
            k = k+ l[i]
        if l[i] == sep or i==len(l):
            j.append(int(k))
            k = ''
    return j

k = lssepinput()
print (k)