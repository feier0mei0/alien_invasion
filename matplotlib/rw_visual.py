# -- coding: utf-8 --

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活跃状态，就不断模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rm = RandomWalk()
    rm.fill_walk()
    plt.scatter(rm.x_values, rm.y_values, s=15)
    plt.show()

    keep_running = raw_input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break
