# 入手した暗号文(16進数)
c = "71295e3edd417b3a18be48eb67b129508c7a47ce644b2402003bdd4e8c50510167d8c505c310236544b96267806d5fed097af578edba148ead016696be713cff95c68a47aabef5095c32c686008db357"

# 16進数をbytesに変換する
c_bytes = bytes.fromhex(c)

# 前半部
c1 = c_bytes[:32].hex()
# 後半部
c2 = c_bytes[32+16:].hex()

# 結合して出力する
print(c1 + c2)
