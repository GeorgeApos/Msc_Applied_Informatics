def euler_method(y0, h, n):
    y_old = y0
    for i in range(1, n + 1):
        y = y_old + h * (-y_old)
        print(f"{i}-th point value is: {y:.10f}")
        y_old = y


if __name__ == "__main__":
    y0 = 1.0  # Initial condition y(0)
    n = 5  # Number of intervals
    h = 1.0 / n  # Step size

    euler_method(y0, h, n)

# Explanation:
#
# Initialization:
# y0 is the initial value of yy at t=0t=0.
# n is the number of intervals.
# h is the step size, computed as 1nn1​.
#
# Euler Method Function (euler_method):
# Implements the Euler method to solve the ODE y′=−yy′=−y.
# Iterates over n intervals, computing yy at each step using the formula yi+1=yi+h⋅(−yi)yi+1​=yi​+h⋅(−yi​).
#
# Main Execution:
# Initializes y0, n, and computes h.
# Calls euler_method function with these parameters to compute and print the values of yy at each interval.
