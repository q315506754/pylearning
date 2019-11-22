import asyncio
import os
import sys

from pyppeteer import launch

print(sys.argv)
print(sys.path)
win_path = sys.argv[0].replace('/', '\\')
win_cmd = "explorer.exe \"" + win_path + "\""
print(win_cmd)
print(os.getcwd())
os.system(win_cmd)


# exit()


def screen_size():
    """使用tkinter获取屏幕大小"""
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height


headers = {'Pragma': 'no-cache'}


async def main():
    print("1111")
    browser = await launch()
    print("222")
    page = await browser.newPage()
    print("333")
    # await page.goto('http://example.com')
    # 设置页面视图大小
    width, height = screen_size()

    # await page.setViewport(viewport={'width': 1280, 'height': 800})
    await page.setViewport(viewport={'width': width, 'height': height})

    # 是否启用JS，enabled设为False，则无渲染效果
    await page.setJavaScriptEnabled(enabled=True)

    await page.setExtraHTTPHeaders(headers)

    res = await page.goto('https://www.baidu.com/')
    resp_headers = res.headers  # 响应头
    resp_status = res.status  # 响应状态

    print(resp_status, resp_headers)

    """  打印页面文本 """
    # 获取所有 html 内容
    # print(await page.content())

    # 第二种方法，在while循环里强行查询某元素进行等待
    # while not await page.querySelector('.bdbriimgtitle'):
    #     pass

    await page.hover(".bri")

    print("444")

    file_name = 'example.png'
    await page.screenshot({'path': file_name})

    # 打印页面cookies
    print(await page.cookies())

    # 在网页上执行js 脚本
    dimensions = await page.evaluate(pageFunction='''() => {
            return {
                width: document.documentElement.clientWidth,  // 页面宽度
                height: document.documentElement.clientHeight,  // 页面高度
                deviceScaleFactor: window.devicePixelRatio,  // 像素比 1.0000000149011612
            }
        }''', force_expr=False)  # force_expr=False  执行的是函数
    print(dimensions)

    print("555")
    await browser.close()
    print("666")

    win_cmd = "explorer.exe \"" + os.getcwd() + "\\" + file_name + "\""
    print(win_cmd)

    os.system(win_cmd)


print("before")

asyncio.run(main())

print("after")
