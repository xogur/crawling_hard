import sys
from PySide6.QtWidgets import QApplication, QWidget # QApplication : 어플리케이션 설정 관리 담당 / QWidget : Qt 기본 창 클래스
from naver_kin_ui import Ui_Form
import requests
import pandas as pd
import bs4
import re

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
        for i in range(1, input_page + 1) :

            self.textBrowser.append(f'{i} 페이지 크롤링 중...')
            url = "https://kin.naver.com/search/list.naver?query={}&page={}".format(input_keyword,i)
            res = requests.get(url)
            soup = bs4.BeautifulSoup(res.text, "html.parser")
            li_elements = soup.select("ul.basic1 > li")
            if li_elements :

                for li_element in li_elements:
                    title = li_element.select("a._nclicks\:kin\.txt")[0].text.strip()
                    
                    link = li_element.select("a[target='_blank']")[0].get("href")
                    
                    content = li_element.select("dd")[1].text.strip()
                    
                    category = li_element.find("a", class_="txt_g1 _nclicks:kin.cat2").text.strip()
                    
                    text = li_element.select(".hit")[0].text.strip()
                    text = re.search(r"\d+", text).group()

                    self.textBrowser.append(title)
                    QApplication.processEvents()
                    print(title, link, content, category, text)
                    print(" ")
                    self.result.append([title, link, content, category, text])

            else :
                self.textBrowser.append(f'{i} 페이지 이후는 존재하지 않습니다')
                break

            self.textBrowser.append(" ")
                

        self.textBrowser.append('크롤링 완료!')

    def reset(self) :
        self.keyword.setText("")
        self.page.setText("")
        self.textBrowser.setText("")
    
    def save(self) :
        input_keword = self.keyword.text()

        # 데이터 프레임 생성
        df = pd.DataFrame(self.result, columns=['제목', '링크', '날짜', '카테고리', '답변수'])
        df.to_excel(f'{input_keword}.xlsx')
    
    def quit(self) :
        sys.exit()

app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())

# exe파일로 만드들기
# pyinstaller -w -F .\네이버지식인GUI.py