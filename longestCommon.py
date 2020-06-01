def lcsLength(X, Y):
    m = len(X)
    n = len(Y)

    b = list()
    for i in range(m):
        b.append(list())
        for j in range(n):
            b[i].append(0)

    c = list()
    for i in range(m+1):
        c.append(list())
        for j in range(n+1):
            c[i].append(0)

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i][j] = c[i-1][j-1] + 1
                b[i-1][j-1] = 'D' #Diagnole
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = 'U' #Up
            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = 'S' #Sideways

    return c, b

def printLCS(b, X, i, j):
    if i == -1 or j == -1:
        return
    if b[i][j] == 'D':
        printLCS(b, X, i-1, j-1)
        print(X[i])
    elif b[i][j] == 'U':
        printLCS(b, X, i-1, j)
    else:
        printLCS(b, X, i, j-1)

X = 'daily'
Y = 'ailment'
c, b = lcsLength(X, Y)
printLCS(b, X, len(X)-1, len(Y)-1)