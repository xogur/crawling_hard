import sys
from PySide6.QtWidgets import QApplication, QWidget # QApplication : 어플리케이션 설정 관리 담당 / QWidget : Qt 기본 창 클래스
from RISS_ui import Ui_Form
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

        param = {
            'isDetailSearch': 'N',
            'searchGubun': 'true',
            'viewYn': 'OP',
            'order': '/DESC',
            'onHanja': 'false',
            'strSort': 'RANK',
            'iStartCount': 0,
            'sflag': 1,
            'isFDetailSearch': 'N',
            'pageNumber': 1,
            'icate': 're_a_kor',
            'colName': 're_a_kor',
            'pageScale': {input_page},
            'isTab': 'Y',
            'query': {input_keyword}
        }

        headers = {
            'accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding':
            'gzip, deflate, br, zstd',
            'accept-language':
            'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control':
            'max-age=0',
            'connection':
            'keep-alive',
            'cookie':
            'JSESSIONID=xKFrPftFpgy9zYcgZ1Gu9nMbZyBThHjKG9GGYFe34MCdgTI7v3e21mmutHePZf6a.amV1c19kb21haW4vcmlzc3dhczJfY29udGFpbmVyMQ==; WMONID=ZGn2FxH-9ap; _ga=GA1.1.739771833.1740983462; TodayView=1a0202e37d52c72d_dcd1a8e873c0ca787ecd42904f0c5d65_%ED%8C%A8%EC%85%98+%EC%A0%9C%EC%A1%B0+%EA%B8%B0%EC%97%85%EC%9D%98+%EB%94%94%EC%A7%80%ED%84%B8+%ED%8A%B8%EB%9E%9C%EC%8A%A4%ED%8F%AC%EB%A9%94%EC%9D%B4%EC%85%98%EC%9D%84+%EC%9C%84%ED%95%9C+%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5+%EC%86%94%EB%A3%A8%EC%85%98+%EA%B0%9C%EB%B0%9C+%EB%B0%8F+%ED%99%9C%EC%9A%A9+%ED%98%84%ED%99%A9_RISS; TodayKeyword=%ED%8C%A8%EC%85%98+%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5,84,re_a_kor:%ED%8C%A8%EC%85%98+%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5,84,re_a_kor:%ED%8C%A8%EC%85%98+%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5,84,re_a_kor:%ED%8C%A8%EC%85%98+%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5,84,re_a_kor; _ga_E7TB6KFQFY=GS1.1.1740983461.1.1.1740985767.0.0.0',
            'host':
            'www.riss.kr',
            'referer':
            'http://localhost:8888/',
            'sec-ch-ua':
            '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile':
            '?0',
            'sec-ch-ua-platform':
            '"Windows"',
            'sec-fetch-dest':
            'document',
            'sec-fetch-mode':
            'navigate',
            'sec-fetch-site':
            'cross-site',
            'sec-fetch-user':
            '?1',
            'upgrade-insecure-requests':
            '1',
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        }


        url = "https://www.riss.kr/search/Search.do"
        res = requests.get(url, params = param)
        soup = bs4.BeautifulSoup(res.text)
        elements = soup.select(".srchResultListW > ul > li")



        import urllib3
        urllib3.disable_warnings()

        for element in elements :
            title = element.select_one(".title > a").text
            link = "https://www.riss.kr" + element.select_one(".title > a").attrs["href"]

            #상세 페이지 요청
            res = requests.get(link, headers = headers, verify=False)
            soup = bs4.BeautifulSoup(res.text, "html.parser")
            press = soup.select_one("div.infoDetailL ul li:nth-of-type(2) a").text
            years = soup.select_one("div.infoDetailL ul li:nth-of-type(5) > div").text

            tag = soup.select_one("div.infoDetailL ul li:nth-of-type(7) > span").text

            file = soup.find_all('span', string='DOI식별코드')

            if tag == '주제어' :
                tag = soup.select_one("div.infoDetailL ul li:nth-of-type(7) > div > p").text.strip().replace(";",'').split()
            else :
                tag = ""

            if file :
                file = soup.find_all('span', string='DOI식별코드')[0].find_next_sibling()
                file = file.select_one("a").attrs["href"]
            else :
                file = ""
            
            self.textBrowser.append(title)
            QApplication.processEvents()
            print(title, link, press, years, tag, file)
            print(" ")
            self.result.append([title, link, press, years, tag, file])

            self.textBrowser.append(" ")
        
        self.textBrowser.append('크롤링 완료!')


        

    def reset(self) :
        self.keyword.setText("")
        self.page.setText("")
        self.textBrowser.setText("")
    
    def save(self) :
        input_keword = self.keyword.text()

        # 데이터 프레임 생성
        data = pd.DataFrame(self.result, columns = ['제목', '링크', '발행기관', '년도', '태그', '무료논문파일'])
        data.to_excel(f'{input_keword}.xlsx')
    
    def quit(self) :
        sys.exit()

app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())