# wealthExchangeSimulation
封闭系统中定量财富随机流动的简单模拟器

## 背景介绍

条件来自于知乎上的一个[提问](https://www.zhihu.com/question/62250384)，复述如下

> 房间内有 100 人，每人有 100 块，每次迭代给另一个人 1 块，最后这个房间内的财富分布怎样？

在这里我们进行迭代10000次

*本项目所有代码均在Python3.6.0下测试通过*

## 使用的模块

- matplotlib(2.0.0)
- numpy(1.11.3)

## 各部分说明

- #### 迭代函数主体   

      def data_gen():
          for i in range(times):
              for j in range(person):
                  if moneyData[j] > 0:
                      moneyData[j] -= 1
                      chosen_person = np.random.randint(0, person)
                      moneyData[chosen_person] += 1

              yield moneyData
              
 - #### 图表
 
 	- 一张图表上有两个子图(原始数据与排序数据) 
 
			plt.subplot(211)    
			lines = plt.plot(xdata, ydata, lw=2, c=color)
			plt.subplot(212)
			linesRanked = plt.plot(xdata, ydata, lw=2, c=colorRanked)
			
	- 图表左上角显示迭代次数
		
			timesText = plt.text(-10, 340, 'times: 0')
				
	- 播放动画
		
			ani1 = animation.FuncAnimation(fig, update, data_gen, interval=0.1, repeat=False, init_func=init)
			ani2 = animation.FuncAnimation(fig, updateRanked, data_gen, interval=0.1, repeat=False, init_func=initRanked)

## 成果展示

- 开始时

	![image](https://github.com/pancerZH/wealthExchangeSimulation/blob/master/image/start.png)
	
- 结束时

	![image](https://github.com/pancerZH/wealthExchangeSimulation/blob/master/image/end.png)
	
仅从这一次模拟情况来看，在财富流动结束(迭代10000次)时，有1人不幸破产(资产为0)，有5人资产达到300元以上(成为大富翁)。  
这可是完全随机的模拟，得到这样的结果真是令人惊讶。
