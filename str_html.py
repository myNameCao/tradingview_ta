import requests

from bs4 import BeautifulSoup

import re


html=requests.get('https://www.binance.com/zh-CN/markets/trading_data/rankings')

def remove_style_and_script(html_text):
    # 使用正则表达式匹配style和script标签
    pattern = r"<(style|script)[\s\S]*?</\1>"
    
    # 使用re.sub函数将匹配的标签替换为空字符串
    cleaned_html = re.sub(pattern, "", html_text, flags=re.IGNORECASE)

    pattern = r'style=".*?"'
    
    # 使用re.sub函数将匹配的行内样式替换为空字符串
    html = re.sub(pattern, "", cleaned_html)
    
    return html


# # 过滤掉style和script标签后的HTML文本
# filtered_html = remove_style_and_script(html.text)
# html_file = open("index.html","w",encoding='utf-8')
# html_file.write(filtered_html)
# html_file.close()





# 打印处理后的HTML

soup = BeautifulSoup(html.text, 'html.parser')

# 移除所有<script>标签及其内容
for script_tag in soup.find_all(name=['script','style']):
    script_tag.extract()


html=soup.prettify()

html_file = open("index.html","w",encoding='utf-8')
html_file.write(html)
html_file.close()

divs= soup.find_all(name='div',attrs={'class':'css-1v8lj0h'})

target_text=['热门币种','成交榜']

# filtered_divs = [div for div in divs if div.find(string=lambda text: text and target_text in text)]
filtered_divs = [ div for div in divs if any(div.find(string=lambda text: text and target_text in text) for target_text in target_text)]



list_icon= []

for div in filtered_divs:
    for child in div.find_all(name='div', attrs={'class': 'css-lzd0h4'}):
        list_icon.append(child.string)
       


print(list(set(list_icon)) ) # 打印子



