# Do phuc tap thoi gian cua thuat toan khu Gauss voi ma tran vuong n x n: O(n^3)
def gaussian_elimination(aug_matrix):
    m = len(aug_matrix)
    n = len(aug_matrix[0])
    A = [row[:] for row in aug_matrix]

    for k in range(min(m, n) - 1):
        max_row = k
        max_val = abs(A[k][k])
        for i in range(k + 1, m):
            if abs(A[i][k]) > max_val:
                max_val = abs(A[i][k])
                max_row = i
        A[k], A[max_row] = A[max_row], A[k]

        for i in range(k + 1, m):
            if A[k][k] == 0:
                continue
            factor = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]

    for i in range(m):
        for j in range(n):
            A[i][j] = round(A[i][j], 2)

    return A


if __name__ == "__main__":
    augmented_matrix = [
        [2.0, 1.0, -1.0, 8.0],
        [-3.0, -1.0, 2.0, -11.0],
        [-2.0, 1.0, 2.0, -3.0]
    ]
    print("Ma tran bac thang:")
    for row in gaussian_elimination(augmented_matrix):
        print(row)
