import re

import requests  # 导入requests包
from bs4 import BeautifulSoup
url = 'http://www.cntour.cn/'
strhtml = requests.get(url)
# soup = BeautifulSoup(strhtml.text, 'lxml')
soup = BeautifulSoup(strhtml.text, 'html5lib')
data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
# print(strhtml.text)
print(data)

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
           'Connection':'Keep-Alive',
           'Host':'wap.gamersky.com',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
url = 'https://wap.gamersky.com/news/'
strhtml = requests.get(url,headers=headers)
print(strhtml.encoding)
print(strhtml.headers)
# print(strhtml.text)
print(requests.utils.get_encodings_from_content(strhtml.text))
strhtml.encoding = "utf-8"
soup = BeautifulSoup(strhtml.text, 'html5lib')
data=soup.select('li>h5')
print(data)
for i in data:
    # print(str(type(i))+' '+str(i))
    group = re.search('(?<=/span>).*(?=</h5>)',str(i))
    group.group(0)
    print(group.group(0))