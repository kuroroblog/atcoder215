# 文字列の並び替え(順列列挙)を行う関数
def permutations(start, end=[]):
    # 文字列が生成された場合
    if len(start) == 0:
        arr.append("".join(end))
    else:
        for i in range(len(start)):
            # abcの文字列の場合。
            # aの文字列を固定して、bc, cbの並び替えを行う。
            # 次にbの文字列を固定して、ac, caの並び替えを行う。
            # 最後にcの文字列を固定して、ab, baの並び替えを行う。
            # 参考 : https://www.delftstack.com/ja/howto/python/how-to-generate-all-permutations-of-a-list-in-python/
            permutations(start[:i] + start[i+1:], end + start[i:i+1])

# 標準入力を受け付ける。
S, K = input().split()

# 文字列をlist型へ変更し、各文字1つ1つを格納する。
# 参考 : https://qiita.com/cress_cc/items/5600be0416a0be72ecfb#perl%E3%81%A8python%E3%81%AE%E6%AF%94%E8%BC%83
S = list(S)

# 文字列の長さを格納する。
Slen = len(S)

# 各文字を入れ替えて生成される、文字列を格納する。
arr = []

# 文字列の(順列列挙)を行う関数
permutations(S)

# 重複削除を行う。
# 参考 : https://note.nkmk.me/python-list-unique-duplicate/
arr = list(set(arr))
# 文字列を辞書順へ並び替える。
arr.sort()

# K番目の文字列を出力する。
print(arr[int(K) - 1])
