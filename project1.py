import pandas as pd
import seaborn as sns
import project2 as kakao
import requests
from bs4 import BeautifulSoup
import project3 as yok



li_name = []
new_name = []
kakao_chg_name = []
kakao_name = []
kakao_text = []
text_count = []
yok_count = []
kakao_data = []


def clear_list():
    global li_name, new_name, kakao_chg_name, kakao_name, kakao_text, text_count, \
            yok_count,kakao_data
    li_name = []
    new_name = []
    kakao_chg_name = []
    kakao_name = []
    kakao_text = []
    text_count = []
    yok_count = []
    kakao_data = []

def kakao_algorigm_def(file_root):
    with open(file_root, 'r', encoding='UTF-8') as f:
        for i in f:
            list = i.strip()
            if '] [' in list:
                li_name.append(list.split("[")[1])
                kakao_chg_name.append(list.split("]")[0])
                kakao_text.append(list.split("]")[2])

    new_name = kakao.kakao_people_def(li_name)

    kakao_name = kakao.name_chg_def(kakao_chg_name)
    #카톡 내용 초기화
    text_count = kakao.list_reset_def(new_name)
    #카톡 횟수 확인
    text_count = kakao.name_count_def(kakao_name,new_name)
    #욕 리스트 초기화
    yok.clear_list()
    yok_count = yok.list_reset_def(new_name)
    #욕 횟수 확인
    yok_count = yok.list_check_def(new_name,kakao_text,kakao_name)

    for i in range(len(new_name)):
        data = []
        data.append(new_name[i])
        data.append(text_count[i])
        data.append(yok_count[i])
        kakao_data.append(data)


def kakao_data_def() :

    return kakao_data
