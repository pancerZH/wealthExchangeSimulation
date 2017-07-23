import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def init():
    plt.subplot(211).set_ylim(0, initMoney*3.5)
    plt.subplot(211).set_xlim(0, person+1)
    return


def initRanked():
    plt.subplot(212).set_ylim(0, initMoney*3.5)
    plt.subplot(212).set_xlim(0, person+1)
    return


def update(_data):
    for i in range(len(_data)):
        lines[i].set_ydata([0, _data[i]])

    return lines


def updateRanked(_data):
    ranked_data = sorted(_data)
    for i in range(len(ranked_data)):
        linesRanked[i].set_ydata([0, ranked_data[i]])

    return linesRanked


def data_gen():
    for i in range(times):
        timesText.set_text('times: %d' % (i+1))
        for j in range(person):
            if moneyData[j] >= exchange:
                moneyData[j] -= exchange

                chosen_person = np.random.randint(0, person)
                while chosen_person == j:
                    chosen_person = np.random.randint(0, person)

                moneyData[chosen_person] += exchange

        if (i+1) % stepLength == 0:
            yield moneyData

initMoney, person, times, exchange = 100, 100, 10000, 1
# 100人，100元，10000次交换，每次交换1元
stepLength = 100  # 图表更新的间隔迭代次数
moneyData = np.ones(person)*initMoney

color = '#9999ff'
colorRanked = '#99ff99'

fig = plt.figure()

xdata = [[i+1 for i in range(person)], [i+1 for i in range(person)]]
ydata = [[0 for i in range(person)], moneyData]
plt.subplot(211)
lines = plt.plot(xdata, ydata, lw=2, c=color)
plt.xlabel('person')
plt.ylabel('money')
timesText = plt.text(-10, 380, 'times: 0')  # 左上角显示交换次数
plt.subplot(212)
linesRanked = plt.plot(xdata, ydata, lw=2, c=colorRanked)
plt.xlabel('person')
plt.ylabel('money')

ani1 = animation.FuncAnimation(fig, update, data_gen, interval=0.1, repeat=False, init_func=init)
ani2 = animation.FuncAnimation(fig, updateRanked, data_gen, interval=0.1, repeat=False, init_func=initRanked)

plt.show()
