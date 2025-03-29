from matplotlib import pyplot as plt, animation
import numpy as np
import math

# 定义域[-sqrt(10), sqrt(10)]
# 缩放比率
scale = 4
# 控制波长
k = 5
x = np.linspace(-np.sqrt(10)*scale, np.sqrt(10)*scale, 10000)
def f(x, scale, k):
    return scale * (abs(1/scale*x)**(2/3) + (10 - (1/scale*x)**2)**0.5*np.sin(1/scale*k*math.pi*x))

plt.plot(x, f(x, scale, k), label = 'wave heart',color = 'red')
# 刻度等距
plt.axis('scaled')
# 刻度尺
plt.xticks(range(-20, 21, 2))
plt.yticks(range(-20, 21, 2))
plt.legend()
# plt.axis('off')
plt.title("Wave Heart")
plt.show()