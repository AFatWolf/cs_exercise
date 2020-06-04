def v(n):
    ok = [[0] * (2*n) for i in range(n)]
    for i in range(n):
        ok[i][i] = 1
        ok[i][2*n-1-i] = 1
    for i in range(n):
        for j in range(len(ok[i])):
            print("#" if ok[i][j] else " ", end = "")
        print()
v(1)