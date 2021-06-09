from Crypto.Util.number import long_to_bytes
# output.txt -> output.py
from output import pub_key, cipher


def create_lattice(b, c):
    """create_lattice

    CLOS法で使う基底行列を生成する関数

    Args:
        b: 公開鍵
        c: 暗号文

    Returns:
        B: 基底行列    
    """
    # 基底行列のサイズ
    N = len(b) + 1
    # 行列生成のときに使うリスト
    m_list = [[0 for _ in range(N)] for _ in range(N)]
    # bと2Iと-1
    for i in range(N-1):
        m_list[i][0] = b[i]
        m_list[i][i+1] = 2
        m_list[N-1][i+1] = -1
    # -c
    m_list[N-1][0] = -c
    # 基底行列を作成
    B = matrix(ZZ, m_list)

    return B


def valid_vector(llled):
    """valid_vector

    左端が0、それ以外が+1,-1のベクトルを返す関数

    Args:
        llled: LLL()が実行されている基底行列

    Returns:
        v: 左端が0、それ以外が+1,-1のベクトル 
    """
    for v in llled:
        is_valid = True
        if v[0] != 0:
            continue
        for i, x in enumerate(v):
            if i != 0 and abs(x) != 1:
                is_valid = False
                break
        if is_valid:
            return v


B = create_lattice(pub_key, cipher)
llled = B.LLL()
flag_vec = valid_vector(llled)

flag = ""

for x in flag_vec:
    if x == 1:
        flag += "1"
    elif x == -1:
        flag += "0"

flag = long_to_bytes(int(flag, 2))
print(flag.decode())
