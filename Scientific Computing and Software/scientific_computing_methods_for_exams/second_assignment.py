import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Ορισμός παραμέτρων
G = 39.47841760435743
m_A = 1.1
m_B = 0.907
h = 0.01  # βήμα
years = 100
num_steps = int(years / h)

# Αρχικές τιμές
x_A, y_A, z_A = 0, 11.29, 0
v_xA, v_yA, v_zA = 0.1, 0, 0.295
x_B, y_B, z_B = 0, -11.29, 0
v_xB, v_yB, v_zB = -0.061, 0, -0.362

# Αρχικοποίηση πίνακα για αποθήκευση των αποτελεσμάτων
positions = np.zeros((num_steps, 12))


def acceleration(xA, yA, zA, xB, yB, zB, m):
  r = np.sqrt((xA - xB) ** 2 + (yA - yB) ** 2 + (zA - zB) ** 2)
  a_x = -G * m * (xA - xB) / r ** 3
  a_y = -G * m * (yA - yB) / r ** 3
  a_z = -G * m * (zA - zB) / r ** 3
  return a_x, a_y, a_z


for step in range(num_steps):
  # Αποθήκευση θέσεων και ταχυτήτων
  positions[step] = [x_A, y_A, z_A, v_xA, v_yA, v_zA, x_B, y_B, z_B, v_xB, v_yB, v_zB]

  # Υπολογισμός των κλιμακωτών συντελεστών k1, k2, k3, k4
  k1 = np.zeros(12)
  k2 = np.zeros(12)
  k3 = np.zeros(12)
  k4 = np.zeros(12)

  # k1
  k1[0:3] = [v_xA, v_yA, v_zA]
  k1[3:6] = acceleration(x_A, y_A, z_A, x_B, y_B, z_B, m_B)
  k1[6:9] = [v_xB, v_yB, v_zB]
  k1[9:12] = acceleration(x_B, y_B, z_B, x_A, y_A, z_A, m_A)

  # k2
  xA_half = x_A + 0.5 * h * k1[0]
  yA_half = y_A + 0.5 * h * k1[1]
  zA_half = z_A + 0.5 * h * k1[2]
  v_xA_half = v_xA + 0.5 * h * k1[3]
  v_yA_half = v_yA + 0.5 * h * k1[4]
  v_zA_half = v_zA + 0.5 * h * k1[5]
  xB_half = x_B + 0.5 * h * k1[6]
  yB_half = y_B + 0.5 * h * k1[7]
  zB_half = z_B + 0.5 * h * k1[8]
  v_xB_half = v_xB + 0.5 * h * k1[9]
  v_yB_half = v_yB + 0.5 * h * k1[10]
  v_zB_half = v_zB + 0.5 * h * k1[11]

  k2[0:3] = [v_xA_half, v_yA_half, v_zA_half]
  k2[3:6] = acceleration(xA_half, yA_half, zA_half, xB_half, yB_half, zB_half, m_B)
  k2[6:9] = [v_xB_half, v_yB_half, v_zB_half]
  k2[9:12] = acceleration(xB_half, yB_half, zB_half, xA_half, yA_half, zA_half, m_A)

  # k3
  xA_half = x_A + 0.5 * h * k2[0]
  yA_half = y_A + 0.5 * h * k2[1]
  zA_half = z_A + 0.5 * h * k2[2]
  v_xA_half = v_xA + 0.5 * h * k2[3]
  v_yA_half = v_yA + 0.5 * h * k2[4]
  v_zA_half = v_zA + 0.5 * h * k2[5]
  xB_half = x_B + 0.5 * h * k2[6]
  yB_half = y_B + 0.5 * h * k2[7]
  zB_half = z_B + 0.5 * h * k2[8]
  v_xB_half = v_xB + 0.5 * h * k2[9]
  v_yB_half = v_yB + 0.5 * h * k2[10]
  v_zB_half = v_zB + 0.5 * h * k2[11]

  k3[0:3] = [v_xA_half, v_yA_half, v_zA_half]
  k3[3:6] = acceleration(xA_half, yA_half, zA_half, xB_half, yB_half, zB_half, m_B)
  k3[6:9] = [v_xB_half, v_yB_half, v_zB_half]
  k3[9:12] = acceleration(xB_half, yB_half, zB_half, xA_half, yA_half, zA_half, m_A)

  # k4
  xA_full = x_A + h * k3[0]
  yA_full = y_A + h * k3[1]
  zA_full = z_A + h * k3[2]
  v_xA_full = v_xA + h * k3[3]
  v_yA_full = v_yA + h * k3[4]
  v_zA_full = v_zA + h * k3[5]
  xB_full = x_B + h * k3[6]
  yB_full = y_B + h * k3[7]
  zB_full = z_B + h * k3[8]
  v_xB_full = v_xB + h * k3[9]
  v_yB_full = v_yB + h * k3[10]
  v_zB_full = v_zB + h * k3[11]

  k4[0:3] = [v_xA_full, v_yA_full, v_zA_full]
  k4[3:6] = acceleration(xA_full, yA_full, zA_full, xB_full, yB_full, zB_full, m_B)
  k4[6:9] = [v_xB_full, v_yB_full, v_zB_full]
  k4[9:12] = acceleration(xB_full, yB_full, zB_full, xA_full, yA_full, zA_full, m_A)

  # Υπολογισμός επόμενων τιμών
  x_A += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
  y_A += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
  z_A += h / 6 * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2])
  v_xA += h / 6 * (k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3])
  v_yA += h / 6 * (k1[4] + 2 * k2[4] + 2 * k3[4] + k4[4])
  v_zA += h / 6 * (k1[5] + 2 * k2[5] + 2 * k3[5] + k4[5])
  x_B += h / 6 * (k1[6] + 2 * k2[6] + 2 * k3[6] + k4[6])
  y_B += h / 6 * (k1[7] + 2 * k2[7] + 2 * k3[7] + k4[7])
  z_B += h / 6 * (k1[8] + 2 * k2[8] + 2 * k3[8] + k4[8])
  v_xB += h / 6 * (k1[9] + 2 * k2[9] + 2 * k3[9] + k4[9])
  v_yB += h / 6 * (k1[10] + 2 * k2[10] + 2 * k3[10] + k4[10])
  v_zB += h / 6 * (k1[11] + 2 * k2[11] + 2 * k3[11] + k4[11])

# Ολοκλήρωση και επιστροφή αποτελεσμάτων
positions_final = positions

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(positions_final[:, 0], positions_final[:, 1], positions_final[:, 2], label='Body A')
ax.plot(positions_final[:, 6], positions_final[:, 7], positions_final[:, 8], label='Body B')

ax.set_xlabel('X [AU]')
ax.set_ylabel('Y [AU]')
ax.set_zlabel('Z [AU]')
ax.legend()
plt.show()
