'''o・xが３つ連続してる方が勝ち'''
#テストデータの挿入
s = 'oxoxx'
#判定の初期値
con = 'o'
#連続数
con_cnt = 0
#カウント処理
for i in s:
    if con == i:
        con_cnt += 1
    else:
        con = i
        con_cnt = 1
    if con_cnt == 3:
        break
#結果の出力
if con_cnt == 3:
    print(con)
else:
    print('draw')