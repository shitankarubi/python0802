# ライブラリのインポート
import random
import time

# 問1. 1 ～ 10 までの乱数を一度に３つ発生させて、最も小さな値の秒数処理を止める関数を作成せよ。
def stoptime():
    """1 ～ 10 までの乱数を一度に３つ発生させて、最も小さな値の秒数処理を止める関数を作成"""
    # ここに作成せよ
    x = set()
    for i in range(3):
        y = random.randint(1,10)
        print(y)
        x.add(y)

    minx = min(x)
    time.sleep(minx)
    print(minx,"秒待ちました")
if __name__ == "__main__":
    stoptime()



# 問2. 1 ～ 10 までの乱数を発生させ、その合計が 100 を超えるまでループするアルゴリズムを作成せよ。
# 毎回合計値を出力し、100 を超えた場合「終了」と知らせよ。
# ここに作成せよ
if __name__ == "__main__":
    x  = 0
    while x <= 100 :
        rand =  random.randint(1,10)
        print(rand)
        x +=  rand
        print(rand,"足して",x,"になりました")

    print("終了")






# 問3. 現在時刻を表示させよ。
import datetime
if __name__ == "__main__":
    # ここに作成せよ
    print(datetime.datetime.now())

