import numpy as np
import random
import matplotlib.pyplot as plt

def set_random_seed(seed):
    np.random.seed(seed)
    random.seed(seed)

def generate_dataset(N, x_min, x_max):
    X = np.random.uniform(x_min, x_max, N)
    # defining all the functions
    funcs = [
        ('sin', np.sin),
        ('cos', np.cos),
        ('tan', np.tan),
        ('log', lambda x: np.log(np.clip(x, 1e-6, None))),
        ('square', np.square),
        ('cube', lambda x: np.power(x, 3))
    ]
    # randomly choosing functions and coefficients
    f1_name, f1 = random.choice(funcs)
    f2_name, f2 = random.choice(funcs)
    f3_name, f3 = random.choice(funcs)
    A, B = random.uniform(0.5, 2), random.uniform(0.5, 2)
    C, D = random.uniform(0.5, 2), random.uniform(0.5, 2)
    E, F = random.uniform(0.5, 2), random.uniform(0.5, 2)
    Y = A * f1(B * X) + C * f2(D * X) + E * f3(F * X)
    func_str = f"Y = {A:.2f}*{f1_name}({B:.2f}*X) + {C:.2f}*{f2_name}({D:.2f}*X) + {E:.2f}*{f3_name}({F:.2f}*X)"
    return X, Y, func_str

# scatter plot
def plot_scatter(X, Y):
    plt.figure(figsize=(7,5))
    plt.scatter(X, Y, alpha=0.7, label='Data points')
    plt.title('Scatter Plot of X vs Y')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

#histgram
def plot_histogram(X):
    plt.figure(figsize=(7,5))
    bins = int(np.sqrt(len(X)))
    plt.hist(X, bins=bins, color='skyblue', edgecolor='black')
    plt.title('Histogram of X')
    plt.xlabel('X')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# box plot
def plot_box(Y):
    plt.figure(figsize=(5,5))
    plt.boxplot(Y, vert=True, patch_artist=True)
    plt.title('Box Plot of Y')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

# line plot
def plot_line(X, Y):
    idx = np.argsort(X)
    X_sorted = X[idx]
    Y_sorted = Y[idx]
    plt.figure(figsize=(7,5))
    plt.plot(X_sorted, Y_sorted, color='orange', label='Sorted X vs Y')
    plt.title('Line Plot of Sorted X vs Y')
    plt.xlabel('Sorted X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    seed = int(input("Enter random seed (integer): "))
    set_random_seed(seed)
    N = int(input("Enter number of data points (N): "))
    x_min = float(input("Enter minimum value for X: "))
    x_max = float(input("Enter maximum value for X: "))
    X, Y, func_str = generate_dataset(N, x_min, x_max)
    print("Generated function:", func_str)
    plot_scatter(X, Y)
    plot_histogram(X)
    plot_box(Y)
    plot_line(X, Y)
