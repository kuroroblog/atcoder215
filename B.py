# 標準入力を受け付ける。
# python3系のintには、数字の最大値の上限がないため、bitに関して考える必要はない。
# python3系のintについて : https://note.nkmk.me/python-int-max-value/
N = int(input())

# N = 1の時は0を返すようにする。
if N == 1:
    print(0)
else:
    count = 0
    # N != 1の場合は、while文を回す。
    while True:
        # pow : べき乗を行う関数
        # powについて : https://docs.python.org/ja/3/library/functions.html#pow
        if 0 <= (N - pow(2, count)):
            count = count + 1
        else:
            break
    # -1するのは、breakするときのcount(k)の値が格納されているため。
    print(count - 1)
