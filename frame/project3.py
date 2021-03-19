import requests
from bs4 import BeautifulSoup

croling = []
yok_count = []
add_bisok = ['ㅅㅂ','새끼','시발','싀바','ㅗ','존나']

page = requests.get("https://namu.wiki/w/%EC%9A%95%EC%84%A4/%ED%95%9C%EA%B5%AD%EC%96%B4")
soup = BeautifulSoup(page.text, 'html.parser')
tg_list = soup.select('.wiki-heading-content>ul>li>div>a')

for i in tg_list:
    croling.append(i.text.strip())

def clear_list():
    global yok_count
    yok_count = []

# 욕 리스트 초기화
def list_reset_def(new_name):
    for i in range(len(new_name)):
        yok_count.append(0)

    return yok_count


# 크롤링 욕 추가
for i in range(len(add_bisok)):
    croling.append(add_bisok[i])


# 욕 확인
def list_check_def(new_name, kakao_text, kakao_name):
    for i in range(len(kakao_text)):
        for j in range(len(croling)):
            if croling[j] in kakao_text[i]:
                for k in range(len(new_name)):
                    if kakao_name[i] == new_name[k]:
                        yok_count[k] += 1

    return yok_count
