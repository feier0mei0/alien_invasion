# -- coding: utf-8 --

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个RandomWalk实例，并将其包含的点都绘制出来
rm = RandomWalk()
rm.fill_walk()
plt.scatter(rm.x_values, rm.y_values, s=15)
plt.show()
