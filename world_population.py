import json
from country_codes import get_country_code
import pygal 
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

#将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)
	
#打印每个国家2010年的人口数量#创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country_name)
		if code:
			cc_populations[code] = population
			
#根据人口数量将所有国家分成三部分
daguo,zhongguo,xiaoguo ={},{},{}
for cc, pop in cc_populations.items():
	if pop<10000000:
		xiaoguo[cc] = pop 
	elif pop <1000000000:
		zhongguo[cc] = pop
	else:
		daguo[cc] = pop
		
print (len(daguo),len(zhongguo),len(xiaoguo))

wm_style = RS('#336699',base_style =LCS)			
wm = pygal.maps.world.World(style=wm_style)
wm.title = '2010世界人口'
wm.add('大国',daguo)
wm.add('中等',zhongguo)
wm.add('小国',xiaoguo)
wm.render_to_file('world_population_sandeng.svg')
		

