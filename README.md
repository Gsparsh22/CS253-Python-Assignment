# CS253-Python-Assignment
## Table of Contents

- [1. Introduction to Python Programming](#1-introduction-to-python-programming)
    - [1.1 Smart Text-Processing Tool](#11-smart-text-processing-tool)
    - [1.2 Rock-Paper-Scissors](#12-rock-paper-scissors)
- [2. Tony’s Research and Computational Challenges](#2-tonys-research-and-computational-challenges)
    - [2.1 Summing Prime Numbers for a Cryptographic Algorithm](#21-summing-prime-numbers-for-a-cryptographic-algorithm)
    - [2.2 Analyzing Temperature Fluctuations](#22-analyzing-temperature-fluctuations)
    - [2.3 Solving a System of Linear Equations in Physics](#23-solving-a-system-of-linear-equations-in-physics)
- [3. Shivam’s Data Science Experiment](#3-shivams-data-science-experiment)

---

## 1. Introduction to Python Programming

### 1.1 Smart Text-Processing Tool

A Python tool to help writers process text based on a registration number. Features include:

- **Even registration**: Reverses the string.
- **Odd registration**: Converts vowels to uppercase, consonants to lowercase.
- **Substring extraction**: Uses the count of 1s in the binary form of the registration number to determine substring length.
- **Ordering**: Substrings are sorted lexicographically or in reverse, based on a bitwise condition.

**Functions:**
- `validate_input(n, s)`
- `process_string(n, s)`
- `count_set_bits(n)`
- `extract_substrings(s, k)`
- `sort_or_reverse(n, s, substrings)`
- `main()`

**Example:**

```
Input: n = 10, s = "bharat"
Output: hb ah ra ar ta

Input: n = 7, s = "kavita"
Output: ItA vIt AvI kAv
```

---

### 1.2 Rock-Paper-Scissors

A Python program simulating Rock-Paper-Scissors between a user and the computer.

- User input is case-insensitive.
- Handles invalid inputs.
- Displays choices and running score.
- Allows multiple rounds until the user quits.

---

## 2. Tony’s Research and Computational Challenges

### 2.1 Summing Prime Numbers for a Cryptographic Algorithm

Efficiently computes the sum of the first `n` prime numbers using the Sieve of Eratosthenes.

**Function:**  
- `sum_of_primes(n)`

---

### 2.2 Analyzing Temperature Fluctuations

Analyzes a list of temperature readings to compute:

- Mean
- Median
- Standard deviation
- Sample variance (with Bessel’s correction)

Handles edge cases for empty or single-value datasets.

**Function:**  
- `analyze_temperatures(temperatures)`

---

### 2.3 Solving a System of Linear Equations in Physics

Solves `AX = B` for `X` using NumPy, with error handling for singular matrices.

**Function:**  
- `solve_linear_system(A, B)`

---

## 3. Shivam’s Data Science Experiment

Generates and visualizes synthetic environmental datasets.

- Generates `N` random points for variables `X` and `Y` using random mathematical functions.
- Visualizations: scatter plot, histogram, box plot, and line plot.
- Customizable number of points and range for `X`.
- Ensures reproducibility with a random seed.

**Functions:**
- `generate_dataset(N, x_min, x_max)`
- `plot_scatter(X, Y)`
- `plot_histogram(X)`
- `plot_box(Y)`
- `plot_line(X, Y)`
- `set_random_seed(seed)`

---

**Note:**  
Each section is implemented as a separate Python module or function, with input validation and error handling as required.

---

*For academic use in CS253 or similar courses. Contributions and suggestions are welcome!*