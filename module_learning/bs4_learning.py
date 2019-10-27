from bs4 import BeautifulSoup
from bs4 import  Tag
html_doc="""
<html><head><title>THE Dormouse's story</title></head>
<body>
    <a herf='http://www.cunzhang.com'>波多老师</a>
    <a id='li'>刘志超</a>
    <div>
        <p>asdf</p>
     </div>  
     <p>yuzhishui</p> 
</body>
</html>
"""

soup = BeautifulSoup(html_doc,features="lxml") #features="html.parser"
#features可以选择为lxml，性能更好

#1、属性操作 （标签基本都是tag对象）
# print(soup) #返回的结果就是上面文本信息
# tag = soup.find_all('a')  #soup.find,找到a标签
# # tag=soup.find('div',id='li')
# print(tag)
# print(type(tag))  #<class 'bs4.element.ResultSet'>  返回的是结果集，数据集合的格式
# print(tag[0])

#print(type(tag.attrs)) #tag.attrs是指标签的属性,字典类型
# tag.attrs['lovers']="物理老师" #增加属性对象和值
# del tag.attrs['herf']  #删除原来的属性
# print(soup)

#2、
#children:儿子
#标签和内容类型不一样
# tags=soup.find('body').children
# print(tags) #<list_iterator object at 0x000001BA6F6D5208>
# print(type(tags))
# # #print(len(list(tags))) #<list_iterator object at 0x000001B912A78828>迭代对象
# print(type(Tag))
# for tag in tags:
#     if type(tag)==Tag:  #判断是否为标签类型
#         print(tag)
#     # else:
#     print('') #打印出来的是空行
#     print('',end='')#防止含有多个空格，并换行打印连续的数据
    #print(type(tag))   #<class 'bs4.element.Tag'>,
    # <class 'bs4.element.NavigableString'>有些为可导航字符串，网页代码中的换行可以看作导航字符串

#3、找标签，再找内容，所有子子孙孙标签（descendants）
# tags=soup.find('body').descendants
# print(list(tags))

#4、clear,将标签的所有子标签全部清空（保留标签名）
# tags=soup.find("body")
# print(tags)
# tags.clear()
# print(soup)
#5、decompose 递归删除所有标签
#6、extract 递归的删除所有的标签，并获取删除的标签


#7、encode、decode
# tags=soup.find("body")
# #把对象转换成字节类型
# print(tags.encode())
# #把对象转换成字符串类型
# print(tags.decode())

#8、find用法：获取匹配的第一标签
#find中有name属性、attrs、text
# tags=soup.find("body").find('p',recursive=False)
#加上recursive=False会递归找到子p标签，不是第一个p标签了,递归：调用自己本身的程序，它返回的应该是第二个p标签
# print(tags)

#9、find_all,参数与find参数相同，会找到全部匹配的标签
#还支持正则表达式
# tags = soup.find_all('a')
# print(tags)

# tags = soup.find_all('a',limit=1)
# print(tags)

# tags = soup.find_all(name='a', attrs={'class': 'sister'}, recursive=True, text='Lacie')
# # tags = soup.find(name='a', class_='sister', recursive=True, text='Lacie')
# print(tags)


# ####### 列表 #######
# v = soup.find_all(name=['a','div'])  #就是找a和div标签
# print(v)

# v = soup.find_all(class_=['sister0', 'sister'])
# print(v)

# v = soup.find_all(text=['Tillie'])
# print(v, type(v[0]))


# v = soup.find_all(id=['link1','link2'])
# print(v)

# v = soup.find_all(href=['link1','link2'])
# print(v)

# ####### 正则 #######
import re
# rep = re.compile('p')  #re.compile用途
# rep = re.compile('^p')
# v = soup.find_all(name=rep)
# print(v)

# rep = re.compile('sister.*')
# v = soup.find_all(class_=rep)
# print(v)

# rep = re.compile('http://www.oldboy.com/static/.*')
# print(rep) #re.compile('http://www.oldboy.com/static/.*')
# v = soup.find_all(href=rep)
# print(v)

# ####### 方法筛选 #######
# def func(tag):
# return tag.has_attr('class') and tag.has_attr('id')
# v = soup.find_all(name=func)
# print(v)


# ## get,获取标签属性
# tag = soup.find('a')
# v = tag.get('id')
# print(v)

#10、has_attr,检查标签是否具有该属性
# tags=soup.find('a')
# v=tags.has_attr('id')
# print(v)

#11、get_text,获取标签内部文本内容
# tags=soup.find('a')
# v=tags.get_text()
# print(v)

#12、index检查标签在某标签中的索引位置
# tags=soup.find('body')
# v=tags.index(tags.find('div'))
# print(v)

#13、select方法
#14、append方法，在当前标签内部追加一个标签
#15、insert方法，在当前标签内部指定位置插入一个标签
#16、去掉当前标签，将保留其包裹的标签，去掉第一个匹配的标签
# tag = soup.find('a')
# v = tag.unwrap()
# print(soup)
#17、wrap，将指定标签把当前标签包裹起来
# from bs4.element import Tag
# obj1 = Tag(name='div', attrs={'id': 'it'})
# obj1.string = '我是一个新来的'
#
# tag = soup.find('a')
# v = tag.wrap(obj1)
# print(soup)

# tag = soup.find('a')
# v = tag.wrap(soup.find('p'))
# print(soup)