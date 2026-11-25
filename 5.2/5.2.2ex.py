def f(L): # Assume L is a list of integers.
    n = len(L)
    LSum = sum(L)
    M = [LSum]
    CurrentValue = LSum
    for i in range(0, n-1):
        CurrentValue -= L[i]
        M.append(CurrentValue)
    return M

print(f([-1, 2, 0, 1]))