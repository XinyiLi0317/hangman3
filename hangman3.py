

#第9章　ファイル

#
import os

os.path.join("Users","bob", "st.txt")

#

st = open("st.txt","w")
st.write("Hi from Python!")
st.close() 

#

st = open("st.txt","w",encoding="utf-8")
st.write("Pythonこんにちは")
st.close()


#

with open("st.txt","w") as f:
    f.write("Hi from Python!")

#

with open("st.txt","r")as f:
    print(f.read())

#

with open("st.txt","r", encoding="utf-8")as f:
    print(f.read())


#

my_list=[]
with open("st.txt","r") as f:
    my_list.append(f.read())

print(my_list)


#

import csv

with open("st.csv","w", newline=) as f:


#


#


#challenge

st=open("xyc.text","w")
st.write("I miss u sooo much")
st.close()


with open("xyc.txt","w")as l:
    l.write("I think I miss u right now")
#

ques=input("好きな人は誰：")

with open("xyc.txt","w", encoding="utf-8") as l:
    l.write(ques)
with open("xyc.txt", "r") as l:
    print(l.read())


#

list=[["A","B","C"],["D","E"],["F","G"]]

import csv
with open("list.csv","w",newline='')as f:
    w = csv.writer(f,delimiter=",")
    w.writerow(list[0])
    w.writerow(list[1])
    w.writerow(list[2])

with open("list.csv","r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

#

list=[["あ","い","う"],["え","お"],["か","き"]]

import csv
with open("list.csv","w",newline='', encoding="utf-8")as f:
    w = csv.writer(f,delimiter=",")
    w.writerow(list[0])
    w.writerow(list[1])
    w.writerow(list[2])

with open("list.csv","r",encoding="utf-8") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))


#第10章
word="cat"

def hangman(word): #hangmanという関数を作る；wordは当ててほしい単語
    wrong=0 #何回間違えたかを数える変数
    stages=["",
            "________         ",
            "|                ",
            "|       |        ",
            "|       0        ",
            "|      /|\       ",
            "|      / \       ",
            "|                "
            ]
    rletters=list(word)#答えをリスト化;答えなければいけない残りの文字を覚えておくのに使う
    board=["_"]*len(word)#見せるヒントを記録する
    win=False#初期状態ではFalseを割り当てる；ゲームに勝ったかどうかの状態を記録する
    print("ハングマンへようこそ！")
    while wrong< len(stages)-1:
        print("\n")#改行、ゲームの見た目をよくするために
        msg="1文字を予想してね"#回答を入力してもらうためにinput関数を使う
        char=input(msg)#入力された回答を変数charに割り当てる
        if char in rletters:#入力された答えがrlettersの要素にあったら、正解
            cind=rletters.index(char)#入力された文字がrlettersの何番目かにあるかのインデックスを取得する
            board[cind]=char#boardのcind番目がcharに変換する
            rletters[cind]="$"#rlettersの2番目を$に変換し、aを入力してももう答えではない;次のループでindexメソッドがもう一つの文字のインデックス値を返してくれるようになる
        else:
            wrong+=1#間違えたら、wrongを一回増やす
        print(" ".join(board))#見やすいように_の間に半角スペースを入力
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win=True
            break
        if not win:#if():()がTrueだったら下のコマンドが実行される。()--not win
            print("\n".join(stages[0:wrong+1]))
            print("あなたの負け！正解は{}.".format(word))

hangman("cat")



#




