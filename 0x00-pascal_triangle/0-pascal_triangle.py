def pascal_triangle(n):
    if isinstance(n, int):
        if n <= 0:
            return []

        pascal = [[0] * (i+1) for i in range(n)]

        for i in range(n):
            pascal[i][0] = 1
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
            pascal[i][i] = 1

        return pascal


triangle = pascal_triangle(5)

for row in triangle:
    print("[{}]".format(",".join([str(x) for x in row])))
