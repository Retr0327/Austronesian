from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium import webdriver  
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
print("[族語代號]\n"+"阿美：1 南勢 2 秀姑巒 3 海岸 4 馬蘭 5 恆春\n"+"泰雅：6 賽考利 7 澤敖利 8 汶水 9 萬大 10 四季 11 宜蘭澤敖利\n"+"賽夏：13\n"+"邵：14\n"+"賽德克：15 都達 16 德固達雅 17 德路固\n"+"布農：18 卓群 19 卡群布 20 丹群 21 巒群 22 郡群\n"+"排灣：23 東 24 北 25 中 26 南"+"魯凱：27 東 28 霧台 29 大武 30 多納 31 茂林 32 萬山\n"+"太魯閣語：33\n"+"噶瑪蘭：34\n"+"鄒：35\n"+"卡那卡那富：36\n"+"拉阿魯哇：37"+"卑南：38 南王 39 知本 40 西群 41 建和\n"+"雅美：42\n"+"撒奇萊雅：43")
name=str(input("族語："))
for i in range(1,int(input("篇數："))+1):
    driver = webdriver.Chrome('C:/Users/user/Desktop/Python/chromedriver.exe')
    driver.get('http://web.klokah.tw/extension/cu_practice/index.php?d='+name+'&l='+str(i)+'&view=article')
    driver.maximize_window()
    iframe = driver.find_elements_by_tag_name('iframe')[0]
    driver.switch_to.frame(iframe)
    soup = BeautifulSoup(driver.page_source)
    print(soup.find_all("title")[0].text)
    a=soup.find_all("div", class_="word")  
    contain=[]                      #純族語
    indent=' '
    for i in range(len(a)):
        contain.append(a[i].text)
    print(indent.join(contain))
    print("")
    