import sys
import pandas as pd
import pandas as pd
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from PySide6.QtWidgets import (
    QApplication, QWidget, QMessageBox, QFileDialog
)
from 알라딘_ui import Ui_Form  # UI 클래스는 Qt Designer → py로 변환한 파일입니다

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 🔒 시작할 때는 크롤링 버튼 비활성화
        self.start_btn.setEnabled(False)

        # 🔗 버튼 연결
        self.login_btn.clicked.connect(self.login)
        self.start_btn.clicked.connect(self.start_crawling)
        self.save_btn.clicked.connect(self.save_result)
        self.file.clicked.connect(self.select_file)  # 📁 파일 선택 버튼 기능 추가

    def login(self):
        user_id = self.id.text()
        user_pw = self.pw.text()

        if user_id == "admin" and user_pw == "1234":
            QMessageBox.information(self, "로그인 성공", "환영합니다!")
            self.account.setText(user_id)
            self.start_btn.setEnabled(True)
        else:
            QMessageBox.warning(self, "로그인 실패", "아이디 또는 비밀번호가 틀렸습니다.")
            self.start_btn.setEnabled(False)

    def start_crawling(self):

        # 1. 데이터 불러오기
        df = pd.read_excel(self.file_path)
        df['바코드'] = df['바코드'].apply(lambda x: x.replace('\xa0', '') if isinstance(x, str) else x)
        self.ing.setText(len(df['바코드']))
        QApplication.processEvents()
        # 2. 등급 매핑
        grade_map = {'최상': 1, '상': 2, '중': 3}

        # 3. 결과 저장용 딕셔너리
        self.result_dict = defaultdict(list)

        # 4. requests 세션 사용
        session = requests.Session()
        self.ing.setText("x1")
        QApplication.processEvents()

        # 5. 바코드 + 품질등급 순회
        for num, (code, want_grade_str) in enumerate(zip(df['바코드'], df['품질등급']), start=1):
            self.ing.setText(f"{num}/{len(df)}")
            self.textBrowser.append(f"\n[{num}/{len(df)}] 바코드: {code} | 등급: {want_grade_str}")
            QApplication.processEvents()

            want_grade = grade_map.get(str(want_grade_str).strip(), 0)

            # 검색 페이지
            try:
                search_url = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&SearchWord={code}"
                res = session.get(search_url)
                soup = BeautifulSoup(res.text, "html.parser")
                code_url_table = soup.select_one("#Search3_Result > div:nth-child(1) > table")
                a_tag = code_url_table.select_one("div.ss_book_list > ul > li > a")
                if a_tag is None:
                    continue
                full_url = "https://www.aladin.co.kr" + a_tag['href']
            except Exception as e:
                print(f"❌ 검색 오류: {e}")
                continue

            # 6. 두 번 크롤링: 전체등급 / 등급필터
            for mode, quality_type in [('전체', 0), ('등급필터', want_grade)]:
                print(f"  🔍 모드: {mode} | QualityType={quality_type}")
                page = 1
                while True:
                    try:
                        detail_url = (
                            f"{full_url}&TabType=0&QualityType={quality_type}&Fix=1&ShopCode=0"
                            f"&HalfDelivery=0&SortOrder=9&page={page}&PublishDay=84"
                            f"&PriceFilterMin=0&PriceFilterMax=0"
                        )
                        res = session.get(detail_url)
                        soup = BeautifulSoup(res.text, "html.parser")
                        detail_td = soup.select_one(
                            "#Ere_prod_allwrap_box > div.Ere_prod_middlewrap > div.Ere_usedsell_table table > tbody"
                        )
                        rows = detail_td.select("tr")
                        if len(rows) <= 1:
                            break
                    except Exception as e:
                        print(f"  ❌ 페이지 파싱 오류: {e}")
                        break

                    for row in rows[1:]:
                        try:
                            book_name = row.select_one(".sell_tableCF2 a").text.strip()
                            book_grade = row.select_one("span.Ere_sub_top").text.strip()
                            price = row.select_one(".Ere_sub_pink").text.strip()
                            delivery = [li.text.strip() for li in row.select(".price li")[2:]]

                            self.result_dict[book_name].append({
                                'book_name': book_name,
                                'book_grade': book_grade,
                                'price': price,
                                'delivery': ', '.join(delivery),
                                'mode': mode
                            })

                            self.textBrowser.append(f"    📚 {book_name} | {book_grade} | {price} | {delivery}")
                            QApplication.processEvents()
                            break  # 최저가만 추출

                        except Exception as e:
                            print(f"    ⚠️ 행 파싱 오류: {e}")
                            continue

                    break  # 페이지 1페이지만 확인 (최저가용)

        # 7. 결과 정리 및 저장
        self.all_rows = []
        for book_group in self.result_dict.values():
            self.all_rows.extend(book_group)


        self.ing.setText("완료되었습니다.")

    def save_result(self):
        df_result = pd.DataFrame(self.all_rows)
        df_result.to_csv("알라딘_도서_중고정보.csv", index=False, encoding="utf-8-sig")
        print("\n✅ CSV 저장 완료: 알라딘_도서_중고정보.csv")
        self.textBrowser.append("결과를 저장했습니다.")
        QMessageBox.information(self, "저장", "엑셀 파일로 저장 완료!")

    def select_file(self):
        # 📁 파일 탐색기 열기
        self.file_path, _ = QFileDialog.getOpenFileName(
            self,
            "파일 선택",
            "",
            "Excel Files (*.xlsx *.xls);;CSV Files (*.csv);;All Files (*)"
        )

        if self.file_path:
            self.file_name.setText(self.file_path)

            try:
                # 🧾 엑셀 파일 읽기
                df = pd.read_excel(self.file_path)

                # ✅ '바코드' 컬럼이 존재하는지 확인
                if '바코드' in df.columns:
                    total = len(df['바코드'])
                    self.total_books.setText(f"전체 책 수 : {total}")
                else:
                    self.total_books.setText("⚠️ '바코드' 컬럼 없음")
            except Exception as e:
                QMessageBox.warning(self, "오류", f"파일을 불러오는 중 오류 발생:\n{str(e)}")
                self.total_books.setText("⚠️ 파일 오류")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
