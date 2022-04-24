'''36進数への変換'''
#テストデータ
s = 5555
#結果
ans = ''
#sが０になるまでループ
while s != 0:
    mod = s % 36
    if mod > 9:
        ans += chr(mod+55)
    else:
        ans += str(mod)
    s = s // 36
if ans == '':
    ans = '0'
ans = ans[::-1]
print(ans)