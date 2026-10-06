def norm_l1(v):
    total = 0
    for x in v:
        total += abs(x)
    return total


def norm_l2(v):
    sum_sq = 0
    for x in v:
        sum_sq += x ** 2
    return sum_sq ** 0.5


if __name__ == "__main__":
    error_vector = [3, -4]
    print(f"L1 Norm: {norm_l1(error_vector)}")
    print(f"L2 Norm: {norm_l2(error_vector)}")
