import numpy as np
import matplotlib.pyplot as plt

# Ορισμός της αναλυτικής λύσης
def analytic_solution(x):
    return x + np.exp(-x)

# Υλοποίηση της μεθόδου Euler για την επίλυση της διαφορικής εξίσωσης
def euler_method(f, x0, y0, h, n):
    x = np.zeros(n+1)
    y = np.zeros(n+1)

    x[0] = x0
    y[0] = y0

    for i in range(n):
        y[i+1] = y[i] + h * f(x[i], y[i])
        x[i+1] = x[i] + h

    return x, y

# Η συνάρτηση που περιγράφει τη διαφορική εξίσωση y' = -y + x + 1
def f(x, y):
    return -y + x + 1

# Παράμετροι για την επίλυση
x0 = 0   # Αρχικό x
y0 = 1   # Αρχική τιμή της y(x0)
h = 0.1  # Μέγεθος βήματος
n = 10   # Αριθμός βημάτων

# Επίλυση της διαφορικής εξίσωσης με τη μέθοδο Euler
x_euler, y_euler = euler_method(f, x0, y0, h, n)

# Υπολογισμός της αναλυτικής λύσης για τα ίδια σημεία x
y_analytic = analytic_solution(x_euler)

# Υπολογισμός του σφάλματος
error = np.abs(y_euler - y_analytic)

# Εκτύπωση των αποτελεσμάτων
print(f"Approximate solution (Euler method):\n{x_euler}\n{y_euler}")
print(f"Analytical solution:\n{x_euler}\n{y_analytic}")
print(f"Error:\n{error}")

# Σχεδιασμός γραφικής παράστασης
plt.figure(figsize=(10, 6))
plt.plot(x_euler, y_euler, marker='o', linestyle='-', color='b', label='Approximate solution (Euler)')
plt.plot(x_euler, y_analytic, linestyle='-', color='r', label='Analytical solution')
plt.title('Comparison of Euler Method and Analytical Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
