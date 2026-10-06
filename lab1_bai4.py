def matrix_multiply(A, B):
    m = len(A)
    n = len(A[0])
    n_b = len(B)
    p = len(B[0])
    if n != n_b:
        print("Loi: So cot cua A phai bang so hang cua B")
        return None
    C = [[0 for _ in range(p)] for _ in range(m)]
    mult_count = 0
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += A[i][k] * B[k][j]
                mult_count += 1
            C[i][j] = total
    print(f"Tong so phep nhan da thuc hien: {mult_count}")
    return C


if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    B = [
        [7, 8],
        [9, 1],
        [2, 3]
    ]
    print("C =", matrix_multiply(A, B))
