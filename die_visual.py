from die import Die
import pygal

#创建D6
die_1 = Die()
die_2 = Die()

#掷几次骰子，将结果储存至列表
results = []
for  roll_num in range(1000):
	result = die_1.roll()+die_2.roll()
	results.append(result)
	
#分析结果
frequencies = [ ]
max_result = die_1.mianshu+die_2.mianshu
for value in range(2,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
	
#对结果可视化
hist=pygal.Bar()
hist.x_labels =['1','2','3','4','5','6']
hist.title = 'roll D6'
hist.x_title = 'dianshu'
hist.y_titel ='cishu'

hist.add ('d6+d6',frequencies)
hist.render_to_file('die_visuals.vsg')







 

