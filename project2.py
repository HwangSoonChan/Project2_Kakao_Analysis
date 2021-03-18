
fren_name = []
kakao_name = []
count_list = []
new_name = []

def clear_list():
    global fren_name, kakao_name, count_list, new_name
    fren_name = []
    kakao_name = []
    count_list = []
    new_name = []

#대화 인원 파악_1
def kakao_people_def(li_name):
    new_name = []
    for i in range(len(li_name)):
        fren_name.append(li_name[i].split(']'))
        fren_name[i] = fren_name[i][0]

        if fren_name[i] in new_name:
            continue
        else:
            new_name.append(fren_name[i])

    return new_name

#카톡대화 전체 이름 저장_2
def name_chg_def(kakao_chg_name):
    kakao_name = []
    for i in range(len(kakao_chg_name)):
        kakao_name.append(kakao_chg_name[i].split('['))
        kakao_name[i] = kakao_name[i][1]
    return kakao_name

#리스트 초기화_3
def list_reset_def(new_name):
    global count_list
    for i in range(len(new_name)):
        count_list.append(0)

#카톡한 횟수_4
def name_count_def(kakao_name,new_name):
    for i in range(len(kakao_name)) :
        for j in range(len(new_name)) :
            if kakao_name[i] == new_name[j]:
                count_list[j] += 1
    return count_list

