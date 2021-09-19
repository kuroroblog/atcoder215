# 標準入力を受け付ける。
N, M = map(int, input().split())
A = list(map(int, input().split()))

# AのリストとMの値の最大値を洗い出す。
# 答えとしてとりうる値を絞るため。
maxA = max(max(A), M)

# 各index = kの値(答え)とし、kの値(答え)として採用すべきかを(True or False)で表す。
# 初期値としてTrue(採用すべき)を格納する。
# ※ indexの0番目, 1番目の値は利用しない。
k = [True] * (maxA + 1)
# 素数かどうかを判定するために利用する。
# ※ indexの0番目, 1番目の値は利用しない。
isprime = [True] * (maxA + 1)
# Aの素因数(使えない素数)を格納する。
# 素因数とは? : Aを整数で割ることのできる素数。
prime = []

# kの値がAiの値だった場合を考える。
# k = Aiとなるため、gcd(k, k) = 1の場合のみ、成立する事になる。
# k = 1以外は、1よりも大きい最大公約数を取得するため、Aの要素は不採用にする。
for a in A:
    k[a] = False

# 素数の判定を行う。
# 素因数となる値を探すため。
# 2からrangeを回しているのは、indexの0番目, 1番目の値は利用しないため。
for i in range(2, maxA + 1):
    # 不採用になる素因数を探すだけなので、素数にならないfor文に関しては、continueを行う。
    if not isprime[i]:
        continue
    # エラトステネスのふるいとは? : https://club.informatix.co.jp/?p=13457
    for j in range(i * 2, maxA + 1, i):
        # 素数に当てはまらないものをFalseとする。
        isprime[j] = False
        # 先ほど不採用にした値を利用して、素因数になる場合は、不採用にする。
        # (例) : 先ほど不採用にした値が8の場合、素因数2が不採用に含まれるようになる。
        k[i] = k[i] and k[j]
    if not k[i]:
        prime.append(i)

# 使えない素数pに対して、 pの倍数をかけて不採用にする。
for p in prime:
    for j in range(p * 2, M + 1, p):
        k[j] = k[j] and k[p]

# 使える数をansに入れる。
# 1は必ず答えになるので初期化しておく。
ans = [1]
for i in range(2, M + 1):
    if k[i]:
        ans.append(i)

# 出力
print(len(ans))
for i in ans:
    print(i)
