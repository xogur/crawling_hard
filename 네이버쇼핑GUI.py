import sys
from PySide6.QtWidgets import QApplication, QWidget # QApplication : 어플리케이션 설정 관리 담당 / QWidget : Qt 기본 창 클래스
from naver_shop_ui import Ui_Form
import requests
import pandas as pd
import bs4
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import requests
import pandas as pd
import bs4
import re
from selenium.webdriver.support.select import Select

class MainWindow(QWidget, Ui_Form) : # QWidget과 Ui_Form을 상속속
    def __init__(self):
        super().__init__() # 부모인 QWidget의 생성자 호출출
        self.setupUi(self) # Ui_Form의 setupUi를 실행

        # self.객체이름.clicked.connect(self.실행할메서드이름)
        self.start_btn.clicked.connect(self.start)
        self.reset_btn.clicked.connect(self.reset)
        self.save_btn.clicked.connect(self.save)
        self.quit_btn.clicked.connect(self.quit)

    def start(self) :
        input_keyword = self.keyword.text()
        input_page = int(self.page.text())

        self.result = []
        

        url = "https://search.shopping.naver.com/search/all?query={}".format(input_keyword)
        driver = webdriver.Chrome()  # User-Agent 적용된 드라이버 실행
        driver.get(url)

        time.sleep(1)

        html = driver.page_source
        soup = bs4.BeautifulSoup(html)

        time.sleep(1)



        for e in range(1, input_page + 1) :

            self.textBrowser.append(f'{e} 페이지 크롤링 중...')
            url = "https://search.shopping.naver.com/search/all?query={}&pagingIndex={}&arriveGuarantee=true&freeDelivery=true&pagingSize=40&productSet=total&agency=true&exagency=true".format(input_keyword,e)
            driver.get(url)
            time.sleep(2)
            html = driver.page_source
            soup = bs4.BeautifulSoup(html, "html.parser")
            last_height = driver.execute_script("return document.body.scrollHeight")

            while True :
                # 스크롤 끝까지 내리기
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(1)
                # 스크롤 후 높이
                after_height = driver.execute_script("return document.body.scrollHeight")
                
                # 비교 (if, break)
                if last_height == after_height :
                    break
            
                # 스크롤 전 높이 업데트
                last_height = after_height
                time.sleep(1)

            soup = bs4.BeautifulSoup(driver.page_source, "html.parser")


            elements = soup.find_all("div", class_="product_item__MDtDF")



            for element in elements :
                product_name = element.select_one("div.product_title__Mmw2K > a").text
                product_link = element.select_one('a').get('href')
                price_text = element.select_one("strong > span.price > span.price_num__S2p_v").text
                numeric_str = re.sub(r'\D', '', price_text)
                try :
                    text_value = element.select_one("div.product_info_area__xxCTi > div.product_etc_box__ElfVA > a:nth-child(2) > span > span").text
                    if '구매' in text_value:
                        text_value = text_value.replace("구매",'')
                        if '만' in text_value :
                            text_value = int(text_value.replace("만",'').replace(".",'')) * 1000
                    
                except :
                    text_value = ''
                
                self.textBrowser.append(product_name)
                self.textBrowser.append(" ")
                QApplication.processEvents()
                self.result.append([product_name, product_link, int(numeric_str), text_value])
                time.sleep(1)



            self.textBrowser.append(" ")
                

        self.textBrowser.append('크롤링 완료!')

    def reset(self) :
        self.keyword.setText("")
        self.page.setText("")
        self.textBrowser.setText("")
    
    def save(self) :
        input_keword = self.keyword.text()

        # 데이터 프레임 생성
        df = pd.DataFrame(self.result, columns=['상품이름', '링크', '가격', '구매수'])
        df.to_excel(f'{input_keword}.xlsx')
    
    def quit(self) :
        sys.exit()

app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())

# exe파일로 만드들기
# pyinstaller -w -F .\네이버지식인GUI.py