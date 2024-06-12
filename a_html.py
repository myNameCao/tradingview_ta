import requests

from bs4 import BeautifulSoup

import re



L=[]
def geta_html(page):

    html=requests.get('https://www.binance.com/zh-CN/markets/overview?p={}'.format(page))


    # 打印处理后的HTML

    soup = BeautifulSoup(html.text, 'html.parser')

    # 移除所有<script>标签及其内容
    for script_tag in soup.find_all(name=['script','style']):
        script_tag.extract()

    
# #  取出 所有的属性
#     whitelist= ['style']
#     for tag in soup.findAll(True):
#         for attr in [attr for attr in tag.attrs if attr in whitelist]:
#             del tag[attr]

    html=soup.prettify()

    html_file = open("index.html","w",encoding='utf-8')
    html_file.write(html)
    html_file.close()


    divs= soup.find_all(name='div',attrs={'class':'css-cn2h2t'})


  
   
    for div in divs:
            for child in  div.find_all(name='div',attrs={'class':'subtitle3'}):
                    L.append(child.string)



geta_html(1)

print(L)