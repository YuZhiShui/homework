import asyncio

@asyncio.coroutine
def task():
    print('before...task....')
    yield from asyncio.sleep(5) #发送http请求，获取结果（不支持HTTP）
    print('end....task....')    #支持TCP

#单线程
"""都是固定用法
tasks=[task(),task()]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
"""



