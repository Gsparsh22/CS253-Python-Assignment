import numpy as np

def solve_linear_system(A, B, tol=1e-12):
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    n, m = A.shape

    if n != m:
        raise ValueError("Matrix A must be square.")

    rankA = np.linalg.matrix_rank(A, tol)
    aug  = np.column_stack((A, B))
    rankAug = np.linalg.matrix_rank(aug, tol)

    if rankA < rankAug:
        # inconsistent
        raise ValueError("No solution exists (system is inconsistent).")
    elif rankA < n:
        # infinitely many solutions
        # return one least‐squares solution as a “particular” solution
        X_particular, *_ = np.linalg.lstsq(A, B, rcond=None)
        print("Warning: infinitely many solutions exist.")
        return X_particular
    else:
        # unique solution
        return np.linalg.solve(A, B)

if __name__ == "__main__":
    n = int(input("Enter the size of matrix (if NxN, then enter N): "))
    A = []
    print("Enter the coefficients matrix A (each row separated by space):")
    for i in range(n):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != n:
            raise ValueError(f"Each row must have exactly {n} elements.")
        A.append(row)

    print("Enter the constants vector B (separated by space):")
    B = list(map(float, input().split()))
    if len(B) != n:
        raise ValueError(f"Constants vector must have exactly {n} elements.")

    try:
        X = solve_linear_system(A, B)
        print("Solution X:", X)
    except ValueError as e:
        print("Error:", e)
