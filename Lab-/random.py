import matplotlib.pyplot as plt
import random

x = [0]
y = [0]

for _ in range(100):
    direction = random.choice(['up', 'down', 'left', 'right'])
    if direction == 'up':
        x.append(x[-1])
        y.append(y[-1] + 1)
    elif direction == 'down':
        x.append(x[-1])
        y.append(y[-1] - 1)
    elif direction == 'left':
        x.append(x[-1] - 1)
        y.append(y[-1])
    elif direction == 'right':
        x.append(x[-1] + 1)
        y.append(y[-1])

plt.plot(x, y, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Random Movement')
plt.show()
