def solve_quadratic(a, b, c):
    disc = pow(b, 2) - 4 * a * c
    x1 = (-b + pow(disc, 1/2)) / 2
    x2 = (-b - pow(disc, 1/2)) / 2
    
    return x1, x2

roots = solve_quadratic(1, 6, 9)
if __name__ == "__main__":
    print(roots)
    print(f"The roots are {roots[0]} and {roots[1]}")