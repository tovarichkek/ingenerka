import numpy as np
import matplotlib.pyplot as plt

with open("data.txt", "r") as f:
    lines = f.readlines()
x_data = []
y_data = []
for i in range(len(lines)):
    y = float(lines[i])
    x_data.append(0.0264 * i)
    y_data.append(y * 3.3 / 255)

fig, ax = plt.subplots()
x = np.linspace(0.99 * min(x_data), 1.01 * max(x_data), 100)
ax.set_title("RC зарядка/разрядка")
ax.plot(x_data, y_data, '', label="U(t)")
plt.text(0.57 * max(x_data), 0.78*max(y_data), "Время заряда:  6.02с")
plt.text(0.57 * max(x_data), 0.71*max(y_data), "Время разряда: 1.63с")
plt.grid(True)
plt.xlabel('Время, с')
plt.ylabel(r'Напряжение, В')
plt.legend() 

plt.savefig("plt.png")

plt.show()