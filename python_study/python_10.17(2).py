# # #python json
# import json

# # data = [{'name':'zhangdashan','age':'11'},{'name':'wangdachui','age':'13'},{'name':'zhaoxiohu','age':'16'}]
# # #列表
# # json_str = json.dumps(data) #数据转化成json字符串
# # print(type(json_str))
# # print(json_str)
# # #字典
# # d = {'name':'zhoujielun','add':'taibei'}
# # json_str = json.dumps(d)
# # print(type(json_str))
# # print(json_str)

# s ='[{"name": "zhangdashan", "age": "11"}, {"name": "wangdachui", "age": "13"}, {"name": "zhaoxiohu", "age": "16"}]'
# l = json.loads(s)
# print(type(l))
# print(l)

from pyecharts.charts import Line

line = Line()

line.add_xaxis(['china','USA','japan'])
line.add_yaxis('GDP',[30,20,10])
line.render

