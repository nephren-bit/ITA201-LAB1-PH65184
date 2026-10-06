def matrix_vector_multiply(W, x):
    m = len(W)
    n = len(W[0])
    if n != len(x):
        print("Loi: So cot cua W phai bang so phan tu cua x")
        return None
    y = [0 for _ in range(m)]
    for i in range(m):
        total = 0
        for j in range(n):
            total += W[i][j] * x[j]
        y[i] = total
    return y


if __name__ == "__main__":
    W = [
        [0.2, 0.5, -0.1],
        [0.8, -0.3, 0.4]
    ]
    x = [10, 2, 5]
    print("y =", matrix_vector_multiply(W, x))
