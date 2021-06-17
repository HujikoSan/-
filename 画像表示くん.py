#coding:utf-8
import os
import random
import queue
import tkinter
from PIL import Image, ImageTk

# -------------↓初期設定↓---------------

# フォルダ内の画像の読み込み
path = "./images"
files = os.listdir(path)
files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]

# windowを描画
window = tkinter.Tk()
# アイコン画像を指定
window.iconbitmap('picture2.ico')
# windowサイズを変更
window.geometry("150x220+1305+571")
# windowタイトルを設定
window.title("画像表示くん")
window.update()
# キャンバスの作成
canvas = tkinter.Canvas(bg = "#b5f5ff")
canvas.pack(expand=True, fill=tkinter.BOTH)

pos_w = 1
pos_h = 1

left_files = list(range(0))
mazime = 0

# -------------↑初期設定↑---------------


def illustrate():
    global window,canvas
    global img

    canvas.delete("all")

    if mazime == 0:  # 省電力モードではない時

        if(len(left_files) == 0):
            for i in range(len(files_file)):  # コピー
                left_files.append(files_file[i])

        name = left_files.pop(random.randrange(len(left_files)))  # 残存ファイルの中からランダムにひとつ抽出
        img = Image.open("./images/" + name)

        # 画像サイズの取得
        width = img.width
        height = img.height

        # ウィンドウサイズの取得、余白の吟味
        w_width = window.winfo_width() - 10
        w_height = window.winfo_height() - 10

        # リサイズ
        w_ratio = w_width / float(width)
        h_ratio = w_height / float(height)
        ratio = min( w_ratio, h_ratio)
        img = img.resize(( int(width * ratio), int(height * ratio) ),Image.ANTIALIAS)

        img = ImageTk.PhotoImage(img)

        # キャンバスへの画像表示
        canvas.create_image(
            ( w_width - width * ratio ) / 2 + 5, ( w_height - height * ratio ) / 2 + 5 
            , image = img, anchor = tkinter.NW)

    window.after(5000,illustrate)

def print_key(event):  # 各キーが押された時の処理
    global pos_h, pos_w, mazime
    if event.keysym == 'Escape':
        window.destroy()
    if event.keysym == 'Left':
        pos_w = 0
    if event.keysym == 'Up':
        pos_h = 0
    if event.keysym == 'Right':
        pos_w = 1
    if event.keysym == 'Down':
        pos_h = 1
    if event.keysym == 's':  # 省電力モード
        mazime = 1
    if event.keysym == "l":  # 省電力モードオフ
        mazime = 0

    if event.keysym == 'Left' or event.keysym == 'Up' or event.keysym == "Right" or event.keysym == "Down":  # 位置変更、自分の環境に最適化しています
        if pos_w == 0:
            if pos_h == 0:
                window.geometry("150x235+71+0")
            else:
                window.geometry("150x220+71+571")
        else:
            if pos_h == 0:
                window.geometry("150x235+1305+0")
            else:
                window.geometry("150x220+1305+571")

window.bind( '<Key>' , print_key )

illustrate()

window.mainloop()