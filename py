
常见语法
循环：for x in x    
for x in range(10): #range(10) 1-10的队列
  print(x)

n=100;
while n<0:
  sum+=n-2


list 列表
list可以不同数据类型 	 L = ['Apple', 123, True]
二维数组 	 s = ['python', 'java', ['asp', 'php'], 'scheme']
创建：	classmates = ['Michael', 'Bob', 'Tracy']
查询：	classmates[1] ==》 'Bob'        classmates[-2]==》 'Bob'
classmates.append('aaa')     最后加一个
classmates.insert(1, 'Jack')     第1位加一个
classmates.pop(x)     删除第x个，没有默认删最后一个
classmates[1] = 'Sarah'    第一个替换成Sarah

tuple 元组	
tuple和list非常类似，但是tuple一旦初始化就不能修改
创建 ： classmates = ('Michael', 'Bob', 'Tracy')
查询还是  classmates[1]
创建只有一个数字的元组 t=(1) 会变成 t=1 ，因此需要t=(1,r)
可变的话便是  t = ('a', 'b', ['A', 'B'])   元组嵌套list

dict字典
