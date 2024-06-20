import numpy as np
import matplotlib.pyplot as plt

# Define grid parameters
N = 8  # Number of interior grid points in each direction
h = 0.1  # Grid spacing
x = np.linspace(0, 1, N+2)  # Including boundaries
y = np.linspace(0, 1, N+2)  # Including boundaries

# Define the function f(x, y)
def f(x, y):
    return (x**2 + y**2) * np.exp(x) * y

# Initialize the solution matrix u with boundary conditions
u = np.zeros((N+2, N+2))
u[:, 0] = 1  # u(x, 0) = 1
u[:, -1] = np.exp(x)  # u(x, 1) = e^x
u[0, :] = 1  # u(0, y) = 1
u[-1, :] = np.exp(y)  # u(1, y) = e^y

# Define the 9-point stencil coefficients
A = np.zeros((N+2, N+2))
stencil = (1/6) * np.array([[1, 4, 1],
                            [4, -20, 4],
                            [1, 4, 1]])

# Apply the stencil to the interior points of A
for i in range(1, N+1):
    for j in range(1, N+1):
        A[i, j] = np.sum(stencil * u[i-1:i+2, j-1:j+2]) - h**2 * f(x[i], y[j])

# Print and plot the results
print("Approximate solution (u):\n", u)

# Plotting the approximate solution u(x, y)
plt.figure(figsize=(8, 6))
plt.imshow(u, extent=[0, 1, 0, 1], origin='lower', cmap='jet')
plt.colorbar(label='u')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximate Solution u(x, y)')
plt.grid(True)
plt.show()
