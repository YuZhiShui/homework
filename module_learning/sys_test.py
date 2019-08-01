"""
这是python系统自带的系统库
Python模块sys常用方式示例
sys模块常用方法有：
argv[]：命令行参数List,sys.argv[0]表示是程序本身
exit()：退出程序，正常退出是sys.exit(0)
version()：获取python解释程序的版本信息
path:返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
platform:返回操作系统平台名称
stdout.write():标准输出
stdin.readline()[:-1]:标准输入
sys.stdout  标准输出
sys.stdin  标准输入
sys.stderr  错误输出
getdefaultencoding()：获取解释器默认编码
getfilesystemencoding():获取内存数据存在文件的默认编码
sys.modules  返回系统导入的模块字段，key时模块名，value是模块
"""
import sys


"""
1、argv[]
print(sys.argv[0])
print(sys.argv[:4])
结果展示：
H:\>python3 Pytest.py  2,2,3,4,5
Pytest.py
['Pytest.py', '2,2,3,4,5']

H:\>python3 Pytest.py  2,2,3,4,5 2 3 5
Pytest.py
['Pytest.py', '2,2,3,4,5', '2', '3']

以空格隔开表示一个字符
"""
"""
2、sys.exit()
order=int(input("input number："))
if order == 1:
    sys.exit(0)
else:
    print("不退出，请手动退出程序")
"""

"""
3、sys.stdin
for line in sys.stdin:
    print(line) #每个后面有一个回车

$:cat test.txt | python3 test.py
hello world

1

2

3

4
"""
"""
4、sys.stdout
    1、
sys.stdout的形式就是print的一种默认输出格式，等于print "%VALUE%"
print函数是对sys.stdout的高级封装
print是默认调用了sys.stdout.write()方法将输出打印到控制台
print 也可通过file参数将输出打印到其他文件中
例子：
f = open('test.txt','a') #a表示在末尾追加
print('this is a test',file=f) #将文件内容打印到test.txt
    2、
sys.stdout.write()输出不会自动换行，没有end,可用转义字符自行控制
/n 换行
/r  回车到本行首，可刷新输出
如用sys.stdout.write() 和\r实现自定义进度条
from tqdm import tqdm
import time


for i in tqdm(range(100)):
    time.sleep(.1)
for i in range(100):
    a = (i + 1) / 5
    b = 20 - a
    # sys.stdout.write('\r>>convert image %d/%d'%(i,b))

    sys.stdout.write('\r|%s%s|%d%%' % (a * '▇', b * ' ', i + 1))
    #can't multiply sequence by non-int of type 'float'
    #出错原因在于a,b为float类型，不能与字符相乘
    #sys.stdout.write('\r|%s%s|%d%%' % (int(a) *'▇', int(b) *' ',(i + 1)))
    sys.stdout.flush()
    time.sleep(.1)
    
    3、sys.stdout.flush()强制刷新缓冲区
缓冲区的刷新方式：
    1.flush()刷新缓存区
    2.缓冲区满时，自动刷新
    3.文件关闭或者是程序结束自动刷新
当我们需要打印一些字符时，并不是立刻就打印，而是先将需要打印的字符
放入缓冲区，在缓冲区刷新时打印，当缓冲区未满，或者程序运行未结束时，
可使用sys.stdout.flush()强制刷新缓冲区，立刻进行打印；
附：写出漂亮的进度条模块tqdm
from tqdm import tqdm 
import time
for i in tqdm(range(10000)):  
    time.sleep(0.01) 
"""


