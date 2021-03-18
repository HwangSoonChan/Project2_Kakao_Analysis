import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np

import pandas as pd
import project1 as k_data
import project2 as kakao

font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/batang.ttc").get_name()
kakao_data = []


root = tk.Tk()
root.geometry("500x500")
root.pack_propagate(False)
root.resizable(0,0)

frame1 = tk.LabelFrame(root, text="kakao Data")
frame1.place(height=300, width=500)

gh_frame = tk.LabelFrame(root, text="Graphic")
gh_frame.place(height=100, width=400, rely=0.60, relx= 0)

file_frame = tk.LabelFrame(root, text="Open File")
file_frame.place(height=100, width=400, rely=0.75, relx= 0)


gh_button1 = tk.Button(gh_frame, text = "All_Count_Graphic", command= lambda: All_Count_Gh())
gh_button1.place(rely=0.15, relx=0.1)

gh_button2 = tk.Button(gh_frame, text = "curse_Graphic", command= lambda: Curse_Count_Gh())
gh_button2.place(rely=0.15, relx=0.50)

button1 = tk.Button(file_frame, text = "Browse A File", command= lambda: File_dialog())
button1.place(rely=0.55, relx=0.50)

button2 = tk.Button(file_frame, text="Load File", command = lambda : Load_txt_data())
button2.place(rely=0.55, relx=0.30)

button3 = tk.Button(file_frame, text="All Reset", command = lambda : Remove_all())
button3.place(rely=0.55, relx=0.10)

label_file = ttk.Label(file_frame, text="No File Seleted")
label_file.place(rely=0, relx=0)

#트리뷰 위젯
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1)

#스크롤바
treescrolly = tk.Scrollbar(frame1,orient="vertical", command=tv1.yview)
treescrollx = tk.Scrollbar(frame1,orient="horizontal", command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom", fill="x")
treescrolly.pack(side="right", fill="y")


def File_dialog():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("txt files","*.txt"),("All files","*.*")))
    label_file["text"] = filename
    return None

def Load_txt_data():
    #파일 경로를 불러옴
    file_path = label_file["text"]

    try:
        #경로를 보낸 후, 카톡 내용 분석
        k_data.kakao_algorigm_def(file_path)
        #카톡 내용 테이블 형태로 변형
        df = pd.DataFrame(data=k_data.kakao_data_def(),
                          columns=['name','all_count','curse_count'])
    #예외처리 코드
    except ValueError:
        tk.messagebox.showerror("Information","The file you have chosen is invailed")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information",f"No such file as {file_path}")
        return None

    k_data.clear_list()
    kakao.clear_list()

    clear_data()

    # 테이블 헤더부분
    tv1["column"] = list(df.columns)
    # 테이블 헤더 보여짐
    tv1["show"] = "headings"
    # 테잉블 헤더 뿌려짐
    for column in tv1["columns"]:
        tv1.heading(column, text=column)

    df_rows = df.to_numpy().tolist()
    #데이터들 각 row에 뿌려짐
    for row in df_rows:
        tv1.insert("", "end", values=row)


    return df
#초기화 알고리즘
def clear_data():
    print(*tv1.get_children())
    tv1.delete(*tv1.get_children())
    return None

def Remove_all():
    for recode in tv1.get_children():
        tv1.delete(recode)

def All_Count_Gh():

    df = Load_txt_data()

    df_name = df['name']
    df_all_count = df['all_count']

    kakao_name = list(df_name.values)
    kakao_all_text = list(df_all_count.values)

    rc('font', family=font_name)
    plt.pie(kakao_all_text, labels=kakao_name, autopct='%1.1f%%')
    plt.show()

    return None

def Curse_Count_Gh():

    df = Load_txt_data()

    df_name = df['name']
    df_curse_count = df['curse_count']

    kakao_name = list(df_name.values)
    kakao_curse_text = list(df_curse_count.values)

    rc('font', family=font_name)
    plt.pie(kakao_curse_text, labels=kakao_name, autopct='%1.1f%%')
    plt.show()

    return None


root.mainloop()