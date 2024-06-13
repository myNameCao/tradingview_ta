import requests

from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


import time




L=[]
def geta_html(page):

    # html=requests.get('https://x.com/xiaomucrypto'.format(page))


    


    driver = webdriver.Chrome()

    driver.add_cookie({'name' : 'auth_token', 'value' : '37213cc5778652f45343c86880f5f9dcb05965e6'})

  

    driver.get("https://x.com/xiaomucrypto")



    # wait = WebDriverWait(driver, 10)

    # wait.until(EC.presence_of_element_located((By.ID, "id__o6a061w0s9a")))

    time.sleep(10)



    # 打印处理后的HTML

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    driver.close()

    # # 移除所有<script>标签及其内容
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