import matplotlib.pyplot as plt 
from random_wallk import RandomWalk

#只要程序处于活动状态，就不断的模拟随机漫步
while True:
	#创建实例，并绘制点
	rw = RandomWalk()
	rw.fill_walk()
	
	#设置绘图窗口的尺寸
	plt.figure(figsize=(10,6))
	
	point_number= list(range(rw.num_points))
	#折线图
	plt.plot(rw.x,rw.y,linewidth=2)
	#点图
	#plt.scatter(rw.x,rw.y,c=point_number,cmap=plt.cm.Reds,edgecolor = 'none',s=5)
	#突出起点和终点
	plt.scatter(0,0,c='green',edgecolors='none',s= 100)
	plt.scatter(rw.x[-1],rw.y[-1],c='blue',edgecolors= 'none',s=100)
	
	#隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	plt.show()
	
	keep_running = input("yes/no?")
	if keep_running == 'n':
		break
