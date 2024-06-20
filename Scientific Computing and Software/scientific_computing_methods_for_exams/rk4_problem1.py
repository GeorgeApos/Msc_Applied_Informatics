def f(x, y):
    return -y

def runge_kutta_4th_order(y0, a, b, n):
    h = (b - a) / n
    y_old = y0
    x = a
    for i in range(1, n + 1):
        k1 = h * f(x, y_old)
        k2 = h * f(x + h / 2, y_old + k1 / 2)
        k3 = h * f(x + h / 2, y_old + k2 / 2)
        k4 = h * f(x + h, y_old + k3)
        y = y_old + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

        print(f"Value of y at {x + h:.10f} is: {y:.10f}")

        y_old = y
        x += h

if __name__ == "__main__":
    y0 = 1.0  # Initial condition y(0)
    a = 0.0   # Start of interval
    b = 1.0   # End of interval
    n = 5     # Number of intervals

    runge_kutta_4th_order(y0, a, b, n)

# Explanation:
#
# Initialization:
# y0 is the initial value of yy at t=0t=0.
# a and b define the interval [a,b][a,b].
# n is the number of intervals.
#
# Function f(x, y):
# Defines the function f(x,y)=−yf(x,y)=−y, which represents the derivative of yy.
#
# Runge-Kutta 4th Order Function (runge_kutta_4th_order):
# Implements the 4th-order Runge-Kutta method to solve the ODE y′=−yy′=−y.
# Iterates over n intervals, computing yy at each step using the RK4 method.
# Calculates k1,k2,k3,k1,k2,k3, and k4k4 based on the RK4 formulas.
# Updates yy using the weighted average of these slopes.
#
# Main Execution:
# Initializes y0, a, b, and n.
# Calls runge_kutta_4th_order function with these parameters to compute and print the values of yy at each interval.

